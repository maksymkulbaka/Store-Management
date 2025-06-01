# Store-Management
## Description
Python module for managing inventory, sales, and customer data in a store environment
## Installation
Download the `store_management.py` file and import it into your project.
```python
import store_management 
```
## Class Documentation
Class and its methods are fully documented with clear Python docstrings, following practices for easy understanding and use.
### Classes
* `Store(name,address)`

* `Category(id,name,products,store)`

* `Product(id,name,price,quantity,category,store)`

* `User(id,name,surname)`

* `Cashier(name,surname)`

* `Customer(phone,cashback,percent,purchases)`

## Error Handling
* Raises `TypeError` if incorrect types are passed to methods.
* Raises a`ValueError` if an incorrect value is entered (For example: raise ValueError(“Purchase amount must be non-negative.”).
