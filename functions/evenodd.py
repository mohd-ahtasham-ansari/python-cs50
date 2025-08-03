def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("the x is EVEN")
    else:
        print("the x is ODD")
        
def is_even(n):
    if n%2==0:
        return True
    else:
        return False 

main()