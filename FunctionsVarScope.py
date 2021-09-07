# Global vars
# defined outside of fn scope
# have preference in main prog

print('Global vars')
country = 'USA'
city = 'Seattle'

def some_fn():
	print('country = ',country)
	print('city = ',city)
	
some_fn()

# local vars
# variable defined and assigned within fn
# can hide global vars if they have the same name
# have preference in fn

print('\nlocal and global vars')
def some_fn():
	country = 'India'
	print('country = ',country)
	print('city = ',city)
	
some_fn()

# using global keyword

print('\nUsing Global Keyword')
def some_fn():
	global city
	city = 'Washington'
	print('country = ',country)
	print('city = ',city)
	
some_fn()

# values of local vars cannot change global vars
# for simple data types

salary = 1000
expenditure = 200
name = 'james'
interest = 0.4

print('\nsavings fn - passed values')
def print_savings():
	print('name= ',name,' Savings = ',salary-expenditure,' interest = ',interest)
	
print_savings()

print('\nsavings fn - local vars')
def print_savings(name,salary,expenditure,interest):
	print('name = ',name)
	expenditure = expenditure + 100
	savings = salary - expenditure
	print('Savings = ',savings)
	print('Interest = ',interest)
	
print_savings('Julie',10000,2000,0.2)

# with tuples

print('\nshow scope of vars in fns using tuples')
fruits_tuple = ('apple','grapes','mango')

def change_tuple(fruits_tuple):
	fruits_tuple = ('kiwi','strawberry')
	print('inside fn ',fruits_tuple)
	
change_tuple(fruits_tuple)
print('Outside fn ',fruits_tuple)

# with lists - no chnge in global vars

print('\nshow scope of vars in fns using lists')
fruits_list = ['apple','grapes','mango']

def change_list(fruits_list):
	fruits_list = ['kiwi','strawberry']
	print('inside fn - LOCAL VARIABLE - ',fruits_list)
	
change_list(fruits_list)
print('Outside fn - GLOBAL VARIABLE - ',fruits_list)

# with lists. Changing global vars by changing local vars

print('\nLists. Changing global vars by changing local vars')
fruits_list = ['apple','grapes','mango']

def change_list(fruits_list):
	fruits_list[0] = 'kiwi'
	print('inside fn - LOCAL VARIABLE - ',fruits_list)
	
change_list(fruits_list)
print('Outside fn - GLOBAL VARIABLE - ',fruits_list)

# with lists. changing local vars nusing append

print('\nLists. Changing global vars by changing local vars using append')
fruits_list = ['apple','grapes','mango']

def change_list(fruits_list):
	fruits_list.append('kiwi')
	print('inside fn - LOCAL VARIABLE - ',fruits_list)
	
change_list(fruits_list)
print('Outside fn - GLOBAL VARIABLE - ',fruits_list)

# with dictionary
print('\nDictionary')

car_speeds_dict = {'camry':120,'accord':130,'cayenne':250}

def change_dict(car_speeds_dict):
	car_speeds_dict['mustang'] = 200
	print('inside fn - LOCAL VARIABLE - ',car_speeds_dict)
	
change_dict(car_speeds_dict)
print('Outside fn - GLOBAL VARIABLE - ',car_speeds_dict)


