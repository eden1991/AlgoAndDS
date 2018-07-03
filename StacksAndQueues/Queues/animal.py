class Animal():
    def __init__(self, type, breed):
        self.type = type
        self.breed = breed
        self.next = None
        self.previous = None

    def set_data(self, new_type, new_breed):
        self.type = new_type
        self.breed = new_breed

    def get_data(self):
        return self.type, self.breed

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

    def set_previous(self, new_previous):
        self.previous = new_previous

    def get_previous(self):
        return self.previous
