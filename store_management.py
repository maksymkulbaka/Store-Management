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
    """Represents a base user with name, surname, and optional ID."""

    def __init__(self, name: str, surname: str):
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
        self._id = None
        self._name = name
        self._surname = surname

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
            str: Stringified user data including class name.
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

    def __init__(self, name: str, surname: str):
        """
        Initializes a Cashier instance.

        Args:
            name (str): The cashier's first name.
            surname (str): The cashier's last name.
        """
        super().__init__(name, surname)

    def __str__(self) -> str:
        """
        Returns a string representation of the cashier with class name.

        Returns:
            str: Stringified cashier data including class name.
        """
        return str({'class': type(self).__name__, **self.to_dict()})

class Customer(User):
    """Represents a customer with phone number, cashback, and purchase history."""

    def __init__(self, name: str, surname: str, phone: int):
        """
        Initializes a Customer instance.

        Args:
            name (str): The customer's first name.
            surname (str): The customer's last name.
            phone (int): The customer's phone number.

         Raises:
            ValueError: If phone is not a positive integer.
        """
        super().__init__(name, surname)
        if not isinstance(phone, int) or phone <= 0:
            raise ValueError("Phone must be a positive integer.")
        super().__init__(name, surname)
        self._phone = phone
        self._cashback = 0
        self._percent = 1
        self._purchases = []

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
            str: Stringified customer data with class name and purchases.
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

    def add_purchase(self, order):
        """
        Adds a new purchase to the customer's history.

        Args:
            order: An order object or identifier to be added to purchases.
        """
        self._purchases.append(order)

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

class ShoppingCart:
    def __init__(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("product must be an instance of Product")

        self._id = None
        self._products = [product]
        self._cashier = None
        self._customer = None
        self._cashback = 0
        self._total = product.price
        self._database = None
        self._shop = None

    def to_dict(self) -> dict:
        return {'id': self._id, 'employee': self._cashier, 'customer': self._customer,
                'cashback': self._cashback, 'total': self._total, 'shop': self._shop}

    def __str__(self):
        return str({'class': type(self).__name__, **self.to_dict(),
            'products': [product.to_dict() for product in self._products]})

    @property
    def id(self) -> int:
        return self._id

    @property
    def products(self) -> list:
        return self._products

    @property
    def cashier(self) -> Cashier:
        return self._cashier

    @cashier.setter
    def cashier(self, new):
        if not isinstance(new, Cashier):
            raise TypeError("cashier must be an instance of Cashier")
        self._cashier = new

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def cashback(self) -> int:
        return self._cashback

    @property
    def total(self) -> int:
        return self._total

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("product must be an instance of Product")
        self._products.append(product)
        self._total += product.price

    def add_customer(self, phone: int):
        if not isinstance(phone, int) or len(str(phone)) < 7:
            raise ValueError("phone must be a valid integer phone number")

        for customer in self._database.customers:
            if customer.phone == phone:
                self._customer = customer
                return True
        return False

    def withdraw_cashback(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("amount must be a positive integer")

        if self._customer and self._customer.withdraw_cashback(amount):
            self._cashback += amount
            self._total -= amount
            return True
        return False

    def make_payment(self, card_number: int, expiration_date: list, cvv: int):

        #TODO: Finish the method
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

        pass

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