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