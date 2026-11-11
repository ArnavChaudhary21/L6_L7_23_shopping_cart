import pytest
from shopping_cart import item_total, cart_discount, shipping_fee

# Branch coverage tests: every if / elif / else decision in shopping_cart.py
# is driven to both its True and False outcome, including boundary values.


# ---------- item_total ----------
def test_food_item():
    assert item_total("food", 100, 2) == 210


def test_unknown_category_raises():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


def test_negative_price_raises():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", -1, 1)


def test_zero_quantity_raises():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", 100, 0)


def test_zero_price_allowed():
    assert item_total("clothing", 0, 1) == 0


def test_qty_9_no_bulk_discount():
    # 10 * 9 = 90, GST 5% -> 4
    assert item_total("food", 10, 9) == 94


def test_qty_10_bulk_discount():
    # 10 * 10 = 100, bulk discount 10 -> 90, GST 5% -> 4
    assert item_total("food", 10, 10) == 94


def test_clothing_gst():
    # 50 * 3 = 150, GST 12% -> 18
    assert item_total("clothing", 50, 3) == 168


def test_electronics_bulk_gst():
    assert item_total("electronics", 100, 10) == 1062


# ---------- cart_discount ----------
def test_discount_exactly_5000():
    assert cart_discount(5000, False, None) == 500


def test_discount_just_below_5000():
    assert cart_discount(4999, False, None) == 200


def test_discount_exactly_2000():
    assert cart_discount(2000, False, None) == 200


def test_discount_just_below_2000():
    assert cart_discount(1999, False, None) == 0


def test_discount_prime_only():
    assert cart_discount(500, True, None) == 100


def test_coupon_flat10_at_1000():
    assert cart_discount(1000, False, "FLAT10") == 100


def test_coupon_flat10_below_1000():
    # right coupon but cart too small -> no coupon discount
    assert cart_discount(999, False, "FLAT10") == 0


def test_wrong_coupon_code():
    # big enough cart but wrong code -> no coupon discount
    assert cart_discount(3000, False, "SAVE20") == 200


def test_all_discounts_combined():
    # 500 slab + 100 prime + 6000 // 10 coupon
    assert cart_discount(6000, True, "FLAT10") == 1200


# ---------- shipping_fee ----------
def test_free_shipping():
    assert shipping_fee(1000, False, False) == 0


def test_prime_standard_shipping():
    assert shipping_fee(100, True, False) == 0


def test_shipping_exactly_500():
    assert shipping_fee(500, False, False) == 0


def test_shipping_just_below_500():
    assert shipping_fee(499, False, False) == 40


def test_express_non_prime_low_value():
    assert shipping_fee(100, False, True) == 140


def test_express_non_prime_high_value():
    assert shipping_fee(600, False, True) == 100


def test_express_prime():
    assert shipping_fee(100, True, True) == 50
