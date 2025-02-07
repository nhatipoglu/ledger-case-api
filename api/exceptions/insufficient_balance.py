class InsufficientBalance(Exception):

    def __init__(self, message="Insufficient Balance"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
