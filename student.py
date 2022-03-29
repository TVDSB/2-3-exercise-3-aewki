def main():
    #your code goes here
    X = input()
    Y = int(X)
    if Y %3 == 0 and Y %5 == 0:
        print("fizzbuzz")
    elif Y %3 == 0:
        print("fizz")
    elif Y %5 == 0:
        print("buzz")
    else:
        print(Y)

if __name__ =='__main__':
    main()
