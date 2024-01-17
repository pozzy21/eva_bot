from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def poehali() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Поехали!")
    return kb.as_markup(resize_keyboard=True)


def super_pristupim() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Супер! Приступить к подбору")
    kb.button(text="Мне нужна помощь")
    return kb.as_markup(resize_keyboard=True)


def buy1() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Указать параметры моего авто")
    kb.button(text="Мне нужна помощь")
    kb.button(text="Назад")
    return kb.as_markup(resize_keyboard=True)


def buy2() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Мне нужна помощь")
    kb.button(text="Назад")
    return kb.as_markup(resize_keyboard=True)


def chose_help() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Перезвоните мне")
    kb.button(text="Напишите мне")
    return kb.as_markup(resize_keyboard=True)


def type_of() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Комплект ковриков в салон (1+2 ряд)")
    kb.button(text="Один коврик в салон")
    kb.button(text="Комплект на один ряд (1 или 2)")
    kb.button(text="Коврик в багажник")
    kb.button(text="Мне нужна помощь")
    kb.button(text="Назад")
    return kb.as_markup(resize_keyboard=True)


def material_of() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Ромб🔶")
    kb.button(text="Сота")
    return kb.as_markup(resize_keyboard=True)


def color_of() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Выберете цвет коврика")
    kb.button(text="Выберете цвет канта")
    kb.button(text="Мне нужна помощь")
    kb.button(text="Назад")
    return kb.as_markup(resize_keyboard=True)
