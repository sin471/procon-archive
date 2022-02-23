from sys import stdin
import typing

# 1:=通行可能 0:通行不能
room = [[1]*30 for _ in range(30)]


class Creature():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.direction = "U"

    def _basic_act(self, command: str):
        if command == ".":
            pass
        elif command == "U":
            self.x -= 1
        elif command == "D":
            self.x += 1
        elif command == "L":
            self.y -= 1
        elif command == "R":
            self.y += 1

    def can_pass(self, x: int, y: int):
        if not (1 <= x <= 30):
            return False

        if not (1 <= y <= 30):
            return False

        return room[x-1][y-1]

    def exist(self, x: int, y: int):
        if self.x == x and self.y == y:
            return True
        else:
            return False


class Person(Creature):
    def __init__(self, x: int, y: int, i: int):
        super().__init__(x, y)
        self.number = i

    def __impassable(self, command: str):
        if command == "u":
            room[self.x-2][self.y-1] = 0
        elif command == "d":
            room[self.x][self.y-1] = 0
        elif command == "l":
            room[self.x-1][self.y-2] = 0
        elif command == "r":
            room[self.x-1][self.y] = 0

    def move_down(self):
        command = "."
        if self.can_pass(self.x+1, self.y):
            command = "D"
            self._basic_act(command)

        return command

    def spread_crosswise(self):
        width = 3
        column = self.number*width
        command = "."
        if self.y < column:
            command = "R"

        elif self.y > column:
            command = "L"

        self._basic_act(command)
        return command

    def move_palewise(self):
        if not self.can_pass(self.x-1, self.y):
            self.direction = "D"

        elif not self.can_pass(self.x+1, self.y):
            self.direction = "U"

        command = self.direction

        self._basic_act(command)
        return command

    def impassable_left_column(self):
        if can_make_impassable(self.x, self.y-1):
            command = "l"
            self.__impassable(command)
        else:
            command = self.move_palewise()

        return command


class Cow(Creature):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.actable_number = 1

    def act(self, command: str):
        self._basic_act(command)


class Pig(Creature):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.actable_number = 2

    def act(self, commands: str):
        for command in commands:
            self._basic_act(command)


class Rabbit(Creature):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.actable_number = 3

    def act(self, commands: str):
        for command in commands:
            self._basic_act(command)


class Dog(Creature):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.actable_number = 2

    def act(self, commands: str):
        # todo:実装
        for command in commands:
            self._basic_act(command)


class Cat(Creature):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.actable_number = 2

    def act(self, commands: str):
        # todo:実装
        for command in commands:
            self._basic_act(command)


Pets_class = typing.Union[typing.Type[Cow], typing.Type[Pig],
                          typing.Type[Rabbit], typing.Type[Dog], typing.Type[Cat]]
Pets = typing.Union[Cow, Pig,
                    Rabbit, Dog, Cat]


def can_make_impassable(x: int, y: int):
    # todo:メソッド名と実装を変える("通行不能"に"できるか"だと分かりにくい)

    # if 1 <= x <= 30:return Trueなどにすると、他の条件を確認せずに終了してしまうのでダメ
    if not 1 <= x <= 30:
        return False
    if not 1 <= y <= 30:
        return False

    if not room[x-1][y-1]:
        return False

    for person in persons:
        if person.exist(x, y):
            return False

    for i, j in zip([0, 1, -1, 0, 0], [0, 0, 0, 1, -1]):
        for pet in pets:
            if pet.exist(x+i, y+j):
                return False

    return True


def judge_pets(pets_kind: int) -> Pets_class:
    pets_dict = {
        1: Cow,
        2: Pig,
        3: Rabbit,
        4: Dog,
        5: Cat
    }
    return pets_dict[pets_kind]


def input_():
    pet_num = int(stdin.readline())
    pets: typing.List[Pets] = []
    for _ in range(pet_num):
        x, y, pet_num = list(map(int, stdin.readline().split()))
        Species = judge_pets(pet_num)  # type:ignore
        pets.append(Species(x, y))
    person_num = int(stdin.readline())
    persons: typing.List[Person] = []
    for i in range(1, person_num+1):
        x, y = list(map(int, stdin.readline().split()))
        persons.append(Person(x, y, i))

    return pet_num, pets, person_num, persons


pet_num, pets, person_num, persons = input_()


def main():
    for i in range(300):
        if i < 30:
            commands = "".join(map(lambda person: person.move_down(), persons))

        elif 30 <= i < 60:
            commands = "".join(
                map(lambda person: person.spread_crosswise(), persons))

        else:
            # commands = "".join(
            # map(lambda person: person.impassable_left_column(), persons))
            commands = "".join([person.impassable_left_column() if person.number != 1 else "."
                                for person in persons])

        print(commands, flush=True)

        pet_commands = stdin.readline().split()

        for pet, pet_command in zip(pets, pet_commands):
            pet.act(pet_command)


main()
