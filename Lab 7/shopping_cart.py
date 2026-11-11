ZONES = {"1": "North", "2": "North", "3": "West", "4": "West",
         "5": "South", "6": "South", "7": "East", "8": "East"}

MAX_DIGITS = 9  # keeps int() fast and away from Python's huge-number limit


def _to_number(text):
    # A non-negative whole number written with ASCII digits only.
    # Rejects "", "-5", "1.5", " 7", unicode digits like "²" or "١", and huge values.
    text = text.strip()
    if not text.isascii() or not text.isdigit() or len(text) > MAX_DIGITS:
        return None
    return int(text)


def cart_total(cart):
    # Returns the cart total, 0 for an empty cart, or None if the cart is invalid.
    if not isinstance(cart, str):
        return None
    if cart.strip() == "":
        return 0
    total = 0
    for item in cart.split(','):
        parts = item.split(':')
        if len(parts) != 2 or parts[0].strip() == "":
            return None
        amounts = parts[1].lower().split('x')
        if len(amounts) != 2:
            return None
        price, qty = _to_number(amounts[0]), _to_number(amounts[1])
        if price is None or qty is None or qty == 0:
            return None
        total += price * qty
    return total


def promo_percent(code):
    # Returns the discount for a code like "OFF20" (0-100), or 0 if the code is invalid.
    if not isinstance(code, str):
        return 0
    code = code.strip().upper()
    if not code.startswith('OFF'):
        return 0
    percent = _to_number(code[3:])
    if percent is None or percent > 100:
        return 0
    return percent


def delivery_zone(pincode):
    # Returns the zone for a 6 digit pincode, or None if the pincode is invalid.
    if not isinstance(pincode, str):
        return None
    pincode = pincode.strip()
    if len(pincode) != 6 or _to_number(pincode) is None:
        return None
    return ZONES.get(pincode[0])


def main():
    print("==== Running cart_total ====")
    user_input = input("Enter cart as name:pricexqty CSV (e.g. pen:10x2,book:250x1): ")
    result = cart_total(user_input)
    if result is None:
        print("Invalid cart. Use name:pricexqty separated by commas.")
    else:
        print("Cart Total:", result)

    print("\n==== Running promo_percent ====")
    user_input = input("Enter a promo code (e.g. OFF20): ")
    result = promo_percent(user_input)
    if result == 0:
        print("Invalid or unknown promo code. Discount Percent: 0")
    else:
        print("Discount Percent:", result)

    print("\n==== Running delivery_zone ====")
    user_input = input("Enter a 6 digit pincode (e.g. 560085): ")
    result = delivery_zone(user_input)
    if result is None:
        print("Invalid pincode or no delivery to this area.")
    else:
        print("Delivery Zone:", result)


if __name__ == "__main__":
    main()
