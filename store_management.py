from datetime import datetime

class Database:
    """Represents a centralized system to manage all entities related to a retail environment.

    Stores references to stores, categories, products, cashiers, customers, and purchases.
    Provides methods to add, remove, and query these entities.
    """

    def __init__(self, name: str):
        """Initialize a new Database instance.

        Args:
            name (str): The name of the database.
        """
        self._name = name
        self._stores = []
        self._categories = []
        self._products = []
        self._cashiers = []
        self._customers = []
        self._purchases = []

    @property
    def stores(self) -> tuple:
        """Returns all registered Store instances.

        Returns:
            tuple: Tuple containing all Store instances in the database.
        """
        return tuple(self._stores)

    def add_stores(self, *stores: 'Store'):
        """Add one or more Store instances to the database.

        Args:
            *stores (Store): Variable number of Store instances to add.

        Raises:
            TypeError: If any argument is not a Store instance.
        """
        for store in stores:
            if not isinstance(store, Store):
                raise TypeError(f"Expected Store instance, got {type(store).__name__}")
        for store in stores:
            if store not in self._stores:
                self._stores.append(store)
                store.set_database(self)

    def remove_stores(self, *stores: 'Store'):
        """Remove one or more Store instances from the database.

        Args:
            *stores (Store): Variable number of Store instances to remove.

        Raises:
            TypeError: If any argument is not a Store instance.
        """
        for store in stores:
            if not isinstance(store, Store):
                raise TypeError(f"Expected Store instance, got {type(store).__name__}")
        for store in stores:
            if store in self._stores:
                self._stores.remove(store)
                store.set_database(None)

    @property
    def categories(self) -> tuple:
        """Returns all registered Category instances.

        Returns:
            tuple: Tuple containing all Category instances in the database.
        """
        return tuple(self._categories)

    def add_categories(self, *categories: 'Category'):
        """Add one or more Category instances to the database.

        Args:
            *categories (Category): Variable number of Category instances to add.

        Raises:
            TypeError: If any argument is not a Category instance.
        """
        for category in categories:
            if not isinstance(category, Category):
                raise TypeError(f"Expected Category instance, got {type(category).__name__}")
        for category in categories:
            if category not in self._categories:
                self._categories.append(category)
                category.set_database(self)

    def remove_categories(self, *categories: 'Category'):
        """Remove one or more Category instances from the database.

        Args:
            *categories (Category): Variable number of Category instances to remove.

        Raises:
            TypeError: If any argument is not a Category instance.
        """
        for category in categories:
            if not isinstance(category, Category):
                raise TypeError(f"Expected Category instance, got {type(category).__name__}")
        for category in categories:
            if category in self._categories:
                self._categories.remove(category)
                category.set_database(None)

    @property
    def products(self) -> tuple:
        """Returns all registered Product instances.

        Returns:
            tuple: Tuple containing all Product instances in the database.
        """
        return tuple(self._products)

    def add_products(self, *products: 'Product'):
        """Add one or more Product instances to the database.

        Args:
            *products (Product): Variable number of Product instances to add.

        Raises:
            TypeError: If any argument is not a Product instance.
        """
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
        for product in products:
            if product not in self._products:
                self._products.append(product)
                product.set_database(self)

    def remove_products(self, *products: 'Product'):
        """Remove one or more Product instances from the database.

        Args:
            *products (Product): Variable number of Product instances to remove.

        Raises:
            TypeError: If any argument is not a Product instance.
        """
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
        for product in products:
            if product in self._products:
                self._products.remove(product)
                product.set_database(None)

    @property
    def cashiers(self) -> tuple:
        """Returns all registered Cashier instances.

        Returns:
            tuple: Tuple containing all Cashier instances in the database.
        """
        return tuple(self._cashiers)

    def add_cashiers(self, *cashiers: 'Cashier'):
        """Add one or more Cashier instances to the database.

        Args:
            *cashiers (Cashier): Variable number of Cashier instances to add.

        Raises:
            TypeError: If any argument is not a Cashier instance.
        """
        for cashier in cashiers:
            if not isinstance(cashier, Cashier):
                raise TypeError(f"Expected Cashier instance, got {type(cashier).__name__}")
        for cashier in cashiers:
            if cashier not in self._cashiers:
                self._cashiers.append(cashier)
                cashier.set_database(self)

    def remove_cashiers(self, *cashiers: 'Cashier'):
        """Remove one or more Cashier instances from the database.

        Args:
            *cashiers (Cashier): Variable number of Cashier instances to remove.

        Raises:
            TypeError: If any argument is not a Cashier instance.
        """
        for cashier in cashiers:
            if not isinstance(cashier, Cashier):
                raise TypeError(f"Expected Cashier instance, got {type(cashier).__name__}")
        for cashier in cashiers:
            if cashier in self._cashiers:
                self._cashiers.remove(cashier)
                cashier.set_database(None)

    @property
    def customers(self) -> tuple:
        """Returns all registered Customer instances.

        Returns:
            tuple: Tuple containing all Customer instances in the database.
        """
        return tuple(self._customers)

    def add_customers(self, *customers: 'Customer'):
        """Add one or more Customer instances to the database.

        Args:
            *customers (Customer): Variable number of Customer instances to add.

        Raises:
            TypeError: If any argument is not a Customer instance.
        """
        for customer in customers:
            if not isinstance(customer, Customer):
                raise TypeError(f"Expected Customer instance, got {type(customer).__name__}")
        for customer in customers:
            if customer not in self._customers:
                self._customers.append(customer)
                customer.set_database(self)

    def remove_customers(self, *customers: 'Customer'):
        """Remove one or more Customer instances from the database.

        Args:
            *customers (Customer): Variable number of Customer instances to remove.

        Raises:
            TypeError: If any argument is not a Customer instance.
        """
        for customer in customers:
            if not isinstance(customer, Customer):
                raise TypeError(f"Expected Customer instance, got {type(customer).__name__}")
        for customer in customers:
            if customer in self._customers:
                self._customers.remove(customer)
                customer.set_database(None)

    def find_customer_by_phone(self, phone):
        """Search for a Customer instance by phone number.

        Args:
            phone (Any): Phone number to search for.

        Returns:
            Customer | bool: The matching Customer instance if found, otherwise False.
        """
        for customer in self._customers:
            if customer.phone == phone:
                return customer
        return False

    @property
    def purchases(self) -> tuple:
        """Returns all registered Purchase instances.

        Returns:
            tuple: Tuple containing all Purchase instances in the database.
        """
        return tuple(self._purchases)

    def add_purchases(self, *purchases: 'Purchase'):
        """Add one or more Purchase instances to the database.

        Args:
            *purchases (Purchase): Variable number of Purchase instances to add.

        Raises:
            TypeError: If any argument is not a Purchase instance.
        """
        for purchase in purchases:
            if not isinstance(purchase, Purchase):
                raise TypeError(f"Expected Purchase instance, got {type(purchase).__name__}")
        for purchase in purchases:
            if purchase not in self._purchases:
                self._purchases.append(purchase)
                purchase.set_database(self)

    def remove_purchases(self, *purchases: 'Purchase'):
        """Remove one or more Purchase instances from the database.

        Args:
            *purchases (Purchase): Variable number of Purchase instances to remove.

        Raises:
            TypeError: If any argument is not a Purchase instance.
        """
        for purchase in purchases:
            if not isinstance(purchase, Purchase):
                raise TypeError(f"Expected Purchase instance, got {type(purchase).__name__}")
        for purchase in purchases:
            if purchase in self._purchases:
                self._purchases.remove(purchase)
                purchase.set_database(None)

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
        self._database = None

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

    @property
    def database(self) -> Database:
        return self._database

    def set_database(self, database: Database | None):
        if not isinstance(database, Database | None):
            raise TypeError(f"Expected Database or None instance, got {type(Database).__name__}")
        if self._database is not None:
            self._database.remove_stores(self)
        self._database = database
        if database is not None:
            if self not in self._database.stores:
                database.add_stores(self)

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
        self._database = None

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

    @property
    def database(self) -> Database:
        return self._database

    def set_database(self, database: Database | None):
        if not isinstance(database, Database | None):
            raise TypeError(f"Expected Database or None instance, got {type(Database).__name__}")
        if self._database is not None:
            self._database.remove_categories(self)
        self._database = database
        if database is not None:
            if self not in self._database.categories:
                database.add_categories(self)

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
        self._database = None

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

    @property
    def database(self) -> Database:
        return self._database

    def set_database(self, database: Database | None):
        if not isinstance(database, Database | None):
            raise TypeError(f"Expected Database or None instance, got {type(Database).__name__}")
        if self._database is not None:
            self._database.remove_products(self)
        self._database = database
        if database is not None:
            if self not in self._database.products:
                database.add_products(self)

