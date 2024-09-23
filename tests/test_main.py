import pytest

from src.main import Category, Product


@pytest.fixture
def product1():
    return Product("Product1", "Description1", 10.99, 5)


@pytest.fixture
def product2():
    return Product("Product2", "Description2", 20.99, 2)


@pytest.fixture
def category(product1, product2):
    return Category("Category1", "Description1", [product1, product2])


def test_product_initialization(product1):
    assert product1.name == "Product1"
    assert product1.description == "Description1"
    assert product1.price == 10.99
    assert product1.quantity == 5


def test_total_products(category):
    assert Category.total_products == 2


def test_category_initialization(category):
    assert category.name == "Category1"
    assert category.description == "Description1"
    assert len(category.products) == 2


def test_total_categories(category):
    assert Category.total_categories == 3


@pytest.fixture
def other_category():
    return Category("Category2", "Description2", [])


def test_increment_total_categories(other_category):
    assert Category.total_categories == 4
