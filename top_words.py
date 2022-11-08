def most_frequent(List):
    cnt = 0
    word = ""
    for i in List:
        cur = List.count(i)
        if(cur > cnt) and (len(i) > 3):
            cnt = cur
            word = i

    for i in range(List.count(word)):
        mText.remove(word)
    return word

##########

while True:
    mText = input("Введіть текст: ").split()

    z = input("Введіть що зробити A B C exit: ")

    if z.lower() == "a":
        for i in range(5):
            print(most_frequent(mText))

    elif z.lower() == "b":
        mText.sort()
        for i in range(len(mText)):
            print(mText[i])

    elif z.lower() == "c":
        mText = set(mText)
        mText = list(mText)
        mText.sort(reverse = True, key = len)
        for i in range(5):
            print(mText[i])

    elif z.lower() == "exit":
        break

    else:
        print("Такого завдання не існує")
