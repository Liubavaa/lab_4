# Complicated game "Wanderer"

## Instaliation

Print in your terminal:

```bash
git clone https://github.com/Liubavaa/lab_4/task_6
```

Then:

```bash
python3 task_6/my_main_game.py
```

##  Rules of the game

The player travels through the rooms, which are objects and characters: friends, enemies, sellers and buyers. 
Player can:
- take item that is in room
- talk to every character and find out the price information
- combine items and get new ones
- help your friend and get prize
- bargain with traders for the price of the item
- buy item
- sell item
- fight with enemies(actually player will help them)
After defeating two enemies secret room with the last enemy will be opened.

## Module my_game_class.py

Module contains classes of the game: Room, SecretRoom, Item, Backpack, Character, Friend, Enemy, Trader, Seller, Buyer.

## Module my_main_game.py

The module contains the main cycle of the game and assigning values to rooms, objects and characters.

## Example of usage

```
Майстерня
--------------------
Велика дерев'яна кімната з купою інструментів.

Бібліотека - захід
Водосховище - північ
Столова - схід

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Лялька', 'Золото']
> захід


Бібліотека
--------------------
Розграбована кімната, де залишилась єдина книжка.

Майстерня - схід
Роза тут! - Твоя молодша сестра.

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Лялька', 'Золото']
> поговорити
[Роза каже]: Повезло тобі, я теж хочу молодшу сестричку


Бібліотека
--------------------
Розграбована кімната, де залишилась єдина книжка.

Майстерня - схід
Роза тут! - Твоя молодша сестра.

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Лялька', 'Золото']
> допомогти
Чим ти хочеш допомогти?
Введи номер предмета в інвентарі: 3

Роза каже: Це саме те що я хотіла. У мене недавно випав зуб, тому тримай.
Ти отримав Зуб !
[Зуб] - Молочний зуб меншої сестри


Бібліотека
--------------------
Розграбована кімната, де залишилась єдина книжка.

Майстерня - схід

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Золото', 'Зуб']
> схід


Майстерня
--------------------
Велика дерев'яна кімната з купою інструментів.

Бібліотека - захід
Водосховище - північ
Столова - схід

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Золото', 'Зуб']
> схід


Столова
--------------------
Порожні столики та посуда.

Дитяча - північ
Майстерня - захід
Підвал - південь

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Золото', 'Зуб']
> північ


Дитяча
--------------------
Стіни оббиті різкольоровими обоями. Можна побачити ляльки на полиці.

Водосховище - захід
Столова - південь
Офіс - схід
Стьопа тут! - Циган беззубий.

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Золото', 'Зуб']
> поговорити
[Стьопа каже]: Поможіть, я щедро заплачу)
Заплачу 1400 грн за Золотий зуб.


Дитяча
--------------------
Стіни оббиті різкольоровими обоями. Можна побачити ляльки на полиці.

Водосховище - захід
Столова - південь
Офіс - схід
Стьопа тут! - Циган беззубий.

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Золото', 'Зуб']
> торгуватися
Твоя ціна: 2000
Нууу, давай 1600 і по рукам.


Дитяча
--------------------
Стіни оббиті різкольоровими обоями. Можна побачити ляльки на полиці.

Водосховище - захід
Столова - південь
Офіс - схід
Стьопа тут! - Циган беззубий.

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Золото', 'Зуб']
> торгуватися
Твоя ціна: 2400
Нууу, давай 1866 і по рукам.


Дитяча
--------------------
Стіни оббиті різкольоровими обоями. Можна побачити ляльки на полиці.

Водосховище - захід
Столова - південь
Офіс - схід
Стьопа тут! - Циган беззубий.

У тебе 0 грн
Твій інвентар: ['Ножиці', 'Стакан води', 'Золото', 'Зуб']
> торгуватися
Твоя ціна: 3000
Нууу, давай 2244 і по рукам.
```
