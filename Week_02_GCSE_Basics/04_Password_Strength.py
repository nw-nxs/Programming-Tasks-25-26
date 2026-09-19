"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
password = str(input("Enter a password: "))
strength = 0
num = str(1234567890)
lower = str(abcdefghijklmnopqrstuvwxyz)
cap = str(ABCDEFGHIJKLMNOPQRSTUVWXYZ)
if len(password) == 8:
    strength += 1
for i in range(len(num)):
    if num[i] in password:
        strength += 1
for i in range(len(lower)):
    if lower[i] in password:
        strength += 1
for i in range(len(cap)):
    if cap[i] in password:
        strength += 1
if strength == 0 or strength == 1:
    print("password is weak")
if strength == 2:
    print("password is medium")
if strength == 3:
    print("password is strong")












