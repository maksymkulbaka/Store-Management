# Store-Management
### Description
 Store-Management - this is a python module that allows you to create a database, add stores, categories, products, employees, and customers, as well as make purchases with cashback.
  
# How to start working with the module?
+ Download the `store_management.py` file
+ Import it into your project: 
```python
import store_management 
```
+ Done! Now you can work with the module.
   
# Features
+ Management of stores, categories, and products.
+ Registration of customers and cashiers.
+ Ability to make purchases with cashback.
+ Payment processing (simulation).
+ Output of information in the form of dictionaries or readable lines.

# Data verification  
## This module implements verification of the correctness of the entered data.

**1).** Type Checking  
Use `isinstance()` to check if an object has the correct type:
```py
if not isinstance(name, str):
    raise TypeError("Name must be a string.")
```  
+ This is in class constructors: `Store`, `Category`, `Product`, `User`, `Customer`, `ShoppingCart`
+ addition methods (`add_product`, `add_category`, `add_customer`)
---
**2).** Checking logical constraints  
```py
if not name.strip():
    raise ValueError("Name must be a non-empty string.")
if phone <= 0:
    raise ValueError("Phone must be a positive integer.")
if not (0 <= percent <= 100):
    raise ValueError("Percent must be an integer between 0 and 100.")
```
---
**3).** Data structure verification  
In the `make_payment method`:
```py
if not (isinstance(expiration_date, list) and len(expiration_date) == 2):
    raise ValueError("expiration_date must be a list of [month, year]")
```
---
**4).** Error handling  
In the `make_payment method`, the entire block is enclosed in `try`/`except` to prevent the program from crashing:
```py
except Exception as e:
    self._status = "failed"
    print(f"Payment failed: {str(e)}")
```  
# Class Documentation
Class and its methods are fully documented with clear Python docstrings, following practices for easy understanding and use.
   
### Description of available classes
  
**Class: Database** - *Represents a database to manage stores, categories, products, cashiers, customers, and purchases.*  
|Attribute | Attribute definition |
|----------|-|
|`_name: str` | Name of the database.|
|`_stores: list` | Registered stores.|
|`_categories: list` | Registered categories.|
|`_products: list` | Registered products.|
|`_cashiers: list` | Registered cashiers.|
|`_customers: list` | Registered customers.|
|`_purchases: list` | List of purchase records (currently unused).|
___
|Methods | Definition of methods |
|--------|-|
|`add_stores(*stores: Store)` | Add Store instances.|
|`remove_stores(*stores: Store)` | Remove Store instances.|
|`add_categories(*categories: Category)` | Add Category instances.|
|`remove_categories(*categories: Category)` | Remove Category instances.|
|`add_products(*products: Product)` | Add Product instances. |
|`remove_products(*products: Product)` | Remove Product instances. |
|`add_cashiers(*cashiers: Cashier)` | Add Cashier instances. |
|`remove_cashiers(*cashiers: Cashier)` | Remove Cashier instances. |
|`add_customers(*customers: Customer)` | Add Customer instances. |
|`remove_customers(*customers: Customer)` | Remove Customer instances. |
|`find_customer_by_phone(phone) → Customer _bool_` | Returns a customer by phone or False if not found. |
   
---
**Class: Store** - *Represents a retail store.*  
|Attribute | Attribute definition |
|----------|-|
|`_id: int (None)` | A unique identifier for the store (optional). |
|`_name: str` | The name of the store. |
|`_address: str` | The physical address of the store. |
|`_categories: list [Category]`  | A list of Category instances associated with the store. |
|`_products: list[Product]` | A list of Product instances available in the store. |
|`_database: Database (None)` | The Database instance the store is registered with (or None if not linked). |
___
|Methods | Definition of methods |
|--------|-|
|`to_dict() → dict` | Returns dictionary representation. |
|`__str__() → str` | Human-readable format. |
|`add_category(*categories: Category)` | Adds one or more Category instances to the store. |
|`remove_category(*categories: Category)` | Removes one or more Category instances from the store. |
|`add_product(*products: Product)` | Adds one or more Product instances to the store. |
|`remove_product(*products: Product)` | Removes one or more Product instances from the store. |
|`set_database(database: Database (None)` | Links or unlinks the store to a Database instance. |

