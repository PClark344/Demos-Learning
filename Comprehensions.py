# python comprehensions

# numbers
num = range(10)
print([x*x for x in num if x % 2 ==0])
print(chr(10))
print([i for i in range(300) if i % 27 == 0])
print(chr(10))
msg = 'Hello 242 World'
nums = [int(x) for x in msg if x.isdigit()]
print('numbers in ',msg,' are: ',nums)
print(chr(10))
num_list = [number for number in range(51) if number % 2 ==0 if number % 5 == 0]
print('num_list = ',num_list)
print(chr(10))
nums = [12,66,33,22,95,87,64,19]
res = ['small' if num < 20 else 'large' for num in nums if num %2 == 0 if num %3 == 0]
print('Result = ',res)

# strings
print([letter for letter in 'anxiety'])
print(chr(10))
#print([i for i in "Mathematics" if i in ["A","E","I","O","U"])

# lists
list_of_weeks = ['this','is','a','list','of','weeks','honest']
print([word[0] for word in list_of_weeks])
print(chr(10))
print([word.upper() for word in list_of_weeks])
print(chr(10))
print([word[0].upper() for word in list_of_weeks])
print(chr(10))

# nested loops
stationery = ['Pen','Rubber','Ink']
colours = ['Red','Blue','Green']

combined = [(i,j) for j in stationery for i in colours]
print(combined)
