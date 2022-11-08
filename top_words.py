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
    return word, cnt

##########

while True:
    mText = input("Введіть текст: ").split()

    z = input("Введіть що зробити A B C exit: ")

    if z.lower() == "a":
        print("топ 5 що повторюються:")
        for i in range(5):
            p1, p2 = most_frequent(mText)
            print(p1, p2)

    elif z.lower() == "b":
        mText = set(mText)
        mText = list(mText)
        mText.sort()
        print("словник:")
        for i in range(len(mText)):
            if len(mText[i]) > 3:
                print(mText[i])

    elif z.lower() == "c":
        mText = set(mText)
        mText = list(mText)
        mText.sort(reverse = True, key = len)
        print("топ 5 найдовших:")
        for i in range(5):
            print(mText[i], len(mText[i]))

    elif z.lower() == "exit":
        break

    else:
        print("Такого завдання не існує")
