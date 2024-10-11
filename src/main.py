class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


class Category:
    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0.0

    def __repr__(self):
        return f"Category(name={self.name}, products={self.products})"


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print("Возникла ошибка ValueError: ", e)

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print("Средняя цена товаров категории 'Смартфоны':", category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print("Средняя цена товаров в пустой категории:", category_empty.middle_price())
