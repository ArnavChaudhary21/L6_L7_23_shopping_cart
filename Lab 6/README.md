# L6_L7_23_shopping_cart — Shopping Cart

Lab 6: Code and Branch Coverage

## About

A small Python module that works out item totals with GST and bulk discounts, calculates cart discounts and works out shipping fees.

## Files

| File | Description |
|------|-------------|
| `shopping_cart.py` | The module under test |
| `test_shopping_cart.py` | Starter test file |

Refer to the lab handout for instructions.

## Submission — Arnav Chaudhary (PES1UG24CS081)

| File | Purpose |
|------|---------|
| `CodeCoverageTest_PES1UG24CS081_shopping_cart.py` | Test cases for code (line) coverage, 12 tests |
| `BranchCoverageTest_PES1UG24CS081_shopping_cart.py` | Test cases for branch coverage, 25 tests |
| `code_coverage_screenshot.png` | Code coverage terminal output: **100%** |
| `branch_coverage_screenshot.png` | Branch coverage terminal output: **100%** |

### Commands

```bash
pip install coverage pytest

coverage run -m pytest CodeCoverageTest_PES1UG24CS081_shopping_cart.py
coverage report -m

coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS081_shopping_cart.py
coverage report -m
```

### Results (`shopping_cart.py`)

| Stage | Line coverage | Branch coverage |
|-------|---------------|-----------------|
| Starter test file | 44% | 37% |
| Code coverage tests | **100%** | 98% (missed `38->40`: express, non-Prime) |
| Branch coverage tests | 100% | **100%** (22/22 branches) |
