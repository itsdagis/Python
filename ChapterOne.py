# this is my first python code

print("hello class, how are you doing?")

#data or value

print("Efrem") #varchar : text character
print(25) #int 
print("AB101") #varchar 
print("efrem@test.com") #varchar
print(10) #int
print(True) #boolean
print(type("Efrem")) #to check data type

#data type
# 1. string any thing under single or double qoute
# 2. number int (number with no decimal point or fraction)
# 3. number float and double  (number with decimal point)
# 4. boolean true or false

Student_Name = "Efrem" #varchar : text character
Age = 25 #int 
ID = "AB101" #varchar 
Email = "efrem@test.com" #varchar
Grade = 10 #int
Height = 1.70
Active = True #boolean

print(Student_Name) #when mentioning variable we don't need qoutation
print(ID)
print(Email)
print(Grade)
print(Height)
print(Active)

#variable rule
#1. Letter capital or smal , numbers $ or _
#2. Can't start with number 
#3. Can't any symbol or words that are keywords 

#operators 
#arthimetic op +/*%

a = 119
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # divides a by b and shows the remaining number 

#comparison <, >, ==,>=, <=, !=,

print (100 == 200)

#logical operator
#and, or, not
# true and true = true
# true and false = false
# false and true = false
# false and false = false

# true or true = true
# true or false = false
# false or true = false
# false or false = false

print(10 < 100 or 10 == 100)

print(200 >= 100)


age = 18

if age >= 18:
    print("You are eligible to vote.")


    age = 10

if age >= 18:
    print("You are eligible to vote.")

else:
    print("YOu are not eligible to voten")


num1 = 100
num2 = 100

if num1 > num2:
    print('Num 1 is greater that Num 2')
elif num1 == num2: 
    print("Num 1 is equal to Num 2")
else:
    print('Num 2 is greater than Num 1')


mark = 80

if mark >= 90:
    print("A")
elif mark >= 80:
    print("B")
elif mark >= 70:
    print("C")
elif mark >= 60:
    print('D')
else:
    print("F")


n = 7

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

mark = 75 

if mark >= 90:
    print("A")
elif mark >= 80:
    print("B")
elif mark >= 70:
    print("C")
elif mark >= 60:
    print("D")
else:
    print("F")

for i in range(10):
    print("Hello World!")


for i in range(1,25,3):
    print(i * 2)
    if i % 2 == 0:
        print("Even",i)
    else:
        print("Odd", i)


for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            print(i+j)

sum = 0
for i in range(1,100):
    sum = sum + i
print(sum)

for i in range(1,10):
    print(i * i)

n=0
while(n<10):
    print("Hellow World")
    n = n + 1



#def used to define a function def followed by name of function

def add(x,y):
    print(x+y)

add(10,20)
add(20,30)
add(100,200)


def add(x,y):
    return(x+y)
a = add(20,30)

print(a)



def checknumber(q,p):
    if  q == p:
        return q,p
    else:
	    return 0
		
def add(num1, num2):
    e,f = checknumber(num1, num2)
    z = e + f
    return z

def main(x,y):
   a = add(x,y)
   return a

x=main(20,20)