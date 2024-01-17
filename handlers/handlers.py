from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
# from keyboards.kb_common import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio


router = Router()


class MakeOrder(StatesGroup):
    start_message = State()
    name = State()
    phone = State()
    start_message_2 = State()
    help_state = State()
    help_state_message = State()
    help_state_phoneme = State()  # А потом сброс стейта или чи шо
    start_message_3 = State()  # Тут указывать параметры авто
    model_auto = State()
    date_auto = State()
    kuzov_auto = State()
    additional_info = State()
    type_of = State()
    material_of = State()
    color_of = State()
    color_cover = State()
    color_cant = State()
    dopniki = State()
    pyatka = State()
    shield = State()
    final = State()
    wait30 = State()
    wait120 = State()
    wait1440 = State()

# Это еще не конец блин

# @router.message(F.animation)
# async def echo_gif(message: Message):
#     await message.reply_animation(message.animation.file_id)


@router.message(MakeOrder.start_message)
@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Поехали",
        callback_data="poehali")
    )
    await message.answer(
        text="Привет! С помощью этого сервиса ты можешь быстро\n оформить заявку на коврики Eva Standart в твое авто.\n\n\
Как это работает? \n\n \
Тебе нужно будет заполнить данные в трех блоках:\n\
1. Технические характеристики автомобиля\n\
2. Выбрать цвет ковриков и канта\n\
3. Указать дополинтельные параметры\n\n \
Нажми на кнопку ниже, чтобы начать подбор👇\n",
        reply_markup=builder.as_markup()
    )

    await state.set_state(MakeOrder.start_message)


@router.callback_query(F.data == 'Back_to_start')
async def back2start(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Поехали",
        callback_data="poehali")
    )
    await query.message.edit_text(
        text="Привет! С помощью этого сервиса ты можешь быстро\n оформить заявку на коврики Eva Standart в твое авто.\n\n\
Как это работает? \n\n \
Тебе нужно будет заполнить данные в трех блоках:\n\n\
1. Технические характеристики автомобиля\n\
2. Выбрать цвет ковриков и канта\n\
3. Указать дополинтельные параметры\n\n \
Нажми на кнопку ниже, чтобы начать подбор👇\n",
        reply_markup=builder.as_markup()
    )
    await state.set_state(MakeOrder.start_message)


@router.message(MakeOrder.start_message)
@router.callback_query(F.data == "poehali")
async def set_name(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        text="Как тебя зовут?"
    )
    await state.set_state(MakeOrder.name)
    current_state = await state.get_state()
    print(current_state)
    # Проверить как работает
    # await asyncio.sleep(15)
    # if (current_state == await state.get_state()):
    #     await query.message.edit_text(text='поменялось')
    # else:
    #     pass


@router.message(MakeOrder.name)
async def set_phone(message: Message, state: FSMContext):
    await state.update_data(chosen_name=message.text)
    user_data = await state.get_data()  # по хорошему потом убрать подобное
    await message.answer(
        text="После оформления заказа мы свяжемся с тобой для подтверждения заявки. Для этого укажи свой номер телефона, чтобы не потерять связь с нами👇"
    )
    print(f"Клиент ввел имя {user_data['chosen_name']}")
    await state.set_state(MakeOrder.phone)


@router.message(MakeOrder.phone)
async def start_message(message: Message, state: FSMContext):
    await state.update_data(chosen_phone=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Супер! Приступим к подбору",
        callback_data="Super")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="Back_to_start")
    )

    # тут вставить картинку
    await message.answer(
        text="У нас собственное четко отлаженное производство ковриков по более чем 1000 лекал для разных марок и моделей авто \n \
            Для изготовления ковриков мы используем EVA-материал российского производства высокого качества и технологию 3Д-печати\n \
            Срок изготовления - 2-3 рабочих для с омента внесения оплаты (предоплаты) \n \
            \n \
            Цена зависит от количества материала с среднем за салон(без багажника) - от 3400 рублей \n",
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()  # по хорошему потом убрать подобное
    print(
        f"Клиент ввел имя {user_data['chosen_name']} и телефон {user_data['chosen_phone']}")
    await state.set_state(MakeOrder.start_message_2)


@router.callback_query(F.data == 'Back')
async def back(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Супер! Приступим к подбору",
        callback_data="Super")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="Back_to_start")
    )

    # тут вставить картинку
    await query.message.edit_text(
        text="У нас собственное четко отлаженное производство ковриков по более чем 1000 лекал для разных марок и моделей авто \n \
            Для изготовления ковриков мы используем EVA-материал российского производства высокого качества и технологию 3Д-печати\n \
            Срок изготовления - 2-3 рабочих для с омента внесения оплаты (предоплаты) \n \
            \n \
            Цена зависит от количества материала с среднем за салон(без багажника) - от 3400 рублей \n",
        reply_markup=builder.as_markup()
    )
    user_data = await state.get_data()  # по хорошему потом убрать подобное
    print(
        f"Клиент ввел имя {user_data['chosen_name']} и телефон {user_data['chosen_phone']}")
    await state.set_state(MakeOrder.start_message_2)

