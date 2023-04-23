import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
csvpath_output = os.path.join("budget_analysis.txt")

total_months = 0
total_profits = 0
total_PL = []
prev_PL = 0
month_change = []
PL_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
total_profit_changeLS = []
average_PL = 0

with open(csvpath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    

    for row in csv_reader:

        total_months = total_months + 1
        
        total_profits = total_profits + int(row["Profit/Losses"])

        PL_change = int(row["Profit/Losses"]) - prev_PL
        prev_PL = int(row["Profit/Losses"])
        total_profit_changeLS = total_profit_changeLS + [PL_change]
        month_change = [month_change] + [row["Date"]]
        
        if (PL_change > greatest_increase[1]):
            greatest_increase[1] = PL_change
            greatest_increase[0] = row["Date"]

        if (PL_change < greatest_decrease[1]):
            greatest_decrease[1] = PL_change
            greatest_decrease[0] = row["Date"]

    total_profit_changeLS.append(int(row["Profit/Losses"]))

average_PL = sum(total_profit_changeLS) / (len(total_profit_changeLS))

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total : " + "$" + str(total_profits))
print("Average Change: " + "$" + str(average_PL))  
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
       
with open(csvpath_output, 'w') as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write("Total Months: " + str(total_months))
    file.write("\n")
    file.write("Total : " + "$" + str(total_profits))
    file.write("\n")
    file.write("Average Change: " + "$" + str(average_PL))  
    file.write("\n")
    file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    file.write("\n")
    file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")