---
**Class: Category** - *Represents a product category within a store.*
|Attribute | Attribute definition |
|----------|-|
|`_id: int (None)` | A unique identifier for the category. |
|`_name: str` | The name of the category. |
|`_products: list[Product]` | List of products assigned to this category. |
|`_store: Store (None)` | Reference to the store the category belongs to (or None). |
|`_database: Database (None)` | The database instance managing this category. |
___
|Methods | Definition of methods |
|--------|-|
|`to_dict()` | dict: Returns a dictionary with the category’s id and name. |
|`__str__() → str:` | Returns a readable string with category details, products, and its store. |
|`add_product(*products: Product)` | Adds one or more Product instances to the category. |
|`remove_product(*products: Product)` | Removes one or more Product instances from the category. |
|`set_store(store: Store (None)` | Links or unlinks the category to a Store. |
|`set_database(database: Database (None))` |  Links or unlinks the category to a Database. |

---
**Class: Product** - *Represents an item for sale.*
|Attribute | Attribute definition |
|----------|-|
|`_id: int` | None — A unique identifier for the product. |
|`_name: str` | The product name. |
|`_price: int` | The price of the product in smallest currency units. |
|`_quantity: int` | The number of units available in stock. |
|`_category: Category (None)` | The category this product belongs to. |
|`_store: Store (None)` | The store this product is sold in. |
|`_database: Database (None)` | The parent database managing this product. |
___
|Methods | Definition of methods |
|--------|-|
|`to_dict() → dict:` | Returns a dictionary with product data (id, name, price, quantity). |
|`__str__() → str:` | Returns a string representation of the product including its category and store. |
|`set_category(category: Category (None))` |  Links or unlinks the product to a Category. |
|`set_store(store: Store (None))` | Links or unlinks the product to a Store. |
|`set_database(database: Database (None))` | Links or unlinks the product to a Database. |

---
**Class: User _(Base class)_** - *Represents a person with a name and surname.*
|Attribute | Attribute definition |
|----------|-|
|`_id: int (None)` | Unique identifier for the user. |
|`_name: str` | First name of the user. |
|`_surname: str` | Last name of the user. |
|`_database: Database (None)` | Reference to the associated Database instance. |
___
|Methods | Definition of methods |
|--------|-|
|`to_dict() → dict:` | Returns a dictionary with the user’s id, name, and surname. |
|`__str__() → str:` | Returns a string representation of the user with their class type and data. |
  
---
**Class: Cashier _(inherits from User)_** - *Represents an employee responsible for transactions.*
|Attribute | Attribute definition |
|----------|-|
|`_id` | See above. _(Not a unique attribute)_ |
|`_name` | See above. _(Not a unique attribute)_ |
|`_surname` | See above. _(Not a unique attribute)_ |
|`_database` | See above. _(Not a unique attribute)_ |
___
|Methods | Definition of methods |
|--------|-|
|`__str__() → str:` | Returns a string representation of the cashier including their user data. |
|`set_database(database: Database (None))` | Links or unlinks the cashier to a Database. |
  
