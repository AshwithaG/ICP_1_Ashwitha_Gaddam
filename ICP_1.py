def prog_1_string():
    string = input("Enter a string: ")[::-1]
    print('\n' + string[2:])


def prog_1_list():
    list_string = list(input("Enter a string: ")[::-1])
    print('\n' + ''.join(list_string)[2:])


def prog_2():
    list_string = (input("Enter a sentence containing word python: ")).split() #I love playing with python
    for i in range(len(list_string)):
        if list_string[i] == "python":
            list_string[i] = "pythons"
    print('\n' + ' '.join(list_string))


def prog_3():
    score = int(input("Enter class score between 1 to 100: "))
    if 90 <= score <= 100:
        print("Grade : A")
    elif 80 <= score <= 89:
        print("Grade : B")
    elif 70 <= score <= 79:
        print("Grade : C")
    elif 60 <= score <= 69:
        print("Grade : D")
    elif 0 <= score <= 59:
        print("Grade : E")
    else:
        print("Please enter a valid score!")
