# Store-Management
### Description
 Store-Management - this is a python module that allows you to create a database, add stores, categories, products, employees, and customers, as well as make purchases with cashback.
# How to start working with the module?
+ 1). Download the `store_management.py` file
+ 2). Import it into your project: 
```python
import store_management 
```
+ 3). Done! Now you can work with the module.
# Class Documentation
Class and its methods are fully documented with clear Python docstrings, following practices for easy understanding and use.
### Description of available classes
* `Database`
##### Stores objects: stores, categories, products, cashiers, customers.
##### Methods: add_*, remove_*, find_customer_by_phone.
#
* `Store`
##### Name, address, categories, products.
##### Methods: add_category, add_product, remove_category, remove_product.
#
* `Category`
##### Category name, store affiliation.
##### Methods: add_product, remove_product.
#
* `Product`
##### Name, price, quantity, links to category and store.
#
* `User`
##### Parent class for Customer and Cashier
##### Stores first name and last name.
#
* `Customer`
##### Additionally stores phone number, cashback, purchase history.
##### Methods: withdraw_cashback, accrue_cashback.
#
* `Cashier`
##### Represents a store employee (inherits User).
#
* `ShoppingCart`
##### Shopping cart with products, customer, cashier, total amount.
##### Methods: add_product, add_customer, withdraw_cashback, make_payment.
#
# Error handling
* Raises `TypeError` if incorrect types are passed to methods.
* Raises a`ValueError` if an incorrect value is entered (For example: raise ValueError(“Purchase amount must be non-negative.”).
#
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


