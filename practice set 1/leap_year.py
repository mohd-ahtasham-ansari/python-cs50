def main():
    year=int(input("what is year"))
    print(is_leap(year))

def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 != 0) or (year % 400 == 0):
            return True
    return False
main()