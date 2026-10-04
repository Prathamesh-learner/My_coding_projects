import math

def solve():
    if (b**2) - (4*a*c) < 0:
        print("\nThere are no real solutions to this equation")
        solution1 = (-b + math.sqrt( (b**2) -(4*a*c) )) / (2*a) 
        solution2 = (-b - math.sqrt( (b**2) -(4*a*c) )) / (2*a)
        print("\nThe imaginary solutions are")
    
    elif (b**2) - (4*a*c) == 0:
        print(f"\nThe solution and x coordinate of vertex to your equation is: '{(-b)/(2*a)}'")
    
    elif (b**2) - (4*a*c) > 0:
        solution1 = (-b + math.sqrt( (b**2) - (4*a*c) )) / (2*a) 
        solution2 = (-b - math.sqrt( (b**2) - (4*a*c) )) / (2*a) 
        print(f"\nThe solutions to your equation are: {solution1} and {solution2}")

def vertex():
    h = -(b/(2*a))
    k = (a*(h**2)) + (b*h) + c
    print(f"\nthe vertex of your equation is ({h},{k})")

def value_error(self):
    try:
        int(self)
    except ValueError:
        return False
    else:
        return True
    
def standard_form():
    print()
    print()
    if a == 0:
        print("your equation is not a quadratic as the a in your equation is 0")
    elif a == 1:
        if b == 1:
            if c == 0:
                print(f"Your equation in standard form is:\nx^2 +x")
            elif c < 0:
                print(f"Your equation in standard form is:\nx^2 +x {c}")
            elif c > 0:
                print(f"Your equation in standard form is:\nx^2 +x +{c}")  
        elif b > 0:
            if c == 0:
                print(f"Your equation in standard form is:\nx^2 +{b}x")
            elif c < 0:
                print(f"Your equation in standard form is:\nx^2 +{b}x {c}")
            elif c > 0:
                print(f"Your equation in standard form is:\nx^2 +{b}x +{c}")      
        elif b < 0:
            if c == 0:
                print(f"Your equation in standard form is:\nx^2 {b}x")
            elif c < 0:
                print(f"Your equation in standard form is:\nx^2 {b}x {c}")
            elif c > 0:
                print(f"Your equation in standard form is:\nx^2 {b}x +{c}")
        elif b == 0:
            if c == 0:
                print(f"Your equation in standard form is:\nx^2")
            elif c < 0:
                print(f"Your equation in standard form is:\nx^2 {c}")
            elif c > 0:
                print(f"Your equation in standard form is:\nx^2 +{c}")

    else:
        if b == 1:
            if c == 0:
                print(f"Your equation in standard form is:\n{a}x^2 +x")
            elif c < 0:
                print(f"Your equation in standard form is:\n{a}x^2 +x {c}")
            elif c > 0:
                print(f"Your equation in standard form is:\n{a}x^2 +x +{c}")  
        elif b > 0:
            if c == 0:
                print(f"Your equation in standard form is:\n{a}x^2 +{b}x")
            elif c < 0:
                print(f"Your equation in standard form is:\n{a}x^2 +{b}x {c}")
            elif c > 0:
                print(f"Your equation in standard form is:\n{a}x^2 +{b}x +{c}")      
        elif b < 0:
            if c == 0:
                print(f"Your equation in standard form is:\n{a}x^2 {b}x")
            elif c < 0:
                print(f"Your equation in standard form is:\n{a}x^2 {b}x {c}")
            elif c > 0:
                print(f"Your equation in standard form is:\n{a}x^2 {b}x +{c}")
        elif b == 0:
            if c == 0:
                print(f"Your equation in standard form is:\n{a}x^2")
            elif c < 0:
                print(f"Your equation in standard form is:\n{a}x^2 {c}")
            elif c > 0:
                print(f"Your equation in standard form is:\n{a}x^2 +{c}")
    
def error_check():
    pass   

while True:
    print("\nWelcome to the quadratic equation solver")
    form = input("Choose which form you quadratic equation is in\nIf standard form enter 's'\nIf vertex form enter 'v'\nIf factored form enter 'f'\n")
  
    if form == 's': #or 'S' or 'Standard' or 'standard' or 'standard form' or 'Standard form'
        a = input("\nEnter the a of your equation\n")
        b = input("\nEnter the b of your equation\n")
        c = input("\nEnter the c of your equation\n")

        if value_error(a) == False:
            print(f"please enter a numerical value for a")        
        elif value_error(a) == True:
            a = int(a)
        if value_error(b) == False:
            print(f"please enter a numerical value for b")  
        elif value_error(b) == True:
            b = int(b)
        if value_error(c) == False:
            print(f"please enter a numerical value for c")
        elif value_error(c) == True:
            c = int(c)
        
        vertex()
        solve()
        # try:
        #     int(a)
        # except ValueError:
        #     print("please enter a numerical value")
        #     break
        # else:
        #     a = int(a)

    elif form == 'v': #or 'V' or 'Vertex form' or 'vertex form' or 'vertex' or 'Vertex':
        h = input("Enter the h of the equation or the x of the vertex\n")
        k = input("Enter teh k of the equation or the y of the vertex\n")
        a = input("Enter the a of this equation\n")

        if value_error(a) == False:
            print(f"please enter a numerical value for a")        
        elif value_error(a) == True:
            a = int(a)
        if value_error(h) == False:
            print(f"please enter a numerical value for h")  
            break
        elif value_error(h) == True:
            h = int(h)

        if value_error(k) == False:
            print(f"please enter a numerical value for k")
            break
        elif value_error(k) == True:
            k = int(k)
        
        b = -h*2*a
        c = (((-h)**2)*a) + k

        standard_form()
        print(f"the vertex of your equation is ({h},{k})")
        solve()
        # if c < 0:
        #     print(f"Your equation in standard form is:\n{a}x^2 {b}x {c}")
        # elif c == 0:
        #     print(f"{a}x^2 {b}x")
        # elif c > 0:
        #     print(f"Your equation in standard form is:\n{a}x^2 {b}x +{c}")

        # vertex form is a*(x-h)^2 + k
    elif form == 'f':
        a = int(input("Enter the a of this equation\n"))
        p = int(input("Enter the p of this equation\n"))
        q = int(input("Enter the q of this equation\n"))

        if value_error(a) == False:
            print(f"please enter a numerical value for a")        
            break
        elif value_error(a) == True:
            a = int(a)
        if value_error(b) == False:
            print(f"please enter a numerical value for p")  
            break
        elif value_error(b) == True:
            p = int(b)
        if value_error(c) == False:
            print(f"please enter a numerical value for q")
            break
        elif value_error(c) == True:
            q = int(c)

        b = ((-p)+(-q))*a
        c = ((-p)*(-q))*a

        standard_form()
        vertex()
        solve()

    else:
        print("Invalid form chosen\nplease try again")
