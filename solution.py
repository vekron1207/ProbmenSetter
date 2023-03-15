from typing import List, Dict, Union

# A global variable to keep track of users
users = {}

# A global variable to keep track of products
products = {}

# A global variable to keep track of carts
carts = {}


def register(username: str, password: str) -> bool:
    """Registers a new user."""
    if username in users:
        return False
    users[username] = password
    return True


def login(username: str, password: str) -> bool:
    """Logs in an existing user."""
    if username not in users or users[username] != password:
        return False
    return True


def add_product(name: str, category: str, price: float, stock: int) -> bool:
    """Adds a new product to the catalog."""
    product_id = len(products) + 1
    products[product_id] = {
        "name": name, "category": category, "price": price, "stock": stock}
    return True


def edit_product(product_id: int, name: str, category: str, price: float, stock: int) -> bool:
    """Edits an existing product in the catalog."""
    if product_id not in products:
        return False
    products[product_id] = {
        "name": name, "category": category, "price": price, "stock": stock}
    return True


def remove_product(product_id: int) -> bool:
    """Removes a product from the catalog."""
    if product_id not in products:
        return False
    del products[product_id]
    return True


def search_products(query: str) -> List[Dict[str, Union[int, str, float]]]:
    """Searches for products by name or category."""
    results = []
    for product_id, product in products.items():
        if query.lower() in product["name"].lower() or query.lower() in product["category"].lower():
            result = {"id": product_id, "name": product["name"], "category": product["category"],
                      "price": product["price"], "stock": product["stock"]}
            results.append(result)
    return results


def add_to_cart(user_id: int, product_id: int, quantity: int) -> bool:
    """Adds a product to the user's cart."""
    if user_id not in carts:
        carts[user_id] = {}
    if product_id not in products:
        return False
    if products[product_id]["stock"] < quantity:
        return False
    if product_id not in carts[user_id]:
        carts[user_id][product_id] = 0
    carts[user_id][product_id] += quantity
    products[product_id]["stock"] -= quantity
    return True


def remove_from_cart(user_id: int, product_id: int, quantity: int) -> bool:
    """Removes a product from the user's cart."""
    if user_id not in carts or product_id not in carts[user_id]:
        return False
    if carts[user_id][product_id] < quantity:
        return False
    carts[user_id][product_id] -= quantity
    products[product_id]["stock"] += quantity
    if carts[user_id][product_id] == 0:
        del carts[user_id][product_id]
    if not carts[user_id]:
        del carts[user_id]
    return True


def checkout(user_id: int) -> bool:
    """Checks out the user's cart."""
    if user_id not in carts:
        return False
    total = 0
    for product_id, quantity in carts[user_id].items():
        if product_id not in products or products[product_id]["stock"] < quantity:
            return False
    total += products[product_id]["price"] * quantity
    if total > 0:
        # TODO: process payment
        carts[user_id] = {}
    return True
