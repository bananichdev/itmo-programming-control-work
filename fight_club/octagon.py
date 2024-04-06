from random import randint
from asyncio import sleep
from time import time

from database.controllers.fighter import FighterController

from exceptions import FightEnd

from .fighter import UFCFighter, KarateFighter

from multiprocessing.pool import ThreadPool


class Square:
    def __init__(self, width: int, length: int):
        if not isinstance(width, int) or not isinstance(length, int):
            raise AttributeError("width and length must be int")
        self.width = width
        self.length = length

    def __str__(self):
        return f"{self.width}cm × {self.length}cm"


class Octagon:
    def __init__(self, name: str, square: Square,
                 fighter_1: UFCFighter | KarateFighter, fighter_2: UFCFighter | KarateFighter):
        if not isinstance(square, Square):
            raise AttributeError("square must be instance of Square")
        if not isinstance(name, str):
            raise AttributeError("square must be instance of str")
        self.name = name
        self.square = square
        self.fighters = (fighter_1, fighter_2)
        self.round = 1
        self.controller = FighterController()
        self.pool = ThreadPool(processes=1)

    @staticmethod
    def __fight_timer(func):
        async def wrapper(self):
            start = time()
            await self.controller.register_fighter(self.fighters[0])
            await self.controller.register_fighter(self.fighters[1])
            await self.controller.update_fights(*self.fighters)
            await func(self)
            end = time() - start
            print(f"The fight lasted {round(end)} seconds")
        return wrapper

    @__fight_timer
    async def fight(self):
        print(f"The fight at the {self} begins!!!\n")
        await sleep(2)
        while True:
            try:
                print(f"Round {self.round}\n")
                fighter_idx = randint(0, 1)
                if self.round > 1:
                    heal = self.fighters[fighter_idx].heal(randint(0, 1))
                    if heal:
                        print(f"Fighter {self.fighters[fighter_idx].name} heal {heal} HP\n"
                              f"Remaining health {self.fighters[fighter_idx].health}\n")
                        await sleep(3)
                    heal = self.fighters[1 - fighter_idx].heal(randint(0, 1))
                    if heal:
                        print(f"Fighter {self.fighters[1 - fighter_idx].name} heal {heal} HP\n"
                              f"Remaining health {self.fighters[1 - fighter_idx].health}\n")
                        await sleep(3)
                voice, damage = self.pool.apply_async(self.fighters[fighter_idx].punch).get()
                health = self.fighters[1 - fighter_idx].take_damage(damage)
                print(f"{voice} from {self.fighters[fighter_idx].name} "
                      f"to {self.fighters[1 - fighter_idx].name} damaged {damage}\n"
                      f"{self.fighters[1 - fighter_idx].name} remaining health: {health}\n")
                await sleep(3)
                if not health:
                    raise FightEnd()
                self.round += 1
            except FightEnd as e:
                print(e)
                await sleep(2)
                await self.controller.update_wins(self.fighters[fighter_idx])
                fighter_entity = await self.controller.select_fighter_by_name(self.fighters[fighter_idx].name)
                self.fighters[fighter_idx].win(fighter_entity.fights, fighter_entity.wins)
                break

    def __str__(self):
        return f"Octagon {self.name} sized {self.square}"