# Тут нужно будет сделать отправку о звонке на почту


@router.callback_query(F.data == 'help')
async def help_message(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Перезвоните мне",
        callback_data="callme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Напишите мне",
        callback_data="textme")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="Back")
    )
    await query.message.edit_text(
        text='Возможно, у тебя появились сложности при заказе через бот😢\n\
        \n\
        Мы готовы проконсультировать по телефону +7 (914)5-501-502 или свяжись с нами любым другим удобным способом',
        reply_markup=builder.as_markup()
    )
    await state.set_state(MakeOrder.help_state)


@router.callback_query(F.data == 'callme')
async def call_me(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text(text='Приняли! Перезвоним в ближайшее время 🤝')
    pass  # Отправить email с номером телефона
    await state.set_state(MakeOrder.help_state_phoneme)


@router.callback_query(F.data == 'textme')
async def text_me(query: CallbackQuery, state: FSMContext):
    # Отправить email с просьбой написать по номеру телефона(Ватсап получается, или запросить шаринг своего контакта?)
    await query.message.edit_text(text='Отлично, мы свяжемся в ближайшее время!')
    pass
    await state.set_state(MakeOrder.help_state_message)


@router.callback_query(F.data == 'Super')
async def order(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Указать параметры моего авто",
        callback_data="auto")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back")
    )
    await query.message.edit_text(
        text='Чтобы коврики легли четко, нам нужно знать параметры твоего автомобиля 👌\n\
        \n \
        В сообщениях ниже укажи параметры своего авто \n \
        В любой момент ты сможешь обратиться за консультацией. Для этого нажми кнопку "Мне нужна помощь"',
        reply_markup=builder.as_markup()
    )
    await state.set_state(MakeOrder.start_message_3)


@router.callback_query(F.data == 'auto')
@router.message(MakeOrder.start_message_3)
async def order_1(query: CallbackQuery, state: FSMContext):
    await query.message.answer(
        text='Где найти все точные характеристики твоего авто?(Отправка картинки)'
    )
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_0")
    )
    await query.message.answer(
        text='Введите марку и модель авто',
        reply_markup=builder.as_markup()
    )
    await state.set_state(MakeOrder.model_auto)


@router.message(MakeOrder.model_auto)
async def order_2(message: Message, state: FSMContext):
    await state.update_data(chosen_model=message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_1")
    )
    await message.answer(
        text="Чтобы долго не искать все параметры, просто открой свид-во о регистрации или загляни в ПТС(картинка)"
    )
    await message.answer(
        text='Введите год выпуска',
        reply_markup=builder.as_markup()
    )
    await state.set_state(MakeOrder.date_auto)


@router.message(MakeOrder.date_auto)
async def order_3(message: Message, state: FSMContext):
    await state.update_data(chosen_date=message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_2")
    )
    await message.answer(
        text="Картинка"
    )
    await message.answer(
        text='Укажите какой кузов у авто'
    )
    await state.set_state(MakeOrder.kuzov_auto)


@router.message(MakeOrder.kuzov_auto)
async def order_4(message: Message, state: FSMContext):
    await state.update_data(chosen_kuzov=message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_3")
    )
    await message.answer(
        text="Картинка"
    )
    await message.answer(
        text='1. Бензин/дизель/гибрид \n \
            2. автомат/механика \n \
            3. расположение руля : правый/левый \n \
            Напишите ответы на эти вопросы в одном сообщении в свободной форме', reply_markup=builder.as_markup()
    )
    await state.set_state(MakeOrder.additional_info)


