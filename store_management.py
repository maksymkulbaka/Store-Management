from abc import ABC, abstractmethod
from datetime import datetime


class AbstractDatabase(ABC):
    @property
    @abstractmethod
    def products(self) -> list:
        """Return list of product dictionaries."""
        pass

    @abstractmethod
    def add_products(self, *products: 'Product'):
        """Add product(s) to the database."""
        pass

    @abstractmethod
    def get_product_by_id(self, id: int | str) -> 'Product | None':
        """Return a product by its ID, or None if not found."""
        pass

    @abstractmethod
    def get_product_by_barcode(self, barcode: int | str) -> 'Product | None':
        """Return a product by its barcode, or None if not found."""
        pass

    @abstractmethod
    def update_products(self, *products: 'Product'):
        """Update one or more products in the database."""
        pass

    @abstractmethod
    def remove_products(self, *products: 'Product'):
        """Remove one or more products from the database."""
        pass


class Database(AbstractDatabase):
    """Represents a centralized system to manage all entities related to a retail environment.

    Stores references to stores, categories, products, cashiers, customers, and purchases.
    Provides methods to add, remove, and query these entities.
    """

    def __init__(self):
        """Initialize a new Database instance."""
        self._stores = []
        self._categories = []
        self._products = []
        self._cashiers = []
        self._customers = []
        self._purchases = []
        self._ids_count = {}

    def _get_new_id(self, table_name: str):
        if table_name not in self._ids_count:
            self._ids_count[table_name] = 0
        self._ids_count[table_name] += 1
        return self._ids_count[table_name]

    @property
    def stores(self) -> list:
        return self._stores

    def add_stores(self, *stores: 'Store'):
        for store in stores:
            if not isinstance(store, Store):
                raise TypeError(f"expected Store instance, got {type(store).__name__}")
            for s in stores:
                if s is not store and s.address == store.address:
                    raise ValueError(f"arguments have identical address: {s.to_dict(), store.to_dict()}")
            for d in self._stores:
                if d['address'] == store.address:
                    raise ValueError(f"address '{store.address}' exists in store with id '{d['store_id']}'")
        for store in stores:
            store.set_id(self._get_new_id("store"))
            self._stores.append(store.to_dict())

    def get_store_by_id(self, id: int | str) -> 'Store | None':
        if not isinstance(id, (int, str)):
            raise TypeError(f"expected id as integer or string, got {type(id).__name__}")
        for d in self._stores:
            if d['store_id'] == id:
                store = Store(d['name'], d['address'])
                store.set_id(d['store_id'])
                return store
        return None

    def get_store_by_address(self, address: str) -> 'Store | None':
        if not isinstance(id, (int, str)):
            raise TypeError(f"expected address as string, got {type(address).__name__}")
        for d in self._stores:
            if d['address'] == address:
                store = Store(d['name'], d['address'])
                store.set_id(d['store_id'])
                return store
        return None

    def update_stores(self, *stores: 'Store'):
        for store in stores:
            if not isinstance(store, Store):
                raise TypeError(f"Expected Store instance, got {type(store).__name__}")
            if not store.id:
                raise ValueError(f"arguments have store without id: {store.to_dict()}")
        for d in self._stores:
            for store in stores:
                if d['store_id'] == store.id:
                    d = store.to_dict()

    def remove_stores(self, *stores: 'Store'):
        for store in stores:
            if not isinstance(store, Store):
                raise TypeError(f"Expected Store instance, got {type(store).__name__}")
            if not store.id:
                raise ValueError(f"arguments have store without id: {store.to_dict()}")
        for d in self._stores:
            for store in stores:
                if d['store_id'] == store.id:
                    self._stores.remove(d)

    @property
    def categories(self) -> list:
        return self._categories

    def add_categories(self, *categories: 'Category'):
        for category in categories:
            if not isinstance(category, Category):
                raise TypeError(f"expected Category instance, got {type(category).__name__}")
            for c in categories:
                if c is not category and c.name == category.name:
                    raise ValueError(f"arguments have identical name: {c.to_dict(), category.to_dict()}")
            for d in self._categories:
                if d['name'] == category.name:
                    raise ValueError(f"name '{category.name}' exists in category with id '{d['category_id']}'")
        for category in categories:
            category.set_id(self._get_new_id("category"))
            self._categories.append(category.to_dict())

    def get_category_by_id(self, id: int | str) -> 'Category | None':
        if not isinstance(id, (int, str)):
            raise TypeError(f"expected id as integer or string, got {type(id).__name__}")
        for d in self._categories:
            if d['category_id'] == id:
                category = Category(d['name'])
                category.set_id(d['category_id'])
                return category
        return None

    def get_category_by_name(self, name: str) -> 'Category | None':
        if not isinstance(id, (int, str)):
            raise TypeError(f"expected address as string, got {type(name).__name__}")
        for d in self._categories:
            if d['name'] == name:
                category = Category(d['name'])
                category.set_id(d['category_id'])
                return category
        return None

    def update_categories(self, *categories: 'Category'):
        for category in categories:
            if not isinstance(category, Category):
                raise TypeError(f"Expected Category instance, got {type(category).__name__}")
            if not category.id:
                raise ValueError(f"arguments have category without id: {category.to_dict()}")
        for d in self._categories:
            for category in categories:
                if d['category_id'] == category.id:
                    d = category.to_dict()

    def remove_categories(self, *categories: 'Category'):
        for category in categories:
            if not isinstance(category, Category):
                raise TypeError(f"Expected Category instance, got {type(category).__name__}")
            if not category.id:
                raise ValueError(f"arguments have category without id: {category.to_dict()}")
        for d in self._categories:
            for category in categories:
                if d['category_id'] == category.id:
                    self._categories.remove(d)

    @property
    def products(self) -> list:
        return self._products

    def add_products(self, *products: 'Product'):
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"expected Product instance, got {type(product).__name__}")
            for p in products:
                if p is not product and p.barcode == product.barcode:
                    raise ValueError(f"arguments have identical barcode: {p.to_dict(), product.to_dict()}")
            for d in self._products:
                if d['barcode'] == product.barcode:
                    raise ValueError(f"barcode '{product.barcode}' exists in product with id '{d['product_id']}'")
        for product in products:
            product.set_id(self._get_new_id("product"))
            self._products.append(product.to_dict())

    def get_product_by_id(self, id: int | str) -> 'Product | None':
        if not isinstance(id, (int, str)):
            raise TypeError(f"expected id as integer or string, got {type(id).__name__}")
        for d in self._products:
            if d['product_id'] == id:
                product = Product(d['name'], d['barcode'], d['price'], d['discount_percent'])
                if d['category_id']:
                    product.set_category(self.get_category_by_id('category_id'))
                product.set_id(d['product_id'])
                return product
        return None

    def get_product_by_barcode(self, barcode: int) -> 'Product | None':
        if not isinstance(id, (int, str)):
            raise TypeError(f"expected barcode as int, got {type(barcode).__name__}")
        for d in self._products:
            if d['barcode'] == barcode:
                product = Product(d['name'], d['barcode'], d['price'], d['discount_percent'])
                if d['category_id']:
                    product.set_category(self.get_category_by_id('category_id'))
                product.set_id(d['product_id'])
                return product
        return None

    def update_products(self, *products: 'Product'):
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
            if not product.id:
                raise ValueError(f"arguments have product without id: {product.to_dict()}")
        for d in self._products:
            for product in products:
                if d['product_id'] == product.id:
                    d = product.to_dict()

    def remove_products(self, *products: 'Product'):
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product instance, got {type(product).__name__}")
            if not product.id:
                raise ValueError(f"arguments have product without id: {product.to_dict()}")
        for d in self._products:
            for product in products:
                if d['product_id'] == product.id:
                    self._products.remove(d)

    @property
    def cashiers(self) -> list:
        return self._cashiers

    def add_cashiers(self, *cashiers: 'Cashier'):
        for cashier in cashiers:
            if not isinstance(cashier, Cashier):
                raise TypeError(f"expected Cashier instance, got {type(cashier).__name__}")
            for c in cashiers:
                if c is not cashier and c.name == cashier.name:
                    raise ValueError(f"arguments have identical name: {c.to_dict(), cashier.to_dict()}")
            for d in self._cashiers:
                if d['name'] == cashier.name:
                    raise ValueError(f"address '{cashier.name}' exists in cashier with id '{d['cashier_id']}'")
        for cashier in cashiers:
            cashier.set_id(self._get_new_id("cashier"))
            self._cashiers.append(cashier.to_dict())

    def get_cashier_by_id(self, id: int | str) -> 'Cashier | None':
        if not isinstance(id, (int, str)):
            raise TypeError(f"expected id as integer or string, got {type(id).__name__}")
        for d in self._cashiers:
            if d['cashier_id'] == id:
                cashier = Cashier(d['name'], d['surname'], d['password'])
                if d['store_id']:
                    cashier.set_store(self.get_store_by_id('store_id'))
                cashier.set_id(d['cashier_id'])
                return cashier
        return None

    def update_cashiers(self, *cashiers: 'Cashier'):
        for cashier in cashiers:
            if not isinstance(cashier, Cashier):
                raise TypeError(f"Expected Cashier instance, got {type(cashier).__name__}")
            if not cashier.id:
                raise ValueError(f"arguments have cashier without id: {cashier.to_dict()}")
        for d in self._cashiers:
            for cashier in cashiers:
                if d['cashier_id'] == cashier.id:
                    d = cashier.to_dict()

    def remove_cashiers(self, *cashiers: 'Cashier'):
        for cashier in cashiers:
            if not isinstance(cashier, Cashier):
                raise TypeError(f"Expected Cashier instance, got {type(cashier).__name__}")
            if not cashier.id:
                raise ValueError(f"arguments have cashier without id: {cashier.to_dict()}")
        for d in self._cashiers:
            for cashier in cashiers:
                if d['cashier_id'] == cashier.id:
                    self._cashiers.remove(d)

    @property
    def customers(self) -> tuple:
        """tuple: Tuple containing all Customer instances in the database."""
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

    def get_customer_by_phone(self, phone):
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
        """tuple: Tuple containing all Purchase instances in the database."""
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
            raise TypeError(f"expected name as string, got {type(name).__name__}")
        if not isinstance(address, str):
            raise TypeError(f"expected address as string, got {type(address).__name__}")
        self._id = None
        self._name = name
        self._address = address

    def to_dict(self) -> dict:
        """Return a dictionary representation of the Store.

        Returns:
            dict: Store's basic information.
        """
        return {'store_id': self._id, 'name': self._name, 'address': self._address}

    def __str__(self) -> str:
        """Return a string representation of the Store.

        Returns:
            str: Readable representation of the Store instance.
        """
        return str({'class': type(self).__name__, **self.to_dict()})

    @property
    def id(self) -> int:
        """int: Identifier of the store."""
        return self._id

    def set_id(self, new: int | str):
        """Set a new identifier for the Store.

        Args:
            new (int | str): New identifier.

        Raises:
            TypeError: If new identifier is not an integer or string.
        """
        if not isinstance(new, (int | str)):
            raise TypeError(f"expected id as integer or string, got {type(new).__name__}")
        self._id = new

    @property
    def name(self) -> str:
        """str: Name of the store."""
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
            raise TypeError(f"expected name as string, got {type(new).__name__}")
        self._name = new

    @property
    def address(self) -> str:
        """str: Address of the store."""
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
            raise TypeError(f"expected address as string, got {type(new).__name__}")
        self._address = new


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

    def to_dict(self) -> dict:
        """Return a dictionary representation of the Category.

        Returns:
            dict: Category's basic information.
        """
        return {'category_id': self._id, 'name': self._name}

    def __str__(self) -> str:
        """Return a string representation of the Category including products and associated store.

        Returns:
            str: Readable representation of the Category instance.
        """
        return str({'class': type(self).__name__, **self.to_dict(),
                    'products_id': [product.id for product in self._products]})

    @property
    def id(self) -> int:
        """Return the Category's identifier.

        Returns:
            int: ID of the category.
        """
        return self._id

    def set_id(self, new: int | str):
        """Set a new identifier for the Category.

        Args:
            new (int | str): New identifier.

        Raises:
            TypeError: If new identifier is not an integer or string.
        """
        if not isinstance(new, (int | str)):
            raise TypeError(f"expected id as integer or string, got {type(new).__name__}")
        self._id = new

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
            raise TypeError(f"expected name as string, got {type(new).__name__}")
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


