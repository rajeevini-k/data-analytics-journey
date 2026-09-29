# Day 1 - Sales Analysis
# Basic Python Data Analysis

sales = [1200, 1500, 900, 2200, 1800, 3000, 1700]

print("=" * 50)
print("SALES ANALYSIS")
print("=" * 50)


# Basic statistics

total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sales = max(sales)
lowest_sales = min(sales)


print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sale:", highest_sales)
print("Lowest Sale:", lowest_sales)


# Count sales above 1500

sales_above_1500 = 0

for sale in sales:
    if sale > 1500:
        sales_above_1500 += 1

print("Sales Above 1500:", sales_above_1500)


# Percentage of sales above 1500

percentage_above_1500 = (
    sales_above_1500 / len(sales)
) * 100

print(
    "Percentage Above 1500:",
    percentage_above_1500
)


# Categorize sales

high_sales = []
low_sales = []

for sale in sales:
    if sale >= 1500:
        high_sales.append(sale)
    else:
        low_sales.append(sale)


print("\nHigh Sales:", high_sales)
print("Low Sales:", low_sales)


print("=" * 50)
print("ANALYSIS COMPLETE")
print("=" * 50)
