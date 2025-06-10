from store_management import *

"""
Creating a database and store
"""

db = Database("DB1")
store = Store("SuperSuperSuperMarket", "5 avenue")
db.add_stores(store)

"""
Adding categories
"""
categories = [
    Category("Food"),
    Category("Electronics"),
    Category("Books"),
    Category("Clothing"),
    Category("Toys")]
store.add_category(*categories)
db.add_categories(*categories)

"""
Adding products
"""
products = [
    Product("Bread", 25, 100),
    Product("Milk", 30, 80),
    Product("Smartphone", 8000, 10),
    Product("Laptop", 25000, 5),
    Product("NovelBook", 200, 50),
    Product("Textbook", 500, 30),
    Product("T-shirt", 350, 70),
    Product("Jeans", 900, 40),
    Product("Puzzle", 150, 60),
    Product("Lego Set", 1200, 15), ]

"""
Distribution of products by category
"""
categories[0].add_product(products[0], products[1])  # Food
categories[1].add_product(products[2], products[3])  # Electronics
categories[2].add_product(products[4], products[5])  # Books
categories[3].add_product(products[6], products[7])  # Clothing
categories[4].add_product(products[8], products[9])  # Toys

store.add_product(*products)
db.add_products(*products)

"""
Adding cashiers and customers
"""
cashier = Cashier("Maks", "Vovk", "+380991234012")
customer1 = Customer("Anna", "Block", "+380991234001")
customer2 = Customer("Taras", "Shevchenko", "+380991234002")
customer3 = Customer("Victoria", "Hnatiuk", "+380991234003")
db.add_cashiers(cashier)
db.add_customers(customer1, customer2, customer3)

"""
Creating shopping carts for Customer 1-3
"""

#Customer1 - Transaction success
cart1 = ShoppingCart(products[0], db)  # Bread
cart1.add_product(products[4])     # NovelBook
cart1.cashier = cashier
cart1._database = db
cart1.add_customer("+380991234001")
customer1.cashback = 30
cart1.withdraw_cashback(20)
cart1.make_payment(1234567812345678, [11, 2026], 123)

#Customer2 - Transaction pending
cart2 = ShoppingCart(products[2], db)  # Smartphone
cart2.add_product(products[6])     # T-shirt
cart2.add_product(products[8])     # Puzzle
cart2.cashier = cashier
cart2._database = db
cart2.add_customer("+380991234002")
customer2.cashback = 0
print(cart2.customer)

try:
    #Customer3 - Transaction failed
    cart3 = ShoppingCart(products[3], db)  # Laptop
    cart3.cashier = cashier
    cart3._database = db
    cart3.add_customer("+380991234003")
    customer3.cashback = 1000
    cart3.withdraw_cashback(500)
    cart3.make_payment(3456789034567890, [13, 2025], 456)
    print(cart3.customer)
except Exception as e:
    print(e)


print("Customers and cashback")
for customer in [customer1, customer2, customer3]:
    print(f"{customer.name} {customer.surname} - Cashback: {customer.cashback} ₴")
    print("Shopping:", customer.purchases)
    print([i.get_receipt() for i in customer.purchases])

print("Transaction")
print(f"Cart1 (Anna): {cart1.status}")
print(f"Cart2 (Bohdan): {cart2.status}")