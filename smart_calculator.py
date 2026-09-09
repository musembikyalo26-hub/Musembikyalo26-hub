print("=== Kyaloo's Smart Calculator ===")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2 if num2 != 0 else 'Cannot divide by zero'}")

print("\nBuilt by Future Kenyan Elon Musk 🚀")