class Product:
    """Represents a Product belonging to a Category and a Store."""

    def __init__(self, name: str, barcode: int, price: int, discount_percent: int):
        """Initialize a Product instance.

        Args:
            name (str): Name of the product.
            price (int): Price of the product.

        Raises:
            TypeError: If any argument is of incorrect type.
        """
        if not isinstance(name, str):
            raise TypeError(f"expected name as string, got {type(name).__name__}")
        if not isinstance(barcode, int):
            raise TypeError(f"expected barcode as integer, got {type(name).__name__}")
        if not isinstance(price, int):
            raise TypeError(f"expected price as integer, got {type(price).__name__}")
        if not isinstance(discount_percent, int):
            raise TypeError(f"expected discount percent as integer, got {type(name).__name__}")
        self._id = None
        self._name = name
        self._barcode = barcode
        self._price = price
        self._discount_percent = discount_percent
        self._category = None

    def to_dict(self) -> dict:
        """Return a dictionary representation of the Product.

        Returns:
            dict: Product's basic information.
        """
        return {'id': self._id, 'name': self._name, 'barcode': self._barcode, 'price': self._price,
                'discount_percent': self._discount_percent,
                'category_id': self._category.id if self._category else None}

    def __str__(self) -> str:
        """Return a string representation of the Product including its category and store.

        Returns:
            str: Readable representation of the Product instance.
        """
        return str({'class': type(self).__name__, **self.to_dict()})

    @property
    def id(self) -> str:
        """int: Identifier of the product."""
        return self._id

    def set_id(self, new: int | str | None):
        """Set a new identifier for the Product.

        Args:
            new (int | str): New identifier.

        Raises:
            TypeError: If new name is not an integer or string.
        """
        if not isinstance(new, (int | str | None)):
            raise TypeError(f"expected integer or string, got {type(new).__name__}")
        self._id = new

    @property
    def name(self) -> str:
        """str: Name of the product."""
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
            raise TypeError(f"expected name as string, got {type(new).__name__}")
        self._name = new

    @property
    def barcode(self) -> int:
        """int: Barcode of the product."""
        return self._barcode

    @barcode.setter
    def barcode(self, new: int) -> None:
        """Set a new barcode for the Product.

        Args:
            new (int): New barcode.

        Raises:
            TypeError: If new barcode is not an integer.
        """
        if not isinstance(new, int):
            raise TypeError(f"expected barcode as integer, got {type(new).__name__}")
        self._barcode = new

    @property
    def price(self) -> int:
        """int: Price of the product."""
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
            raise TypeError(f"expected price as integer, got {type(new).__name__}")
        self._price = new

    @property
    def discount_percent(self) -> int:
        """int: Discount percent of the product."""
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, new: int) -> None:
        """Set a new price for the Product.

        Args:
            new (int): New price.

        Raises:
            TypeError: If new price is not an integer.
        """
        if not isinstance(new, int):
            raise TypeError(f"expected discount percent as integer, got {type(new).__name__}")
        self._price = new

    @property
    def category(self) -> Category:
        """Category: Category of the product."""
        return self._category

    def set_category(self, category: Category | None) -> None:
        """Set the parent Category for a Product.

        Args:
            category (Category | None): A Category instance or None.

        Raises:
            TypeError: If an input is not a Category or None instance.
        """
        if not isinstance(category, Category | None):
            raise TypeError(f"expected Category or None instance, got {type(category).__name__}")
        self._category = category


