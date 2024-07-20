"""
- Extension of python file is (.py).

- input ----> program (python) ---> output

"""

# In python print() statement is used to print/display  something on terminal/screen.
print("Hello World")

"""
print() ---> python function to display output on screen.

"Hello World" --->In side " message " double quote which thing we write that is display on screen . double quote shows the string type of data will be print.

"""

#python Character Set 

"""
Letters - A to Z , a to z

Digits - 0 to 9

Special Symbols - (- , + , _ , * , / etc.(present on keyboard))

Whitespaces - Blank Space, tab , carriage return , new line , formfeed.

Other characters - Python can process all ASCII and Unicode characters as part of data or literals.

"""

# If we want to print multiple things in same spearate it by (,) comma operator.
print("Sainath is my name.","my age is 23.");

#print numbers directly.
print(23);
print(35);

#print sum of numbers.
print(23 + 35);

#Variables

"""
A variable is a name given to a memory location in a program.

value can be changes .

variable = value
name = "Shradha"
age = 23
price = 25.09


"""

name = "sainath"; #String (collection words , characters, sentences.)
age = 21; #integer(int)
price = 23.99; # decimal value (float)

print("name") # by using double quote the things inside it will be print.

#if we want to print the value of variable then without double quote write variable name.

print(name); #sainath
print(age); #age
print(price); #price

#how to print message with variable value by using (,) operator 

print("my name is : " , name); # my name is :  sainath
print("my age is : " , age);  # my age is :  21
print("price is : " , price); # price is :  23.99

#In python (=) it is assignment operator. By using it R.H.S. of variable store L.H.S. of variable.

age2 = age; # value of age is assigned to age2.
print("value of age2 = ",age2); # value of age2 =  21

"""
Rules for Identifiers.

1. Identifiers can be combination of uppercase and lowercase letters, digits or an  underscore(_). So myVariable , Variable_1, vairable_for_print all are valid identifiers.

2. An Identifier can not start with digit . So while variable1 is valid. 1variable is not valid.

3. We can't use special symbols like !,#,@,%,$ etc in our identifier.

4. Identifier can be of any length.

5. simple , short & meaningful --> Identifier(variable).

"""

# type() is used to print what type of data is this.

print(type(name)); #<class 'str'>
print(type(age)); #<class 'int'>
print(type(price)); #<class 'float'>