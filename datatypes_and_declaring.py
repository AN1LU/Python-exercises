#Ana Lucia Pelayo Macias 31-05-2025
# Variables in Python

first_name = 'Ana Lucia'        # string
last_name = 'Pelayo'            # string
country = 'Mexico'              # string
city = 'Guadalajara'            # string
age = 22                        # integer
is_married = False              # Boolean
skills = ['HTML', 'CSS', 'Python', 'R', 'PowerShell'] #List
person_info = {                         #dictionary
    'firstname':'Ana Lucia', 
    'lastname':'Pelayo', 
    'country':'Mexico',
    'city':'Guadalajara'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Ana Lucia', 'Pelayo', 'Guadalajara', 22, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)