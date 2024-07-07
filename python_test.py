'''
Q1. Write a Python program that defines a function called "add_numbers" that takes two arguments (i.e.,
numbers) and returns their sum. Within the function, add the two numbers together and return the result
using the return statement. Call the function with the values 5 and 6, and print out the returned result.
This will result in the addition of 5 and 6, with the output of the program being the sum of these two
numbers.

'''
#Ans
def add_number(a,b):
    c=a+b
    return c
    
     
      
sum_number=add_number(5,6)
print('sum of two number',sum_number)


'''
Q2. Write a Python program that calculates the square root of a given number using a built-in function.
Specifically, the program should take an integer or float input from the user, calculate its square root
using the 'sqrt()' function from the 'math' module, and print out the result to the user. As an example,
calculate the square root of the number 625 using this program, which should output the value of 25.

'''
#Ans
from math import sqrt
#data =float(input('Enter number to calculate square root :=  '))
data=625
print(sqrt(data))
#Ans is 25.0 bcoz taken float
'''
Q3.Write a program that prints all prime numbers between 0 to 50.
'''
#Ans
def prime_check(num):
    if num<=1:
        return False
    elif num>2:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
for i in range(51):
    if prime_check(i):
        print(i)

               
'''
Q4.How can we swap the values of three variables (let's say a, b, and c) without using a fourth variable?
For example, if we have a=5, b=8, and c=9, how can we obtain a=9, b=5, and c=8? The challenge is to
perform this operation without using an additional variable to store any of the values during the swapping process.

'''
#Ans:=
a=5
b=8
c=9
print('Before Swaping Variable')
a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)

print("a =", a)
print("b =", b)
print("c =", c)


'''
Q5. Can you write a program that determines the nature of a given number (in this case, 87) as being
positive, negative, or zero? The program should be designed to take the number as input and perform the
necessary calculations to determine if the number is positive (i.e., greater than zero), negative (i.e., less
than zero), or zero (i.e., equal to zero). The output of the program should indicate which of these three
categories the given number falls into.

'''

#ans
def nature_number(num):
    if num<0:
        print('number is negative',num)
    elif num==0:
        print('number is Zero',num)
    elif num>0:
        print('number is Postive',num)
data_number=int(input('Enter number Check Nature:=='))
check=nature_number(data_number)

'''
Q6. How can you create a program that determines whether a given number (in this case, 98) is even or
odd? The program should be designed to take the number as input and perform the necessary calculations to determine whether it is divisible by two. If the number is divisible by two without leaving a
remainder, it is an even number, and if there is a remainder, it is an odd number. The output of the
program should indicate whether the given number is even or odd.

'''


def even_odd(num):
    if num%2==0:
        print('this is even number',num)
    else:
        print('this is odd number',num)
    return num
data_even_odd=98
check_even_odd=even_odd(data_even_odd)
print(check_even_odd)

'''
Q7.Write a program for sum of digits.The digits are 76543 and the output should be 25.
'''
#Ans
sum_digit=0
digit=76543
while(digit>0):
    unit_digit=digit%10
    sum_digit+=unit_digit
    digit=digit//10
print(sum_digit)

'''
Q8.Write a program for reversing the given number 5436 and the output should be 6345.

'''
data_reverse=5436
def reverse_number(data_reverse):
    rev=0
    while(data_reverse>0):
        rev=rev*10+data_reverse%10
        data_reverse=data_reverse//10
    return rev
reverse_check_done=reverse_number(data_reverse)
print(reverse_check_done)

'''
Q9.Write a program to check if a given number 371 is an Armstrong number?


'''
check_armsstrong=371
#take other variable to store orinal to keep safe
temp_arms=check_armsstrong
#count the length
count=len(str(temp_arms))
#take while loop to separte each number and power each and sum
sum_arms=0
while(temp_arms>0):
    digit=temp_arms%10
    sum_arms+=digit**count
    temp_arms//=10
if sum_arms==check_armsstrong:
    print('This Number is Armstrong ')
else:
    print('This Is Not Armstrong')
'''
Q10.Write a program the given year is 1996, a leap year.
'''
#Ans
leap_check_data=1996
def leap_check(leap_check_data):
    if (leap_check_data % 4==0 and leap_check_data % 100 !=0)or (leap_check_data % 400==0):
        print('This is Year ',leap_check_data)
    else:
         print('This is Not Year ',leap_check_data)
year_leap=leap_check(leap_check_data)
    
    
        
'''
Q11. Create a list in python using the followings: 2,3,4,5,6,7 with variable ‘a’ Add ‘mango to the above list
Also add banana, grapes & orange in the list insert apple in the 5th position of a variable ‘a’

Remove last item from the list 

'''
a=[2,3,4,5,6,7]
a.append('mango')
print(a)
a.extend(['banana', 'grapes','orange'])
print(a)
a.insert(4,'apple')
print(a)
a.pop()
print('this is last when last element remove',a)


'''
Q12.

L = [1,2,3,4,5,6,7]

Using the above list slice from 1:4

'''

#ans
L = [1,2,3,4,5,6,7]
slice_data=L[1:4]
print(slice_data)

'''
Q13. Reverse the order of given string L = [4,5,6,8,3] Without using reverse() function
'''
L = [4,5,6,8,3]

print(L[::-1])


'''
Q14. Use list comprehension to square the given list L=[2,4,7,3,6,8]
'''
#Ans
L=[2,4,7,3,6,8]
square_list=[]
for i in L:
    square=i*i
    square_list.append(square)
for j in square_list:
    print(j)
    
    
'''
Q15. Create a function that takes in a tuple of integers and returns the sum of the integers. Test the
 
function with a tuple of your choice.

'''
#Ans
def sum_of_tuple_integers(tuple_of_integers):
    """Function to calculate the sum of integers in a tuple"""
    return sum(tuple_of_integers)

# Test the function with a tuple of integers
test_tuple = (2, 4, 6, 8, 10)
result = sum_of_tuple_integers(test_tuple)
print("Sum of integers in the tuple:", result)


'''
Q16. Create two sets of your favorite fruits, and use the union() method to combine them into a single set.
Print the resulting set to the console.

'''
set1={'apple','mango','bana'}
set2={'pineapple','watermelon','kiwi'}
print(set1.union(set2))

'''
Q17. Create a set of random words, and use the add() method to add a new word to the set.
Print the
resulting set to the console.

'''
random_word={'apple','mango','bana'}
random_word.add('pineapple')
print(random_word)


'''
Q18. Create a set of your favorite animals, and use the remove() method to remove one animal from the
set. Print the resulting set to the console.

'''

#ans=
set_fav_animal={'Element','monkey','leopard','snake'}
print(set_fav_animal)
print('Remove One Animal')
set_fav_animal.remove('snake')
print(set_fav_animal)

'''
Q19. favorite_books = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"} favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]
Use the zip() function to combine the book set and movie list into a list of tuples representing book/
movie pairs. Print the resulting list.


'''
#Ans=
favorite_books = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"}
favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]

# Combine the book set and movie list into a list of tuples

merge_favorite_books_favorite_movies=list(zip(favorite_books,favorite_movies))
print(merge_favorite_books_favorite_movies)

'''
Q20. Write a Python program to find the difference between consecutive numbers in a list. Solutions:

'''


#Ans=
print('Question 20 RUNing')
def diffrence_consecutive(number):
    diffrence_consecutive=[]
    for i in range(len(number)-1):
        print(i)
        difference=number[i+1]-number[i]
        diffrence_consecutive.append(difference)
    return diffrence_consecutive
lst=[1,2,6,10,15]
data=diffrence_consecutive(lst)
print(data)

'''
Q21. Create a dictionary called fruits with the following key-value pairs: "apple": 0.75
"banana": 1.25

"orange": 0.90

Then, print out the price of a banana.

'''
#Ans
dic_fruits={"apple": 0.75,"banana": 1.25,"orange": 0.90}
print(dic_fruits["banana"])
#print(dic_fruits.values())


'''
Q22. Create an empty dictionary called ages. Add the following key-value pairs to the dictionary: "Alice": 30
"Bob": 25
 
"Charlie": 35

Then, print out the age of Charlie.


'''
print('Question No 22 Run')       
#ANS
dict_empty_Age={}
dict_empty_Age["Alice"]=30
dict_empty_Age["Bob"]=25
dict_empty_Age["Charlie"]=35
print(dict_empty_Age["Charlie"])

'''
Q23. Write a function called word_count(text) that takes a string as input and returns a dictionary where
Each key is a word in the text and its value is the number of times that word appears in the text.
For
for example, word_count("hello world hello") should return {"hello": 2, "world": 1}.

'''

