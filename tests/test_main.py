from src.main import Product, Category


def test_add_product():
    product = Product("Test Product", "Test Description", 1000.0, 10)
    category = Category("Test Category", "Test Description")
    category.add_product(product)

    assert len(category._products) == 1
    assert category._products[0].name == "Test Product"


def test_product_price_setter_positive():
    product = Product("Test Product", "Test Description", 1000.0, 10)
    product.price = 500
    assert product.price == 500


def test_product_price_setter_negative():
    product = Product("Test Product", "Test Description", 1000.0, 10)
    product.price = -500
    assert product.price == 1000


def test_category_product_count():
    product1 = Product("Product 1", "Description 1", 1000.0, 5)
    product2 = Product("Product 2", "Description 2", 1500.0, 3)
    category = Category("Test Category", "Test Description", [product1, product2])

    assert category.product_count == 2


def test_category_products():
    product1 = Product("Product 1", "Description 1", 1000.0, 5)
    category = Category("Test Category", "Test Description", [product1])

    assert category.products == "Product 1, 1000.0 руб. Остаток: 5 шт."
