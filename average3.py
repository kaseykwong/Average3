def main():
    sum1 = add_three(1,1,10)
    divide_three(sum1)

def add_three(v1,v2,v3):
    """ Adds the three numbers
    """
    p = v1 + v2 + v3
    print("The sum of the three numbers is: {}".format(p))
    return p

def divide_three(sum1):
    """ Divides the result of add_three
    """
    p = sum1 / 3
    print("The average of the three numbers is: {}".format(p))

if __name__ == "__main__":
    main()
