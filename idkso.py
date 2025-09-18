# for number in range (3,11):     
#     print(number)

# letters = ['a','b','c']

# def print_abcs():
#     for letter in letters:
# print_abcs(letter)

var1 = "hello"

def my_function(var):
    global var1
    var1 = "goodbye"
    return 4

var1 = my_function(var1)
print(var1)