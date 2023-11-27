import asyncio
import os

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.markdown import hide_link, hlink
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InputFile, InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, InputMedia, ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime

import math
from jsonwriter import *
from time import sleep

from mangaparser import *
from texts import *


API_KEY = '6056114434:AAELexyjt28rMSLaR8Me2BGZMDXwHkrZnHI'
previous_msg = ''
del_msgs = list()

parser = MParser()
storage = MemoryStorage()
bot = Bot(token=API_KEY)
dp = Dispatcher(bot, storage=storage)

users = {}


class Form(StatesGroup):
    message = State()

async def delete_msgs(msg):
    global users
    del_msgs = users[str(msg.from_user.id)]['del_msgs']
    for i in reversed(del_msgs):
        await i.delete()
    del_msgs = list()



@dp.message_handler(commands=['start'])
async def send_start(msg: types.Message):
    # users = read_json(file_path='users.json')
    if str(msg.from_user.id) not in users:
        users[str(msg.from_user.id)] = {'vols': [], 'urls': [], 'manga_msg': '', 'del_msgs': [], 'manga_pages': []}
        write_json(file_path='users.json', data=users)
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='search'))
    await bot.send_message(chat_id=msg.from_user.id, text=start_text, reply_markup=reply_markup)


@dp.message_handler(commands=['help'])
async def send_help(msg: types.Message):
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='search'))
    await bot.send_message(chat_id=msg.from_user.id, text=help_text, reply_markup=reply_markup)


@dp.message_handler(content_types=['text'])
async def msg_handler(msg: types.Message):
    # users = read_json(file_path='users.json')
    if msg.text == 'search':
        await Form.message.set()
        previous_msg = await bot.send_message(chat_id=msg.from_user.id, text=search_text)
        users[str(msg.from_user.id)]['previous_msg'] = previous_msg
        # write_json(file_path='users.json', data=users)



# ''' ----------   State handler   ---------- '''
@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        # User is not in any state, ignoring
        return

    # Cancel state and inform user about it
    await state.finish()
    await bot.send_message(chat_id=msg.from_user.id, text='Отменено успешно!')


@dp.message_handler(state=Form.message, content_types=['photo', 'text'])
async def process_mailing(msg: types.Message, state: FSMContext):
    # users = read_json(file_path='users.json')
    previous_msg = users[str(msg.from_user.id)]['previous_msg']
    if previous_msg.text == search_text:
        del_msgs = list()
        await state.finish()
        manga_name = msg.text
        search_msg = await bot.send_message(chat_id=msg.from_user.id, text='загрузка результата поиска...')
        search_result = parser.search(search=manga_name)
        users[str(msg.from_user.id)]['search_result'] = search_result
        if search_result != None:
            del_msgs.append(await search_msg.edit_text(text=f'результат: {len(search_result)} произведений было найдено!'))
            for n, i in enumerate(search_result[:5]):
                reply_markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Открыть', callback_data=f'op-{n}'))
                del_msgs.append(await bot.send_message(chat_id=msg.from_user.id, text=f'Название: {i[0]}', reply_markup=reply_markup))
            reply_markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text='удалить', callback_data='delete'))
            del_msgs.append(await bot.send_message(chat_id=msg.from_user.id, text=f'страница: 1 из 3', reply_markup=reply_markup))
            users[str(msg.from_user.id)]['del_msgs'] = del_msgs
        else:
            await search_msg.edit_text(text=f'произведений по запросу {manga_name} не найдено!')
        # write_json(file_path='users.json', data=users)


