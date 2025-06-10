import store_management
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Spark123321",
    database = "may_market"
)

class MySqlDatabase(store_management.AbstractDatabase):
    def __init__(self, database):
        self._database = database
        self._cursor = database.cursor(dictionary=True)

    def add_products(self, *products: 'store_management.Product'):
        for product in products:
            if not isinstance(product, store_management.Product):
                raise TypeError(f"expected Product instance, got {type(product).__name__}")
            self._cursor.execute(f"SELECT * FROM product WHERE barcode = (%s) LIMIT 1", (product.barcode,))
            result = self._cursor.fetchone()
            if result:
                raise ValueError(f"barcode '{product.barcode}' exists in product with id '{result['product_id']}'")
        for product in products:
            self._cursor.execute(f"INSERT INTO product (name, barcode, price, category_id) VALUES (%s, %s, %s, %s);",
                (product.name, product.barcode, product.price, product.category.id if product.category else None))
            self._database.commit()
            product.set_id(self.get_product_by_barcode(product.barcode).id)

    def get_products(self) -> list:
        self._cursor.execute(f"SELECT * FROM product")
        return self._cursor.fetchall()

    def get_product_by_id(self, id: int | str) -> 'Product | None':
        if not isinstance(id, (int, str)):
            raise TypeError(f"expected id as integer or string, got {type(id).__name__}")
        self._cursor.execute(
            f"SELECT * FROM product WHERE product_id = %s", (id,))
        result = self._cursor.fetchall()
        if not result:
            return None
        if len(result) > 1:
            raise ValueError(f"table has several records with the same id: {result}")
        result = result[0]
        product = store_management.Product(result['name'], result['barcode'], result['price'])
        product.set_id(result['product_id'])
        return product

    def get_product_by_barcode(self, barcode: int | str) -> 'Product | None':
        if not isinstance(barcode, int):
            raise TypeError(f"expected barcode as integer, got {type(barcode).__name__}")
        self._cursor.execute(
            f"SELECT * FROM product WHERE barcode = %s", (barcode,))
        result = self._cursor.fetchall()
        if not result:
            return None
        if len(result) > 1:
            raise ValueError(f"table has several records with the same barcode: {result}")
        result = result[0]
        product = store_management.Product(result['name'], result['barcode'], result['price'])
        product.set_id(result['product_id'])
        return product

    def update_products(self, *products: 'store_management.Product'):
        for product in products:
            if not isinstance(product, store_management.Product):
                raise TypeError(f"expected Product instance, got {type(product).__name__}")
            if not product.id:
                raise ValueError(f"product has no id")
        for product in products:
            self._cursor.execute(
                f"UPDATE product SET name = %s, barcode = %s, price = %s, category_id = %s WHERE product_id = %s",
                (product.name, product.barcode, product.price, product.category, product.id))
            self._database.commit()

    def remove_products(self, *products: 'store_management.Product'):
        for product in products:
            if not isinstance(product, store_management.Product):
                raise TypeError(f"expected Product instance, got {type(product).__name__}")
            if not product.id:
                raise ValueError(f"product has no id")
        for product in products:
            self._cursor.execute(f"DELETE FROM product WHERE product_id = %s", (product.id,))
            self._database.commit()
            product.set_id(None)

    def remove_products_by_id(self, *ids: int | str):
        for id in ids:
            if not isinstance(id, (int | str)):
                raise TypeError(f"expected id as integer or string, got {type(id).__name__}")
        for id in ids:
            self._cursor.execute(f"DELETE FROM product WHERE product_id = %s", (id,))

    def add_customer(self, customer: 'store_management.Customer'):
        if not isinstance(customer, store_management.Customer):
            raise TypeError(f"Expected Customer instance, got {type(customer).__name__}")
        sql = "INSERT INTO customer (name, surname, phone, cashback, percent) VALUES (%s, %s, %s, %s, %s)"
        val = (customer.name, customer.surname, customer.phone, customer.cashback, customer.percent)
        self._cursor.execute(sql, val)
        self._database.commit()