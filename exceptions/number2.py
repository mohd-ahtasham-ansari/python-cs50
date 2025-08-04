while True:
    try:
        x=int(input("what is x? "))
        break
    except ValueError:
        print("x is not an integer")
    
print(f"x is {x}")
 