---
**Class: Customer _(inherits from User)_** - *Represents a client with cashback and phone.*
|Attribute | Attribute definition |
|----------|-|
|`_id: int (None)` | A unique identifier for the cart (optional). | 
|`_products: list[Product]` | A list of Product instances currently in the cart. |
|`_cashier: Cashier (None)` | The Cashier assigned to the transaction (or None if not assigned). |
|`_customer: Customer (None)` | The Customer linked to the cart (or None if not assigned). |
|`_cashback: int` | The cashback amount applied to this transaction. |
|`_total: int` | The total price of the products in the cart after cashback is applied. |
|`_store: Store (None)` | The Store where the cart is being used (optional). |
|`_database: Database (None)` | The Database instance the cart is linked to (or None if not linked). |
|`_status: str` | The current status of the cart ("pending", "success", or "failed"). |
___
|Methods | Definition of methods |
|--------|-|
|`to_dict() → dict` | Returns a dictionary containing the customer’s basic data including name, surname, phone number, cashback amount, and cashback percent. Does not include purchases.|
|`__str__() → str` | Returns a human-readable string with all customer data including class name and purchase history. |
|`add_purchase(order: dict)` | Adds a purchase record (typically a dictionary of cart info) to the customer's list of purchases. |
|`withdraw_cashback(amount: int) → bool` | Attempts to deduct the given cashback amount from the customer's balance. Returns True if successful; False if the amount exceeds the current balance. |
|`accrue_cashback(order_amount: int)` | Increases the customer’s cashback balance by calculating a percentage (_percent) of the given order amount. |
|`set_database(database: Database (None))` | Associates the customer with a Database instance, or removes the association if None. Automatically updates both sides of the relationship. |
  
---
**Class: ShoppingCart** - *Manages a customer's shopping session and handles payment.*
|Attribute | Attribute definition |
|----------|-|
|`_id: int (None)` | A unique identifier for the cart (optional). |
|`_products: list[Product]` | A list of Product instances currently in the cart. |
|`_cashier: Cashier (None)` | The Cashier assigned to the transaction (or None if not assigned). |
|`_customer: Customer (None)` | The Customer linked to the cart (or None if not assigned). |
|`_cashback: int` | The cashback amount applied to this transaction. |
|`_total: int` | The total price of the products in the cart after cashback is applied. |
|`_store: Store (None)` | The Store where the cart is being used (optional). |
|`_database: Database (None)` | The Database instance the cart is linked to (or None if not linked). |
|`_status: str` | The current status of the cart ("pending", "success", or "failed"). |
___
|Methods | Definition of methods |
|--------|-|
|`to_dict() → dict` | Returns a dictionary representation of the cart including its ID, cashier, customer, cashback used, total price, store, and current status. Excludes the product list.
|`__str__() → str` | Returns a readable string with full cart details, including the product list and class name.
|`add_product(product: Product)` | Adds a product to the cart and updates the total amount payable accordingly. Raises a TypeError if the input is not a Product.
|`add_customer(phone: int) → bool` | Searches for a customer in the database by phone number. If found, assigns the customer to the cart and returns True; otherwise returns False.
|`withdraw_cashback(amount: int) → bool` | Applies cashback from the customer’s account to reduce the total. Returns True if successfully applied; False otherwise.
|`make_payment(card_number: int, expiration_date: list[int], cvv: int) → bool` | Simulates payment processing. Validates input fields, checks product availability, deducts quantities, applies cashback, stores the order, and updates the cart status to "success" or "failed". Returns True on success and False on failure. |
  

# How it works
```python
import store_management

# Creating a database
db = Database("DataBase")

# Creating a store
store1 = Store("Big Price Store", "Ordinary street 32")

# Adding categories
category1 = Category("Food")
category2 = Category("Clothing")
store1.add_category(category1, category2)
# Adding products
product1 = Product("Sausage", 1050, 200)
product2 = Product("T-shirt", 1500, 50)
category1.add_product(product1)
category2.add_product(product2)
store1.add_product(product1, product2)
# Creating a customer
customer = Customer("Maks", "Vovk", 380661234556)
db.add_customers(customer)
# Creating a shoppingcart
cart = ShoppingCart(product1)
cart._database = db  # прив'язка бази даних
cart.add_customer(380991234567)
# Use cashback, if available
cart.withdraw_cashback(100)
# Making payments, what can be success, pending, failed
cart.make_payment(1234567890123, [12, 2025], 123)
```
