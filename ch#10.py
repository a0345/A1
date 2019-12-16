t1 = ('a',)
type(t1)

t2 = ('a')
type(t2)

t = tuple()
print(t)

t = tuple('lupins')
print(t)

t = ('a', 'b', 'c', 'd', 'e')
print(t[0])
print(t[1:3])
t = ('A',) + t[1:]
print(t)

(0, 1, 2) < (0, 3, 4)
(0, 1, 2000000) < (0, 3, 4)


txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(res)


m = [ 'have', 'fun' ]
x, y = m
x
y

m = [ 'have', 'fun' ]
x = m[0]
y = m[1]

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)


d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)
t.sort()

d = {'a':10, 'b':1, 'c':22}
for key, val in list(d.items()):
    print(val, key)


d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items() :
... l.append( (val, key) )
l
l.sort(reverse=True)


import string
fhand = open('mbox.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:10]:
    print(key, val)




                             Exercise
Question 1
fname =input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()
emails = dict()
for line in fhandle:
	if line.startswith('From '):
		line = line.split()
		email = line[1]
		emails[email] = emails.get(email,0) + 1
list = []
for email, count in emails.items():
	list.append( (count, email) )
list.sort(reverse=True)
for count, email in list[:1]:
	print (email, count)



Question 2
fname = input('Enter file name: ')
fhand = open(fname)
c = dict()
for line in fhand:
    if not line.startswith('From ') : 
        continue
    pieces = line.split()
    time = pieces[5]
    parts = time.split(':')
    hour = parts[0]
    c[hour] = c.get(hour,0) +1
lists=[]
for key in c.items():
    value = c[key]
    lists.append( (value, key) )
lists.sort()
for value, key in lists:
    print (key, value)


