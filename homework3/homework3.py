#Goodbye
def say_goodbye(name):
    print("Goodbye,",name)
say_goodbye("evan")
#Area and Circumference of a Circle
def circle(r):
    area=3.14*r**2
    circumference=2*3.14*r
    print(area)
    print(circumference)
circle(2)
circle(3)
circle(4)
#Subtract
def subtract(a,b):
    return a-b
print(subtract(3,2))
print(subtract(5,7))
#Multiply
def multiply(a,b):
    return a*b
print(multiply(2,3))
print(multiply(17,24))
#Divide
def divide(a,b):
    return a/b
print(divide(10,5))
print(divide(100000,20))
#What to Wear?
def temperature(readings):
    cold=min(readings)
    hot=max(readings)
    return(cold,hot)
readings=[55,60,65,70,75,80,85]
print(temperature(readings))
#Weekend
def is_weekend(day):
    if day == 6 or day == 7:
        return "True :D"
    else: return "False :("
print(is_weekend(6))
print(is_weekend(2))
#fuel efficiency
def fuel_efficiency(d,g):
    return d/g
print(fuel_efficiency(150,2))
#Secret Code
def secret_code(number):
    last=number%10
    remain=number//10
    digits=len(str(number))
    secret=last*10**(digits -1) + remain
    return secret
print(secret_code(12345))
print(secret_code(6789))
#Exponents
def exponent(a,b):
    result=1
    for i in range (b):
             result=result*a
    return result

print(exponent(2,4))
print(exponent(5,6))
print(exponent(3,2))
#min and max
def min_for(numbers):
    smallest=numbers[0]
    for number in numbers:
        if number <smallest:
            smallest=number
    return smallest
numbers=[3,5,1,5,3,4,7,4,3,0]
print(min_for(numbers))
def max_for(numbers):
    largest=numbers[0]
    for number in numbers:
        if number>largest:
            largest=number
    return largest
numbers=[3,5,1,5,3,4,7,4,3,0]
print(max_for(numbers))
#while loops
def min_while(numbers):
    smallest=numbers[0]
    i=0
    while i<len(numbers):
        if numbers[i]<smallest:
            smallest=numbers[i]
        i=i+1
    return smallest
numbers=[3,5,1,5,3,4,7,4,3,0]
print(min_while(numbers))
def max_while(numbers):
    largest=numbers[0]
    i=0
    while i<len(numbers):
        if numbers[i]>largest:
            largest=numbers[i]
        i=i+1
    return largest
numbers=[3,5,1,5,3,4,7,4,3,0]
print(max_while(numbers))
#Calculate the Sum
def calculations(number):
    total=0

    while number>0:
        last_digit=number % 10
        total=total+last_digit
        number=number//10
    return total
print(calculations(2468))
print(calculations(12345))