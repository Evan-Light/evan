# File: homework1.py
# --- Variables and Data Types ---
a = "10"
print(a)
print(type(a)) #a is an integer, a whole number with no decimals
b = 1.5
print(b)
print(type(b)) #b is a float, a fraction or decimal
c = 1.5j
print(c)
print(type(c)) #c is a complex, a number with a real and imaginary part
d = "hello"
print (d)
print(type(d)) #d is a str, words or text
e = [1 , 2, 3]
print(e)
print(type(e)) #e is a list, a way to store multiple items in one variable
f = {"name": "Evan", "favorite fruit": "mango"}
print(f)
print(type(f)) #f is a dict/dictionary, stores information in a key
g = (1, 2)
print(g)
print(type(g)) #g is a tuple, stores multiple items together but cannot be changed after it is made
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is also a list
i = True
print(i)
print(type(i)) #i is a bool/boolean it is either true/false or yes/no conditions
j = None
print(j)
print(type(j)) #j is NoneType, it has no value
k = [True, "blue", 12]
print(k)
print(type(k)) #k is also a list
l = str(14)
print(l)
print(type(l)) #l is a str, words or text
m = 1e4
print(m)
print(type(m)) #m is a float, fractions/decimals
#Data Types (9): Integer, Float, Complex, Str, List, Dict, Tuple, Bool, NoneType
#Variables with same data type: D and L (str), E, H, and K (list), 
#l is a string because str()turns it into one
n = frozenset({1, 2, 3})
print(n)
print(type(n))
print(10>9) #True 10 is greater than 9
print(10==9) #False 10 DNE 9
print(10<=9) #False 10 is not less than or equal to 9
print(bool("abc")) #True
print(bool(["apple", "cherry", "banana"])) #True
print(bool(True)) #True
print(bool(False)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(" ")) #True
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print(bool(True and False)) #False
print(bool(True and True)) #True
print(bool(False and False)) #False
print(bool(True or False)) #True
print(bool(True or True)) #True
print(bool(False or False)) #False
print(bool(not(False))) #True
print(bool(not(True))) #False
#Pattern: strings are true, if it is completely empty it is false. For and, both must be true, for or, one must be true
#I am surprised that the empty space came back as true
print(bool("2+2==4"))
#This came back true
print(bool("2+3+1==11"))
#This also came back true, but its because the quotation marks sees it as a string
print(bool(2+3==4))
#This came back false because I didn't use quotation marks so it checks the math
print(10+5) #15 + performs addition
print(10-5) #5 - performs subtraction
print(6/3) #2.0 / performs division
print(5%2) #1 % gives the remaineder
print (3**2) #** performs exponents
print(15//2) #// gives whole number and drops remainder
print(5==2) #False 5 DNE 2
print(10 !=10) #False != means not equal to
print(2<5) #True 2 is less than 5
print(12>5) #True 12 is greater than 5
print(5<=6) #True, 5 is less than or equal to 6
print(1>=10) #False 1 is not greater than or equal to 10
x=5
x+=5
print(x) #x=10, x+5
x-=4
print(x) #x=6, 10-4=6
x*=3
print(x) #=18, 6 times 3 =18
#and operator tells you both must be true
print(2+2==4 and 3+3==6) #True
print(2+4==6 and 4-3==3) #False
#or operator tells you at least one must be true
print(3**3==27 or 3**3==26) #True
print(3+3==5 or 2+2==3) #False
# / performs division and // also performs addition but as a whole number answer only
# % only gives you the remainer from division // does division but only the whole number
# to calculate the raminder I would use %
print(255%2) #1, remainder 1
#Assignment operators give a varaible a value/change its value, basically math.
my_string= "hello"
print(my_string) #Prints: hello
print(my_string[0]) #Prints: h
print(my_string[1]) #Prints: e
print(my_string[2]) #Prints: l
print(my_string[3]) #Prints: l
print(my_string[4]) #Prints: o
print(my_string[-1]) #Prints: o
print(my_string[1:3]) #Prints: el
print(my_string[0:5:2]) #Prints: hlo
print(len(my_string)) #Prints: 5
print(my_string + "goodbye") #Prints: hellogoodbye
print(my_string*7) #Prints: hellohellohellohellohellohellohello
#slicing means to take a slice of a phrase. I used this to just take one letter or combinations like h or hlo etc
name = "Oski"
print("hello, my name is", name) #Prints: hello, my name is Oski
print(f"hello, my name is {name}") #Prints: hello, my name is Oski
#f strings are formatted string and are ways to put variables/calculations inside of a string
#the first one seperates things with a , and the second seperates things with f string {name} gets replaced with Oski
#cd
#changes from directory to another
#ex: cd desktop
#ls
#lists the files and folders inside the directory that you're in
#ls -a
#lists everything in the current folder, the -a means all
#mkdir
#makes a directory
#ex: mkdir homework1
#cat
#shows contents of a file
#ex: cat homework1.py
#pwd
#print working directory. tells you what folder you are in
#cd ..
#go back one folder. Went from homework1 to evan
#cd .
#changes directories to the one you're in... seems useless
#cd ~
#change to home directory
#cp
#copy, makes a copy of a file/folder. make sure you're in the spot you want to copy. write cp the one you're in name of new copy
#cp homework1.py homework1_copy.py
#mv
#moves to a file/folder or rename a file
#ex: mv homework1_copy.py homework1_copy2.py
#rm
#removes a file
#ex: rm homework1 (dont test it)
#clear
#clears up terminal screen
#grep
#searches for text inside a file
#ex: "Oski" homework1.py
#whoami
#tells you who you are
#date
#says the date and time
#tail
#shows the end of file
#ex: tail homework1
#differnece between ls and ls -a is that ls -a shows all files even hidden ones
#a hidden file is a file that exists on computer but not normally shown through folders
#ls -l
#tells how many and extra info
#ls -h
#human readable files
#ls -t
#sorts files by time
