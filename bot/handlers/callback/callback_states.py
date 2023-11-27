from aiogram.fsm.state import State, StatesGroup


class SearchState(StatesGroup):
    search_request = State()
    goto = State()
    manga_info = State()