from math import pi 
print(pi)

print(f"Co chesz obliczyc? a - bryly ,b - figuty plaskie")
inp = input(": ").lower()
if inp == "a":
    print(f"wybierz a - Pc brył, b - objetosci")
    inp = input(": ").lower()
    if inp == "a":
        print(f"Wybierz bryłe: a-sześcian b-prostopadłościan c-graniastosłup d-ostrosłup e-Walec f-stożek g-Kula")
        inp = input(": ").lower()
        if inp == "a":
            a = float(input("Wpisz krawędź sześcianu a: "))
            print(f"Pole powierzcni całkowitej sześcianu o krawędzi {a} jest równe {6*a*a}")
        elif inp == "b":
            a = float(input("Wpisz krawędź prostopadłościanu a:"))
            b = float(input("Wpisz krawędź prostopadłościanu b:"))
            c = float(input("Wpisz krawędź prostopadłościanu c:"))
            print(f"Pole powierzchni całkowitej prostopadłościanu o krawędziach {a}, {b} i {c} jest równe {2*(a*b + b*c + a*c)}")
        elif inp == "c":
            a = float(input("Wpisz pole podstawy graniastosłupa a: "))
            b = float(input("Wpisz pole boczne graniastosłupa b: "))
            print(f"Pole powierzchni całkowitje graniastosłupa wynosi {2*a + b}")
        elif inp == "d":
            a = float(input("Wpisz pole podstawy ostrosłupa a:"))
            b = float(input("Wpisz pole boczne ostrosłupa b:"))
            print(f"Pole powierzcni całkowitej ostrosłupa wynosi {a + b}")
        elif inp == "e":
            a = float(input("Wpisz wysokość walca H: "))
            b = float(input("Wpisz promien podstawy walca r: "))
            print(f"Pole powierzcni całkowitej wynosi {(2*pi*b*b) + (2*pi*b*a)}")
        elif inp == "f":
            a = float(input("Wpisz długość tworzącej stożka l: "))
            b = float(input("Wpisz promień podstawy stożka r: "))
            print(f"Pole powierzchni całkowitej stożka wynosi {(pi*b*b) + (pi*b*a)}")
        elif inp == "g":
            a = float(input("Wpisz promień kuli r: "))
            print(f"Pole powierzchni całkowitej kuli z promieniem {a} wynosi {4*pi*a*a}")
        else:
            print("Nie ma takiej komendy")
    elif inp == "b":
        print(f"Wybierz bryłe: a-sześcian b-prostopadłościan c-graniastosłup d-ostrosłup e-Walec f-stożek g-Kula")
        inp = input(": ").lower()
        if inp == "a":
            a = float(input("Wpisz krawędź sześcianu a: "))
            print(f"Objętość sześcianu o krawędzi {a} wynosi {a*a*a}")
        elif inp == "b":
            a = float(input("Wpisz krawędź prostopadłościanu a:"))
            b = float(input("Wpisz krawędź prostopadłościanu b:"))
            c = float(input("Wpisz krawędź prostopadłościanu c:"))
            print(f"Objętość prostopadłościanu o krawędziach {a} {b} i {c} wynosi {a*b*c}")
        elif inp == "c":
            a = float(input("Wpisz pole podstawy graniastosłupa pp: "))
            b = float(input("Wpisz wysokość graniastosłupa H: "))
            print(f"Objętośc graniastosłupa wynosi {a*b}")
        elif inp == "d":
            a = float(input("Wpisz pole podstawy ostrosłupa pp: "))
            b = float(input("Wpisz wysokość ostrosłupa H: "))
            print(f"Objętość ostrosłupa wynosi {(a*b)/3}")
        elif inp == "e":
            a = float(input("Wpisz promień podstawy walca r: "))
            b = float(input("Wpisz wysokość walca H:"))
            print(f"Objętość walca wynosi {pi*a*a*b}")
        elif inp == "f":
            a = float(input("Wpisz promień podstawy stożka r: "))
            b = float(input("Wpisz wysokość stożka H: "))
            print(f"Objętośc stożka wynosi {pi*a*a*b*(1/3)}")
        elif inp == "g":
            a = float(input("Wpisz promień kuli r: "))
            print(f"Objętość kuli wynosi {pi*a*a*a*(4/3)}")
        else:
            print("Nie ma takiej komendy")
    else:
        print("nie ma takiej komendy")   

elif inp == "b":
    print(f"a - obwody figur, b - PP figut")
    inp = input(": ").lower()
    if inp == "a":
        print("Wybierz figure: a-kwadrat b-prostokąt c-równoległoboku d-trapez e-trójkąt f-koło g-romb")
        inp = input(": ").lower()
        if inp == "a":
            a = float(input("Wpisz bok kwadratu: "))
            print(f"obwód kwadratu wynosi {a*4}")
        elif inp == "b":
            a = float(input("wpisz bok prostokątu a: "))
            b = float(input("wpisz bok prostokątu b: "))
            print(f"obwód ptostokątu wynosi {2*a + 2*b}")
        elif inp == "c":
            a = float(input("wpisz bok równoległobboku a: "))
            b = float(input("wpisz bok równoległobboku b: "))
            print(f"obwód równoległoboku wynosi {2*a + 2*b}")
        elif inp == "d":
            a = float(input("wpisz bok trapezu a: "))
            b = float(input("wpisz bok trapezu b: "))
            c = float(input("wpisz bok trapezu c: "))
            d = float(input("wpisz bok trapezu d: "))
            print(f"obwód trapezu wynosi {a + b + c + d}")
        elif inp == "e":
            a = float(input("wpisz bok trójkąta a: "))
            b = float(input("wpisz bok trójkąta b: "))
            c = float(input("wpisz bok trójkąta c: "))
            print(f"obwód trójkąta wynosi {a + b + c}")
        elif inp == "f":
            a = float(input("wpisz promień koła"))
            print(f"obwód koła wynosi {2*pi*a}")
        elif inp == "g":
            a = float(input("wpisz bok rombu a:"))
            print(f"obwód rombu wynosi {a*4} ")
        else:
            print("nie ma takiej komendy")
    elif inp == "b":
        print("Wybierz figure: a-kwadrat b-prostokąt c-równoległoboku d-trapez e-trójkąt f-koło g-romb")
        inp = input(": ").lower()
        if inp == "a":
            a = float(input("wpisz bok kwadratu a: "))
            print(f"pole kwadratu wynosi {a*a}")
        elif inp == "b":
            a = float(input("wpisz bok prostokąta a:"))
            b = float(input("wpisz bok prostokąta b:"))
            print(f"pole prostokątu wynosi {a*b}")
        elif inp == "c":
            a = float(input("wpisz długość podstawy równoległoboku a: "))
            b = float(input("wpisz wysokość równoległoboku h: "))
            print(f"pole równoległoboku wynosi {a*h}")
        elif inp == "d":
            a = float(input("wpisz górną podstawę trapezu a: "))
            b = float(input("wpisz dolną podstawę trapezu b: "))
            c = float(input("wpisz wysokość trapezu h: "))
            print(f"pole trapezu wynosi {((a+b)*c)/2}")
        elif inp == "f":
            pass
        elif inp == "g":
            pass
        else:
            print("nie ma takiej komendy")
    else:
        print("nie ma takiej komendy")
else:
    print("nie ma takiej komendy")