class AdminNotFoundException(Exception):
    def __init__(self, message="Vehicle with that ID doesnot exists"):
        self.message = message
        super().__init__(self.message)