@router.message(MakeOrder.additional_info)
async def order_5(message: Message, state: FSMContext):
    await state.update_data(chosen_info=message.text)
    user_data = await state.get_data()
    print(
        f"Клиент ввел имя {user_data['chosen_name']} и телефон {user_data['chosen_phone']} а так же {user_data['chosen_model']} {user_data['chosen_kuzov']} {user_data['chosen_date']} {user_data['chosen_info']} "
    )
    await message.answer(
        text='Отлично! Переходим к самому приятному блоку) Выбери то, как будут выглядеть твои будущие коврики'
    )
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_4")
    )
    await message.answer(
        text="Выберете тип коврика и отправь его номер в сообщении:",
        reply_markup=builder.as_markup()
    )
    await state.set_state(MakeOrder.type_of)

# Добавить гифку

#
#
# тут надо добавить выбор ромб или сота


@router.message(MakeOrder.type_of)
async def order_6(message: Message, state: FSMContext):
    await state.update_data(chosen_typeof=message.text)
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton(
        text="Выбрать тип коврика",
        callback_data="choose_type")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_5")
    )
    await message.answer(
        text='Наши коврики: \n \
▫️без запаха \n \
▫️не впитывают влагу \n \
▫️ложатся без щелей и зазоров\n \
▫️легко моются и обслуживаются\n \
▫️удерживают грязь и воду, поэтому обувь остается чистой'
    )
    await message.answer(
        text="Выберите тип покрытия",
        reply_markup=builder.as_markup()
    )
    await state.set_state(MakeOrder.material_of)


@router.callback_query(F.data == 'choose_type')
async def ordery_7_1(query: CallbackQuery, state: FSMContext):
    await state.set_state(MakeOrder.material_of)


@router.message(MakeOrder.material_of)
async def order_7(message: Message, state: FSMContext):
    # await state.update_data(chosen_materialof=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_6")
    )
    await message.answer(text='*картинка с инфографикой с цветами"')
    await message.answer(
        text='Введите номер цвета коврика и цвета канта\nЦвет не влияет на стоимость ',
        reply_markup=builder.as_markup()
    )
    await state.set_state(MakeOrder.color_cover)


# @router.message(MakeOrder.color_of)
# @router.callback_query(F.data == 'choose_color')
# async def order_7(query: CallbackQuery, state: FSMContext):
#     # await state.update_data(chosen_colorof=message.text)

#     builder = InlineKeyboardBuilder()

#     builder.add(types.InlineKeyboardButton(
#         text="Мне нужна помощь",
#         callback_data="help")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text="Назад",
#         callback_data="back_to_input_7")
#     )
#     await query.message.answer_dice()
#     await query.message.edit_text(text='Выбери цвет коврика и напиши его номер в поле ниже', reply_markup=builder.as_markup)
#     await state.set_state(MakeOrder.color_cover)


@router.message(MakeOrder.color_cover)
async def order_8(message: Message, state: FSMContext):
    await state.update_data(chosen_colorof=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Продолжить",
        callback_data="continue_dopnik")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_8")
    )
    await message.answer(text='Видео о важности допников')
    await message.answer(text='Осталось еще чуть чуть! Заполни последних важный блок! \n От него зависит, насколько ровно лягут коврики', reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.color_cant)


@router.message(MakeOrder.color_cant)
@router.callback_query(F.data == 'continue_dopnik')
async def order_9(query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_9")
    )
    await query.message.answer(text='Картинка \n')
    await query.message.answer(text='Укажи тип крепления для ковриков \n\n \
У каждого автомобиля есть свои заводские штатные крепления:\n\
-крючки\n-штыри\n-поворотные механизмы\n\n\
Они нужны для дополнительной безопасности и фиксации, чтобы коврик случайным образом не запал под педали газа и тормоза', reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.dopniki)


@router.message(MakeOrder.dopniki)
async def order_10(message: Message, state: FSMContext):
    await state.update_data(type_of_fastening=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_10")
    )
    await message.answer(text='Картинка \n')
    await message.answer(text='Выбере тип подпятника \n\
Зачем он вообще нужен? Надежно защищает от вмятин и трещин, увеличивает срок службы водительского коврика', reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.pyatka)


@router.message(MakeOrder.dopniki)
async def order_10(message: Message, state: FSMContext):
    await state.update_data(type_of_fastening=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_11")
    )
    await message.answer(text='Картинка \n')
    await message.answer(text='Выбере тип подпятника \n\
Зачем он вообще нужен? Надежно защищает от вмятин и трещин, увеличивает срок службы водительского коврика', reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.pyatka)


