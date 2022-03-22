"""Main module of the game"""
import my_game_class

library = my_game_class.Room("Бібліотека")
library.set_description("Розграбована кімната, де залишилась єдина книжка.")

workshop = my_game_class.Room("Майстерня")
workshop.set_description("Велика дерев'яна кімната з купою інструментів.")

reservoir = my_game_class.Room("Водосховище")
reservoir.set_description("Кімната з металевими стінами та дюжиною цистерн води.")

playroom = my_game_class.Room("Дитяча")
playroom.set_description("Стіни оббиті різкольоровими обоями. Можна побачити ляльки на полиці.")

dinning_room = my_game_class.Room("Столова")
dinning_room.set_description("Порожні столики та посуда.")

office = my_game_class.Room("Офіс")
office.set_description("Холодна кімната з порожніми робочими місцями.")

basement = my_game_class.Room("Підвал")
basement.set_description("Непроглядна темрява. З стелі капає вода...")

secret_room = my_game_class.Secret_Room("Секретна кімната")
secret_room.set_description("Краще було сюди не заходити.")

library.link_room(workshop, "схід")
workshop.link_room(library, "захід")
workshop.link_room(reservoir, "північ")
workshop.link_room(dinning_room, "схід")
reservoir.link_room(workshop, "південь")
reservoir.link_room(playroom, "схід")
playroom.link_room(reservoir, "захід")
playroom.link_room(dinning_room, "південь")
playroom.link_room(office, "схід")
dinning_room.link_room(playroom, "північ")
dinning_room.link_room(workshop, "захід")
dinning_room.link_room(basement, "південь")
basement.link_room(dinning_room, "північ")
office.link_room(playroom, "захід")
office.link_room(secret_room, "схід")
secret_room.link_room(office, "захід")

book = my_game_class.Item("Книга")
book.set_description("'Книга, про те як стати джентельменом'")
library.set_item(book)

flower = my_game_class.Item("Букет квітів")
flower.set_description("Яскравий букетик, що радує око)")
flower.set_price(2000)

scissors = my_game_class.Item("Ножиці")
scissors.set_description("Гостро заточені металеві ножиці")
workshop.set_item(scissors)

doll = my_game_class.Item("Лялька")
doll.set_description("Гарна дівчинка з довгим фіолетовим волоссям")
playroom.set_item(doll)

beer = my_game_class.Item("Пиво")
beer.set_description("Прохолодний освіжаючий бокальчик пивка")

water = my_game_class.Item("Стакан води")
water.set_description("Стаканчик холодної води")
reservoir.set_item(water)

grain = my_game_class.Item("Зерно")
grain.set_description("Маленьке зелене зерно")

gold = my_game_class.Item("Золото")
gold.set_description("Маленький шматочок золота, що виблискує на сонці")
office.set_item(gold)

thread = my_game_class.Item("Нитка")
thread.set_description("Шматок тонкої нитки")
dinning_room.set_item(thread)

wax = my_game_class.Item("Віск")
wax.set_description("Віск циліндричної форми")
basement.set_item(wax)

matches = my_game_class.Item("Коробка сірників")
matches.set_description("Коробочка сірників 'Козацька слава'. Залився один нещасний сірник.")

candle = my_game_class.Item("Свічка")
candle.set_description("Поки що толку з неї небагато")

fired_candle = my_game_class.Item("Запалена свічка")
fired_candle.set_description("А от така допоможе в темноті")

flowerpot = my_game_class.Item("Вазон")
flowerpot.set_description("Горшечок з глиною")
secret_room.set_item(flowerpot)

teeth = my_game_class.Item("Зуб")
teeth.set_description("Молочний зуб меншої сестри")

hop = my_game_class.Item("Хміль")
hop.set_description("Ну понятно)")

gold_teeth = my_game_class.Item("Золотий зуб")
gold_teeth.set_description("Те що треба циганам")
gold_teeth.set_price(1400)

grain.set_united_item(flowerpot, hop)
flowerpot.set_united_item(grain, hop)

hop.set_united_item(water, beer)
water.set_united_item(hop, beer)

wax.set_united_item(thread, candle)
thread.set_united_item(wax, candle)

matches.set_united_item(candle, fired_candle)
candle.set_united_item(matches, fired_candle)

teeth.set_united_item(gold, gold_teeth)
gold.set_united_item(teeth, gold_teeth)


rose = my_game_class.Friend("Роза", "Твоя молодша сестра")
rose.set_conversation("Повезло тобі, я теж хочу молодшу сестричку")
rose.set_success("Це саме те що я хотіла. У мене недавно випав зуб, тому тримай.")
rose.set_change(doll, teeth)
library.set_character(rose)

