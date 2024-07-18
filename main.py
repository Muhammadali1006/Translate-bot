from aiogram import Bot, Dispatcher, types, filters
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from googletrans import Translator


bot = Bot(token='7364081736:AAFGFjg42OdyOUWKwx6fVynCSSVxBbEURbI')
dp = Dispatcher(bot=bot)


class Translate(StatesGroup):
    language = State()
    text = State()


translator = Translator()


@dp.message(filters.Command("start"))
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Translate.language)
    await message.answer("Xush kelibsiz !️ Qaysi tilga tarjima qilib beri?")


@dp.message(Translate.language)
async def language_function(message: types.Message, state: FSMContext):
    await state.update_data(language=message.text)
    await state.set_state(Translate.text)
    await message.answer("Endi text jo'nating")


@dp.message(Translate.text)
async def text_function(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    language = data['language']
    text = data['text']

    result = translator.translate(text=text, dest=language).text

    await message.answer(text=result)
    await state.clear()





async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
