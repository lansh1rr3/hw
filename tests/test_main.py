from src.main import Product, Category


def test_product_price_getter_setter():
    product = Product("Test Product", "Description", 1000, 10)
    assert product.price == 1000

    product.price = 1500
    assert product.price == 1500

    product.price = -500
    assert product.price == 1500


def test_new_product_classmethod():
    product_data = {
        "name": "New Product",
        "description": "New description",
        "price": 5000,
        "quantity": 20
    }
    new_product = Product.new_product(product_data)

    assert new_product.name == "New Product"
    assert new_product.description == "New description"
    assert new_product.price == 5000
    assert new_product.quantity == 20


def test_add_product_to_category():
    product1 = Product("Product 1", "Description 1", 1000, 5)
    product2 = Product("Product 2", "Description 2", 2000, 3)
    category = Category("Test Category", "Category description")

    assert category.product_count == 0

    category.add_product(product1)
    assert category.product_count == 1

    category.add_product(product2)
    assert category.product_count == 2

    expected_product_list = (
        "Product 1, 1000 руб. Остаток: 5 шт.\n"
        "Product 2, 2000 руб. Остаток: 3 шт."
    )
    assert category.products == expected_product_list


def test_product_category_str():
    product1 = Product("Product 1", "Description 1", 1000, 5)
    product2 = Product("Product 2", "Description 2", 2000, 3)
    category = Category("Test Category", "Category description", [product1, product2])

    assert str(product1) == "Product 1, 1000 руб. Остаток: 5 шт."
    assert str(product2) == "Product 2, 2000 руб. Остаток: 3 шт."

    assert str(category) == "Test Category, количество продуктов: 2 шт."


def test_product_addition():
    product1 = Product("Product 1", "Description 1", 1000, 5)
    product2 = Product("Product 2", "Description 2", 2000, 3)

    total_price = product1 + product2
    assert total_price == (1000 * 5) + (2000 * 3)


def test_negative_price():
    product = Product("Test Product", "Description", 1000, 10)
    product.price = -100
    assert product.price == 1000
