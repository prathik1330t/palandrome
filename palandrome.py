import sys

def palandrome(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    if s == rev:
        return "Palandrome"
    else:
        return "Not palandrome"


if __name__ == "__main__":
    print("=== Palandrome ===")
    try:
        if len(sys.argv) == 2:
            # Case 1: Argument passed
            s = sys.argv[1]
        else:
            # Case 2: Console input
            s = input("Enter value: ")

        print("=== Program parameters ===")
        print("Input value :", s)

        # Print the result
        print(palandrome(s))

    except ValueError:
        print("Invalid input! Please enter valid values.")

