import os 
import csv

csvpath= os.path.join('..','PyBank','budget_data.csv')

month_count = []
profit = []
change_profit = []

with open (csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_reader = next(csvreader)

    for budget_info in csvreader:
        month_count.append(budget_info[0])
        profit.append(int(budget_info[1]))

    for i in range(len(profit)-1):
       change_profit.append(profit[i+1]-profit[i])
                      
#evaluate the max and min from the list made
increase = max(change_profit)
decrease = min(change_profit)

#month greatest increase/ greatest , 
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")

output_path =os.path.join('..','PyBank','budget_data.txt')
with open(output_path, 'w',newline='') as txtfile: 
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------\n")
    txtfile.write(f"Total Months:{len(month_count)}\n")
    txtfile.write(f"Total: ${sum(profit)}\n")
    txtfile.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})\n")
    txtfile.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})\n")
    