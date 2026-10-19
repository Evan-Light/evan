#3.1
fav_foods=["mac and cheese","pizza","burriots","ice cream","cookies"]
print(fav_foods[1]) 
#I encountered error: print(fav_foods(1)) TypeError: 'list' object is not callable.
#I needed to use [] instead of ()
print(fav_foods[-1])
fav_foods.append("milkshake")
fav_foods.insert(0, "apple")
del fav_foods[2]
print(len(fav_foods))
for food in fav_foods:
    print(food.upper())
first_last=fav_foods[:1]+fav_foods[-1:]
print(first_last)
#  first_last=fav_foods[:1]+fav_foods[-1] TypeError: can only concatenate list (not "str") to list
#I forgot the : after -1
if "potato" in fav_foods:
    print("A potato!")
else:
    print("No potato :(")
#3.2
numbers=list(range(21))
print(numbers)
def get_first_15(numbers):
    return numbers[:15]
step1=get_first_15(numbers)
print(step1)
def get_every_5th(lst):
    return lst[::5]
step2=get_every_5th(step1)
print(step2)
#SyntaxError: invalid syntax
#I thought it was a 1 not an l
def reverse_and_stride(lst):
    reversed_list=lst[::-1]
    return reversed_list[::3]
step3=reverse_and_stride(step2)
print(step3)
#3.3
numbers=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])
def sum_nested(numbers):
    total=0
    for row in numbers:
        for num in row:
            total+=num
    return total
print(sum_nested(numbers))
#3.4
def create_5x5():
    grid=[]
    num=1
    for row in range(5):
        new_row=[]
        for col in range(5):
            new_row.append(num)
            num+=1
        grid.append(new_row)
    return grid
grid=create_5x5()
print(grid)
def replace_multiples_of_3(grid):
    for row in range(5):
        for col in range(5):
            if grid[row][col]%3==0:
                grid[row][col]="?"
    return grid
updated_grid=replace_multiples_of_3(grid)
print(updated_grid)
def sum_grid(grid):
    total=0
    for row in grid:
        for num in row:
            if num !="?":
                total += num
    return total
final_sum=sum_grid(updated_grid)
print(final_sum)
#IndentationError: expected an indented block. I didnt indent correctly
#4.1
ages={
    "Katie":30,
    "Mariam":42,
    "Safia":25,
    "Mira":48
}
print(ages["Katie"])
ages["Mira"]=100
print(ages["Mira"])
ages["Milana"]=52
print(ages["Milana"])
del ages["Mariam"]
print(ages)
for name, age in ages.items():
    print(name,age)
#5.2
print(sum_grid(updated_grid))