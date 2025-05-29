class Store:
    def __init__(self, name: str, address: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(address, str):
            raise TypeError("Address must be a string.")
        self._id = None
        self._name = name
        self._address = address
        self._categories = []
        self._products = []

    def to_dict(self) -> dict:
        return {'id': self._id, 'name': self._name, 'address': self._address}

    def __str__(self) -> str:
        return str({'class': type(self).__name__, **self.to_dict(),
            'categories': [category.to_dict() for category in self._categories],
            'products': [product.to_dict() for product in self._products]})

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new: str) -> None:
        if not isinstance(new, str):
            raise TypeError("Name must be a string.")
        self._name = new

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, new: str) -> None:
        if not isinstance(new, str):
            raise TypeError("Address must be a string.")
        self._address = new

    @property
    def categories(self) -> tuple:
        return tuple(self._categories)

    def add_category(self, *categories: 'Category') -> None:
        for category in categories:
            if not isinstance(category, Category):
                raise TypeError(f"Expected Category instance, got {type(category).__name__}")
        for category in categories:
            if category not in self._categories:
                self._categories.append(category)
                category.set_store(self)

    def remove_category(self, *categories: 'Category') -> None:
        for category in categories:
            if not isinstance(category, Category):
                raise TypeError(f"Expected Category instance, got {type(category).__name__}")
        for category in categories:
            if category in self._categories:
                self._categories.remove(category)
                category.set_store(None)

    @property
    def products(self) -> tuple:
        return tuple(self._products)

    def add_product(self, *products: 'Product') -> None:
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
        for product in products:
            if product not in self._products:
                self._products.append(product)
                product.set_store(self)

    def remove_product(self, *products: 'Product') -> None:
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
        for product in products:
            if product in self._products:
                self._products.remove(product)
                product.set_store(None)
