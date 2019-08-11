print("Ecuatii si inecuatii ver 1.0")
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
        a = float(input("Introduceti pe a: "))
        if a == 0:
            print("Valoarea lui a trebuie sa fie diferita de zero!")
        elif a != 0:
            z = 0;
    b = float(input("Introduceti pe b: "))
    c = float(input("Introduceti pe c: "))
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
        a = float(input("Introduceti pe a: "))
        if a == 0:
            print("Valoarea lui a trebuie sa fie diferita de zero!")
        elif a != 0:
            z = 0;
    b = float(input("Introduceti pe b: "))
    c = float(input("Introduceti pe c: "))
    d = float(input("Introduceti pe d: "))
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
    print("Alege o optiune: ")
    print("1) Ecuatii")
    print("2) Inecuatii")
    print("0) Iesire")
    optiune1 = int(input("Introduceti optiunea: "))
    if optiune1 == 1:
        loop2 = 10
        optiune2 = 10
        while loop2 != 0:
            print("1) Ecuatii de gradul I")
            print("2) Ecuatii de gradul II")
            print("0) Iesire")
            optiune2 = int(input("Introduceti optiunea: "))
            if optiune2 == 1:
                print("Model: aX + b = c")
                print("X = ", ecgr1())
            elif optiune2 == 2:
                print("Model: aX", str(chr(178)), " + bX + c = d")
                delta, x1, x2, xa, xb = ecgr2()
                if delta < 0:
                    print("Ecuatia nu are solutii care sa apartina multimii numerelor reale (R)")
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
            print("1) Inecuatii de gradul I")
            print("2) Inecuatii de gradul II")
            print("0) Iesire")
            optiune3 = int(input("Introduceti optiunea: "))
            if optiune3 == 1:
                loop4 = 10
                optiune4 = 10
                while loop4 != 0:
                    print("1) Model aX + b < c")
                    print("2) Model aX + b <= c")
                    print("3) Model aX + b >= c")
                    print("4) Model aX + b > c")
                    print("0) Iesire")
                    optiune4 = int(input("Introduceti optiunea: "))
                    if optiune4 == 1:
                        print("x apartine intervalului ( - inf , +", ecgr1(), " )")
                    elif optiune4 == 2:
                        print("x apartine intervalului ( - inf , +", ecgr1(), " ]")
                    elif optiune4 == 3:
                        print("x apartine intervalului [ ", ecgr1(), " , inf )")
                    elif optiune4 == 4:
                        print("x apartine intervalului ( ", ecgr1(), " , inf )")
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
                    optiune5 = int(input("Introduceti optiunea: "))
                    if optiune5 == 1:
                        delta, x1, x2 = ecgr2()
                        if delta < 0:
                            print("Inecuatia nu are solutii care sa apartina multimii numerelor reale (R)")
                        elif delta >= 0:
                            print("x apartine intervalului ( ", x1, " , ", x2, " )")
                    elif optiune5 == 2:
                        if delta < 0:
                            print("Inecuatia nu are solutii care sa apartina multimii numerelor reale (R)")
                        elif delta >= 0:
                            print("x apartine intervalului [ ", x1, " , ", x2, " ]")
                    elif optiune5 == 3:
                        if delta < 0:
                            print("Inecuatia nu are solutii care sa apartina multimii numerelor reale (R)")
                        elif delta >= 0:
                            if x1 <= x2:
                                print("x apartine intervalului ( - inf, ", x1, "] U [ ", x2, " )")
                            elif x1 > x2:
                                print("x apartine intervalului ( - inf, ", x2, "] U [ ", x1, " )")
                    elif optiune5 == 4:
                        if delta < 0:
                            print("Inecuatia nu are solutii care sa apartina multimii numerelor reale (R)")
                        elif delta >= 0:
                            if x1 <= x2:
                                print("x apartine intervalului ( - inf, ", x1, ") U ( ", x2, " )")
                            elif x1 > x2:
                                print("x apartine intervalului ( - inf, ", x2, ") U ( ", x1, " )")
                    elif optiune5 == 0:
                        loop5 = 0

            elif optiune3 == 0:
                loop3 = 0

    elif optiune1 == 0:
        loop1 = 0
        print("La revedere!")