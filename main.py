                                          # Calculator by python
choice = input("Enter your choice: ")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if choice == '1':
    print(a + b)
elif choice == '2':
    print(a - b)
elif choice == '3':
    print(a * b)
elif choice == '4':
    print(a / b)
else:
    print("Invalid choice")