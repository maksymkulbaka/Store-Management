class Store:
    """Represents a Store structure containing Categories and Products."""
    def __init__(self, name: str, address: str):
        """Initialize a Store instance.

        Args:
            name (str): Name of the store.
            address (str): Address of the store.

        Raises:
            TypeError: If any argument is of incorrect type.
        """
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
        """Return a dictionary representation of the Store.

        Returns:
            dict: Store's basic information.
        """
        return {'id': self._id, 'name': self._name, 'address': self._address}

    def __str__(self) -> str:
        """Return a string representation of the Store including categories and products.

        Returns:
            str: Readable representation of the Store instance.
        """
        return str({'class': type(self).__name__, **self.to_dict(),
            'categories': [category.to_dict() for category in self._categories],
            'products': [product.to_dict() for product in self._products]})

    @property
    def id(self) -> int:
        """Return the Store's identifier.

        Returns:
            int: ID of the store.
        """
        return self._id

    @property
    def name(self) -> str:
        """Return the Store's name.

        Returns:
            str: Name of the store.
        """
        return self._name

    @name.setter
    def name(self, new: str) -> None:
        """Set a new name for the Store.

        Args:
            new (str): New name.

        Raises:
            TypeError: If new name is not a string.
        """
        if not isinstance(new, str):
            raise TypeError("Name must be a string.")
        self._name = new

    @property
    def address(self) -> str:
        """Return the Store's address.

        Returns:
            str: Address of the store.
        """
        return self._address

    @address.setter
    def address(self, new: str) -> None:
        """Set a new address for the Store.

        Args:
            new (str): New address.

        Raises:
            TypeError: If new address is not a string.
        """
        if not isinstance(new, str):
            raise TypeError("Address must be a string.")
        self._address = new

    @property
    def categories(self) -> tuple:
        """Return the Store categories.

        Returns:
            tuple: Categories of the store.
        """
        return tuple(self._categories)

    def add_category(self, *categories: 'Category') -> None:
        """Add one or more categories to the Store.

        Args:
            *categories (Category): One or more Category instances.

        Raises:
            TypeError: If any input is not a Category instance.
        """
        for category in categories:
            if not isinstance(category, Category):
                raise TypeError(f"Expected Category instance, got {type(category).__name__}")
        for category in categories:
            if category not in self._categories:
                self._categories.append(category)
                category.set_store(self)

    def remove_category(self, *categories: 'Category') -> None:
        """Remove one or more categories from the Store.

        Args:
            *categories (Category): One or more Category instances.

        Raises:
            TypeError: If any input is not a Category instance.
        """
        for category in categories:
            if not isinstance(category, Category):
                raise TypeError(f"Expected Category instance, got {type(category).__name__}")
        for category in categories:
            if category in self._categories:
                self._categories.remove(category)
                category.set_store(None)

    @property
    def products(self) -> tuple:
        """Return the Store products.

        Returns:
            tuple: Products of the store.
        """
        return tuple(self._products)

    def add_product(self, *products: 'Product') -> None:
        """Add one or more products to the Store.

        Args:
            *products (Product): One or more Product instances.

        Raises:
            TypeError: If any input is not a Product instance.
        """
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
        for product in products:
            if product not in self._products:
                self._products.append(product)
                product.set_store(self)

    def remove_product(self, *products: 'Product') -> None:
        """Remove one or more products from the Store.

        Args:
            *products (Product): One or more Product instances.

        Raises:
            TypeError: If any input is not a Product instance.
        """
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
        for product in products:
            if product in self._products:
                self._products.remove(product)
                product.set_store(None)


