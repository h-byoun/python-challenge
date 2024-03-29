#import modules
import os
import csv

# Read in the CSV file
csvpath = os.path.join('../csv_files','budget_data.csv')
with open(csvpath) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #move to next line skip header
    header = next(csvreader)

    #create variables and empty lists we will need
    monthcount = 0
    totalprofit = 0
    monthlist = []
    profitlist = []
    profitlist2 = []
    
    
    # Loop through the data
    for row in csvreader:
        #count the number of months(or rows)
        monthcount +=1
        #add up all the values in profit/losses column to get the total profit
        totalprofit += int(row[1])
        #list with profit values
        profitlist.append(row[1])
        #list with profit values so we can calculate the change in profits
        profitlist2.append(row[1])
        #list with months
        monthlist.append(row[0])
        
#here we pop the first value so we can now subtract the values in profitlist from profitlist2 to get the change between months      
profitlist2.pop(0)

#using this to format all the list elements as integers
#for i in range(len(change)):
#    change[i] = int(change[i])
#not sure if this is neccessary but seemed to fix some issues I had
for i in range(len(profitlist)):
    profitlist[i] = int(profitlist[i])
for i in range(len(profitlist2)):
    profitlist2[i] = int(profitlist2[i])

#now we can subtract the values from the previous month to find the change, then append to list 
#for i in range(len(profitlist2)):
#    change.append(profitlist2[i]-profitlist[i])
#^ let's clean this up and use comprehension
change = [(profitlist2[i]-profitlist[i]) for i in range(len(profitlist2))]

#calculate average change
#round function to get 2 decimals
averagechange = round(sum(change) / len(change),2)
#max and min functions for lists
maxincrease = max(change)
maxdecrease = min(change)

#find the corresponding month of the greatest increase/decrease in profits
for i in range(len(change)):
    if change[i] == maxincrease:
        maxmonth = monthlist[i+1]
    elif change[i] == maxdecrease:
        lossmonth = monthlist[i+1]

#print(profitlist)
#print(profitlist2)
#print(change)

#finally print results!    
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {monthcount}")
print(f"Total: ${totalprofit}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {maxmonth} (${maxincrease})")
print(f"Greatest Decrease in Profits: {lossmonth} (${maxdecrease})")


#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)


#write the code output into a text file
output_file = os.path.join("../txt_outputs", "financial_analysis.txt")

with open(output_file, "w+") as f:
    print("Financial Analysis",file=f)
    print("-------------------------",file=f)
    print(f"Total Months: {monthcount}",file=f)
    print(f"Total: ${totalprofit}",file=f)
    print(f"Average Change: ${averagechange}",file=f)

    print(f"Greatest Increase in Profits: {maxmonth} (${maxincrease})",file=f)
    print(f"Greatest Decrease in Profits: {lossmonth} (${maxdecrease})",file=f)      