class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all_contracts]
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all_contracts])
    pass


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self] 
    
    def authors(self):
        return [contract.author for contract in Contract.all_contracts if contract.book == self]

    pass


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception
        self.author = author
        if not isinstance(book, Book):
            raise Exception
        if not isinstance(date, str):
            raise Exception
        if not isinstance(royalties, int):
            raise Exception
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
    pass