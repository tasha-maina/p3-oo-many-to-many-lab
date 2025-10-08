class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return a list of all contracts related to this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of authors who have contracts for this book."""
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"<Book {self.title}>"


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return a list of all contracts for this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of books for this author via contracts."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new contract between author and book."""
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book.")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return total royalties for this author."""
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"<Author {self.name}>"


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # ============ VALIDATIONS ============

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("royalties must be a number")
        self._royalties = value

    # ============ CLASS METHOD ============

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that match a given date."""
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f"<Contract {self.author.name} - {self.book.title} ({self.date})>"