carl = my_game_class.Friend("Карл", "Твій друг школяр-хуліган")
carl.set_conversation("Мені це більше не подобається, я хочу стати хорошим")
carl.set_success("Клас, я погнав читати. Тримай, це мені більше не потрібно.")
carl.set_change(book, matches)
dinning_room.set_character(carl)

john = my_game_class.Friend("Джон",
                            "Садівник, який останні декілька років приглядав за твоїм садом")
john.set_conversation("Хочу зробити дерево у формі спіралі, а ще у формі коня...(")
john.set_success("Це точно мені допоможе. Ось тримай, воно тобі точно знадобиться ;)")
john.set_change(scissors, grain)
office.set_character(john)

grandma = my_game_class.Seller("Олівія", "Бабця-торговець")
grandma.set_conversation("Придбай букетик, порадуй даму")
grandma.set_goods(flower)
reservoir.set_character(grandma)

gypsy = my_game_class.Buyer("Стьопа", "Циган беззубий")
gypsy.set_conversation("Поможіть, я щедро заплачу)")
gypsy.set_goods(gold_teeth)
playroom.set_character(gypsy)

miya = my_game_class.Enemy("Mія", "Маленька чупакабра")
miya.set_conversation("Тут так темно і страшно :(")
miya.set_weakness(fired_candle)
miya.set_defeated("Тепер тут світло, ура!")
workshop.set_character(miya)

elisa = my_game_class.Enemy("Еліза", "Красива відьмочка")
elisa.set_conversation("Чому я нікому не подобаюсь?(плаче)")
elisa.set_weakness(flower)
elisa.set_defeated("Невже?...спасибі")
basement.set_character(elisa)

alcoholic = my_game_class.Enemy("Іван", "Алкоголік Іван")
alcoholic.set_conversation("Ддде...я? Скільки я вчора випив? як погано...")
alcoholic.set_weakness(beer)
alcoholic.set_defeated("Охххх, тепер як огірок")
secret_room.set_character(alcoholic)


current_room = library
backpack = my_game_class.Backpack([])
BALANCE = 0
DEFEATED_ENEMIES = 0

DEAD = False

while DEAD is False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()
    print("")
    print(f"У тебе {BALANCE} грн")
    print(f"Твій інвентар: {backpack}")

    command = input("> ")

    if command in ["північ", "південь", "схід", "захід"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "поговорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "допомогти":
        try:
            print("Чим ти хочеш допомогти?")
            item_id = int(input("Введи номер предмета в інвентарі: ")) - 1
            if inhabitant.help(backpack.backpack[item_id], backpack):
                current_room.character = None
        except IndexError:
            print("Некоректний номер.")
    elif command == "битися":
        if inhabitant is not None:
            try:
                print("Чим хочеш перемогти?")
                item_id = int(input("Введи номер предмета в інвентарі: ")) - 1
                if inhabitant.fight(backpack.backpack[item_id], backpack) is True:
                    current_room.character = None
                    DEFEATED_ENEMIES += 1
                    if DEFEATED_ENEMIES == 2:
                        print("Ти відкрив секретну кімнату")
                        print("Ось інформація про неї:")
                        secret_room.get_details()
                        print("")
                        print("Удачі в пошуках!")
                    elif DEFEATED_ENEMIES == 3:
                        print("")
                        print("Ти пройшов гру!")
                        DEAD = True
                else:
                    print("Ти програв.")
                    print("Кінець гри")
                    DEAD = True
            except IndexError:
                print("Некоректний номер.")
        else:
            print("Тут немає підходящого персонажа.")
    elif command == "взяти":
        if item is not None:
            print(item.get_name() + " тепер у інвентарі.")
            backpack.append(item)
            current_room.set_item(None)
        else:
            print("Тут нема що брати!")
    elif command == "об'єднати":
        try:
            first_id = int(input("Введи номер першого предмету в інвентарі: ")) - 1
            second_id = int(input("Введи номер другого предмету в інвентарі: ")) - 1
            item = backpack.backpack[first_id].unite(backpack.backpack[second_id], backpack)
            if item is not None:
                backpack.append(item)

        except IndexError:
            print("Некоректний номер.")
    elif command == "торгуватися":
        if isinstance(inhabitant, my_game_class.Trader):
            price = int(input("Твоя ціна: "))
            inhabitant.bargain(price)
        else:
            print("Тут немає підходящого персонажа.")
    elif command == "купити":
        if isinstance(inhabitant, my_game_class.Seller):
            new_balance = inhabitant.buy(backpack, BALANCE)
            if new_balance is not None:
                BALANCE = new_balance
                current_room.character = None
        else:
            print("Тут немає підходящого персонажа.")
    elif command == "продати":
        if isinstance(inhabitant, my_game_class.Buyer):
            new_balance = inhabitant.sell(backpack)
            if new_balance is not None:
                BALANCE += new_balance
                current_room.character = None
        else:
            print("Тут немає підходящого персонажа.")
    else:
        print("Неможна " + command)
