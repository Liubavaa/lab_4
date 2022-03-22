"""Module contain class for game"""


class Room:
    """Class of room"""
    def __init__(self, name):
        """Initialises class object"""
        self.name = name
        self._description = None
        self._linked_rooms = []
        self.character = None
        self._item = None

    def set_description(self, description):
        """Set description of the room"""
        self._description = description

    def get_details(self):
        """Return all information about the room and the nearest rooms"""
        print(self.name)
        print('--------------------')
        print(self._description)
        for room, direction in self._linked_rooms:
            print(f"The {room.name} is {direction}")

    def link_room(self, room, direction):
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

    def move(self, direction):
        """Move to the room in given direction"""
        for room, room_direction in self._linked_rooms:
            if room_direction == direction:
                return room
        print(f"There are no rooms in this direction. You are still in the {self.name}.")
        return self


class Item:
    """Class of item"""
    def __init__(self, name):
        """Initialises class object"""
        self._name = name
        self._description = None

    def get_name(self):
        """Return item's name"""
        return self._name

    def set_description(self, description):
        """Set description about the item"""
        self._description = description

    def describe(self):
        """Return all information about the item"""
        print(f"The [{self.get_name()}] is here - {self._description}")


class Character:
    """Class of character"""
    def __init__(self, name, description):
        """Initialises class object"""
        self.name = name
        self._description = description
        self._phrase = None

    def set_conversation(self, phrase):
        """Set the phrase that the character should say"""
        self._phrase = phrase

    def describe(self):
        """Return all information about the character"""
        print(f"{self.name} is here!")
        print(self._description)

    def talk(self):
        """Print character's phrase"""
        print(f"[{self.name} says]: {self._phrase}")


class Friend(Character):
    """Class of friend"""


DEFEATED_ENEMIES = 0


class Enemy(Character):
    """Class of enemy"""
    def __init__(self, name, description):
        """Initialises class object"""
        super().__init__(name, description)
        self._weakness = None

    def set_weakness(self, weakness):
        """Set weakness of the enemy"""
        self._weakness = weakness

    def fight(self, item: Item):
        """Check if the item is enemy's weakness"""
        if self._weakness == item:
            print(f"You fend {self.name} off with the {item}")

            global DEFEATED_ENEMIES
            DEFEATED_ENEMIES += 1

            return True
        print(f"{self.name} crushes you, puny adventurer!")
        return False

    def get_defeated(self):
        """Check if user fights two enemies"""
        global DEFEATED_ENEMIES
        return DEFEATED_ENEMIES
