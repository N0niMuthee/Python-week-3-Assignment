# Discount Calculator

A simple Python program that calculates the final price of an item after applying a discount.  
If the discount is **20% or higher**, the program applies the discount.  
Otherwise, it returns the original price without any changes.

---

## Features
- Prompts the user to enter the original price of an item.
- Prompts the user to enter the discount percentage.
- Applies the discount only if it is **20% or higher**.
- Handles invalid inputs gracefully.

---

## Function Used
```python
def calculate_discount(price, discount_percent):
    """
    Function to calculate final price after applying discount.
    If discount is less than 20%, no discount is applied.
    """