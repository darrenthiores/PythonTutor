#While loop
a = 0
while (a < 5):
    print('ini yang ke ', a)
    a += 1

#For loop
b = 5
for i in range(b) :
    print('ini for yange ke-' , i)

name = ['john', 'guido', 'bill gates']
for names in name:
    print(names)

#Nested loop

x = 2
y = 2
while (x < 10):
    while (y <= (x/y)):
        if not (x%y): break
        y += 1
    if (x > (x/y)) :
        print(x, "is prime")
    x += 1