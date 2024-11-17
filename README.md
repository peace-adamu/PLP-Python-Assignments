# PLP-Python-Assignment
## Week 1 Assignment
#### Instructions:
- Create a new Python file and name it "user_input.py"
- Use the input() function to ask the user for their name and store it in a variable called "name".
- Use the input() function to ask the user for their age and store it in a variable called "age".
- Use the input() function to ask the user for their location and store it in a variable called "location".
- Print out a personalized message using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
- Save and run the program to see the output.

#### Assignment solution
code
```
# Use the input() function to ask the user for their name and store it in a variable called "name".
name = input('Enter your name: ')

# Use the input() function to ask the user for their age and store it in a variable called "age"
age = input('What is your age: ')

# Use the input() function to ask the user for their location and store it in a variable called "location".
location = input('Give details of your location: ')

# Print out a personalized message using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
print(f"Hello {name}, you are {age} years old and live in {location}")
```



# Week 2 Assignment
#### Instructions:
1. Create an empty list called my_list.
2. Append the following elements to my_list: 10, 20, 30, 40.
3. Insert the value 15 at the second position in the list.
4. Extend my_list with another list: [50, 60, 70].
5. Remove the last element from my_list.
6. Sort my_list in ascending order.
7. Find and print the index of the value 30 in my_list.

#### Assignment solution
```
1. # Create an empty list called my_list.
my_list = [] 

2.# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

3. # Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print(my_list) 

4. # Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print(my_list)

5. # Remove the last element from my_list
my_list.pop()
print(my_list)

6.# Sort my_list in ascending order.
my_list.sort()
print(my_list) 

7. # Find and print the index of the value 30 in my_list.
print(my_list[3])
```


# Week 3 Assignment

#### Instructions:
- Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

#### Assignment Solution
```
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
```

# Week 4 Assignment

#### Instructions:
1. File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
2. Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

#### Assignment Solution
```
def modified_file():
    input_file = "requirements.txt"
    output_file = "modified_file"

    try:
        with open(input_file, "r") as infile:
            document = infile.read()
            modified_document = document.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_document)
            print(f"Modified document written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
    except IOError:
        print(f"Error: Could not read the file")
    except Exception as e:
        print(f"An unexcepted error occured: {e}")


modified_file()
```