@dp.callback_query_handler()
async def query_handler(query: CallbackQuery):
    global users
    print(query.data)
    # users = read_json(file_path='users.json')
    search_result = users[str(query.from_user.id)]['search_result']
    manga_msg = users[str(query.from_user.id)]['manga_msg']
    if query.data == 'delete':
        await delete_msgs(query)

    elif 'op' in query.data:
        await delete_msgs(query)
        manga = search_result[int(query.data.split("-")[-1])]
        url = hide_link(manga[3])
        response = parser.open_page(url=manga[1])
        vols = parser.get_vols(response)
        users[str(query.from_user.id)]['vols'] = vols
        reply_markup = InlineKeyboardMarkup()
        reply_markup.add(InlineKeyboardButton(text='Открыть', callback_data=f'rd--{query.data.split("-")[-1]}'))
        manga_msg = await bot.send_message(chat_id=query.from_user.id, text=f'{url}Манга: {manga[0]}\n\nДругие названия: {manga[2]}\n\nГлав (всего): {len(vols)}', reply_markup=reply_markup, parse_mode='HTML')
        users[str(query.from_user.id)]['magna_msg'] = manga_msg

    elif 'rd' in query.data:
        print(query.data)
        manga_msg = users[str(query.from_user.id)]['magna_msg']
        # url = users[str(query.from_user.id)]['search_result'][int(query.data.split('--')[-1])][1]
        # print(users)
        vols = users[str(query.from_user.id)]['vols']
        print(vols)
        reply_markup = InlineKeyboardMarkup()
        for i in range(1, len(vols) + 1):
            reply_markup.add(InlineKeyboardButton(text=vols[-i][1], callback_data=f'vol--{i}'))
            if i % 6 == 0:
                reply_markup.add(InlineKeyboardButton(text='Следующая страница', callback_data='next-vols'))
                break
        await manga_msg.edit_reply_markup(reply_markup=reply_markup)


    elif query.data == 'next-vols':
        vols = users[str(query.from_user.id)]['vols']
        manga_msg = users[str(query.from_user.id)]['magna_msg']
        reply_markup = InlineKeyboardMarkup()
        try:
            count = users[str(query.from_user.id)]['count']
        except:
            count = 7
            users[str(query.from_user.id)]['count'] = count
        while True:
            if count % 6 != 0:
                reply_markup.add(InlineKeyboardButton(text=vols[-count][1], callback_data=str(-count)))
            else:
                reply_markup.add(InlineKeyboardButton(text='Следующая страница', callback_data='next-vols'))
                break
            count += 1
            print(users[str(query.from_user.id)]['count'])


        await manga_msg.edit_reply_markup(reply_markup=reply_markup)

    elif 'vol' in query.data:
        page = query.data.split('--')[-1]
        pages = parser.get_manga(users[str(query.from_user.id)]['vols'][-(int(page))][0])
        vol_title = users[str(query.from_user.id)]['vols'][-(int(page))][1]
        group = types.input_media.MediaGroup()
        reply_markup = InlineKeyboardMarkup()
        reply_markup.add(InlineKeyboardButton(text='К следующей главе...', callback_data=f'next-vol--{int(page) + 1}'))
        c = 0
        for i in reversed(pages):
            if c != 10:
                group.attach_photo(photo=i)
                c += 1
            else:
                users[str(query.from_user.id)]['manga_pages'].append(await bot.send_media_group(chat_id=query.from_user.id, media=group))
                group = types.input_media.MediaGroup()
                c = 0
        users[str(query.from_user.id)]['manga_pages'].append(await bot.send_media_group(chat_id=query.from_user.id, media=group))
        users[str(query.from_user.id)]['manga_pages'].append(await bot.send_message(chat_id=query.from_user.id, text=f'Глава: {vol_title}', reply_markup=reply_markup))
            # users[str(query.from_user.id)]['manga_pages'].append(await bot.send_photo(chat_id=query.from_user.id, photo=i))
        # users[str(query.from_user.id)]['manga_pages'].append(await bot.send_message(chat_id=query.from_user.id, text='Удалить сообщения...', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='delete', callback_data='del-manga'))))

    elif query.data == 'del-manga':
        for i in users[str(query.from_user.id)]['manga_pages']:
            await i.delete()

    elif 'next-vol--' in query.data:
        page = int(query.data.split('--')[-1])
        if page + 1 > len(users[str(query.from_user.id)]['vols']):
            await bot.send_message(chat_id=query.from_user.id, text='Дальше нет глав!')
        else:
            for i in users[str(query.from_user.id)]['manga_pages']:
                await i.delete()
            page += 1
            pages = parser.get_manga(users[str(query.from_user.id)]['vols'][-(int(page + 1))][0])
            vol_title = users[str(query.from_user.id)]['vols'][-(int(page + 1))][1]
            group = types.input_media.MediaGroup()
            reply_markup = InlineKeyboardMarkup()
            reply_markup.add(InlineKeyboardButton(text='К следующей главе...', callback_data=f'next-vol--{page + 1}'))
            c = 0
            for i in reversed(pages):
                if c != 10:
                    group.attach_photo(photo=i)
                    c += 1
                else:
                    users[str(query.from_user.id)]['manga_pages'].append(
                        await bot.send_media_group(chat_id=query.from_user.id, media=group))
                    group = types.input_media.MediaGroup()
                    c = 0
            users[str(query.from_user.id)]['manga_pages'].append(
                await bot.send_media_group(chat_id=query.from_user.id, media=group))
            users[str(query.from_user.id)]['manga_pages'].append(
                await bot.send_message(chat_id=query.from_user.id, text=f'Глава: {vol_title}',
                                       reply_markup=reply_markup))

    # write_json(file_path='users.json', data=users)
        # for i in pages:
        #     await bot.send_photo(chat_id=query.from_user.id, photo=i) # https://one-way.work/auto/24/00/55/001.jpg
        # await bot.send_message(chat_id=query.from_user.id, text='test')




if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(get_percents())
    executor.start_polling(dp)
    # https://staticrm.rmr.rocks/uploads/pics/00/57/055_o.png
    # https://staticrm.rmr.rocks/uploads/pics/00/57/055.jpg # high
    # https://staticrm.rmr.rocks/uploads/pics/00/57/055_p.jpg # low