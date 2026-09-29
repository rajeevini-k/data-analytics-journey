# Day 1 - Python Fundamentals
# Data Analytics Learning Journey

# 1. Variables and Data Types

name = "Raji"
age = 23
salary = 50000
is_employed = True

print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Employed:", is_employed)


# 2. Lists

sales = [1200, 1500, 900, 2200, 1800]

print("\nSales:", sales)
print("First sale:", sales[0])
print("Last sale:", sales[-1])
print("Number of sales:", len(sales))


# 3. Conditions

score = 72

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print("\nScore:", score)
print("Grade:", grade)


# 4. For Loop

print("\nSales values:")

for sale in sales:
    print(sale)


# 5. Finding Highest Sale Without max()

highest = sales[0]

for sale in sales:
    if sale > highest:
        highest = sale

print("\nHighest sale:", highest)


# 6. Counting Sales Above 1500

count = 0

for sale in sales:
    if sale > 1500:
        count += 1

print("Sales above 1500:", count)


# 7. Dictionary

student = {
    "name": "Raji",
    "age": 23,
    "score": 85
}

print("\nStudent name:", student["name"])
print("Student score:", student["score"])


# 8. Function

def analyze_sales(sales):
    total = sum(sales)
    average = total / len(sales)
    return total, average


total, average = analyze_sales(sales)

print("\nTotal sales:", total)
print("Average sales:", average)


# 9. List Comprehension

doubled_sales = [sale * 2 for sale in sales]

print("\nDoubled sales:", doubled_sales)
