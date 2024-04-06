class EmptyPunchPowerError(Exception):
    def __init__(self):
        super().__init__("punch_power mustn't be empty")


class PunchPowerContainError(Exception):
    def __init__(self):
        super().__init__("punch_power must contain only int")


class PunchPowerTypeError(Exception):
    def __init__(self):
        super().__init__("punch_power must be a list of int")
