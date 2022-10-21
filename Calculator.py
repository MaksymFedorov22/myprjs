import math

print("    You started the calculator \n \n    Type Help to get instruction or Exit to stop the program")
res = 0.0
opp = ""
while True:
    n = input("::>")
    if "exit" == n.lower():
        break
    elif "stop" == n.lower():
        res = 0.0
        opp = ""
        continue
    elif "help" == n.lower():
        print("    To start using the calculator you need to enter an integer,\n then enter the operation (+, -, *, /, ^, sqrt; you can do this many times) and when you need the result,\n enter the operation f= (for float resul) or i= (for integer).\n \n   If you entered something incorrectly, enter Stop \n   If you need to finish working with the calculator, enter Exit")
        continue
    elif "pi" == n.lower():
        print(math.pi, "\nU have found the secret func of the calc")
        continue

    if n != "":
        if n == "+":
            opp = "+"
        elif n == "-":
            opp = "-"
        elif n == "*":
            opp = "*"
        elif n == "/":
            opp = "/"
        elif n == "^":
            opp = "^"
        elif n == "sqrt":
            res = math.sqrt(res)
            print("<::", float(res))
            res = 0.0
            opp = ""

        elif n == "f=" or n == "=":
            print("<::", float(res))
            res = 0.0
            opp = ""
        elif n == "i=":
            print("<::", int(res))
            res = 0.0
            opp = ""

        elif opp == "":
            res = float(n)
        elif opp == "+":
            res += float(n)
        elif opp == "-":
            res -= float(n)
        elif opp == "*":
            res *= float(n)
        elif opp == "/":
            res /= float(n)
        elif opp == "^":
            res0 = res
            for i in range(1, int(n)):
                res *= res0
        else:
            print("<::ERR")
            continue
    else:
        print("<::ERR")
        continue
print("\nYou exited the calculator that was made by Fedorov Maksym\n")
print("ez"+"\nP.S. This string (^) was printed by Shcherbyna Andriy")
