s = input("Enter text: ")

rev = ""
for ch in s:
    rev = ch + rev     # building reversed string manually

if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
