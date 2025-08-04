def main():
    x= get_int("what is x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("entered input is not an integer")
            #or we can use another keyword : "pass"

main()

    