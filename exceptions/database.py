class DatabaseError(Exception):
    def __init__(self):
        super().__init__("error while working with the database")