class User:
    """Represents a base user with name, surname, and optional ID."""

    def __init__(self, name: str, surname: str, phone: str):
        """
        Initializes a User instance.

        Args:
            name (str): The user's first name.
            surname (str): The user's last name.

        Raises:
            ValueError: If name or surname is not a valid non-empty string.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(surname, str) or not surname.strip():
            raise ValueError("Surname must be a non-empty string.")
        if not isinstance(phone, str) or not surname.strip():
            raise ValueError("Phone must be a non-empty string.")
        self._id = None
        self._name = name
        self._surname = surname
        self._phone = phone

    def to_dict(self) -> dict:
        """
        Returns user data as a dictionary.

        Returns:
            dict: A dictionary with user ID, name, and surname.
        """
        return {'id': self._id, 'name': self._name, 'surname': self._surname}

    def __str__(self) -> str:
        """
        Returns a string representation of the user with class name.

        Returns:
            str: String of user data including class name.
        """
        return str({'class': type(self).__name__, **self.to_dict()})

    @property
    def id(self) -> int:
        """
        Gets the user's ID.

        Returns:
            int: The user's ID.
        """
        return self._id

    @property
    def name(self) -> str:
        """
        Gets the user's first name.

        Returns:
            str: The user's first name.
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the user's first name.

        Args:
            name (str): New first name.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    @property
    def surname(self) -> str:
        """
        Gets the user's last name.

        Returns:
            str: The user's last name.
        """
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        """
        Sets the user's last name.

        Args:
            surname (str): New last name.
        """
        if not isinstance(surname, str) or not surname.strip():
            raise ValueError("Surname must be a non-empty string.")
        self._surname = surname

