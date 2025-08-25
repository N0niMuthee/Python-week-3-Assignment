 calculate_discount(price, discount_percent):
    """
    Function to calculate final price after applying discount.
    If discount is less than 20%, no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for price and discount.")