@router.message(MakeOrder.pyatka)
async def order_11(message: Message, state: FSMContext):
    await state.update_data(type_of_pyatka=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Да",
        callback_data="yes_shield")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нет",
        callback_data="no_shield")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_12")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    await message.answer(text='Видео с шильдиками \n')
    await message.answer(text='Нужны ли на твои коврики шильдики? \n\
-брендируют коврики\n-улучшают визуал\n\n Смотри видео, чтобы заценить как смотрятся 🔥', reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.shield)


@router.message(MakeOrder.shield)
@router.callback_query(F.data == 'yes_shield')
async def order_12_summary(query: CallbackQuery, state: FSMContext):
    await state.update_data(shield='Нужен')
    user_data = await state.get_data()
    await query.message.answer(text='Фото')
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Получить скидку 5%",
        callback_data="finally")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_13")
    )
    await query.message.answer(text=f"\
Спасибо за заказ! Мы уже подбираем лекала под твои коврики🔥\n\
Проверь, все ли данные в заказе верны, особенно телефон\n\
Если нужно что-то поправить, напиши в поле ниже, мы разберемся :)\n\
Ваше имя: {user_data['chosen_name']}\n\
Ваш телефон: {user_data['chosen_phone']}\n\
Марка и модель: {user_data['chosen_model']}\n\
Год выпуска: {user_data['chosen_date']}\n\
Кузов авто: {user_data['chosen_kuzov']}\n\
Доп.информация: {user_data['chosen_info']}\n\
Тип коврика: {user_data['chosen_typeof']}\n\
Цвет: {user_data['chosen_colorof']}\n\
Тип крепления: {user_data['type_of_fastening']}\n\
Тип подпятника: {user_data['type_of_pyatka']}\n\
Шилдик: {user_data['shield']}", reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.final)


@router.message(MakeOrder.shield)
@router.callback_query(F.data == 'no_shield')
async def order_12_summary(query: CallbackQuery, state: FSMContext):
    await state.update_data(shield='Не нужен')
    user_data = await state.get_data()
    await query.message.answer(text='Фото')
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Получить скидку 5%",
        callback_data="finally")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мне нужна помощь",
        callback_data="help")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_input_13")
    )
    await query.message.answer(text=f"\
Спасибо за заказ! Мы уже подбираем лекала под твои коврики🔥\n\
Проверь, все ли данные в заказе верны, особенно телефон\n\
Если нужно что-то поправить, напиши в поле ниже, мы разберемся :)\n\
Ваше имя: {user_data['chosen_name']}\n\
Ваш телефон: {user_data['chosen_phone']}\n\
Марка и модель: {user_data['chosen_model']}\n\
Год выпуска: {user_data['chosen_date']}\n\
Кузов авто: {user_data['chosen_kuzov']}\n\
Доп.информация: {user_data['chosen_info']}\n\
Тип коврика: {user_data['chosen_typeof']}\n\
Цвет: {user_data['chosen_colorof']}\n\
Тип крепления: {user_data['type_of_fastening']}\n\
Тип подпятника: {user_data['type_of_pyatka']}\n\
Шилдик: {user_data['shield']}", reply_markup=builder.as_markup())
    await state.set_state(MakeOrder.final)


@router.message(MakeOrder.final)
@router.callback_query(F.data == 'finally')
async def order_13_final(query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    print(user_data)
    await query.message.answer(text='*Видео*')
    await query.message.answer(text='Мы свяжемся в ближайшее время для подтверждения заказа!\n\
А пока ты можешь посмотреть ролик о другой нашей продуккции и получить скидку 5%')


# Функционал
# ОтветвлениеРомб или сота
# Поправить все кнопки "Назад"
# Подумать че делать с кнопкой "Мне нужна помощь" -------Мб их захардкодить?
# Отдельный линейный выбор цвета коврика и цвета канта
# Вывод всех данных в финале
# Сообщения после бездействия
# Тест отправки письма на почту


# Визуал
# Начать делать красивый текст, форматирование и отступы
# Начать добавлять картинки


# Тестирование нежелательных данных, фильтры?
# Завернуть в контейнер, и запустить локально в контейнере
# Деплой контейнера на VPS
