cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)
print(cheeses[0])


numbers = [17, 123]
numbers[1] = 5
print(numbers)


cheeses = ['Cheddar', 'Edam', 'Gouda']
'Edam' in cheeses 
'Brie' in cheeses 


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)



[0] * 4

[1, 2, 3] * 3



t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]
t[:4]
t[3:]




t[:]
['a', 'b', 'c', 'd', 'e', 'f']


t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)


t = ['a', 'b', 'c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)


t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)


t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)


t = ['a', 'b', 'c']
del t[1]
print(t)


t = ['a', 'b', 'c']
t.remove('b')
print(t)



t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


s = 'spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)
print(t[2])



s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)


t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)


a = 'banana'
b = 'banana'
a is b



a = [1, 2, 3]
b = a
b is a
b[0] = 17
print(a)

letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)


t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)
t3 = t1 + [3]
print(t3)
t2 is t3


letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)


