class EmptyHealthError(Exception):
    def __init__(self):
        super().__init__("health mustn't be empty")


class HealthContainError(Exception):
    def __init__(self):
        super().__init__("health must contain only int")


class HealthTypeError(Exception):
    def __init__(self):
        super().__init__("health must be a int or a list of int")
