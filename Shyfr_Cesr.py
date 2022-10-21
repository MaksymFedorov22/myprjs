while True:
    n = input()
    abc = "abcdefghijklmnopqrstuvwxyz"
    abk = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    num = "0123456789"
    res = ""
    key = 1
    for i in n:
        if i in abc:
            if abc.find(i) >= (len(abc) - key):
                res += abc[(0 - len(abc)) + abc.find(i) + key]
            else:
                res += abc[abc.find(i) + key]
        elif i in abk:
            if abk.find(i) >= (len(abk) - key):
                res += abk[(0 - len(abk)) + abk.find(i) + key]
            else:
                res += abk[abk.find(i) + key]
        elif i in num:
            if num.find(i) >= (len(num) - key):
                res += num[(0 - len(num)) + num.find(i) + key]
            else:
                res += num[num.find(i) + key]
        elif i == " ":
            res += " "

    print(res)
