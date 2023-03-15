from atexit import register

from main import add_product, add_to_cart, checkout, edit_product, login, remove_from_cart, remove_product, search_products


def test_register():
    assert register("user1", "password1") == True
    assert register("user2", "password2") == True
    assert register("user1", "password2") == False  # Username already exists


def test_login():
    assert login("user1", "password1") == True
    assert login("user2", "password2") == True
    assert login("user1", "password2") == False  # Incorrect password
    assert login("user3", "password3") == False  # User does not exist


def test_add_edit_remove_product():
    assert add_product("Product1", "Category1", 10.0, 20) == True
    assert add_product("Product2", "Category2", 20.0, 30) == True
    products = search_products("Product1")
    assert len(products) == 1
    assert products[0]["name"] == "Product1"
    assert edit_product(products[0]["id"], "NewProduct1",
                        "NewCategory1", 15.0, 25) == True
    products = search_products("NewProduct1")
    assert len(products) == 1
    assert products[0]["name"] == "NewProduct1"
    assert remove_product(products[0]["id"]) == True


def test_search_products():
    assert add_product("Product1", "Category1", 10.0, 20) == True
    assert add_product("Product2", "Category1", 20.0, 30) == True
    assert add_product("Product3", "Category2", 30.0, 40) == True
    products = search_products("Category1")
    assert len(products) == 2
    assert products[0]["name"] == "Product1"
    assert products[1]["name"] == "Product2"


def test_add_to_cart():
    assert register("user1", "password1") == True
    assert add_product("Product1", "Category1", 10.0, 20) == True
    assert add_to_cart(1, 1, 5) == True
    assert add_to_cart(1, 1, 15) == False  # Not enough stock


def test_remove_from_cart():
    assert register("user1", "password1") == True
    assert add_product("Product1", "Category1", 10.0, 20) == True
    assert add_to_cart(1, 1, 5) == True
    assert remove_from_cart(1, 1, 3) == True
    assert remove_from_cart(1, 1, 3) == False  # Not enough quantity in cart


def test_checkout():
    assert register("user1", "password1") == True
    assert add_product("Product1", "Category1", 10.0, 20) == True
    assert add_to_cart(1, 1, 5) == True
    assert checkout(1) == True
    assert checkout(1) == False  # Cart is empty
