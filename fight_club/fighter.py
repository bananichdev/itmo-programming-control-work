from abc import ABC, abstractmethod
from random import randint, choice

from exceptions import (
    EmptyHealthError,
    HealthTypeError,
    HealthContainError,
    EmptyPunchPowerError,
    PunchPowerContainError,
    PunchPowerTypeError
)

from utils.fight_arts import FightArts


class Fighter(ABC):
    def __init__(self, name: str, age: int, fight_art: FightArts | None = None,
                 health: list[int] | int = [100], punch_power: list[int] = [20]):
        self.name = name
        self.age = age
        self.fight_art = fight_art
        if isinstance(health, list):
            if not health:
                raise EmptyHealthError()
            if all(isinstance(num, int) for num in health):
                self.health = choice(health)
            else:
                raise HealthContainError()
        elif isinstance(health, int):
            self.health = health
        else:
            raise HealthTypeError()
        if isinstance(punch_power, list):
            if not punch_power:
                raise EmptyPunchPowerError()
            if all(isinstance(num, int) for num in punch_power):
                self.punch_power = punch_power
            else:
                raise PunchPowerContainError()
        else:
            raise PunchPowerTypeError()

    @abstractmethod
    def punch(self) -> int:
        """Return a random int(given damage) from punch_power range"""
        ...

    def take_damage(self, damage: int) -> int:
        """Return 0 if fighter take the defeat else remaining health"""
        self.health -= damage
        if self.health <= 0:
            return 0
        return self.health

    def win(self, fights: int, wins: int):
        """Print info about winner and exit from program"""
        print(self)
        print("Win!!!\n")
        print(f"{fights} fights, {wins} wins")

    def __add__(self, power: int):
        return self.__class__(name=self.name, age=self.age, punch_voice=self.punch_voice,
                              health=self.health, punch_power=list(map(lambda num: num + power, self.punch_power)))

    def __sub__(self, power: int):
        return self.__class__(name=self.name, age=self.age, punch_voice=self.punch_voice,
                              health=self.health, punch_power=list(map(lambda num: num - power, self.punch_power)))

    def __str__(self) -> str:
        return (f"\nFighter: {self.name}\n"
                f"Age: {self.age}\n"
                f"Fight art: {self.fight_art}\n"
                f"Remaining health: {self.health}\n")


class MixinFighterHeal:
    """Mixin class for UFCFighter"""
    @staticmethod
    def __heal_condition(func):
        def wrapper(self, cond):
            if cond:
                return func(self)
            return 0
        return wrapper

    @__heal_condition
    def heal(self):
        if self.health < 70 and randint(0, 1):
            health = randint(10, 15)
            self.health += health
            return health
        elif self.health >= 70 and randint(1, 3) == 2:
            health = randint(5, 10)
            if self.health + health <= 100:
                self.health += health
                return health
            health = 100 - self.health
            self.health = 100
            return health
        return 0


class UFCFighter(Fighter, MixinFighterHeal):
    def __init__(self, name: str, age: int,
                 health: list = [100], punch_power: list = [20],
                 punch_voice: list = ["Hook", "Uppercut"]):
        super().__init__(name, age, "UFC", health, punch_power)
        self.punch_voice = punch_voice

    def punch(self) -> tuple[str, int]:
        """Return a sting with punch voice and random int(given damage) from punch_power range"""
        return choice(self.punch_voice), choice(self.punch_power)


class KarateFighter(Fighter, MixinFighterHeal):
    def __init__(self, name: str, age: int,
                 health: list = [100], punch_power: list = [20],
                 punch_voice: list = ["Kick", "Palm strike"]):
        super().__init__(name, age, "Karate", health, punch_power)
        self.punch_voice = punch_voice

    def punch(self) -> tuple[str, int]:
        """Return a sting with punch voice and random int(given damage) from punch_power range"""
        return choice(self.punch_voice), choice(self.punch_power)
