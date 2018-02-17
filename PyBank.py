import os
import csv
budget_data = os.path.join("PyBank", "raw_data", "budget_data_1.csv")
# Open and read csv
filename=input("Enter filename\n")
data = list()
with open(filename) as f:
    next(f)
    for line in f:
        entry = (line.split(",")[0], int(line.split(",")[1]))
        data.append(entry)
        # entry = (Date:String, Amount:Integer)

# extract total number of months
dates = list()
for x in data:
    dates.append(x[0])
total_months = len(dates)

# calculate total revenue
total_revenue = 0
revenues = list()
for x in data:
    revenues.append(x[1])

for i in range(0, len(revenues)):
    total_revenue += revenues[i]

# calculate average revenue change
revenue_changes = list()
for i in range(1, len(revenues)):
    change = revenues[i - 1] - revenues[i]
    revenue_changes.append(change)
avg_change = sum(revenue_changes) / len(revenue_changes)

# calculate least and greatest increase
greatest_increase = ('', 0)  # tuple to hold date and amount
greatest_decrease = ('', 0)

for i in range(1, len(data)):
    past_month_revenue = data[i - 1][1]
    current_month_revenue = data[i][1]
    change = current_month_revenue - past_month_revenue
    # if the current month's revenue is higher than previous, then candidate for greatest increase
    if current_month_revenue > past_month_revenue:
        if change > greatest_increase[1]:
            greatest_increase = (data[i][0], change)
    # if the previous month's revenue is higher than current, then candidate for greatest decrease
    if past_month_revenue > current_month_revenue:
        if change < greatest_decrease[1]:
            greatest_decrease = (data[i][0], change)

# print results
f = open("financial-analysis.txt", 'w')
f.write("Financial Analysis\n")
f.write("----------------------------")
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total Revenue: " + str(total_revenue) + "\n")
f.write("Average Revenue Change: " + str(avg_change) +"\n")
f.write("Greatest Increase in Revenue: " + str(greatest_increase)+"\n")
f.write("Greatest Decrease in Revenue: " + str(greatest_decrease)+"\n")
f.close()

print("Financial Analysis")
print("----------------------------\n")
print("Total Months: " + str(total_months))
print("Total Revenue: " + str(total_revenue))
print("Average Revenue Change: " + str(avg_change))
print("Greatest Increase in Revenue: " + str(greatest_increase))
print("Greatest Decrease in Revenue: " + str(greatest_decrease))
