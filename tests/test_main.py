import pytest

from src.main import Category, Product


def test_product_creation():
    product = Product("Товар 1", "Описание товара 1", 100.0, 1)
    assert product.name == "Товар 1"
    assert product.price == 100.0
    assert product.quantity == 1


def test_product_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Описание", 1000.0, 0)


def test_category_middle_price():
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 1)
    product2 = Product("Товар 2", "Описание товара 2", 200.0, 1)
    category = Category("Категория 1", "Описание категории 1", [product1, product2])
    assert category.middle_price() == 150.0


def test_category_empty():
    category = Category("Пустая категория", "Категория без продуктов", [])
    assert category.middle_price() == 0.0
