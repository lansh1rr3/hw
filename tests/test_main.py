import pytest

from src.main import Category, LawnGrass, Product, Smartphone


def test_product_initialization() -> None:
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter_positive_value() -> None:
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.price = 200000.0

    assert product.price == 200000.0


def test_product_addition() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    total_price = product1.price * product1.quantity + product2.price * product2.quantity
    assert total_price == (180000.0 * 5 + 210000.0 * 8)


def test_product_addition_invalid_type() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)

    with pytest.raises(TypeError):
        _ = product1 + 10


def test_category_initialization() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Различные модели смартфонов", [product1, product2])
    assert category.name == "Смартфоны"
    assert category.description == "Различные модели смартфонов"
    assert len(category.products) == 2


def test_category_add_product() -> None:
    category = Category("Смартфоны", "Различные модели смартфонов")
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category.add_product(product)
    assert len(category.products) == 1


def test_category_add_invalid_product() -> None:
    category = Category("Смартфоны", "Различные модели смартфонов")

    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_smartphone_initialization() -> None:
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawngrass_initialization() -> None:
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_product_addition_same_type() -> None:
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    total_quantity = smartphone1 + smartphone2

    assert total_quantity == 13


def test_product_addition_different_type() -> None:
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        _ = smartphone + grass
