# Intro
def intro():
	print('Hello,my name,my name is..')
	
intro()
print(intro)
print('\n')

# with variables outside Function

name = 'John'
city = 'Antwerp'

def intro():
	print('My name is ',name)
	print('I live in ',city)
	
intro()
print('\n')

# Input parameters

def intro(name):
	print('My name is ',name)
		
intro('Pete')
intro('Lilly')
print('\n')

# Positional Arguments - importance of position

def intro(name,city):
	print('My name is ',name)
	print('I live in ',city)		
intro('Pete','Dublin')
intro('London','Lilly')
print('\n')

# Global vars
# Note how result of invoking function
# is independent of positional arguments used

sal = 1000
cost = 300

def my_savings(a,b):
	print('Savings with Global vars = ',sal-cost)
	print('Savings with Positional Arguments = ',a-b)
	
my_savings(888,55)
print('\n')

# Positional Arguments

print('Positional Arguments')
def total_score(maths,physics):
	print('Maths= ',maths,'Physics= ',physics)
	print('Total = ')
	return maths + physics
	
test = total_score(maths=55,physics=60)
print test
print('\n')

# Keyword Arguments

print('Keyword Arguments')
def total_score(maths=35,physics=84):
	print('Maths= ',maths,'Physics= ',physics)
	print('Total = ')
	return maths + physics
	
test = total_score()
print test
print('\n')

# Keyword and Positional Arguments
# NB Positional Arguments always first

print('Keyword and Positional Arguments')
def total_score(maths,physics=99):
	print('Maths= ',maths,'Physics= ',physics)
	print('Total = ')
	return maths + physics
	
test = total_score(maths=55)
print test
print('\n')

# Default Arguments. Specify at end

print('Keyword Arguments')
def st_exam_details(name,school,enrolled=False):
	print('Name= ',name,'School= ',school,' Enrolled= ',enrolled)
	return name + school + str(enrolled)
	
test = st_exam_details('Alice','Columbia')
print(test)
test = st_exam_details('John','Smith','True')
print(test)

print('\n')

# variable length arguments

def prt_fn(*args):
	args_type = type(args)
	print(args_type)
	print(args)
	return str(args_type) + ' ' + str(args)
	
test = prt_fn('Bob')
print(test)
test = prt_fn('Bob','Peter','John')
print(test)
names_list = ['Jill','John','Horatio']
test = prt_fn(names_list)
print(test)
test = prt_fn(*names_list)
print(test)
print('\n')

# variable length arguments *kwargs

def prt_fn(**kwargs):
	
	for key, value in kwargs.items():
		print("{0} = {1}".format(key, value))
	return 
	
kwargs = {'name':'Bob','school':'Oxford'}
print(prt_fn(**kwargs ))

print('\n')

# passing in a tuple and a dictionary

def st_dets(**details):
	
	if 'name' in details:
		print('Name: ',details[name])
	if 'age' in details:
		print('Age: ',details[age])
		
def st_in_coll(*st_names,**coll_details):
	print('STUDENTS')
	print('St names = ',st_names)

	print('passing in tuple')
	
	for s in st_names:
		print(s)
	print('COLLEGE: ')
	print('College details = ',coll_details)
	
	print('passing in dictionary')

	for key, value in coll_details.items():
		print(key,value)
		
test = st_in_coll('Alison','Bob','Charlie',name = 'stanford', city = 'Palo Alto')
print(test)