class User:
    """Represents a base user with name, surname, and optional ID."""

    def __init__(self, name: str, surname: str):
        """Initializes a User instance.

        Args:
            name (str): The user's first name.
            surname (str): The user's last name.

        Raises:
            ValueError: If name or surname is not a valid non-empty string.
        """
        if not isinstance(name, str):
            raise TypeError(f"expected name as string, got {type(name).__name__}")
        if not isinstance(surname, str):
            raise TypeError(f"expected surname as string, got {type(surname).__name__}")
        self._id = None
        self._name = name
        self._surname = surname

    def to_dict(self) -> dict:
        """Returns user data as a dictionary.

        Returns:
            dict: A dictionary with user ID, name, and surname.
        """
        return {'id': self._id, 'name': self._name, 'surname': self._surname}

    def __str__(self) -> str:
        """Returns a string representation of the user with class name.

        Returns:
            str: String of user data including class name.
        """
        return str({'class': type(self).__name__, **self.to_dict()})

    @property
    def id(self) -> int:
        """int: The user's identifier."""
        return self._id

    def set_id(self, new: int | str | None):
        """Set a new identifier for the User.

        Args:
            new (int | str): New identifier.

        Raises:
            TypeError: If new name is not an integer or string.
        """
        if not isinstance(new, (int | str | None)):
            raise TypeError(f"expected integer or string, got {type(new).__name__}")
        self._id = new

    @property
    def name(self) -> str:
        """str: The user's first name."""
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the user's first name.

        Args:
            name (str): New first name.

        Raises:
            TypeError: If the provided argument is not a string.
        """
        if not isinstance(name, str):
            raise ValueError(f"expected name as string, got {type(name).__name__}")
        self._name = name

    @property
    def surname(self) -> str:
        """str: The user's last name."""
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        """Sets the user's last name.

        Args:
            surname (str): New last name.

        Raises:
            TypeError: If the provided argument is not a string.
        """
        if not isinstance(surname, str) or not surname.strip():
            raise ValueError(f"expected surname as string, got {type(surname).__name__}")
        self._surname = surname


