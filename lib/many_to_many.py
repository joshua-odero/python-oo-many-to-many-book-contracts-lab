class Book:
    #class attributes
    all = []

    #Initialize the book object instance attributes
    def __init__(self, title):
        self.title = title

    #Methods
    #method to return all contracts related to a book using Contract object
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    #method to return all authors related to a book using Contract object as intermediary
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Author:

    #Class attributes
    all = []

    #Initialize author object instance attributes
    def __init__(self, name):
        self.name = name

    #properties with @property decorator to control name property(to be a string)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_value):
        if not isinstance(name_value, str):
            raise Exception
        self._name = name_value

    #Methods
    #method to return all contracts related to an author using Contract object as intermediary
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    #method to return all authors related to an author using Contract object as intermediary
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    #method that creates and return a new Contract object between the author and the specified book with the specified date and royalties
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)

    #Method to return the total number of royalties that the author has earned from all their contracts
    #Use generator with sum()
    def total_royalties(self):
        return sum(contract.royalties for contract in Contract.all if contract.author == self)


class Contract:

    #Class attributes
    all = []
    
    #Initialize contract object instance attributes
    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    #properties with @property decorator to raise an error if not valid
    #check if author instance property belongs to Author class
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author_value):
        if not isinstance(author_value, Author):
            raise Exception
        self._author = author_value

    @property
    def book(self):
        return self._book
    
    #check if book instance property belongs to Book class
    @book.setter
    def book(self, book_value):
        if not isinstance(book_value, Book):
            raise Exception
        self._book = book_value
    
    @property
    def date(self):
        return self._date
    
    #check if date instance property is a string
    @date.setter
    def date(self, date_value):
        if not isinstance(date_value, str):
            raise Exception
        self._date = date_value

    @property
    def royalties(self):
        return self._royalties
    
    #check if royalties instance property is an integer
    @royalties.setter
    def royalties(self, royalties_value):
        if not isinstance(royalties_value, int):
            raise Exception
        self._royalties = royalties_value


    #Class Method
    #Return all contracts that have the same date as the date passed into the method.
    @classmethod
    def contracts_by_date(cls,date_value):
        return [contract for contract in cls.all if contract.date == date_value]
    

    