class Category:
    """Represents a Category belonging to a Store and containing Products."""
    def __init__(self, name: str):
        """Initialize a Category instance.

        Args:
            name (str): Name of the category.

        Raises:
            TypeError: If name is not a string.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self._id = None
        self._name = name
        self._products = []
        self._store = None

    def to_dict(self) -> dict:
        """Return a dictionary representation of the Category.

        Returns:
            dict: Category's basic information.
        """
        return {'id': self._id, 'name': self._name}

    def __str__(self) -> str:
        """Return a string representation of the Category including products and associated store.

        Returns:
            str: Readable representation of the Category instance.
        """
        return str({'class': type(self).__name__, **self.to_dict(),
            'products': [product.to_dict() for product in self._products],
            'store': self._store.to_dict() if self._store else None})

    @property
    def id(self) -> int:
        """Return the Category's identifier.

        Returns:
            int: ID of the category.
        """
        return self._id

    @property
    def name(self) -> str:
        """Return the Category's name.

        Returns:
            str: Name of the category.
        """
        return self._name

    @name.setter
    def name(self, new: str) -> None:
        """Set a new name for the Category.

        Args:
            new (str): New name.

        Raises:
            TypeError: If new name is not a string.
        """
        if not isinstance(new, str):
            raise TypeError("Name must be a string.")
        self._name = new

    @property
    def products(self) -> tuple:
        """Return the Category products.

        Returns:
            tuple: Products of the category.
        """
        return tuple(self._products)

    def add_product(self, *products: 'Product') -> None:
        """Add one or more products to the Category.

        Args:
            *products (Product): One or more Product instances.

        Raises:
            TypeError: If any input is not a Product instance.
        """
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
        for product in products:
            if product not in self._products:
                self._products.append(product)
                product.set_category(self)

    def remove_product(self, *products: 'Product') -> None:
        """Remove one or more products from the Category.

        Args:
            *products (Product): One or more Product instances.

        Raises:
            TypeError: If any input is not a Product instance.
        """
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
        for product in products:
            if product in self._products:
                self._products.remove(product)
                product.set_category(None)

    @property
    def store(self) -> Store:
        """Return the Category's store.

        Returns:
            Category: Store of the category.
        """
        return self._store

    def set_store(self, store: Store | None) -> None:
        """Set the parent Store for a Category.

        Args:
            store (Store | None): A Store instance or None.

        Raises:
            TypeError: If an input is not a Store or None instance.
        """
        if not isinstance(store, Store | None):
            raise TypeError(f"Expected Store or None instance, got {type(store).__name__}")
        if self._store is not None:
            self._store.remove_category(self)
        self._store = store
        if store is not None:
            store.add_category(self)


class Product:
    """Represents a Product belonging to a Category and a Store."""
    def __init__(self, name: str, price: int, quantity: int):
        """Initialize a Product instance.

        Args:
            name (str): Name of the product.
            price (int): Price of the product.
            quantity (int): Quantity of the product.

        Raises:
            TypeError: If any argument is of incorrect type.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(price, int):
            raise TypeError("Price must be an integer.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        self._id = None
        self._name = name
        self._price = price
        self._quantity = quantity
        self._category = None
        self._store = None

    def to_dict(self) -> dict:
        """Return a dictionary representation of the Product.

        Returns:
            dict: Product's basic information.
        """
        return {'id': self._id, 'name': self._name,
            'price': self._price, 'quantity': self._quantity}

    def __str__(self) -> str:
        """Return a string representation of the Product including its category and store.

        Returns:
            str: Readable representation of the Product instance.
        """
        return str({'class': type(self).__name__} | self.to_dict() | {
            'category': self._category.to_dict() if self._category else None,
            'store': self._store.to_dict() if self._store else None})

    @property
    def id(self) -> str:
        """Return the Product's identifier.

        Returns:
            int: ID of the product.
        """
        return self._id

    @property
    def name(self) -> str:
        """Return the Product's name.

        Returns:
            str: Name of the product.
        """
        return self._name

    @name.setter
    def name(self, new: str) -> None:
        """Set a new name for the Product.

        Args:
            new (str): New name.

        Raises:
            TypeError: If new name is not a string.
        """
        if not isinstance(new, str):
            raise TypeError("Name must be a string.")
        self._name = new

    @property
    def price(self) -> int:
        """Return the Product's price.

        Returns:
            int: Price of the product.
        """
        return self._price

    @price.setter
    def price(self, new: int) -> None:
        """Set a new price for the Product.

        Args:
            new (int): New price.

        Raises:
            TypeError: If new price is not an integer.
        """
        if not isinstance(new, int):
            raise TypeError("Price must be an integer.")
        self._price = new

    @property
    def quantity(self) -> int:
        """Return the Product's quantity.

        Returns:
            int: Quantity of the product.
        """
        return self._quantity

    @quantity.setter
    def quantity(self, new: int) -> None:
        """Set a new quantity for the Product.

        Args:
            new (int): New quantity.

        Raises:
            TypeError: If new quantity is not an integer.
        """
        if not isinstance(new, int):
            raise TypeError("Quantity must be an integer.")
        self._quantity = new

    @property
    def category(self) -> Category:
        """Return the Product's category.

        Returns:
            Category: Category of the product.
        """
        return self._category

    def set_category(self, category: Category | None) -> None:
        """Set the parent Category for a Product.

        Args:
            category (Category | None): A Category instance or None.

        Raises:
            TypeError: If an input is not a Category or None instance.
        """
        if not isinstance(category, Category | None):
            raise TypeError(f"Expected Category or None instance, got {type(category).__name__}")
        if self._category is not None:
            self._category.remove_product   (self)
        self._category = category
        if category is not None:
            category.add_product(self)

    @property
    def store(self) -> Store:
        """Return the Product's store.

        Returns:
            Category: Store of the product.
        """
        return self._store

    def set_store(self, store: Store | None) -> None:
        """Set the parent Store for a Product.

        Args:
            store (Store | None): A Store instance or None.

        Raises:
            TypeError: If an input is not a Store or None instance.
        """
        if not isinstance(store, Store | None):
            raise TypeError(f"Expected Store or None instance, got {type(store).__name__}")
        if self._store is not None:
            self._store.remove_product(self)
        self._store = store
        if store is not None:
            store.add_product(self)

class User:
    def __init__(self, name: str, surname: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(surname, str) or not surname.strip():
            raise ValueError("Surname must be a non-empty string.")
        self._id = None
        self._name = name
        self._surname = surname

    def to_dict(self) -> dict:
        return {'id': self._id, 'name': self._name, 'surname': self._surname}

    def __str__(self) -> str:
        return str({'class': type(self).__name__, **self.to_dict()})

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        if not isinstance(surname, str) or not surname.strip():
            raise ValueError("Surname must be a non-empty string.")
        self._surname = surname

class Cashier(User):

    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)

    def __str__(self) -> str:
        return str({'class': type(self).__name__, **self.to_dict()})

class Customer(User):

    def __init__(self, name: str, surname: str, phone: int):
        super().__init__(name, surname)
        if not isinstance(phone, int) or phone <= 0:
            raise ValueError("Phone must be a positive integer.")
        super().__init__(name, surname)
        self._phone = phone
        self._cashback = 0
        self._percent = 1
        self._purchases = []

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            'phone': self._phone,
            'cashback': self._cashback,
            'percent': self._percent}

    def __str__(self) -> str:
        return str({
            'class': type(self).__name__,
            **self.to_dict(),
            'purchases': self._purchases
        })

    @property
    def phone(self) -> int:
        return self._phone

    @phone.setter
    def phone(self, phone: int):
        if not isinstance(phone, int) or phone <= 0:
            raise ValueError("Phone must be a positive integer.")
        self._phone = phone

    @property
    def purchases(self) -> list:
        return self._purchases

    def add_purchase(self, order):
        self._purchases.append(order)

    @property
    def cashback(self) -> int:
        return self._cashback

    @cashback.setter
    def cashback(self, cashback: int):
        if not isinstance(cashback, int) or cashback < 0:
            raise ValueError("Cashback must be a non-negative integer.")
        self._cashback = cashback

    @property
    def percent(self) -> int:
        return self._percent

    @percent.setter
    def percent(self, percent: int):
        if not isinstance(percent, int) or not (0 <= percent <= 100):
            raise ValueError("Percent must be an integer between 0 and 100.")
        self._percent = percent

    def withdraw_cashback(self, amount: int) -> bool:
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if amount <= self._cashback:
            self._cashback -= amount
        if amount <= self._cashback:
            self._cashback -= amount
            return True
        return False

    def accrue_cashback(self, order_amount: int):
        if order_amount < 0:
            raise ValueError("Order amount must be non-negative.")
        earned_cashback = (order_amount * self._percent) // 100
        self._cashback += earned_cashback

if __name__ == "__main__":
    store1 = Store("Store", "111 Main St")
    category1 = Category("Food")
    category2 = Category("Clothing")
    product1 = Product("Sausage", 1050, 200)
    product2 = Product("T-shirt", 1500, 50)

    store1.add_category(category1, category2)
    category1.add_product(product1)
    category2.add_product(product2)

    store1.add_product(product1, product2)

    print(store1)
    print(category1)
    print(product1)

    store1.remove_category(category1)
    print(category1)