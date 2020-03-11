class Ebook:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.price = 0.0
        self.cover = ''
        self.intro = ''

    def serialize(self):
        return self.__dict__