def data_text(text):
    data_split=text.split()
    data_text_dic={}
    for word in data_split:
        if word in data_text_dic:
            data_text_dic[word]+=1
        else:
            data_text_dic[word]=1
    return data_text_dic
data='ishan is going school name is ishan'
data=data_text(data)
print(data)



'''
Q24. Create a dictionary called phone_book with the following key-value pairs: "Alice": "555-1234"
"Bob": "555-5678"

"Charlie": "555-9012"

Then, prompt the user to enter a name and print out the corresponding phone number. If the name is not
in the phone book, print out a message saying that the name was not found.

'''
dic_phone={"Alice": "555-1234","Bob": "555-5678","Charlie": "555-9012"}
name=input('Enter Name :=')
if name in dic_phone:
    print(f'this name is {name} this is contact number {dic_phone[name]}')
else:
    print('Name Not Exit')
'''
Q25. Write a program that prompts the user to enter a number between 1 and 10. If the number is less than
5, print out "Too low!", otherwise print out "Too high!".

'''
#Ans
Enter_Number=int(input('Enter Number :=='))
islow="Too low!"
is_high="Too high!"
if Enter_Number<10:
    print(f'this is {Enter_Number} is less then {islow}' )
else:
    print(f'this is {Enter_Number} is greater then {is_high}')

'''
Q26. Write a program that prompts the user to enter a password. If the password is "password123", print
out "Access granted", otherwise print out "Access denied".
'''
Enter_Password=input("Enter Password  :=")
if Enter_Password=="password123":
    print(f'User is Access granted')
else:
    print('User Access denied')


'''
Q27. Write a program that prompts the user to enter a positive integer. Then, use a loop to print out all the
odd numbers from 1 to that integer.

'''

#this solution not work else condition beacuse funtion inside if condtion when negative or zero output funtion not define error
enter_number=int(input('Enter Number := '))

if enter_number>0:
    print('this is postive number')
    def print_odd_number(enter_number):
        odd_number=[]
        for i in range(1,enter_number):
            if i%2!=0:
                odd_number.append(i)
        return odd_number
    
                
                
        
else:
    print('this number is negative or either zero')

data=print_odd_number(enter_number)
print(data)

print('------------------------------------------------------------')
#this is correct function 
def print_odd_number(enter_number):
        odd_number=[]
        for i in range(1,enter_number):
            if i%2!=0:
                odd_number.append(i)
        return odd_number
   
enter_number_2nd_method=int(input('Enter Number := '))
if enter_number_2nd_method>0:
    print('this is postive number')
    data=print_odd_number(enter_number_2nd_method)
    print(data)
else:
    print('this number is negative or either zero')


'''
Q28. Write a program that generates a random number between 1 and 100 and then prompts the user to
guess the number. If the user's guess is too low, print out "Too low!", if the guess is too high, print out "Too
 
high!", and if the guess is correct, print out "You win!".

'''

#Ans=
import random
def guess_number():
    guess_number=random.randint(1,100)
    print(guess_number)
    while True:
        try:
            guess=int(input('Enter number between 1 to 100'))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess<guess_number:
            print('this is Low Number')
        elif guess>guess_number:
            print('this is High')
        else:
            print('Win')
            break
    
guess_number()  



print('---------------solution Begin 29------------------------------------------------------------------')
'''

Q29. Write a program that generates a random number between 1 and 10 and then prompts the user to
guess the number. The user has three attempts to guess the number. If the user guesses correctly within
three attempts, print out "You win!", otherwise print out "You lose!".

'''
#Ans=
import random
def random_gen():
    data_random=random.randint(1,10)
    print(data_random)
    count=1
    while(count<=3):
       
        gus=int(input('Enter Number between 1 and 10'))
        if gus==data_random:
            print("You Win")
        else:
            print("Wrong Prediction")
        count=count+1   
    

random_gen()  
    
'''
Q30. Write a program that prompts the user to enter their age and then prints out whether they are a child
(age 0-12), a teenager (age 13-19), an adult (age 20-59), or a senior (age 60+)

'''

def age_cal():
    age=int(input('Please Enter Your Age :='))
    if age<0:
        print('Invalid Age Please Correct Age Enter ')
    elif age>0 and age<=12:
        print('This is Children')
    elif age>=13 and age<=19:
        print('Your Teenager')
    elif age>=20 and age<=59:
        print('You Are Adult')
    else:
        print('Your Are Senior Citizen')
age_cal()

'''
Q31. Create a class called "Person" with properties for "name", "age", and "gender". Create an object of this
class and print out its properties.

'''
#Ans=

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def method_Call(self):
        print(f'this is name of god {self.name} and age of god is {self.age} gender of god is {self.gender}')
p=Person('Radha',25,'Female')
p.method_Call()


'''
Q32. Write a Python class called "Rectangle" with attributes for "width" and "height". Implement methods
to calculate the area and perimeter of the rectangle. Create an instance of this class and use it to print out
the rectangle's area and perimeter.

'''

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def method_area(self):
        return self.width*self.height
    def method_perimeter(self):
        return 2(self.width+self.height)
        

rec1=Rectangle(10,20)
print(f'this is area of rectangle {rec1.method_area} this is perimeter of rectangle{rec1.method_perimeter}')

'''
33. Write a Python class called "BankAccount" with attributes for "balance" and "interest_rate".
Implement methods to deposit and withdraw money from the account, as well as to calculate the
interest
earned on the balance based on the interest rate. Create an instance of this class and use it to
test out the
implemented methods for deposit, withdrawal, and interest calculation.


'''

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
        

    def deposite(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        self.balance-=amount
        return self.balance
    def interst(self,intrest):
        self.interst_cal=self.balance*intrest/100
        self.balance+=self.interst_cal
b1=BankAccount(10000)
b1.deposite(5000)
b1.withdraw(12200)
b1.interst(8)
print(b1.balance)
        

'''
Q34. Write a Python class called "Animal" with attributes for "name" and "species". Create a
subclass of
"Animal" called "Dog" with additional attributes for "breed" and "owner". Implement both classes
with
appropriate methods and constructors to initialize their properties. Create instances of both
classes and
use them to print out the various properties of the animals and dogs, such as their names,
species,
breeds, and owners.

'''

#Solution
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, species, breed, owner):
        super().__init__(name, species)
        self.breed = breed
        self.owner = owner
    
    def __str__(self):
        return f"{self.name} is a {self.species} of breed {self.breed} and is owned by {self.owner}"

# Creating an instance of Animal
animal = Animal("Milo", "Cat")

# Creating an instance of Dog
dog = Dog("Buddy", "Dog", "Golden Retriever", "Alice")

# Printing properties of Animal
print(animal)  # Output: Milo is a Cat

# Printing properties of Dog
print(dog)     # Output: Buddy is a Dog of breed Golden Retriever and is owned by Alice



'''Q35. Create a class called "Car" with properties for "make", "model", and "year". Create a
subclass of "Car"
called "ElectricCar" with additional properties for "battery_size" and "range". Create objects of
both
classes and print out their properties.


'''
class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def __str__(self):
        return f'this is make {self.make} and model name {self.model}'
class ElectricCar(Car):
    def __init__(self,make,model,battery_size,rangee):
        super().__init__(make,model)
        self.battery_size=battery_size
        self.rangee=rangee
    def __str__(self):
        return f'this is make of car {self.make} this is model name {self.model} this is battersize {self.battery_size} this is {self.rangee}'
c1=Car(2019,'fg')
print(c1)
ele=ElectricCar(2020,'fg1','everedy',45)
print(ele)



'''
Q36. Create a class called "Student" with properties for "name" and "id". Create a subclass of
"Student"
called "GraduateStudent" with additional properties for "advisor" and "research_area". Create
objects of
both classes and print out their properties.


'''
# Solutuon

class Student:
    def __init__(self,name,id1):
        self.name=name
        self.id1=id1
    def __str__(self):
        return f'this is name of student {self.name} and this is id of student {self.id1}'
class GraduateStudent(Student):
    def __init__(self,name,id1,advisor,research_area):
        super().__init__(name,id1)
        self.advisor=advisor
        self.research_area=research_area
    def __str__(self):
        return f'this is name of student {self.name} this is id of student{self.id1} this is advisor {self.advisor} this is advisor {self.research_area} '


stu=Student('ram',11)
grd=GraduateStudent('ram',11,45,'science')
print(grd)


