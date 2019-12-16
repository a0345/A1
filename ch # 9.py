                                  Examples
eng2speng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
len(eng2sp)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10 :
        print(key, counts[key])

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])

                               Exercise    

Question 1
import string
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
counts = dict()
for line in fhand:
    line = line.rstrip()
line = line.translate(line.maketrans('', '', string.punctuation))
line = line.lower()
words = line.split()
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
print(counts)

Question 2
counts= dict()                       # Initializes the dictionary
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in counts:
            counts[words[2]] = 1       # First entry
        else:
            counts[words[2]] += 1      # Additional counts

print(counts)

Question 3 
fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    if line.startswith('From:'):
        line = line.split()
        email = line[1]
        counts[email] = counts.get(email,0)+1
print(counts)


Question 5
fhand = open('mbox.txt')
counts = {}
for line in fhand:
    if line.startswith('From:'):
       line = line.strip()
       atpos = line.find('@')
       domain = line[atpos+1:]
       counts[domain] = counts.get(domain,0)+1
print(counts)


