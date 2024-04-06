class FightEnd(Exception):
    def __init__(self):
        super().__init__("Fight have ended")
