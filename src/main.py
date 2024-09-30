class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data):
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products else []
        self._product_count = len(self._products)

    def add_product(self, product):
        self._products.append(product)
        self._product_count += 1

    @property
    def products(self):
        product_list = [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self._products
        ]
        return "\n".join(product_list)

    @property
    def product_count(self):
        return self._product_count


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print("Список товаров:")
    print(category1.products)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("\nПосле добавления продукта:")
    print(category1.products)
    print(f"Общее количество товаров: {category1.product_count}")

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}
    )
    print("\nСозданный продукт через класс-метод:")
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    print("\nИзменение цены продукта:")
    new_product.price = 800
    print(new_product.price)
    new_product.price = -100
    print(new_product.price)
