# 1. Conditional Statements
print("1. Conditional Statement :")
number = 10
if number > 0:
    print("Number is positive.")
elif number == 0:
    print("Number is zero.")
else:
    print("Number is negative.")

# 2. For Loop
print("\n2. For Loop (printing numbers from 1 to 5):")
for i in range(1, 6):
    print(i, end=' ')

# 3. While Loop
print("\n\n3. While Loop (counting down from 5):")
count = 5
while count > 0:
    print(count, end=' ')
    count -= 1

# 4. Loop Control Statements
print("\n\n4. Loop Control (break):")
print("Using break:")
for i in range(1, 10):
    if i == 5:
        print("Breaking at", i)
        break
    print(i, end=' ')
