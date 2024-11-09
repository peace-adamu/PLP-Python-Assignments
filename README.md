# PLP-Python-Assignment
## Week 1 Assignment
#### Instructions:
- Create a new Python file and name it "user_input.py"
- Use the input() function to ask the user for their name and store it in a variable called "name".
- Use the input() function to ask the user for their age and store it in a variable called "age".
- Use the input() function to ask the user for their location and store it in a variable called "location".
- Print out a personalized message using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
- Save and run the program to see the output.

## Assignment solution
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

## Assignment solution
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
