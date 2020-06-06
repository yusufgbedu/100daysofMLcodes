"""welcome to our first hellow world program in
Introduction to Python for Datascience"""

print('Hello World!!')

"""data types and variable decleration in python summary"""

Name= 'Gbedu Yusuf'
#string

Age= 20
#interger

height= 6.1
#float

Black= True
#boolen

Fam_Age=['MARYAM', 25, 'MOHAMMED', 22, 'NAFISA', 17.5, 'MUSA', 10]
#list
#using comma, and format operators to print
print('my name is {}, i am {}yrs old'.format (Name, Age))
print('let say am approximately {}ft tall and am black yeah that {}'.format (height, Black))
print('my siblins name are ages are:',Fam_Age)
#comma printout

"""lIST
List are essential part in DataScience 
so let do a summary on using Fam_age list
"""
#accessing items in list
Eldest= Fam_Age[0]
youngest= Fam_Age[-1]
#adding items using append attribute
Father= Fam_Age.append('Adamu Gbedu')
#editing items in a list
age_correction= Fam_Age[1]=26

print(Father)
print(age_correction)

#Nested list
todo_list = [['learn', 10], ['apply', 20], ['Build', 100]]
print(todo_list)
#other list method
upper_Case= Fam_Age[-1].upper()
print(upper_Case)