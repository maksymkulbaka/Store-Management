class Product:
    def __init__(self, name: str, category: str, price: int):
        if isinstance(name, str):
            raise TypeError("Argument 'name' should be str data type")
        if isinstance(category, str):
            raise TypeError("Argument 'category' should be str data type")
        if isinstance(price, int):
            raise TypeError("Argument 'price' should be str data type")
        self._name = name
        self._category = category
        self._price = price

    def get_info(self) -> dict:
        return {'name': self._name, 'category': self._category, 'price': self._price}

    def __str__(self) -> str:
        return str(self.get_info())

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new):
        if not isinstance(new, str):
            raise TypeError("Argument should be str data type")
        self._name = new

if __name__ == "__main__":
    prod1 = Product("Sausage", "Meat", 3050)