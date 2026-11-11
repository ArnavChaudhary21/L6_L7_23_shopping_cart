# L6_L7_23_shopping_cart — Shopping Cart

Lab 7: Fuzz Testing

## Files

| File | Description |
|------|-------------|
| `shopping_cart.py` | Buggy code to test and fix |
| `test_shopping_cart.py` | Fuzz test file to complete using Hypothesis |

Refer to the lab handout for instructions.

## Submission — Arnav Chaudhary (PES1UG24CS081)

| File | Description |
|------|-------------|
| `shopping_cart.py` | Fixed code, hardened against invalid input |
| `test_shopping_cart.py` | Completed Hypothesis fuzz tests (8 property tests) |
| `step2_buggy_run.png` | Buggy program: works on valid input, crashes on `pen:10x2,` |
| `step4_tests_failing.png`, `step4_crashes_found.png` | Fuzz tests on buggy code: 5 failed, 3 passed |
| `step5_fixed_run.png` | Fixed program handles the same bad input safely |
| `step6_tests_passing.png` | Fuzz tests on fixed code: 8 passed |

### Bugs found by Hypothesis and fixes

| Function | Failing input | Crash | Fix |
|----------|---------------|-------|-----|
| `cart_total` | `None` | `AttributeError` | Return `None` if input is not a string |
| `cart_total` | `"0"`, `"pen:10x2,"` | `ValueError` (unpack) | Check each item has exactly one `:` and one `x`; return `None` otherwise |
| `cart_total` | `"a:1x²"`, `"a:1x-2"` | `ValueError` / negative total | Price and quantity must be ASCII digits, at most 9 long; quantity > 0 |
| `promo_percent` | `None` | `AttributeError` | Return 0 if input is not a string |
| `promo_percent` | `""`, `"SAVE"` | `IndexError` | Code must start with `OFF`, else 0 |
| `promo_percent` | `"OFF101"`, `"OFF-5"`, `"OFF20abc"` | wrong value / `ValueError` | Percent must be digits in 0–100, else 0 |
| `delivery_zone` | `None`, `560085` (int) | `TypeError` | Return `None` if input is not a string |
| `delivery_zone` | `""` | `IndexError` | Pincode must be exactly 6 ASCII digits |
| `delivery_zone` | `"000000"`, `"9…"` | `KeyError` | Use `ZONES.get()`; unknown zone gives `None` |

### Commands

```bash
pip install hypothesis pytest
python shopping_cart.py
python -m pytest test_shopping_cart.py
```
