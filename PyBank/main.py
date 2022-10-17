#Importing dependencies
import os
import csv

# Set path for files
cvspath = os.path.join('Resources', "budget_data.csv")
output_path = os.path.join('analysis',"Financial_Analysis.txt")

#Lists to store data
totalmonths=[]
net_total=[]
average_change=[]
   
with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    csvheader=next(csvreader)
    
    for row in csvreader:
        totalmonths.append(row[0])
        net_total.append(int(row[1]))
        
    monthlytotal = len(totalmonths)
    total_net=sum(net_total)
   
   #Revenue change
    for e in range(1, len(net_total)):
        average_change.append((int(net_total[e]) - int(net_total[e-1])))

    average_final = sum(average_change) / len(average_change)
    greatest_increase = max(average_change)
    greatest_decrease = min(average_change)

#Printing
print ('\n')
print("Financial Analysis")
print("-"*25)
print(f"Total Months: {len(totalmonths)}")
print("Total: " + "$" + str(total_net))
print("Average Change: " + "$" + str(round(average_final, 2)))
print("Greatest Profit Increase: " + str(totalmonths[average_change.index(max(average_change))+1]) + " " + "$" + str(greatest_increase))
print("Greatest Profit Decrease: " + str(totalmonths[average_change.index(min(average_change))+1]) + " " + "$" + str(greatest_decrease))

# export text file with financial results
with open(output_path, "w+") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("__________________________\n")
    text_file.write("\n")
    text_file.write("Total Months: " + str(monthlytotal))
    text_file.write("\n")
    text_file.write("Total: " + "$" + str(total_net))
    text_file.write("\n")
    text_file.write("Average Change: " + "$" + str(round(average_final, 2)))
    text_file.write("\n")
    text_file.write("Greatest Profit Increase: " + str(totalmonths[average_change.index(max(average_change))+1]) + " " + "$" + str(greatest_increase))
    text_file.write("\n")
    text_file.write("Greatest Profit Decrease: " + str(totalmonths[average_change.index(min(average_change))+1]) + " " + "$" + str(greatest_decrease))
