import string

from hypothesis import given, strategies as st
from shopping_cart import cart_total, promo_percent, delivery_zone, ZONES

# Any kind of input a user (or attacker) might send: random unicode text,
# None, or a value of the wrong type altogether.
anything = st.text() | st.none() | st.integers() | st.floats()


# ---------- Property 1: the functions never crash ----------

@given(anything)
def test_cart_total_no_crash(s):
    try:
        result = cart_total(s)
    except Exception as e:
        assert False, f"cart_total crashed with: {e!r}"
    assert result is None or (isinstance(result, int) and result >= 0)


@given(anything)
def test_promo_percent_no_crash(s):
    try:
        result = promo_percent(s)
    except Exception as e:
        assert False, f"promo_percent crashed with: {e!r}"
    assert isinstance(result, int) and 0 <= result <= 100


@given(anything)
def test_delivery_zone_no_crash(s):
    try:
        result = delivery_zone(s)
    except Exception as e:
        assert False, f"delivery_zone crashed with: {e!r}"
    assert result is None or result in ZONES.values()


# ---------- Property 2: valid inputs still give the right answer ----------

item = st.tuples(
    st.text(alphabet=string.ascii_letters, min_size=1, max_size=10),
    st.integers(min_value=0, max_value=100000),
    st.integers(min_value=1, max_value=1000),
)


@given(st.lists(item, min_size=1, max_size=10))
def test_cart_total_valid_cart(items):
    cart = ",".join(f"{name}:{price}x{qty}" for name, price, qty in items)
    assert cart_total(cart) == sum(price * qty for _, price, qty in items)


@given(st.integers(min_value=0, max_value=100), st.sampled_from(["OFF", "off", "Off"]))
def test_promo_percent_valid_code(percent, prefix):
    assert promo_percent(f"{prefix}{percent}") == percent


@given(st.from_regex(r"[1-8][0-9]{5}", fullmatch=True))
def test_delivery_zone_valid_pincode(pincode):
    assert delivery_zone(pincode) == ZONES[pincode[0]]


# ---------- Property 3: specific invalid inputs are rejected ----------

@given(st.integers(min_value=101, max_value=10**6))
def test_promo_percent_over_100_rejected(percent):
    assert promo_percent(f"OFF{percent}") == 0


@given(st.from_regex(r"[09][0-9]{5}", fullmatch=True))
def test_delivery_zone_unknown_first_digit(pincode):
    assert delivery_zone(pincode) is None
