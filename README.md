# PLP-Python-Assignment

## Table of Content
- [Week 1 Assignment](#week-1-assignment)
- [Week 2 Assignment](#week-2-assignment)
- [Week 3 Assignment](#week-3-assignment)
- [Week 4 Assignment](#week-4-assignment)
- [Week 5 Assignment](#week-5-assignment)
- [Week 6 Assignment](#week-6-assignment)
- [Week 7 Assignment](#week-7-assignment)
- [Week 8 Assignment](#week-8-assignment)

  
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


## Week 5 Assignment 1

#### Instructions:
- Design Your Own Class! 🏗️
- Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
- Add attributes and methods to bring the class to life!
- Use constructors to initialize each object with unique values.
- Add an inheritance layer to explore polymorphism or encapsulation.

#### Assinment 1 Solution
```
# Defination amd construction a class smartphone
class smartphone:
    def __init__(self, product, battery_capacity):
        self.product = product
        self.__battery_capacity = battery_capacity  # Private variable

    # Methods for displaying specification
    def display_specs(self):
        print(f"Product: {self.product}")
        print(f"Battery Capacity: {self.__battery_capacity}mAh")
    
    # Encapsulation with Getter and Setter Methods:
    # method to access private battery capacity attribute
    def get_battery_capacity(self):
        return self.__battery_capacity

    def set_battery_capacity(self, capacity):
        if capacity > 0:
            self.__battery_capacity = capacity
        else:
            print("Invalid capacity")


# Inheritance and Polymorphism
# Defining a subclass AndroidPhone
class AndroidPhone(smartphone):
    def __init__(self, product, battery_capacity, os_version):
        super().__init__(product, battery_capacity)
        self.os_version = os_version


    def display_specs(self):
        super().display_specs()
        print(f"OS Version: {self.os_version}")

# creating objects and using methods:
my_smartphone = smartphone("Generic phone", 3000)
my_smartphone.display_specs()
print(f"Battery Capacity (accessed through method): {my_smartphone.get_battery_capacity()}")     
    
my_android = AndroidPhone("Android Phone", 4000, "Android 12")
my_android.display_specs()

```

#### Assignment 2 Instructions:
######  Polymorphism Challenge! 🎭
- Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

#### Assignment 2 Solution
```
# Definition
class  Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclass definition
class car(Vehicle):
    def move(self):
        print("Driving")

class plane(Vehicle):
    def move(self):
        print("Flying")

class bicycle(Vehicle):
    def move(self):
        print("Pedaling") 


 # polymorphism demonstration:
def demonstrate_movement(vehicle):
    vehicle.move()
```

## Week 7 Assignment

#### Instructions:
- Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
Load the dataset using pandas.
Display the first few rows of the dataset using .head() to inspect the data.
Explore the structure of the dataset by checking the data types and any missing values.
Clean the dataset by either filling or dropping any missing values.
- Task 2: Basic Data Analysis
Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
Identify any patterns or interesting findings from your analysis.
- Task 3: Data Visualization
Create at least four different types of visualizations:
Line chart showing trends over time (for example, a time-series of sales data).
Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
Histogram of a numerical column to understand its distribution.
Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
Customize your plots with titles, labels for axes, and legends where necessary.

#### Assignment Solution
- Using Iris dataset
  ```
  # Importing the library pandas

import pandas as pd

# Load the dataset using pandas:

df = pd.read_csv('C:/Users/HP/Desktop/python classes/week 6/Iris.csv')

# Display the first 10 rows of the dataset using .head():

df.head(10)

# Compute basic statistics of the numerical columns:

df.describe(include='all')

# # Fill missing values (if any)
df = df.fillna(df.mode())

# Perform groupings on a categorical column and compute the mean of a numerical column for each group:

species_mean = df.groupby('Species').mean()
print(species_mean)

# DATA VISUALIZATION
# importing the needed libraries

import matplotlib.pyplot as plt
import seaborn as sns
# pair chart showing the correction of the different species and their lengths

sns.pairplot(df)
```
![output1](https://github.com/user-attachments/assets/deb3dfd8-51f5-4410-87b1-f7224b7a3c1a)
- The pair plot displays histograms for individual variables on the diagonal and scatter plots for pairwise relationships between variables off-diagonally. It reveals the distribution of each variable and shows correlations, such as the strong positive correlation between PetalLengthCm and PetalWidthCm. This visual summary aids in understanding variable distributions and relationships, identifying correlations, and spotting outliers.
##### ## Line chart showing trends over time:
```
# Line chart
plt.figure(figsize=(10, 6))
species_mean['SepalLengthCm'].plot(kind='line')
plt.title('Mean Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length')
plt.show()
```
![output2](https://github.com/user-attachments/assets/b9778afc-3be6-4e1c-817f-4a479942447e)
- A line chart titled "Mean Sepal Length per Species," showing the mean sepal length for three Iris species: Iris-setosa, Iris-versicolor, and Iris-virginica. The chart indicates a clear upward trend, with Iris-setosa having the shortest mean sepal length and Iris-virginica having the longest. This visualization highlights the differences in mean sepal length among the species, suggesting a progression in sepal length from Setosa to Virginica.

```
# Line chart
plt.figure(figsize=(10, 6))
species_mean['SepalWidthCm'].plot(kind='line')
plt.title('Mean Sepal Width per Species')
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length')
plt.show()
```
![output3](https://github.com/user-attachments/assets/a924734d-134f-4c74-950c-34cfb3e3fc5b)
- a line chart titled "Mean Sepal Length per Species," displaying the mean sepal length for the Iris species: Iris-setosa, Iris-versicolor, and Iris-virginica. In this chart, Iris-setosa has the highest mean sepal length, followed by a sharp decrease for Iris-versicolor, which has the lowest mean sepal length. Then, there is a slight increase for Iris-virginica. This visualization shows a notable drop in mean sepal length from Iris-setosa to Iris-versicolor, with Iris-virginica having an intermediate value.

```
# Line chart
plt.figure(figsize=(10, 6))
species_mean['PetalLengthCm'].plot(kind='line')
plt.title('Mean Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Mean Petal Length')
plt.show()
```
![output4](https://github.com/user-attachments/assets/a85552bf-0370-4a8a-b14c-1d5b039577fc)


```
# Line chart
plt.figure(figsize=(10, 6))
species_mean['PetalWidthCm'].plot(kind='line')
plt.title('Mean Petal width per Species')
plt.xlabel('Species')
plt.ylabel('Mean Petal Width')
plt.show()
```
![output5](https://github.com/user-attachments/assets/277f32cb-7b3f-4072-b83e-baff6751a554)


##### Bar chart showing the comparison of a numerical value across categories:
```
plt.figure(figsize=(10,6))
species_mean['SepalLengthCm'].plot(kind='bar')
plt.title("Average Sepal Length per Species")
plt.xlabel('Species')
plt.ylabel('Average Sepal Length')
```
![output6](https://github.com/user-attachments/assets/2b1a6036-8af4-4d9c-bbc6-7692e2771243)

```
plt.figure(figsize=(10,6))
species_mean['SepalWidthCm'].plot(kind='bar')
plt.title("Average Sepal Width per Species")
plt.xlabel('Species')
plt.ylabel('Average Sepal Width')
```


```
plt.figure(figsize=(10,6))
species_mean['PetalWidthCm'].plot(kind='bar')
plt.title("Average Petal Width per Species")
plt.xlabel('Species')
plt.ylabel('Average Petal Width')
```

```
plt.figure(figsize=(10,6))
species_mean['PetalLengthCm'].plot(kind='bar')
plt.title("Average Petal Length per Species")
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
```
##### ## Histogram of a numerical column:
```
plt.figure(figsize=(10,6))
sns.histplot(df['Species'], kde=True)
plt.title("Distribution of the Species")
plt.xlabel("species")
plt.ylabel("height")
```
##### ## Scatter plot to visualize the relationship between two numerical columns:

```
#  Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).

plt.figure(figsize=(10,6))
sns.scatterplot(x='SepalLengthCm', y='PetalLengthCm', hue='Species', data=df)
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal length vs Petal")
```



