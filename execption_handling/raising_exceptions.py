def enterage(age):
    if age < 0:
        raise ValueError("Only positive integer are allowed")
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")


try:
    num = -5
    enterage(num)
except ValueError:
    print("only positive integers are allowed")
except:
    print("something is worng")
