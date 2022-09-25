# Implement the Book class, as shown in the following diagram. 
# In the main program, create an object of class Book.

# ------------------------
# | Book                 |
# ------------------------
# | title                |
# | author               |
# | page_qty             |
# ------------------------
# _______________________|


class Book:
    def __init__(self, title, author, page_qty):
        self.title = title
        self.author = author
        self.page_qty = page_qty

book1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 264)
print(book1.title)
print(book1.author)
print(book1.page_qty)