class Cashier(User):
    """Represents a cashier, inherited from User."""

    def __init__(self, name: str, surname: str, password: int | str):
        """Initializes a Cashier instance.

        Args:
            name (str): The cashier's first name.
            surname (str): The cashier's last name.
        """
        super().__init__(name, surname)
        if not isinstance(password, (int, str)):
            raise ValueError(f"expected password as integer or string, got {type(password).__name__}")
        self._password = password
        self._store = None

    def to_dict(self) -> dict:
        """Returns cashier data as a dictionary.

        Returns:
            dict: A dictionary with basic information of cashier.
        """
        return {**super().to_dict(), 'password': self._password, 'store': self._store.id if self._store else None}

    def __str__(self) -> str:
        """Returns a string representation of the cashier with class name.

        Returns:
            str: String of cashier data including class name.
        """
        return str({'class': type(self).__name__, **self.to_dict()})

    @property
    def store(self) -> Store:
        """int: Cashier store."""
        return self._store

    def set_store(self, new: Store):
        """Sets the cashier's store.

        Args:
            new (Store): New store.

        Raises:
            TypeError: If the provided argument is not a Store instance.
        """
        if not isinstance(new, str):
            raise TypeError(f"expected Store instance, got {type(new).__name__}")
        self._store = new


class Customer(User):
    """Represents a customer with phone number, cashback, and purchase history."""

    def __init__(self, name: str, surname: str, phone: str):
        """Initializes a Customer instance.

        Args:
            name (str): The customer's first name.
            surname (str): The customer's last name.
            phone (int): The customer's phone number.

         Raises:
            ValueError: If phone is not a positive integer.
        """
        super().__init__(name, surname)
        if not isinstance(phone, str):
            raise ValueError(f"expected phone as string, got {type(phone).__name__}")
        self._phone = phone
        self._cashback = 0
        self._cashback_percent = 1

    def to_dict(self) -> dict:
        """Returns customer data as a dictionary (excluding purchases).

        Returns:
            dict: Dictionary with user info and customer-specific fields.
        """
        return {**super().to_dict(), 'phone': self._phone, 'cashback': self._cashback,
                'cashback_percent': self._cashback_percent}

    def __str__(self) -> str:
        """Returns a string representation of the customer including purchases.

        Returns:
            str: String of customer data with class name and purchases.
        """
        return str({'class': type(self).__name__, **self.to_dict()})

    @property
    def phone(self) -> str:
        """int: Customer phone number."""
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the customer's phone number.

        Args:
            phone (int): New phone number.

        Raises:
            TypeError: If the provided argument is not a string.
        """
        if not isinstance(phone, str):
            raise TypeError(f"expected phone as string, got {type(phone).__name__}")
        self._phone = phone

    @property
    def cashback(self) -> int:
        """int: Cashback amount."""
        return self._cashback

    @cashback.setter
    def cashback(self, cashback: int):
        """Sets the cashback amount.

        Args:
            cashback (int): New cashback balance.

        Raises:
            ValueError: If the provided argument is not a positive integer.
        """
        if not isinstance(cashback, int) or cashback < 0:
            raise ValueError(f"expected cashback as non-negative integer, got {type(cashback).__name__}")
        self._cashback = cashback

    @property
    def cashback_percent(self) -> int:
        """int: Cashback percent."""
        return self._cashback_percent

    @cashback_percent.setter
    def cashback_percent(self, new: int):
        """Sets the cashback percentage.

        Args:
            new (int): New cashback percent.

        Raises:
            ValueError: If the provided argument is not an integer in range of 0 and 100.
        """
        if not isinstance(new, int) or not (0 <= new <= 100):
            raise ValueError(f"expected valid cashback percent as integer, got {type(new).__name__}")
        self._cashback_percent = new

    def withdraw_cashback(self, amount: int) -> bool:
        """Attempts to withdraw cashback.

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
        """Accrues cashback from a purchase based on the cashback percent.

        Args:
            order_amount (int): Total amount of the purchase.

        Raises:
            ValueError: If order amount is negative.
        """
        if order_amount < 0:
            raise ValueError("Order amount must be non-negative.")
        earned_cashback = (order_amount * self._cashback_percent) // 100
        self._cashback += earned_cashback


