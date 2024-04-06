import asyncio

from fight_club import Octagon, UFCFighter, Square


async def main():
    fighter_1 = UFCFighter(
        name="Dmitriy",
        age=18,
        punch_power=[i for i in range(15, 26)]
    ) + 100
    fighter_2 = UFCFighter(
        name="Igor",
        age=18,
        punch_power=[i for i in range(15, 26)]
    ) + 100

    octagon = Octagon(
        name="Octagon",
        square=Square(20, 20),
        fighter_1=fighter_1,
        fighter_2=fighter_2,
    )
    await octagon.fight()


if __name__ == "__main__":
    asyncio.run(main())