class Cashier(User):
    """Represents a cashier, inherited from User."""
    def __init__(self, name: str, surname: str, phone: str):
        """
        Initializes a Cashier instance.

        Args:
            name (str): The cashier's first name.
            surname (str): The cashier's last name.
        """
        super().__init__(name, surname, phone)
        self._database = None

    def __str__(self) -> str:
        """
        Returns a string representation of the cashier with class name.

        Returns:
            str: String of cashier data including class name.
        """
        return str({'class': type(self).__name__, **self.to_dict()})

    @property
    def database(self) -> Database:
        return self._database

    def set_database(self, database: Database | None):
        if not isinstance(database, Database | None):
            raise TypeError(f"Expected Database or None instance, got {type(Database).__name__}")
        if self._database is not None:
            self._database.remove_cashiers(self)
        self._database = database
        if database is not None:
            if self not in self._database.cashiers:
                database.add_cashiers(self)

class Customer(User):
    """Represents a customer with phone number, cashback, and purchase history."""
    def __init__(self, name: str, surname: str, phone: str):
        """
        Initializes a Customer instance.

        Args:
            name (str): The customer's first name.
            surname (str): The customer's last name.
            phone (int): The customer's phone number.

         Raises:
            ValueError: If phone is not a positive integer.
        """
        super().__init__(name, surname, phone)
        self._cashback = 0
        self._percent = 1
        self._purchases = []
        self._database = None

    def to_dict(self) -> dict:
        """
        Returns customer data as a dictionary (excluding purchases).

        Returns:
            dict: Dictionary with user info and customer-specific fields.
        """
        return {
            **super().to_dict(),
            'phone': self._phone,
            'cashback': self._cashback,
            'percent': self._percent}

    def __str__(self) -> str:
        """
        Returns a string representation of the customer including purchases.

        Returns:
            str: String of customer data with class name and purchases.
        """
        return str({
            'class': type(self).__name__,
            **self.to_dict(),
            'purchases': self._purchases
        })

    @property
    def phone(self) -> int:
        """
        Gets the customer's phone number.

        Returns:
            int: Phone number.
        """
        return self._phone

    @phone.setter
    def phone(self, phone: int):
        """
        Sets the customer's phone number.

        Args:
            phone (int): New phone number.
        """
        if not isinstance(phone, int) or phone <= 0:
            raise ValueError("Phone must be a positive integer.")
        self._phone = phone

    @property
    def purchases(self) -> list:
        """
        Gets the list of customer purchases.

        Returns:
            list: List of purchases.
        """
        return self._purchases

    def add_purchase(self, purchase):
        """
        Adds a new purchase to the customer's history.

        Args:
            purchase: An order object or identifier to be added to purchases.
        """
        self._purchases.append(purchase)

    @property
    def cashback(self) -> int:
        """
        Gets the current cashback balance.

        Returns:
            int: Cashback amount.
        """
        return self._cashback

    @cashback.setter
    def cashback(self, cashback: int):
        """
        Sets the cashback amount.

        Args:
            cashback (int): New cashback balance.
        """
        if not isinstance(cashback, int) or cashback < 0:
            raise ValueError("Cashback must be a non-negative integer.")
        self._cashback = cashback

    @property
    def percent(self) -> int:
        """
        Gets the cashback percentage.

        Returns:
            int: Cashback percent.
        """
        return self._percent

    @percent.setter
    def percent(self, percent: int):
        """
        Sets the cashback percentage.

        Args:
            percent (int): New cashback percent.
        """
        if not isinstance(percent, int) or not (0 <= percent <= 100):
            raise ValueError("Percent must be an integer between 0 and 100.")
        self._percent = percent

    def withdraw_cashback(self, amount: int) -> bool:
        """
        Attempts to withdraw cashback.

        Args:
            amount (int): Amount to withdraw.

        Returns:
            bool: True if successful, False if insufficient balance.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if amount <= self._cashback:
            self._cashback -= amount
            return True
        return False

    def accrue_cashback(self, order_amount: int):
        """
        Accrues cashback from a purchase based on the cashback percent.

        Args:
            order_amount (int): Total amount of the purchase.
        Raises:
            ValueError: If order amount is negative.
        """
        if order_amount < 0:
            raise ValueError("Order amount must be non-negative.")
        earned_cashback = (order_amount * self._percent) // 100
        self._cashback += earned_cashback

    @property
    def database(self) -> Database:
        return self._database

    def set_database(self, database: Database | None):
        if not isinstance(database, Database | None):
            raise TypeError(f"Expected Database or None instance, got {type(Database).__name__}")
        if self._database is not None:
            self._database.remove_customers(self)
        self._database = database
        if database is not None:
            if self not in self._database.customers:
                database.add_customers(self)

class ShoppingCart:
    def __init__(self, product: Product, database: Database):
        """
        Initializes a shopping cart with a single product.

        Args:
            product (Product): The initial product to add to the cart.
        """
        if not isinstance(product, Product):
            raise TypeError("product must be an instance of Product")
        if not isinstance(database, Database):
            raise TypeError("database must be an instance of Database")
        self._id = None
        self._products = [product]
        self._cashier = None
        self._customer = None
        self._used_cashback = 0
        self._total = product.price
        self._store = None
        self._database = None
        self._status = "pending"

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the cart (excluding product list).

        Returns:
            dict: Cart data including ID, cashier, customer, cashback, total, and shop.
        """
        return {'id': self._id, 'employee': self._cashier, 'customer': self._customer,
                'used_cashback': self._used_cashback, 'total': self._total, 'store': self._store, 'status': self._status}

    def __str__(self):
        """
        Returns a string representation of the shopping cart including products.

        Returns:
            str: Human-readable string of the cart details.
        """
        return str({'class': type(self).__name__, **self.to_dict(),
            'products': [product.to_dict() for product in self._products]})

    @property
    def id(self) -> int:
        """
        Returns the cart ID.

        Returns:
            int: Unique identifier for the cart.
        """
        return self._id

    @property
    def products(self) -> list:
        """
        Returns the list of products in the cart.

        Returns:
            list: List of Product instances.
        """
        return self._products

    @property
    def cashier(self) -> Cashier:
        """
        Returns the assigned cashier.

        Returns:
            Cashier: The cashier handling the cart.
        """
        return self._cashier

    @cashier.setter
    def cashier(self, new):
        """
        Assigns a new cashier to the cart.

        Args:
            new (Cashier): The cashier to assign.
        """
        if not isinstance(new, Cashier):
            raise TypeError("cashier must be an instance of Cashier")
        self._cashier = new

    @property
    def customer(self) -> Customer:
        """
        Returns the customer associated with the cart.

        Returns:
            Customer: The assigned customer.
        """
        return self._customer

    @property
    def used_cashback(self) -> int:
        """
        Returns the cashback applied to the cart.

        Returns:
            int: Total cashback amount.
        """
        return self._used_cashback

    @property
    def total(self) -> int:
        """
        Returns the total price after applying cashback.

        Returns:
            int: Total cart value.
        """
        return self._total

    @property
    def status(self) -> str:
        """
        Returns the current transaction status.

        Returns:
            str: Status of the transaction.
        """
        return self._status

    def add_product(self, product):
        """
        Adds a product to the cart and updates the total price.

        Args:
            product (Product): The product to add.
        """
        if not isinstance(product, Product):
            raise TypeError("product must be an instance of Product")
        self._products.append(product)
        self._total += product.price

    def add_customer(self, phone: int):
        """
        Searches for a customer by phone number and assigns them to the cart.

        Args:
            phone (int): Customer's phone number.

        Returns:
            bool: True if customer is found and assigned, False otherwise.
        """
        if not isinstance(phone, int) or len(str(phone)) < 7:
            raise ValueError("phone must be a valid integer phone number")

        for customer in self._database.customers:
            if customer.phone == phone:
                self._customer = customer
                return True
        return False

    def withdraw_cashback(self, amount):
        """
        Applies cashback from the customer's account to reduce the total price.

        Args:
            amount (int): Amount of cashback to apply.

        Returns:
            bool: True if cashback applied successfully, False otherwise.
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("amount must be a positive integer")

        if self._customer and self._customer.withdraw_cashback(amount):
            self._used_cashback += amount
            self._total -= amount
            return True
        return False

    def make_payment(self, card_number: int, expiration_date: list, cvv: int):
        """
        Placeholder method for processing payment.

        Args:
            card_number (int): Credit/debit card number.
            expiration_date (list): [month, year] of card expiration.
            cvv (int): Card verification value.
        """
        try:
            if not isinstance(card_number, int) or len(str(card_number)) < 13:
                raise ValueError("Invalid card number")
            if not (isinstance(expiration_date, list) and len(expiration_date) == 2):
                raise ValueError("expiration_date must be a list of [month, year]")
            if not (1 <= expiration_date[0] <= 12):
                raise ValueError("Invalid expiration month")
            if not isinstance(expiration_date[1], int) or expiration_date[1] < 2000:
                raise ValueError("Invalid expiration year")
            if not isinstance(cvv, int) or len(str(cvv)) != 3:
                raise ValueError("CVV must be a 3-digit integer")

            if not self._customer:
                raise ValueError("No customer assigned to the cart.")

            for product in self._products:
                if product.quantity < 1:
                    raise ValueError(f"Product {product.name} is out of stock.")
                product.quantity -= 1

            self._customer.accrue_cashback(self._total)
            purchase = Purchase(self._store, self._products, self._cashier, self._customer, self._used_cashback)
            self._customer.add_purchase(purchase)
            self._database.add_purchase(purchase)

            self._status = "success"
            print("Payment successful.")
            return True

        except Exception as e:
            self._status = "failed"
            print(f"Payment failed: {str(e)}")
            return False

class Purchase:
    """Represents a completed purchase made by a customer."""

    def __init__(self, store: Store, products: list[Product], cashier: Cashier,
                 customer: Customer, used_cashback: int):
        """Initialize a Purchase instance.

        Args:
            customer (Customer): The customer who made the purchase.
            products (list[Product]): List of purchased Product instances.

        Raises:
            TypeError: If inputs are not of correct types.
            ValueError: If product list is empty or contains invalid products.
        """
        if not isinstance(store, Store):
            raise TypeError(f"Expected Store instance, got {type(customer).__name__}")
        if not isinstance(customer, Customer):
            raise TypeError(f"Expected Customer instance, got {type(customer).__name__}")
        if not isinstance(cashier, Cashier):
            raise TypeError(f"Expected Cashier instance, got {type(customer).__name__}")
        if not products:
            raise ValueError("Products list cannot be empty.")
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product in products list, got {type(product).__name__}")
        if not isinstance(used_cashback, int) or used_cashback < 0:
            raise ValueError("Cashback must be a non-negative integer.")
        if used_cashback > customer.cashback:
            raise ValueError("Cashback used exceeds available cashback.")

        self._id = None
        self._store = store
        self._products = products
        self._cashier = cashier
        self._customer = customer
        self._used_cashback = used_cashback
        self._purchase_date = datetime.now()
        self._total = sum(product.price for product in products)
        self._database = None

    @property
    def id(self) -> int:
        """int: The unique identifier of the purchase."""
        return self._id

    @property
    def store(self) -> 'Store':
        """The store where purchase was made"""
        return self._store

    @property
    def products(self) -> tuple:
        """tuple: Tuple of Product instances purchased."""
        return tuple(self._products)

    @property
    def customer(self) -> 'Customer':
        """Customer: The customer who made the purchase."""
        return self._customer

    @property
    def used_cashback(self) -> int:
        """int: The used cashback."""
        return self._used_cashback

    @property
    def total(self) -> int:
        """int: The total cost of the purchase."""
        return self._total

    @property
    def purchase_date(self) -> datetime:
        """datetime: The date and time the purchase was made."""
        return self._purchase_date

    def get_receipt(self) -> dict:
        """Return a dictionary representation of the purchase.

        Returns:
            dict: Purchase data including customer, total, and product details.
        """
        return {
            'id': self._id,
            'store': self._store.to_dict(),
            'cashier': self._cashier.to_dict(),
            'customer': self._customer.to_dict(),
            'products': [p.to_dict() for p in self._products],
            'used_cashback': self._used_cashback,
            'purchase_date': self._purchase_date.isoformat(),
            'total': self._total
        }

    def __str__(self) -> str:
        """Return a string representation of the purchase.

        Returns:
            str: Human-readable summary of the purchase.
        """
        return str(self.get_receipt())

    @property
    def database(self) -> Database:
        return self._database

    def set_database(self, database: Database | None):
        if not isinstance(database, Database | None):
            raise TypeError(f"Expected Database or None instance, got {type(Database).__name__}")
        if self._database is not None:
            self._database.remove_purchases(self)
        self._database = database
        if database is not None:
            if self not in self._database.purchases:
                database.add_purchases(self)


if __name__ == "__main__":
    db = Database("may_market")
    store1 = Store("MAY-Market", "8a Kosmichna Street")
    category1 = Category("Food")
    category2 = Category("Clothing")
    product1 = Product("Sausage", 1050, 200)
    product2 = Product("T-shirt", 1500, 50)

    store1.add_category(category1, category2)
    category1.add_product(product1)
    category2.add_product(product2)
    cart = ShoppingCart(product1, db)

    store1.add_product(product1, product2)

    print(store1)
    print(category1)
    print(product1)

    store1.remove_category(category1)
    print(category1)
    print(cart.to_dict())
    print("Transaction status:", cart.status)