'''
Q37. Create a class called "Shape" with methods to calculate the area and perimeter of the
shape. Create
subclasses of "Shape" for "Rectangle", "Circle", and "Triangle" with their own methods for
calculating area
and perimeter. Create objects of each class and print out their area and perimeter

'''
#Solution
import math

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def perimeter(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

# Creating objects of each class
rectangle = Rectangle(4, 5)
circle = Circle(3)
triangle = Triangle(3, 4, 5)

# Printing area and perimeter of Rectangle
print(f"Rectangle area: {rectangle.area()}")          # Output: Rectangle area: 20
print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Output: Rectangle perimeter: 18

# Printing area and perimeter of Circle
print(f"Circle area: {circle.area()}")                # Output: Circle area: 28.274333882308138
print(f"Circle perimeter: {circle.perimeter()}")      # Output: Circle perimeter: 18.84955592153876

# Printing area and perimeter of Triangle
print(f"Triangle area: {triangle.area()}")            # Output: Triangle area: 6.0
print(f"Triangle perimeter: {triangle.perimeter()}")  # Output: Triangle perimeter: 12

            
'''
Q38. Create a class called "Employee" with properties for "name", "id", and "salary". Add
methods to give the employee a raise and to calculate their annual salary. Create objects of this
class and test out the
methods.

'''

class Employee:
    def __init__(self,name,id1,salary):
        self.name=name
        self.id1=id1
        self.salary=salary
    def annual_sal(self):
        self.salary=self.salary*12
    def giverise(self,amount):
        self.salary+=amount
    def __str__(self):
        return f'this is annual salary {self.name} this is salry {self.id1} this is salry {self.salary}'
employee1 = Employee("John Doe", "E123", 5000)
employee2 = Employee("Jane Smith", "E456", 6000)
employee1.giverise(156)
print(employee1)

'''Q39. Create a class called "Book" with properties for "title", "author", and "publisher". Create a
subclass of
"Book" is called "Ebook" with additional properties for "file_format" and "file_size". Create
objects of both
classes and print out their properties.

'''

class Book:
    def __init__(self,title,author,publisher):
        self.title=title
        self.author=author
        self.publisher=publisher
class Ebook(Book):
    def __init__(self,title,author,publisher,file_format,file_size):
        super().__init__(title,author,publisher)
        self.file_format=file_format
        self.file_size=file_size
    def __str__(self):
        return f'this is title {self.title} this is author {self.author} this is publisher {self.publisher} this is fileformate{self.file_format}'

sb=Book('goog','fb','patna')
print(sb)
     
eb=Ebook('goog','fb','patna','jpg',25)
print(eb)


'''
Q40. Create a class called "Bank" with properties for "name" and "accounts". Add methods to
create new
accounts, deposit and withdraw money from accounts, and to calculate the total balance of all
accounts.
Create an object of this class and test out the methods
'''

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def __str__(self):
        return f"Account {self.account_number}: Balance ${self.balance:.2f}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    
    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, initial_balance)
        else:
            print("Account already exists.")
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Account does not exist.")
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account does not exist.")
    
    def total_balance(self):
        total = sum(account.balance for account in self.accounts.values())
        return total
    
    def __str__(self):
        account_details = '\n'.join(str(account) for account in self.accounts.values())
        return f"Bank: {self.name}\nAccounts:\n{account_details}"

# Creating an object of the Bank class
bank = Bank("MyBank")

# Creating new accounts
bank.create_account("A001", 1000)
bank.create_account("A002", 1500)

# Depositing money into accounts
bank.deposit("A001", 500)
bank.deposit("A002", 1000)

# Withdrawing money from accounts
bank.withdraw("A001", 200)
bank.withdraw("A002", 2500)  # This will print "Insufficient funds."

# Printing details of the bank and accounts
print(bank)  # Output will include details of both accounts

# Calculating and printing the total balance of all accounts
print(f"Total balance of all accounts: ${bank.total_balance():.2f}")  # Output: Total balance of all accounts: $3800.00


'''
Q41. Can you create a Python program that reads a text file and counts the number of words
contained
within it? The program should be designed to read the file and break it down into individual
words, using
spaces, punctuation marks, and other delimiters to separate the words. It should then count the
number
of words found in the file and display this count as output. The program should be flexible
enough to work
with different text files and should be able to handle a variety of formatting and punctuation
styles.

'''
#Solution
import re

