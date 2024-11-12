origanal_price = float(input('Enter the original price of your item: '))
discount_percent = float(input('Enter the discount percentage: '))

# Create a function named calculate_discount(price, discount_percent) 
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price 
    

def main():
    origanal_price = float(input('Enter the original price of your item: '))
    discount_percent = float(input('Enter the discount percentage: '))
    final_price = calculate_discount(origanal_price, discount_percent)

# Print the final price after applying the discount, or if no discount was applied, print the original price.
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: {final_price: .2f}")
    else:
        print(f"No discount applied. The original price is: {origanal_price: .2f}")



if __name__ == "__main__":
    main()   
