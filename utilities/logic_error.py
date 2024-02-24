class LogicError(Exception):
    def __init__(self, message="A logic error occurred."):
        self.message = message
        super().__init__(self.message)