def count_words_in_file(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Use regular expression to split the text into words
    words = re.findall(r'\b\w+\b', text)
    
    # Count the number of words
    word_count = len(words)
    
    return word_count

# Example usage
file_path = 'example.txt'  # Replace with your text file path
word_count = count_words_in_file(file_path)
print(f"Number of words in the file: {word_count}")              



'''
Q42. Could you help me create a Python program that can find and display the longest word in
a text file?
The program should be able to read any text file and separate its contents into individual words,
taking
into account various delimiters like spaces, punctuation marks, and other characters. Then, it
should
compare the length of each word and determine which one is the longest, and finally, print that
word as
output. The program should be versatile enough to work with various text files and be able to
handle
different formatting styles and punctuation
'''

#Solution
import re

def find_longest_word_in_file(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Use regular expression to split the text into words
    words = re.findall(r'\b\w+\b', text)
    
    # Find the longest word
    longest_word = max(words, key=len)
    
    return longest_word

# Example usage
file_path = 'example.txt'  # Replace with your text file path
longest_word = find_longest_word_in_file(file_path)
print(f"The longest word in the file is: {longest_word}")
'''
#43. Write a Python program to read a text file and print out the most frequent word(s) in the
file.
'''

data=open('file.txt','r')
doc=data.read()


'''
43. Write a Python program to read a text file and print out the most frequent word(s) in the
file.
'''

#Solution
import re
from collections import Counter

def find_most_frequent_words(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Use regular expression to split the text into words
    words = re.findall(r'\b\w+\b', text.lower())  # Convert text to lowercase to count words case-insensitively
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Find the maximum frequency
    max_frequency = max(word_counts.values())
    
    # Find the words with the maximum frequency
    most_frequent_words = [word for word, count in word_counts.items() if count == max_frequency]
    
    return most_frequent_words, max_frequency

# Example usage
file_path = 'example.txt'  # Replace with your text file path
most_frequent_words, frequency = find_most_frequent_words(file_path)
print(f"The most frequent word(s) in the file are: {', '.join(most_frequent_words)} (appeared {frequency} times)")



'''
Q44. How can you use Python to count the number of rows in a CSV file?
'''
#solution
import csv

def count_rows_in_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)  # Count the number of rows
    return row_count

# Example usage
file_path = 'example.csv'  # Replace with your CSV file path
row_count = count_rows_in_csv(file_path)
print(f"Number of rows in the CSV file: {row_count}")


'''
Q45. How can you use Python to calculate the average of a specific column in a CSV file?

'''
#Solution
import csv

def calculate_column_average(file_path, column_name):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        total = 0
        count = 0
        
        for row in reader:
            try:
                value = float(row[column_name])
                total += value
                count += 1
            except ValueError:
                pass  # Ignore rows with non-numeric values in the specified column
    
    if count == 0:
        return None  # No valid numeric data found
    
    average = total / count
    return average

# Example usage
file_path = 'example.csv'  # Replace with your CSV file path
column_name = 'Age'  # Replace with the specific column name you want to average
average = calculate_column_average(file_path, column_name)

if average is not None:
    print(f"The average of the '{column_name}' column is: {average:.2f}")
else:
    print(f"No valid numeric data found in the '{column_name}' column.")

#Q46. Write a Python program to read a JSON file and print out the value of a specified key

#Solution
import json

def read_json(file_path, key):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            
        # Check if the key exists in the JSON data
        if key in data:
            print(f"The value for key '{key}' is: {data[key]}")
        else:
            print(f"The key '{key}' does not exist in the JSON file.")
    except FileNotFoundError:
        print(f"The file at path '{file_path}' does not exist.")
    except json.JSONDecodeError:
        print("The file is not a valid JSON.")

# Example usage
file_path = 'example.json'  # Replace with the path to your JSON file
key = 'your_key'  # Replace with the key you want to search for

read_json(file_path, key)


'''
Q47. Can you provide a Python code snippet to write a list of strings into a text file where each
string is
written on a new line?

'''
#Solution

def write_list_to_file(file_path, string_list):
    try:
        with open(file_path, 'w') as file:
            for string in string_list:
                file.write(string + '\n')
        print(f"Successfully wrote {len(string_list)} strings to {file_path}.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

# Example usage
file_path = 'output.txt'  # Replace with the path to your text file
string_list = ['Hello, World!', 'Python is great!', 'Writing to a file is easy.']

write_list_to_file(file_path, string_list)

'''
Q48. Can you provide a Python code to read a binary file and display the data in hexadecimal
format.

'''
#Solution

def read_binary_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
            hex_data = binary_data.hex()
            # Display the hexadecimal data in a formatted way
            for i in range(0, len(hex_data), 2):
                print(hex_data[i:i+2], end=' ')
                if (i // 2 + 1) % 16 == 0:  # New line every 16 bytes
                    print()
            print()
    except FileNotFoundError:
        print(f"The file at path '{file_path}' does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

# Example usage
file_path = 'example.bin'  # Replace with the path to your binary file

read_binary_file(file_path)

'''
49. Can you write a Python code to read a Comma-Separated Values (CSV) file, apply a
specific condition
to each row, and create a new CSV file that contains only the rows that satisfy the condition?
For example,
if the CSV file contains information about products and their prices, you may want to create a
new CSV
file that only includes the products that are within a certain price range. The program should be
able to
read the CSV file, compare the values in each row to the specified condition, and write the rows
that meet
the criteria to a new CSV file.

'''

#Solution

import csv

def filter_csv(input_file, output_file, price_range):
    min_price, max_price = price_range
    
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in reader:
                price = float(row['price'])  # Assuming 'price' is the column name for prices
                if min_price <= price <= max_price:
                    writer.writerow(row)
        
        print(f"Filtered data has been written to {output_file}.")
    except FileNotFoundError:
        print(f"The file at path '{input_file}' does not exist.")
    except KeyError:
        print("The specified key does not exist in the CSV file.")
    except ValueError:
        print("There was an error processing the numerical values in the CSV file.")
    except IOError as e:
        print(f"An error occurred while processing the file: {e}")

# Example usage
input_file = 'products.csv'  # Replace



'''
50. Write a Python program to read a text file, count the frequency of each word, and write the
results to
a new text file
'''
#Soltion 

from collections import Counter
import re

def count_word_frequency(input_file, output_file):
    try:
        # Read the content of the file
        with open(input_file, 'r') as file:
            text = file.read()
        
        # Use regular expression to find words and convert them to lowercase
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Count the frequency of each word
        word_count = Counter(words)
        
        # Write the word frequency to the output file
        with open(output_file, 'w') as file:
            for word, count in word_count.items():
                file.write(f"{word}: {count}\n")
        
        print(f"Word frequency has been written to {output_file}.")
    except FileNotFoundError:
        print(f"The file at path '{input_file}' does not exist.")
    except IOError as e:
        print(f"An error occurred while processing the file: {e}")

# Example usage
input_file = 'input.txt'  # Replace with the path to your input text file
output_file = 'word_frequency.txt'  # Replace with the path to your output text file

count_word_frequency(input_file, output_file)


'''
#Q51. Write a program that prints the first 10 even numbers using a for loop
'''

for i in range(11):
    if i%2==0:
        print("this is even number",i)
    else:
        print('')


'''
Q52. Write a program that takes a list of strings and prints out each string in reverse order using
     a for loop
'''
#Solution

def print_reversed_strings(string_list):
    for string in string_list:
        reversed_string = string[::-1]
        print(reversed_string)

# Example usage
string_list = ['hello', 'world', 'python', 'programming']
print_reversed_strings(string_list)


'''
Q53. Write a program that prints the multiplication table of a given number using a for loop.
'''

def print_multiplication_table(number, up_to=10):
    print(f"Multiplication Table for {number}")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

# Example usage
number = 5  # Replace with the number you want the multiplication table for
print_multiplication_table(number)

'''
Q54. Write a program that takes a list of integers as input and returns the sum of all the
numbers in the list
using a for loop.

'''
#Solution

def sum_of_integers(int_list):
    total = 0
    for number in int_list:
        total += number
    return total

# Example usage
int_list = [1, 2, 3, 4, 5]  # Replace with your list of integers
total_sum = sum_of_integers(int_list)
print(f"The sum of all the numbers in the list is: {total_sum}")

'''
55. Write a program that prompts the user for a positive integer and then prints out all the
prime numbers up to that number using a for loop.

'''
#Solution
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_up_to(limit):
    print(f"Prime numbers up to {limit}:")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=' ')
    print()

# Example usage
try:
    limit = int(input("Enter a positive integer: "))
    if limit > 0:
        print_primes_up_to(limit)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")


'''
Q56. Write a program that prompts the user to enter a password until the correct password is
entered using a while loop
'''
#Solution
def prompt_for_password(correct_password):
    while True:
        password = input("Enter the password: ")
        if password == correct_password:
            print("Password correct. Access granted.")
            break
        else:
            print("Incorrect password. Try again.")

# Example usage
correct_password = "vikash"  # Replace with the correct password

prompt_for_password(correct_password)



'''
Q57. Write a program that takes a list of strings and prints out each string in reverse order using
a while
loop.

'''
#Solution
def print_strings_reverse(string_list):
    i = 0
    while i < len(string_list):
        reversed_string = string_list[i][::-1]
        print(reversed_string)
        i += 1

# Example usage
string_list = ['hello', 'world', 'python', 'programming']
print_strings_reverse(string_list)



'''
Q58. Write a program that prompts the user to enter a positive integer and then prints out all the
Fibonacci numbers up to that number using a while loop
'''
#Solution

def fibonacci_up_to(limit):
    # Initialize Fibonacci sequence
    fib_list = [0, 1]
    
    # Print Fibonacci numbers up to the limit
    while fib_list[-1] <= limit:
        print(fib_list[-1], end=' ')
        fib_list.append(fib_list[-1] + fib_list[-2])

# Example usage
try:
    limit = int(input("Enter a positive integer: "))
    if limit > 0:
        fibonacci_up_to(limit)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")

'''
Q59. Write a program that takes a list of integers as input and returns the product of all the
numbers in the list using a while loop
'''

#Solution
def product_of_integers(int_list):
    product = 1
    i = 0
    while i < len(int_list):
        product *= int_list[i]
        i += 1
    return product

# Example usage
int_list = [1, 2, 3, 4, 5]  # Replace with your list of integers
total_product = product_of_integers(int_list)
print(f"The product of all the numbers in the list is: {total_product}")


'''
60. Write a program that prompts the user to enter a positive integer and then prints out the
factorial of that number using a while loop.
'''

#Solution
def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0:
        return 1  # 0! is defined as 1
    else:
        result = 1
        while n > 0:
            result *= n
            n -= 1
        return result

# Example usage
try:
    num = int(input("Enter a positive integer: "))
    if num >= 0:
        fact = factorial(num)
        print(f"The factorial of {num} is: {fact}")
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")


'''
Q61. Write a program that spawns two threads. One thread should print even numbers between
0 and 10, and the other thread should print odd numbers between 1 and 9.
'''
#Solution
import threading

def print_even_numbers():
    for i in range(0, 11, 2):
        print(f"Even Thread: {i}")

def print_odd_numbers():
    for i in range(1, 10, 2):
        print(f"Odd Thread: {i}")

# Create threads
even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)

# Start threads
even_thread.start()
odd_thread.start()

# Wait for threads to complete (optional)
even_thread.join()
odd_thread.join()

# Optional: You can also join threads to wait for their completion
# even_thread.join()
# odd_thread.join()

print("Threads execution finished.")



'''
Q62. Write a program that generates a list of random numbers and sorts them using
multithreading. Use two threads to sort the first half and the second half of the list in parallel.

'''
#Solution

import threading
import random

def sort_half(lst, start, end):
    lst[start:end] = sorted(lst[start:end])

def parallel_sort(lst):
    mid = len(lst) // 2
    
    # Create threads to sort each half of the list
    t1 = threading.Thread(target=sort_half, args=(lst, 0, mid))
    t2 = threading.Thread(target=sort_half, args=(lst, mid, len(lst)))
    
    # Start threads
    t1.start()
    t2.start()
    
    # Join threads to wait for their completion
    t1.join()
    t2.join()

# Generate a list of random numbers
random.seed(42)  # Setting seed for reproducibility
num_elements = 10
numbers = [random.randint(1, 100) for _ in range(num_elements)]
print("Original List:", numbers)

# Sort the list using multithreading
parallel_sort(numbers)
print("Sorted List:", numbers)


'''
Q63. Write a program that simulates a bank account transaction. The program should create
two threads,one for a deposit and one for a withdrawal. The deposit thread should add
100 to the account,and the withdrawal thread should withdraw
50 from the account. Run the program for 10 iterations.
'''
#Solution
import threading
import time

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()  # Lock to synchronize access to balance
    
    def deposit(self, amount):
        with self.lock:
            print(f"Depositing {amount}...")
            self.balance += amount
            print(f"New balance after deposit: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount}...")
                self.balance -= amount
                print(f"New balance after withdrawal: {self.balance}")
            else:
                print("Insufficient funds for withdrawal.")

def deposit_thread(account, iterations):
    for _ in range(iterations):
        account.deposit(100)
        time.sleep(0.1)  # Simulate some processing time

def withdraw_thread(account, iterations):
    for _ in range(iterations):
        account.withdraw(50)
        time.sleep(0.1)  # Simulate some processing time

# Create a bank account instance
account = BankAccount()

# Create threads for deposit and withdrawal
deposit_thread = threading.Thread(target=deposit_thread, args=(account, 10))
withdraw_thread = threading.Thread(target=withdraw_thread, args=(account, 10))

# Start threads
deposit_thread.start()
withdraw_thread.start()

# Wait for threads to complete
deposit_thread.join()
withdraw_thread.join()

print("Bank transactions completed.")
print(f"Final balance: {account.balance}")



'''
Q64. Write a Python program that creates a thread to print out the current date and time every 5
seconds. The program should continue running until the user presses the 'q' key
'''
#Solution
import threading
import datetime
import time
import keyboard

# Function to print current date and time
def print_current_time():
    while True:
        current_time = datetime.datetime.now()
        print(f"Current Date and Time: {current_time}")
        time.sleep(5)  # Wait for 5 seconds

        # Check if 'q' key is pressed
        if keyboard.is_pressed('q'):
            print("Exiting program...")
            break

# Create a thread for printing current time
time_thread = threading.Thread(target=print_current_time)

# Start the thread
time_thread.start()

# Wait for the thread to finish (this will never happen because the thread runs indefinitely)
time_thread.join()

print("Program ended.")

'''
65. Write a Python program that creates two threads. Each thread should print out the
numbers from 1 to10. The two threads should run concurrently and print out the numbers in an interleaved
fashion.
'''

#Solution

import threading

# Global variables for synchronization
lock = threading.Lock()
count = 1

def print_numbers(start, end):
    global count
    while count <= end:
        with lock:
            if count <= end:
                print(f"Thread-{start}: {count}")
                count += 1

# Create threads
thread1 = threading.Thread(target=print_numbers, args=(1, 10))
thread2 = threading.Thread(target=print_numbers, args=(2, 10))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Threads execution completed.")

'''
Q66. Write a Python program to create a shared variable between two threads and increment its
value in each thread.

'''

#Solution
import threading

# Global shared variable
shared_variable = 0

# Lock for synchronization
lock = threading.Lock()

def increment_shared_variable():
    global shared_variable
    for _ in range(1000000):  # Increment 1 million times in each thread
        with lock:
            shared_variable += 1

# Create two threads
thread1 = threading.Thread(target=increment_shared_variable)
thread2 = threading.Thread(target=increment_shared_variable)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print(f"Final value of shared variable: {shared_variable}")




'''
Q67. Here's a Python program that creates a thread to count down from 5 to 0 and prints
"Blastoff!" when the count reaches 0:
'''
#Solution
import threading
import time

def countdown():
    count = 5
    while count >= 0:
        print(count)
        count -= 1
        time.sleep(1)  # Sleep for 1 second

    print("Blastoff!")

# Create a thread for countdown
countdown_thread = threading.Thread(target=countdown)

# Start the thread
countdown_thread.start()

# Wait for the thread to complete (this will not happen in this case as countdown runs indefinitely)
countdown_thread.join()

print("Countdown thread completed.")

'''
68. Write a program that creates a thread to print the Fibonacci sequence up to a certain
number n. The main thread should prompt the user for the value of n.

'''
#Solution

import threading

# Function to generate Fibonacci sequence up to a given number
def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

# Main function
def main():
    # Prompt user for input
    n = int(input("Enter the value of n to generate Fibonacci sequence up to: "))
    
    # Create a thread for generating Fibonacci sequence
    fibonacci_thread = threading.Thread(target=fibonacci_sequence, args=(n,))
    
    # Start the thread
    fibonacci_thread.start()
    
    # Wait for the thread to complete (optional)
    fibonacci_thread.join()

# Run the main function
if __name__ == "__main__":
    main()
'''
Q69. Write a program that creates two threads to add and subtract numbers from a shared
variable. The shared variable should start at 0, and each thread should perform 10 iterations of adding or
subtracting a random integer between 1 and 10. The program should print the final value of the shared
variable
'''

#Solution

import threading
import random
import time

# Global shared variable
shared_variable = 0

# Lock for synchronization
lock = threading.Lock()

# Function for thread to add to shared variable
def add_to_shared_variable():
    global shared_variable
    for _ in range(10):
        with lock:
            increment = random.randint(1, 10)
            shared_variable += increment
            print(f"Added {increment}, Current value: {shared_variable}")
        time.sleep(0.1)  # Simulate some processing time

# Function for thread to subtract from shared variable
def subtract_from_shared_variable():
    global shared_variable
    for _ in range(10):
        with lock:
            decrement = random.randint(1, 10)
            shared_variable -= decrement
            print(f"Subtracted {decrement}, Current value: {shared_variable}")
        time.sleep(0.1)  # Simulate some processing time

# Create threads
add_thread = threading.Thread(target=add_to_shared_variable)
subtract_thread = threading.Thread(target=subtract_from_shared_variable)

# Start threads
add_thread.start()
subtract_thread.start()

# Wait for threads to complete
add_thread.join()
subtract_thread.join()

# Print final value of shared variable
print(f"Final value of shared variable: {shared_variable}")


'''
Q70. Write a program that creates a thread to calculate the sum of the numbers from 1 to 100
and prints the result.
'''
#Solution
import threading

# Global variable to store the final sum
total_sum = 0

# Function to calculate sum of numbers from start to end
def calculate_sum(start, end):
    global total_sum
    for num in range(start, end + 1):
        total_sum += num

# Create threads for calculating sum
thread1 = threading.Thread(target=calculate_sum, args=(1, 50))
thread2 = threading.Thread(target=calculate_sum, args=(51, 100))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

# Print the final sum
print(f"Sum of numbers from 1 to 100: {total_sum}")


'''
Q71.Write a Python program to create two processes that print out the numbers from 1 to 10
simultaneously.

'''
#Solution 


import multiprocessing

# Function to print numbers from start to end
def print_numbers(start, end):
    for num in range(start, end + 1):
        print(num)

# Main function
def main():
    # Create two processes
    process1 = multiprocessing.Process(target=print_numbers, args=(1, 5))
    process2 = multiprocessing.Process(target=print_numbers, args=(6, 10))
    
    # Start processes
    process1.start()
    process2.start()
    
    # Wait for processes to complete
    process1.join()
    process2.join()

if __name__ == "__main__":
    main()



'''
Q72.Write a Python program that creates four processes and computes the sum of the first
1000 integers using multiprocessing
'''
#Solution


import multiprocessing

# Function to compute sum of numbers from start to end
def compute_sum(start, end, result_queue):
    total_sum = sum(range(start, end + 1))
    result_queue.put(total_sum)

# Main function
def main():
    # Number of integers to sum
    total_numbers = 1000

    # Number of processes
    num_processes = 4

    # Create a Queue to store results
    result_queue = multiprocessing.Queue()

    # Compute range for each process
    step = total_numbers // num_processes
    processes = []
    start = 1

    for i in range(num_processes):
        end = start + step - 1 if i < num_processes - 1 else total_numbers
        process = multiprocessing.Process(target=compute_sum, args=(start, end, result_queue))
        processes.append(process)
        start = end + 1

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    # Get results from the queue and calculate final sum
    final_sum = 0
    while not result_queue.empty():
        final_sum += result_queue.get()

    print(f"Sum of the first {total_numbers} integers: {final_sum}")

if __name__ == "__main__":
    main()


'''
Q73.Write a Python program that creates two processes and communicates between them
using a Queue. The first process should send a list of numbers to the second process, which
should calculate the sum of the numbers and send it back to the first process.

'''
#Solution
import multiprocessing

# Function for the first process to send numbers to the second process
def send_numbers(numbers, queue):
    # Send numbers to the second process
    for num in numbers:
        queue.put(num)
    # Signal end of numbers
    queue.put(None)

# Function for the second process to receive numbers and calculate sum
def calculate_sum(queue):
    total_sum = 0
    while True:
        num = queue.get()
        if num is None:
            break
        total_sum += num
    return total_sum

# Main function
def main():
    # Create a Queue for communication between processes
    queue = multiprocessing.Queue()

    # Numbers to send to the second process
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create processes
    send_process = multiprocessing.Process(target=send_numbers, args=(numbers, queue))
    sum_process = multiprocessing.Process(target=calculate_sum, args=(queue,))

    # Start processes
    send_process.start()
    sum_result = sum_process.start()

    # Wait for processes to finish
    send_process.join()
    sum_process.join()

    # Print the result calculated by the second process
    print(f"Sum of numbers: {sum_result}")

if __name__ == "__main__":
    main()

'''
Q74.Write a program to find the maximum number in a list of lists using multiprocessing.

'''
#Solution
import multiprocessing

# Function to find maximum in a sublist
def find_max_in_sublist(sublist, result_queue):
    max_value = max(sublist)
    result_queue.put(max_value)

# Function to find overall maximum using multiprocessing
def find_overall_max(list_of_lists):
    # Create a Queue for communication between processes
    result_queue = multiprocessing.Queue()

    # Create a list to hold all process instances
    processes = []

    # Create processes to find max in each sublist
    for sublist in list_of_lists:
        process = multiprocessing.Process(target=find_max_in_sublist, args=(sublist, result_queue))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Get max values from the result queue
    max_values = []
    while not result_queue.empty():
        max_values.append(result_queue.get())

    # Find the overall maximum
    overall_max = max(max_values)

    return overall_max

# Main function
def main():
    # Example list of lists
    list_of_lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Find the maximum number in the list of lists using multiprocessing
    max_number = find_overall_max(list_of_lists)
    print(f"The maximum number in the list of lists is: {max_number}")

if __name__ == "__main__":
    main()

'''
Q75.Write a Python program that uses the Pool class from the multiprocessing module to
calculate the squares of a list of integers.
'''
#Solution

import multiprocessing

# Function to calculate square of a number
def calculate_square(number):
    return number ** 2

# Main function
def main():
    # List of integers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create a Pool of worker processes
    with multiprocessing.Pool() as pool:
        # Apply calculate_square function to each number in numbers list
        results = pool.map(calculate_square, numbers)

    # Print results
    print("Original numbers:", numbers)
    print("Squares of numbers:", results)

if __name__ == "__main__":
    main()


'''
Q76.How do you create a new process using the multiprocessing module in Python?

'''
#Solution
import multiprocessing
import time

# Define a target function for the process
def worker_function():
    print("Worker process is executing")
    time.sleep(2)  # Simulate some work

def main():
    # Create a Process object with target function
    process = multiprocessing.Process(target=worker_function)

    # Start the process
    process.start()

    # Optionally, wait for the process to complete
    process.join()

    print("Main process continues...")

if __name__ == "__main__":
    main()




'''
Q77.How do you use a Pool to execute a function with multiple arguments in parallel?


'''
#Solution
import multiprocessing

# Function to process data with multiple arguments
def process_data(arg1, arg2):
    result = arg1 + arg2
    return result

def main():
    # Create a Pool object
    with multiprocessing.Pool() as pool:
        # List of argument tuples
        arguments = [(1, 2), (3, 4), (5, 6)]

        # Execute process_data function in parallel with multiple arguments
        results = pool.starmap(process_data, arguments)

    # Print results
    print("Results:", results)

if __name__ == "__main__":
    main()

'''
Q78.Write a Python program to calculate the sum of squares of numbers in a list using
multiprocessing.

'''
#Solution

import multiprocessing

# Function to calculate square of a number
def calculate_square(number):
    return number ** 2

# Function to calculate sum of squares using multiprocessing
def sum_of_squares(numbers):
    # Create a Pool of worker processes
    with multiprocessing.Pool() as pool:
        # Apply calculate_square function to each number in numbers list
        squares = pool.map(calculate_square, numbers)

    # Calculate sum of squares
    total_sum = sum(squares)
    return total_sum

# Main function
def main():
    # List of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Calculate sum of squares using multiprocessing
    result = sum_of_squares(numbers)

    # Print result
    print(f"The sum of squares of numbers {numbers} is: {result}")

if __name__ == "__main__":
    main()

'''
Q79.Write a Python program that uses the multiprocessing module to calculate the sum of a
large list of integers.

'''
#Solution

import multiprocessing

# Function to calculate sum of integers in a chunk
def sum_chunk(chunk):
    return sum(chunk)

# Function to calculate sum using multiprocessing
def calculate_sum(numbers):
    # Determine chunk size based on number of CPUs
    num_cpus = multiprocessing.cpu_count()
    chunk_size = len(numbers) // num_cpus

    # Create a Pool of worker processes
    with multiprocessing.Pool() as pool:
        # Split numbers into chunks
        chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]

        # Apply sum_chunk function to each chunk in parallel
        results = pool.map(sum_chunk, chunks)

    # Calculate total sum
    total_sum = sum(results)
    return total_sum

# Main function
def main():
    # Generate a large list of integers (e.g., from 1 to 10000)
    numbers = list(range(1, 10001))

    # Calculate sum using multiprocessing
    result = calculate_sum(numbers)

    # Print result
    print(f"The sum of the list of numbers is: {result}")

if __name__ == "__main__":
    main()

'''
Q80.Write a Python program that uses the multiprocessing module to parallelize the
computation of the factorial of a number
'''
#Solution
import multiprocessing
from math import factorial

# Function to compute factorial of a range of numbers
def compute_factorial(start, end, result_queue):
    results = {}
    for i in range(start, end + 1):
        results[i] = factorial(i)
    result_queue.put(results)

# Function to compute factorial using multiprocessing
def parallel_factorial(number):
    # Create a Queue for communication between processes
    result_queue = multiprocessing.Queue()

    # Determine number of CPUs
    num_cpus = multiprocessing.cpu_count()

    # Calculate chunk size based on number of CPUs
    chunk_size = (number // num_cpus) + 1

    # Create list of processes
    processes = []
    for i in range(num_cpus):
        start = i * chunk_size + 1
        end = min((i + 1) * chunk_size, number)
        process = multiprocessing.Process(target=compute_factorial, args=(start, end, result_queue))
        processes.append(process)
        process.start()

    # Collect results from processes
    results = {}
    for _ in range(num_cpus):
        results.update(result_queue.get())

    # Wait for all processes to finish
    for process in processes:
        process.join()

    return results[number]

# Main function
def main():
    number = 10  # Example number to compute factorial
    result = parallel_factorial(number)
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()

'''
Q81.Write a Python program that prompts the user for two integers and divides the first integer
by the second integer. If the either variable are none integer then print the value error and
second integer is zero, catch the ZeroDivisionError and print an error message to the user.

'''

#Solution
def main():
    try:
        # Prompt user for two integers
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        # Perform division
        result = num1 / num2

        # Print the result
        print(f"The result of {num1} divided by {num2} is: {result}")

    except ValueError:
        # Handle ValueError (if input is not a valid integer)
        print("Error: Please enter valid integers.")

    except ZeroDivisionError:
        # Handle ZeroDivisionError (if second integer is zero)
        print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()



'''
Q82.Write a Python program that prompts the user for a password and checks whether the
password meets certain criteria (e.g., at least 8 characters, contains at least one uppercase
letter, etc.). If the password does not meet the criteria, raise a custom exception called
PasswordError with a custom error message.
'''

#Solution

# Define a custom exception class for password validation
class PasswordError(Exception):
    pass

# Function to validate password
def validate_password(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters long.")

    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        raise PasswordError("Password must contain at least one uppercase letter.")

    # Add more criteria as needed (e.g., lowercase, digits, special characters)

    # If all criteria are met, return True
    return True

# Main function
def main():
    try:
        # Prompt user for password input
        password = input("Enter a password: ")

        # Validate the password
        validate_password(password)

        # If password meets criteria, print success message
        print("Password is valid.")

    except PasswordError as e:
        # Handle custom exception (PasswordError) and print error message
        print(f"Password Error: {e}")

if __name__ == "__main__":
    main()


'''
Q83.Write a Python program that prompts the user for a number and calculates the square root
of the number using the math.sqrt() function. If the number is negative, raise a ValueError with a
custom error message.

'''

#Solution

import math

# Function to calculate square root with error handling
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")

    return math.sqrt(number)

# Main function
def main():
    try:
        # Prompt user for a number
        number = float(input("Enter a number to calculate its square root: "))

        # Calculate square root and handle negative number case
        result = calculate_square_root(number)

        # Print the result
        print(f"The square root of {number} is: {result}")

    except ValueError as ve:
        # Handle ValueError (negative number) and print custom error message
        print(f"Error: {ve}")

    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()



'''
Q84.Write a Python program that prompts the user for a number and calculates the square root
of the number using the math.sqrt() function. If the number is negative, raise a ValueError with a
custom error message.

'''
#Solution
import math

# Function to calculate square root with error handling
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    
    return math.sqrt(number)

# Main function
def main():
    try:
        # Prompt user for a number
        number = float(input("Enter a number to calculate its square root: "))

        # Calculate square root and handle negative number case
        result = calculate_square_root(number)

        # Print the result
        print(f"The square root of {number} is: {result}")

    except ValueError as ve:
        # Handle ValueError (negative number) and print custom error message
        print(f"Error: {ve}")

    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()





'''
Q85.Write a Python program that prompts the user for a list of integers and calculates the
average of the list. If the list is empty, raise a ValueError with a custom error message.

'''
#Solution
# Function to calculate average with error handling
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")

    return sum(numbers) / len(numbers)

# Main function
def main():
    try:
        # Prompt user for input
        input_list = input("Enter a list of integers separated by spaces: ").strip()

        # Convert input to a list of integers
        numbers = list(map(int, input_list.split()))

        # Calculate average and handle empty list case
        average = calculate_average(numbers)

        # Print the result
        print(f"The average of the list {numbers} is: {average}")

    except ValueError as ve:
        # Handle ValueError (empty list) and print custom error message
        print(f"Error: {ve}")

    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

'''
Q86.Write a function that takes a string as input and returns the number of vowels in the string.
If the input is not a string, raise a TypeError with a custom error message.
'''
#Solution
# Function to count vowels with error handling
def count_vowels(input_str):
    if not isinstance(input_str, str):
        raise TypeError("Input should be a string.")

    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_str:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Example usage
def main():
    try:
        input_str = input("Enter a string: ")

        # Calculate number of vowels and handle type error
        num_vowels = count_vowels(input_str)

        # Print the result
        print(f"Number of vowels in '{input_str}': {num_vowels}")

    except TypeError as te:
        print(f"TypeError: {te}")

if __name__ == "__main__":
    main()




'''
Q87.write a python program how to handle simple runtime error?

'''
#Solution

def main():
    try:
        # Attempt to perform an operation that may raise an exception
        x = 10 / 0  # This will raise a ZeroDivisionError

    except ZeroDivisionError as e:
        # Handle the specific exception (ZeroDivisionError)
        print(f"Error: {e}. Division by zero is not allowed.")

    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()



'''
Q88.write a program how to handle multiple errors with one answer:# Program to handle
multiple errors with one

'''
#Solution
def main():
    try:
        # Attempt to perform operations that may raise exceptions
        x = 10 / 0  # This will raise a ZeroDivisionError
        y = int('abc')  # This will raise a ValueError

    except (ZeroDivisionError, ValueError) as e:
        # Handle both ZeroDivisionError and ValueError
        if isinstance(e, ZeroDivisionError):
            print(f"Error: {e}. Division by zero is not allowed.")
        elif isinstance(e, ValueError):
            print(f"Error: {e}. Invalid conversion to integer.")

    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


'''
Q89.write a program to print the reciprocal of even numbers note:we might want to run a certain
block of code if the code block inside try runs without any errors. For these cases, you can use
the optional else keyword with the try statement.

'''
#Solution

def reciprocal_of_even_number(number):
    try:
        if number % 2 != 0:
            raise ValueError(f"{number} is not an even number.")

        result = 1 / number
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        print(f"The reciprocal of {number} is: {result:.2f}")

# Example usage
def main():
    numbers = [2, 4, 6, 8, 10, 3, 5, 7]

    for number in numbers:
        reciprocal_of_even_number(number)

if __name__ == "__main__":
    main()

'''
Q90.How to handle exceptions using the try, except, and finally statements write code

'''
#Solution
def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except TypeError:
        print("Error: Unsupported operand type(s) for division.")
    else:
        print(f"The result of {x} divided by {y} is: {result}")
    finally:
        print("Cleanup: Finished processing division operation.")

# Example usage
def main():
    # Example 1: Handling division by zero
    divide_numbers(10, 0)

    # Example 2: Handling unsupported operand type
    divide_numbers(10, '2')

    # Example 3: Successful division
    divide_numbers(10, 2)

if __name__ == "__main__":
    main()


'''
Q91. Write a Python program to create a MySQL database and a table
'''
#Solution
import mysql.connector

# Function to create a MySQL database
def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="aklash124"  # Replace with your MySQL password
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Execute a SQL query to create a database
        cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

        print("Database 'mydatabase' created successfully.")

    except mysql.connector.Error as error:
        print(f"Error creating database: {error}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Function to create a MySQL table
def create_table():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="asklash123",  # Replace with your MySQL password
            database="sriram"  # Replace with the name of the database created
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Define a SQL query to create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL
        )
        """

        # Execute the SQL query to create the table
        cursor.execute(create_table_query)

        print("Table 'customers' created successfully.")

    except mysql.connector.Error as error:
        print(f"Error creating table: {error}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Main function to run the program
def main():
    create_database()
    create_table()

if __name__ == "__main__":
    main()


'''
Q92. Write a Python program to insert data into a MySQL table
'''
#Solution
import mysql.connector

# Function to create a MySQL table
def create_table():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="aklash123",  # Replace with your MySQL password
            database="sriram"  # Replace with the name of your database
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Define a SQL query to create a table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL
        )
        """

        # Execute the SQL query to create the table
        cursor.execute(create_table_query)

        print("Table 'customers' created successfully.")

    except mysql.connector.Error as error:
        print(f"Error creating table: {error}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Function to insert data into MySQL table
def insert_data(name, address):
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="aklash124",  # Replace with your MySQL password
            database="sriram"  # Replace with the name of your database
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to insert data into the table
        insert_query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        data = (name, address)

        # Execute the SQL query to insert data
        cursor.execute(insert_query, data)

        # Commit changes to the database
        connection.commit()

        print(f"Data inserted successfully: {data}")

    except mysql.connector.Error as error:
        print(f"Error inserting data: {error}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Main function to run the program
def main():
    create_table()

    # Example data to insert into the table
    data_to_insert = [
        ("John Doe", "123 Elm St, Springfield"),
        ("Jane Smith", "456 Oak Ave, Rivertown"),
        ("Michael Brown", "789 Pine Rd, Lakeside")
    ]

    # Insert each set of data into the table
    for name, address in data_to_insert:
        insert_data(name, address)

if __name__ == "__main__":
    main()


'''
Q93. Write a Python program to create an index on a MySQL table
'''
#Solution
import mysql.connector

# Function to create a MySQL table
def create_table():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="aklash123",  # Replace with your MySQL password
            database="sriram"  # Replace with the name of your database
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Define a SQL query to create a table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
        """

        # Execute the SQL query to create the table
        cursor.execute(create_table_query)

        print("Table 'customers' created successfully.")

    except mysql.connector.Error as error:
        print(f"Error creating table: {error}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Function to create an index on a MySQL table
def create_index():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="ram",  # Replace with your MySQL username
            password="aklash123",  # Replace with your MySQL password
            database="sriram"  # Replace with the name of your database
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Define a SQL query to create an index on the 'email' column
        create_index_query = "CREATE INDEX idx_email ON customers (email)"

        # Execute the SQL query to create the index
        cursor.execute(create_index_query)

        print("Index 'idx_email' created successfully on column 'email'.")

    except mysql.connector.Error as error:
        print(f"Error creating index: {error}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Main function to run the program
def main():
    create_table()
    create_index()

if __name__ == "__main__":
    main()


'''
Q94. Write a Python program to join two tables in MySQL
'''
#Solution

import mysql.connector

# Function to perform a SQL join operation
def join_tables():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="aklash123",  # Replace with your MySQL password
            database="sriram"  # Replace with the name of your database
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to join tables and fetch data
        join_query = """
        SELECT customers.name, customers.address, orders.product
        FROM customers
        INNER JOIN orders ON customers.id = orders.customer_id
        """

        # Execute the SQL query
        cursor.execute(join_query)

        # Fetch all rows of the result
        result = cursor.fetchall()

        # Print the result
        for row in result:
            print(row)

    except mysql.connector.Error as error:
        print(f"Error joining tables: {error}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Main function to run the program
def main():
    join_tables()

if __name__ == "__main__":
    main()



'''
Q95. Write a Python program to handle MySQL errors using exception handling.
'''
#Solution
import mysql.connector
from mysql.connector import Error

# Function to connect to MySQL and execute a query
def execute_query(query):
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="ram",  # Replace with your MySQL username
            password="sriram",  # Replace with your MySQL password
            database="sriram"  # Replace with the name of your database
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(query)

        # Commit changes to the database (if required)
        connection.commit()

        # Fetch and print all rows of the result (if SELECT query)
        if cursor.rowcount > 0:
            result = cursor.fetchall()
            for row in result:
                print(row)
        else:
            print("No rows found.")

    except Error as e:
        print(f"Error executing query: {e}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Main function to run the program
def main():
    # Example SQL query (replace with your own query)
    query = "SELECT * FROM customers"

    # Execute the query
    execute_query(query)

if __name__ == "__main__":
    main()


'''
Q96. Write a Python program to connect to a MongoDB database and insert data
'''
#Solution
import pymongo
from pymongo import MongoClient

# Function to connect to MongoDB and insert data
def insert_data(data):
    try:
        # Connect to MongoDB server
        client = MongoClient("mongodb://localhost:27017/")

        # Connect to a database
        db = client["mydatabase"]  # Replace with your database name

        # Connect to a collection
        collection = db["mycollection"]  # Replace with your collection name

        # Insert data into the collection
        result = collection.insert_one(data)

        print(f"Data inserted successfully. Inserted ID: {result.inserted_id}")

    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")

    except pymongo.errors.OperationFailure as e:
        print(f"Error inserting data: {e}")

    finally:
        # Close the MongoDB connection
        if 'client' in locals() or 'client' in globals():
            client.close()
            print("MongoDB connection is closed.")

# Main function to run the program
def main():
    # Example data to insert into MongoDB
    data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30
    }

    # Insert the data into MongoDB
    insert_data(data)

if __name__ == "__main__":
    main()

'''
Q97. Write a Python program to update data in a MongoDB database.

'''


#Solution
import pymongo
from pymongo import MongoClient

# Function to connect to MongoDB and update data
def update_data(query, new_data):
    try:
        # Connect to MongoDB server
        client = MongoClient("mongodb://localhost:27017/")

        # Connect to a database
        db = client["mydatabase"]  # Replace with your database name

        # Connect to a collection
        collection = db["mycollection"]  # Replace with your collection name

        # Update data in the collection
        result = collection.update_one(query, {"$set": new_data})

        print(f"Data updated successfully. Matched {result.matched_count} documents.")

    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")

    except pymongo.errors.OperationFailure as e:
        print(f"Error updating data: {e}")

    finally:
        # Close the MongoDB connection
        if 'client' in locals() or 'client' in globals():
            client.close()
            print("MongoDB connection is closed.")

# Main function to run the program
def main():
    # Example query and new data
    query = {"name": "John Doe"}  # Query to find documents to update
    new_data = {"$set": {"age": 35}}  # New data to update in matching documents

    # Update the data in MongoDB
    update_data(query, new_data)

if __name__ == "__main__":
    main()


'''
Q98. Write a Python program to handle MongoDB errors using exception handling.

'''
#Solution
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

# Function to connect to MongoDB and perform an operation
def perform_mongodb_operation():
    try:
        # Connect to MongoDB server
        client = MongoClient("mongodb://localhost:27017/")

        # Connect to a database
        db = client["mydatabase"]  # Replace with your database name

        # Connect to a collection
        collection = db["mycollection"]  # Replace with your collection name

        # Example query and data
        query = {"name": "John Doe"}
        new_data = {"$set": {"age": 35}}

        # Update data in the collection
        result = collection.update_one(query, new_data)

        # Print the result
        print(f"Data updated successfully. Matched {result.matched_count} documents.")

    except ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")

    except OperationFailure as e:
        print(f"MongoDB operation failure: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # Close the MongoDB connection
        if 'client' in locals() or 'client' in globals():
            client.close()
            print("MongoDB connection is closed.")

# Main function to run the program
def main():
    # Perform MongoDB operation
    perform_mongodb_operation()

if __name__ == "__main__":
    main()




'''
Q99. Write a Python program to query a MongoDB database using aggregation.

'''
#Solution
import pymongo
from pymongo import MongoClient

# Function to connect to MongoDB and perform an aggregation query
def perform_aggregation_query():
    try:
        # Connect to MongoDB server
        client = MongoClient("mongodb://localhost:27017/")

        # Connect to a database
        db = client["mydatabase"]  # Replace with your database name

        # Connect to a collection
        collection = db["mycollection"]  # Replace with your collection name

        # Define aggregation pipeline
        pipeline = [
            {"$group": {"_id": "$category", "total_quantity": {"$sum": "$quantity"}}},
            {"$sort": {"total_quantity": -1}},
            {"$limit": 5}
        ]

        # Perform aggregation
        result = collection.aggregate(pipeline)

        # Print aggregation results
        print("Top 5 categories by total quantity:")
        for doc in result:
            print(doc)

    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")

    except pymongo.errors.OperationFailure as e:
        print(f"MongoDB operation failure: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # Close the MongoDB connection
        if 'client' in locals() or 'client' in globals():
            client.close()
            print("MongoDB connection is closed.")

# Main function to run the program
def main():
    # Perform MongoDB aggregation query
    perform_aggregation_query()

if __name__ == "__main__":
    main()

'''
Q100. Write a Python program to perform a text search on a MongoDB database.
'''
#Solution
import pymongo
from pymongo import MongoClient

# Function to connect to MongoDB and perform a text search
def perform_text_search(search_query):
    try:
        # Connect to MongoDB server
        client = MongoClient("mongodb://localhost:27017/")

        # Connect to a database
        db = client["mydatabase"]  # Replace with your database name

        # Connect to a collection
        collection = db["mycollection"]  # Replace with your collection name

        # Perform text search
        result = collection.find({"$text": {"$search": search_query}})

        # Print search results
        print(f"Search results for '{search_query}':")
        for doc in result:
            print(doc)

    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")

    except pymongo.errors.OperationFailure as e:
        print(f"MongoDB operation failure: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # Close the MongoDB connection
        if 'client' in locals() or 'client' in globals():
            client.close()
            print("MongoDB connection is closed.")

# Main function to run the program
def main():
    # Example search query
    search_query = "Python MongoDB"

    # Perform MongoDB text search
    perform_text_search(search_query)

if __name__ == "__main__":
    main()



'''
Q101. Create a Flask application that displays "Hello, World!" on the homepage.

'''

#Solution
#pip install Flask

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def index():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

'''
Q102. Write a Flask route that takes a name parameter and returns "Hello, [name]!" as plain
text.

'''
#Solution
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route that takes a name parameter
@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)


'''
Q103. Write a Flask route that takes a number parameter and returns the square of that number
as plain text
'''

#Solution

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route that takes a number parameter
@app.route('/square/<int:num>')
def square(num):
    squared_value = num ** 2
    return f'The square of {num} is {squared_value}'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)



'''
Q104. Write a Flask route that displays a simple HTML form that asks for a name and returns
"Hello, [name]!" when submitted.

'''
#Solution

from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# Define a route to display the form
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('greet', name=name))
    return render_template('hello.html')

# Define a route to greet the user
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)


#html file
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Form</title>
</head>
<body>
    <h2>Enter Your Name:</h2>
    <form method="POST">
        <input type="text" name="name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

'''



'''
Q105. Write a Flask route that displays a list of names in an HTML unordered list.

'''
#Solution

from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Route to display a list of names
@app.route('/names')
def names():
    # List of names (replace with your data)
    name_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

    # Render the HTML template with the list of names
    return render_template('names.html', names=name_list)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)



'''
Q106. Write a Flask route that displays a list of names in a table
'''
#Solution
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Route to display a list of names in a table
@app.route('/names')
def names():
    # List of names (replace with your data)
    name_list = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 28},
        {'id': 4, 'name': 'David', 'age': 27},
        {'id': 5, 'name': 'Eve', 'age': 22}
    ]

    # Render the HTML template with the list of names
    return render_template('names.html', names=name_list)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)



#html file below
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of Names</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
            margin: 20px auto;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h2>List of Names:</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
            </tr>
        </thead>
        <tbody>
            {% for person in names %}
                <tr>
                    <td>{{ person.id }}</td>
                    <td>{{ person.name }}</td>
                    <td>{{ person.age }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>

'''




'''
Q107. Write a Flask route that displays a list of names in a dropdown menu.


'''
#Solution
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Route to display a dropdown menu of names
@app.route('/dropdown')
def dropdown():
    # List of names (replace with your data)
    name_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

    # Render the HTML template with the list of names
    return render_template('dropdown.html', names=name_list)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
#html file below
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dropdown Menu of Names</title>
</head>
<body>
    <h2>Select a Name:</h2>
    <form>
        <label for="names">Choose a name:</label>
        <select id="names" name="names">
            {% for name in names %}
                <option value="{{ name }}">{{ name }}</option>
            {% endfor %}
        </select>
        <br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>

'''


'''
Q108. Write a Flask route that receives data through a POST request and returns the data in
JSON format.

'''
#Solution


from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Route to handle POST requests and return JSON data
@app.route('/postdata', methods=['POST'])
def post_data():
    # Get the JSON data from the POST request
    data = request.json

    # Return the received data as JSON response
    return jsonify(data)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)


'''
Q109. Write a Flask route that redirects the user to a different URL
'''
#Solution


from flask import Flask, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# Route to handle the initial request
@app.route('/')
def index():
    return 'Welcome to the Home Page'

# Route to redirect to another URL
@app.route('/redirect')
def redirect_example():
    # Redirect to the '/' route (Home Page)
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)








