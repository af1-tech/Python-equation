print("Ecuation and inequalities ver 1.0")
import math

loop1 = 10
optiune1 = 10


def ecgr1():
    a = 0
    b = 0
    c = 0
    x = 0
    z = 1
    while z != 0:
        a = float(input("Input a: "))
        if a == 0:
            print("The value of 'a' must be different from zero!")
        elif a != 0:
            z = 0;
    b = float(input("Input b: "))
    c = float(input("Input c: "))
    x = (c - b) / a
    return (x)


def ecgr2():
    a = 0
    b = 0
    c = 0
    d = 0
    delta = 0
    x1 = 0
    x2 = 0
    z = 1
    deltac = 0
    xa = 0
    xb = 0
    while z != 0:
        a = float(input("Input a: "))
        if a == 0:
            print("The value of 'a' must be different from zero!")
        elif a != 0:
            z = 0;
    b = float(input("Input b: "))
    c = float(input("Input c: "))
    d = float(input("Input d: "))
    delta = ((b * b) - 4 * a * (c - d))
    if delta >= 0:
        x1 = (-1 * b - math.sqrt(delta)) / (2 * a)
        x2 = (-1 * b + math.sqrt(delta)) / (2 * a)
    elif delta < 0:
        deltac = -1 * delta
        xa = (-1 * b) / (2 * a)
        xb = (math.sqrt(deltac)) / (2 * a)
    return (delta, x1, x2, xa, xb)


while loop1 != 0:
    print("Choose an option: ")
    print("1) Ecuations")
    print("2) Inequalities")
    print("0) Exit")
    optiune1 = int(input("Input the selected option: "))
    if optiune1 == 1:
        loop2 = 10
        optiune2 = 10
        while loop2 != 0:
            print("1) First degree ecuation")
            print("2) Second degree ecuation")
            print("0) Exit")
            optiune2 = int(input("Input the selected option: "))
            if optiune2 == 1:
                print("Model: aX + b = c")
                print("X = ", ecgr1())
            elif optiune2 == 2:
                print("Model: aX", str(chr(178)), " + bX + c = d")
                delta, x1, x2, xa, xb = ecgr2()
                if delta < 0:
                    print("The equation has no solutions in the set of real numbers (R)")
                    print("X1 = ", xa, " - ", xb, "i")
                    print("X2 = ", xa, " + ", xb, "i")
                elif delta >= 0:
                    print("delta este:", delta)
                    print("X1 = ", x1)
                    print("X2 = ", x2)
            elif optiune2 == 0:
                loop2 = 0


    elif optiune1 == 2:
        loop3 = 10
        optiune3 = 10
        while loop3 != 0:
            print("1) First degree inequality")
            print("2) Second degree inequality")
            print("0) Exit")
            optiune3 = int(input("Input the selected option: "))
            if optiune3 == 1:
                loop4 = 10
                optiune4 = 10
                while loop4 != 0:
                    print("1) Model aX + b < c")
                    print("2) Model aX + b <= c")
                    print("3) Model aX + b >= c")
                    print("4) Model aX + b > c")
                    print("0) Iesire")
                    optiune4 = int(input("Input the selected option: "))
                    if optiune4 == 1:
                        print("x belongs to the range ( - inf , +", ecgr1(), " )")
                    elif optiune4 == 2:
                        print("x belongs to the range ( - inf , +", ecgr1(), " ]")
                    elif optiune4 == 3:
                        print("x belongs to the range [ ", ecgr1(), " , inf )")
                    elif optiune4 == 4:
                        print("x belongs to the range ( ", ecgr1(), " , inf )")
                    elif optiune4 == 0:
                        loop4 = 0

            elif optiune3 == 2:
                loop5 = 10
                optiune5 = 10
                while loop5 != 0:
                    print("1) Model aX", str(chr(178)), " + bX +c < d")
                    print("2) Model aX", str(chr(178)), " + bX +c <= d")
                    print("3) Model aX", str(chr(178)), " + bX +c >= d")
                    print("4) Model aX", str(chr(178)), " + bX +c > d")
                    print("0) Iesire")
                    optiune5 = int(input("Input the selected option: "))
                    if optiune5 == 1:
                        delta, x1, x2 = ecgr2()
                        if delta < 0:
                            print("The inequality has no solutions in the set of real numbers (R)")
                        elif delta >= 0:
                            print("x belongs to the range ( ", x1, " , ", x2, " )")
                    elif optiune5 == 2:
                        if delta < 0:
                            print("The inequality has no solutions in the set of real numbers (R)")
                        elif delta >= 0:
                            print("x belongs to the range [ ", x1, " , ", x2, " ]")
                    elif optiune5 == 3:
                        if delta < 0:
                            print("The inequality has no solutions in the set of real numbers (R)")
                        elif delta >= 0:
                            if x1 <= x2:
                                print("x belongs to the range ( - inf, ", x1, "] U [ ", x2, " )")
                            elif x1 > x2:
                                print("x belongs to the range ( - inf, ", x2, "] U [ ", x1, " )")
                    elif optiune5 == 4:
                        if delta < 0:
                            print("The inequality has no solutions in the set of real numbers (R)")
                        elif delta >= 0:
                            if x1 <= x2:
                                print("x belongs to the range ( - inf, ", x1, ") U ( ", x2, " )")
                            elif x1 > x2:
                                print("x belongs to the range ( - inf, ", x2, ") U ( ", x1, " )")
                    elif optiune5 == 0:
                        loop5 = 0

            elif optiune3 == 0:
                loop3 = 0

    elif optiune1 == 0:
        loop1 = 0
        print("Goodbye!")