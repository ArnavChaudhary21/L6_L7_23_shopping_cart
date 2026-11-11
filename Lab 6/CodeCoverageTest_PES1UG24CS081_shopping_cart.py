import pytest
from shopping_cart import item_total, cart_discount, shipping_fee

# Code (line) coverage tests: every statement in shopping_cart.py runs at least once.


# ---------- item_total ----------
def test_food_item():
    assert item_total("food", 100, 2) == 210


def test_unknown_category_raises():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


def test_invalid_price_raises():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", -5, 1)


def test_bulk_discount_electronics():
    # 100 * 10 = 1000, bulk discount 100 -> 900, GST 18% -> 162
    assert item_total("electronics", 100, 10) == 1062


# ---------- cart_discount ----------
def test_cart_discount_above_5000():
    assert cart_discount(6000, False, None) == 500


def test_cart_discount_above_2000():
    assert cart_discount(3000, False, None) == 200


def test_cart_discount_small_cart():
    assert cart_discount(500, False, None) == 0


def test_cart_discount_prime_with_coupon():
    # 200 slab + 100 prime + 2500 // 10 coupon
    assert cart_discount(2500, True, "FLAT10") == 550


# ---------- shipping_fee ----------
def test_free_shipping():
    assert shipping_fee(1000, False, False) == 0


def test_prime_shipping():
    assert shipping_fee(100, True, False) == 0


def test_low_value_shipping():
    assert shipping_fee(100, False, False) == 40


def test_prime_express_shipping():
    # 0 + 100 express - 50 prime
    assert shipping_fee(100, True, True) == 50