class CashRegister:
    def __init__(self, database: Database, cashier: Cashier, barcode: int):
        """Initializes a shopping cart with a single product.

        Args:
            barcode (int): Barcode of product to add to the cart.

        Raises:
            TypeError: If the provided arguments is not a Database or Product instances.
        """
        if not isinstance(database, Database):
            raise TypeError("Database must be an instance of Database")
        if not isinstance(barcode, int):
            raise TypeError("barcode must be an integer")
        self._id = None
        self._products = [database.get_product_by_barcode(barcode)]
        self._cashier = cashier
        self._customer = None
        self._used_cashback = 0
        self._total = self._products[0].price
        self._store = None
        self._database = None

    def to_dict(self) -> dict:
        """Returns a dictionary representation of the cart (excluding product list).

        Returns:
            dict: Cart data including ID, cashier, customer, cashback, total, and shop.
        """
        return {'id': self._id, 'employee': self._cashier, 'customer': self._customer,
                'used_cashback': self._used_cashback, 'total': self._total, 'store': self._store}

    def __str__(self):
        """Returns a string representation of the shopping cart including products.

        Returns:
            str: Human-readable string of the cart details.
        """
        return str({'class': type(self).__name__, **self.to_dict(),
                    'products': [product.to_dict() for product in self._products]})

    @property
    def id(self) -> int:
        """int: Unique identifier for the cart."""
        return self._id

    @property
    def products(self) -> list:
        """list: List of Product instances."""
        return self._products

    @property
    def cashier(self) -> Cashier:
        """Cashier: The cashier handling the cart."""
        return self._cashier

    @cashier.setter
    def cashier(self, new):
        """Assigns a new cashier to the cart.

        Args:
            new (Cashier): The cashier to assign.
        """
        if not isinstance(new, Cashier):
            raise TypeError("cashier must be an instance of Cashier")
        self._cashier = new

    @property
    def customer(self) -> Customer:
        """Customer: The assigned customer."""
        return self._customer

    @property
    def used_cashback(self) -> int:
        """int: Total cashback amount."""
        return self._used_cashback

    @property
    def total(self) -> int:
        """int: Total cart value."""
        return self._total

    def add_product(self, product):
        """Adds a product to the cart and updates the total price.

        Args:
            product (Product): The product to add.

        Raises:
            TypeError: If the provided argument is not a Product instance.
        """
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product")
        self._products.append(product)
        self._total += product.price

    def add_customer(self, phone: str):
        """
        Searches for a customer by phone number and assigns them to the cart.

        Args:
            phone (int): Customer's phone number.

        Returns:
            bool: True if customer is found and assigned, False otherwise.

        Raises:
            TypeError: If the provided argument is not a string of phone number.
        """
        if not isinstance(phone, str) or len(str(phone)) < 7:
            raise ValueError("Phone must be a string phone number")
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

        Raises:
            TypeError: If the provided argument is not a positive integer.
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be a positive integer")
        if self._customer and self._customer.withdraw_cashback(amount):
            self._used_cashback += amount
            self._total -= amount
            return True
        return False

    def make_purchase(self, transaction_id: int | str, payment_status: bool) -> 'Purchase':
        if not isinstance(transaction_id, (int | str)):
            raise TypeError(f"expected transaction id as integer or string, got {type(transaction_id).__name__}")
        if not isinstance(payment_status, bool):
            raise TypeError(f"expected payment status as boolean, got {type(payment_status).__name__}")
        accrued_cashback = (self._total * self._customer.percent) // 100
        self._customer.accrue_cashback(accrued_cashback)
        purchase = Purchase(self._store, self._products, self._cashier, self._customer, self._used_cashback,
                            accrued_cashback, self._total, transaction_id)
        self._customer.add_purchase(purchase)
        return purchase


