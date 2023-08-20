class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

book = Book('Book', 320)
print(len(book)) # 320
# book is object, usually len(book) throws error, but dundar method __len__ solves the issue
