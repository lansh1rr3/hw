from src.main import Category, Product


def test_product_creation():
    product = Product("Тестовый продукт", "Описание", 1000, 10)
    assert product.name == "Тестовый продукт"
    assert product.price == 1000
    assert product.quantity == 10


def test_price_setter():
    product = Product("Тестовый продукт", "Описание", 1000, 10)
    product.price = 500
    assert product.price == 500

    product.price = -100
    assert product.price == 500


def test_product_addition():
    product1 = Product("Продукт1", "Описание1", 1000, 5)
    product2 = Product("Продукт2", "Описание2", 2000, 3)
    assert product1 + product2 == 11000


def test_category_creation():
    category = Category("Тестовая категория", "Описание")
    assert category.name == "Тестовая категория"
    assert category.description == "Описание"


def test_category_add_product():
    category = Category("Тестовая категория", "Описание")
    product = Product("Продукт", "Описание", 1000, 10)
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product


def test_category_product_count():
    category = Category(
        "Тестовая категория",
        "Описание",
        [Product("Продукт1", "Описание1", 1000, 5), Product("Продукт2", "Описание2", 2000, 3)],
    )
    assert category.product_count == 8
