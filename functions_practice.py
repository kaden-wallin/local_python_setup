def hello():
    print("Hello, User")

def pack(item1, item2, item3):
    lunch = []
    lunch.add(item1, item2, item3)
    print(lunch)

def eat_lunch(a_list):
    for i in a_list:
        if i == a_list[0]:
            print("first I eat", i)
        elif i == a_list[1]:
            print("next I eat", i)
        else:
            print("then I eat", i)

def arb_args(*args):
    for i in args:
        print(i)

def inner_func(int_1, int_2):
    def divide():
        return int_1 / int_2
    def modulus():
        return int_1 % int_2
    print(divide() + modulus())

def lunch_lady(kid, meat="Mystery Meat"):
    print("Student:", kid + ", Meat Preference:", meat)

def sum_n_product(a, b):
    sum = a + b
    product = a * b
    print(sum, product)

alias_arb_args = arb_args

def arb_mean(*args):
    total = 0
    for i in args:
        total += i
    print(i/len(args))

def arb_longest_string(*args):
    long = 0
    longest = ""
    for i in args:
        if len(i) > long:
            long = len(i)
            longest = i
    print(longest)

def name_args(**kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])

def all_true(itr):
    return all(itr)

# all_true = lambda itr: all(itr)

# print(all_true([1, 2, True, 0]))

def one_true(itr):
    return any(itr)

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
    
def set_recursive_deduplicate(str):
    return "".join(set(str))

def recursive_reverse(string, i=0):
    if i == len(string) - 1:
        return string[0]
    else:
        return string[-1-i] + recursive_reverse(string, i+1)
    
