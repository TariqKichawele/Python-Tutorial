def hello_world():
    print("Hello World!")

hello_world()

def sum(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        return
    return(num1 + num2)

total = sum(4, 2)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items('Dave', 'john', 'sara')

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="dave", last="gray")