def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount if applicable.
    
    Args:
        price (float): Original price of the item
        discount_percent (float): Discount percentage to apply
        
    Returns:
        float: Final price after discount (if applicable)
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

def get_user_input():
    """
    Get and validate user input for price and discount percentage.
    
    Returns:
        tuple: (price, discount_percent) or None if input is invalid
    """
    try:
        price = float(input("Enter the original price of the item: "))
        discount = float(input("Enter the discount percentage: "))
        
        if price <= 0:
            print("Price must be greater than 0.")
            return None
        if discount < 0 or discount > 100:
            print("Discount must be between 0 and 100.")
            return None
            
        return price, discount
    except ValueError:
        print("Please enter valid numbers.")
        return None

def main():
    """
    Main function to run the discount calculator program.
    """
    print("Welcome to the Discount Calculator!")
    print("----------------------------------")
    
    user_input = get_user_input()
    while user_input is None:
        print("\nLet's try again...")
        user_input = get_user_input()
    
    price, discount = user_input
    final_price = calculate_discount(price, discount)
    
    print("\n--- Receipt ---")
    print(f"Original price: ${price:.2f}")
    print(f"Discount percentage: {discount}%")
    
    if discount >= 20:
        print(f"Discount applied! New price: ${final_price:.2f}")
    else:
        print("No discount applied (must be 20% or higher)")
        print(f"Final price: ${final_price:.2f}")

if __name__ == "__main__":
    main()