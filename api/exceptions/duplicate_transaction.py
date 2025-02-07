

class DuplicateTransaction(Exception):

    def __init__(self, message="Duplicate Transaction"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"