class Purchase:
    """Represents a completed purchase made by a customer."""

    def __init__(self, store: Store, products: list[Product], cashier: Cashier, customer: Customer, used_cashback: int,
                 accrued_cashback: int, total: int, transaction_id: int | str):
        """Initialize a Purchase instance.

        Args:
            customer (Customer): The customer who made the purchase.
            products (list[Product]): List of purchased Product instances.

        Raises:
            TypeError: If inputs are not of correct types.
            ValueError: If product list is empty or contains invalid products.
        """
        if not isinstance(customer, Customer):
            raise TypeError(f"Expected Customer instance, got {type(customer).__name__}")
        if not isinstance(cashier, Cashier):
            raise TypeError(f"Expected Cashier instance, got {type(customer).__name__}")
        if not products:
            raise ValueError("Products list cannot be empty.")
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected Product in products list, got {type(product).__name__}")
        self._id = None
        self._products = products
        self._cashier = cashier
        self._customer = customer
        self._used_cashback = used_cashback
        self._accrued_cashback = accrued_cashback
        self._purchase_date = datetime.now()
        self._total = sum(product.price for product in products)

    @property
    def id(self) -> int:
        """int: The unique identifier of the purchase."""
        return self._id

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


if __name__ == "__main__":
    db = Database()
    store1 = Store("MAY-Market", "8a Kosmichna Street")
    category1 = Category("Food")
    category2 = Category("Clothing")
    product1 = Product("Sausage", 4820201379622, 1050, 0)
    product2 = Product("T-shirt", 4820384671759, 1500, 0)

    category1.add_product(product1)
    category2.add_product(product2)

    cashier1 = Cashier("Maksym", "Kulbaka", "+380665612345")
    cash_register1 = CashRegister(db, cashier1, 4820201379622)
    print(store1)
    print(category1)
    print(product1)

    print(category1)
    print(cash_register1.to_dict())