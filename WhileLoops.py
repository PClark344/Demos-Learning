num = 20
while num < 25:
	print(num)
	num = num + 1
print('finished loop')

num = 0
while num in range(0,10):
	print(num)
	num = num + 1
print('finished loop')
	
# single line
x,y = 0,8
while (x < y): x = x + 1; print(x)
print('finished loop')

# nested
x = 1
while x < 5:
	y = 1
	while y < 5:
		print(x,' ',y)
		y = y + 1
	x = x+ 1
print('finished nested loop')	
	
# Conversion

c_degrees = [-20,-30,66,51,23,87,97]
index = 0
print('C to F Conversionj')
while index < len(c_degrees):
	c = c_degrees[index]
	f = ((9.0/5)*c+32)
	print('%5d %5.1f' % (c,f))
	index += 1
	
# 2 lists
print('With 2 lists')
name_list = ['John','James','Olive']
age_list = [22,45,56]

index = 0
while index < len(name_list):
	print(name_list[index],' age ',age_list[index])
	index += 1
	
# with tuples
print('With tuples')
alpha_tuple = ('a','b','c')
count = 0
while count < len(alpha_tuple):
	print(alpha_tuple[count])
	count += 1
	
# with break stmt
print('With break stmt')
num = 10
while num in range(10,100):
	print(num)
	if num == 50:
		break
	num += 10
	
# with continue stmt
print('With continue stmt')
num = 0
while num < 10:
	if num % 2 == 0:
		num += 1
		continue
	else:
		print('Odd no ',num)
		num += 1
	
	


	

