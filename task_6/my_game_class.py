"""Module with game classes"""


class Room:
    """Class of room"""
    def __init__(self, name: str):
        """Initialises class object"""
        self.name = name
        self._description = None
        self._linked_rooms = []
        self.character = None
        self._item = None

    def set_description(self, description: str):
        """Set description of the room"""
        self._description = description

    def get_details(self):
        """Return all information about the room and the nearest rooms"""
        print(self.name)
        print('--------------------')
        print(self._description)
        print('')
        for room, direction in self._linked_rooms:
            if not isinstance(room, SecretRoom):
                print(f"{room.name} - {direction}")

    def link_room(self, room, direction: str):
        """Set tne nearest room"""
        self._linked_rooms.append((room, direction))

    def set_character(self, character):
        """Set the character in the room"""
        self.character = character

    def get_character(self):
        """Return the character that is in the room"""
        return self.character

    def set_item(self, item):
        """Set the item in the room"""
        self._item = item

    def get_item(self):
        """Return the item that is in the room"""
        return self._item

    def move(self, direction: str):
        """Move to the room in given direction"""
        for room, room_direction in self._linked_rooms:
            if room_direction == direction:
                return room
        print(f"Там немає кімнат. Ти досі в {self.name}.")
        return self


class SecretRoom(Room):
    """Class of secret room"""


class Item:
    """Class of item"""
    def __init__(self, name: str):
        """Initialises class object"""
        self._name = name
        self._description = None
        self._price = None
        self._united_with = None
        self._result = None

    def get_name(self):
        """Return item's name"""
        return self._name

    def set_description(self, description: str):
        """Set description about the item"""
        self._description = description

    def describe(self):
        """Return all information about the item"""
        print(f"[{self.get_name()}] - {self._description}")

    def set_price(self, price: int):
        """Set price of item"""
        self._price = price

    def get_price(self):
        """Return price of item"""
        return self._price

    def set_united_item(self, united_item, resulted_item):
        """Set item that can be united and resulted item"""
        self._united_with = united_item
        self._result = resulted_item

    def unite(self, item, backpack):
        """Uniting two item"""
        if item == self._united_with:
            got_item = self._result
            print(f'Ти отримав {got_item.get_name()}!')
            got_item.describe()
            backpack.append(got_item)
            backpack.remove(self)
            backpack.remove(item)
        else:
            print("Неможливо обє'днати(")


class Backpack:
    """Class of item"""
    def __init__(self, backpack: list):
        """Initialises class object"""
        self.backpack = backpack

    def append(self, item: Item):
        """Add item to backpack"""
        self.backpack.append(item)

    def remove(self, item: Item):
        """Remove item with backpack"""
        self.backpack.remove(item)

    def __str__(self):
        """Print backpack"""
        backpack_lst = [item.get_name() for item in self.backpack]
        return str(backpack_lst)


class Character:
    """Class of character"""
    def __init__(self, name: str, description: str):
        """Initialises class object"""
        self.name = name
        self._description = description
        self._phrase = None

    def set_conversation(self, phrase: str):
        """Set the phrase that the character should say"""
        self._phrase = phrase

    def describe(self):
        """Return all information about the character"""
        print(f"{self.name} тут! - {self._description}.")

    def talk(self):
        """Print character's phrase"""
        print(f"[{self.name} каже]: {self._phrase}")


class Friend(Character):
    """Class of friend"""
    def __init__(self, name: str, description: str):
        """Initialises class object"""
        super().__init__(name, description)
        self._success = None
        self._want = None
        self._give = None

    def set_success(self, phrase: str):
        """If you helped friend"""
        self._success = phrase

    def set_change(self, wanted: Item, given: Item):
        """What can help friend and what he/she give"""
        self._want = wanted
        self._give = given

    def help(self, help_with: Item, backpack: Backpack):
        """If you can help"""
        if self._want == help_with:
            print("")
            print(f"{self.name} каже: {self._success}")
            backpack.remove(help_with)
            backpack.append(self._give)
            print(f"Ти отримав {self._give.get_name()} !")
            self._give.describe()
            return True
        print(f"{self.name} каже: це мені не допоможе.")
        return False


class Trader(Character):
    """Class of seller"""
    def __init__(self, name: str, description: str):
        """Initialises class object"""
        super().__init__(name, description)
        self._goods = None

    def set_goods(self, goods: Item):
        """Item that trader want/has"""
        self._goods = goods

    def get_goods(self) -> Item:
        """Return item"""
        return self._goods

    def bargain(self, new_price):
        """Bargain price of goods"""
        price = self.get_goods().get_price()
        if new_price <= int(price/2):
            price = int(price*1.5)
            print(f"{self.name} :")
            print('Добре... ')
            print('Ти це хотів почути, торгаш?')
            print(f'Нова ціна: {int(price*2)}')
            self.get_goods().set_price(price)
        elif new_price <= price:
            difference = price - new_price
            price = int(price - difference/3)
            print(f'{self.name} : Нууу, давай {price} і по рукам.')
            self.get_goods().set_price(price)
        elif new_price >= price*2:
            price = int(price/1.5)
            print(f"{self.name} :")
            print('Добре... ')
            print('Ти це хотів почути, торгаш?')
            print(f'Нова ціна: {int(price/2)}')
            self.get_goods().set_price(price)
        else:
            difference = new_price - price
            price = int(price + difference / 3)
            print(f'{self.name} : Нууу, давай {price} і по рукам.')
            self.get_goods().set_price(price)


class Seller(Trader):
    """Class of seller"""
    def talk(self):
        """Print character's phrase"""
        print(f"[{self.name} каже]: {self._phrase}")
        print(f"{self.get_goods().get_name()} коштує {self.get_goods().get_price()} грн.")

    def buy(self, backpack: Backpack, balance: int):
        """Buy item"""
        price = self.get_goods().get_price()
        if balance >= price:
            print(f"Ти отримав {self.get_goods().get_name()}!")
            self.get_goods().describe()
            backpack.append(self.get_goods())
            return balance-price
        print("У тебе недостатньо грошей(")
        return None


class Buyer(Trader):
    """Class of buyer"""
    def talk(self):
        """Print character's phrase"""
        print(f"[{self.name} каже]: {self._phrase}")
        print(f"Заплачу {self.get_goods().get_price()} грн за {self.get_goods().get_name()}.")

    def sell(self, backpack: Backpack):
        """Sell item"""
        if self.get_goods() in backpack.backpack:
            print(f"Ти отримав {self.get_goods().get_price()} грн!")
            backpack.remove(self.get_goods())
            return self.get_goods().get_price()
        print(f"Ти не маєш {self._goods.get_name()}.")
        return None


class Enemy(Character):
    """Class of enemy"""
    def __init__(self, name: str, description: str):
        """Initialises class object"""
        super().__init__(name, description)
        self._weakness = None
        self._defeated = None

    def set_weakness(self, weakness: Item):
        """Set weakness of the enemy"""
        self._weakness = weakness

    def set_defeated(self, phrase: str):
        """If user win"""
        self._defeated = phrase

    def fight(self, item: Item, backpack: Backpack):
        """Check if the item is enemy's weakness"""
        if self._weakness == item:
            backpack.remove(item)
            print("")
            print(f"{self.name} каже: {self._defeated}")
            print("Молодець!")
            return True
        print(f"{self.name} таке непотрібно!")
        return False
