# invoking fn with no return gives no output
def subt(num1,num2):
	res = num1 - num2

print('running subtraction with no return')
subt(10,7.7)
print('\n')
	

# invoking fn with return
def subt(num1,num2):
	res = num1 - num2
	
	return res
	
print('running subtraction with return')
print(subt(10,7.7))
print('\n')

# multiple return vars

def add_sub(x,y):
	add_res = x + y
	sub_res = x - y
	
	return add_res,sub_res
	
print('running subtraction and addition with return')
print(add_sub(53,9.2))
print('\n')

# returning string vars

print('Test to find first capital letter in string')
print('\n')

def find_first_cap(some_str):
	first_cap_lett = None
	
	for ch in some_str:
		if ch.upper() == ch and ch != ' ':
			first_cap_lett = ch
			break
			
	if first_cap_lett is None:
		return 'No caps found'
	else:
		return 'First Cap = ' + first_cap_lett
	
test = find_first_cap('this is a tEst String for first Capital')
print(test)
print('\n')

# create dictionary

print('Test to Create dictionary from function')
print('\n')

def create_dict(name,age,job):
	dicto = {'name':name,'age':age,'job':job}
	return dicto
	
test = create_dict('John',35,'Swimmer')
print(test)
print('\n')

# create list using comprehensions

print('Test to Create list from function')
print('\n')

def gen_list(name,num_elements):
	return [name for i in range(num_elements)]
	
test = gen_list('Daisy',4)
print(test)
print('\n')

# with other custom functions

def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def calc(a,b,op):
	if op == 'add':
		return 'result of ' + str(a) + ' + ' + str(b),' is: ' + str(add(a,b))
	elif op == 'sub':
		return 'result of ' + str(a) + ' - ' + str(b),' is: ' + str(sub(a,b))
	else:	
		return op + ' is an invalid Operator'
		
test = calc(10,23,'add')
print(test)
test = calc(10,23,'sub')
print(test)
test = calc(10,23,'zzz')
print(test)
print('\n')
	
