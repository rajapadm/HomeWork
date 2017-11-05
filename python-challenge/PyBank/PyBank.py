import os
import csv

filepath=os.path.join('raw_data', 'budget_data_1.csv')

with open(filepath) as csv2:
    csvreader2 = csv.reader(csv2)
    next(csvreader2, None)
    total_revenue=0
    row_count = 0
    difference_count = 0
    prev_revenue = 0
    min_difference = 0
    min_date = 0
    max_difference = 0
    max_date = 0
    for row in csvreader2:
        total_revenue +=int(row[1])
        if row_count == 0:
            prev_revenue = int(row[1])
            min_difference, max_difference = 0, 0
        else:
            difference_count += int(row[1]) - prev_revenue
            if int(row[1]) - prev_revenue < min_difference:
                min_difference = int(row[1]) - prev_revenue
                #min_value = row[1]
                min_date = row[0]
            if int(row[1]) - prev_revenue > max_difference:
                max_difference = int(row[1]) - prev_revenue
                #max_value = row[1]
                max_date = row[0]
            prev_revenue = int(row[1])
        row_count += 1
    print ("Financial Analysis")
    print("------------------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total Revenue: {total_revenue}")
    print("Average Revenue Change: ${0}".format(round(difference_count/row_count)))
    print("Greatest Increase in Revenue: " +str(max_date)+"  ($"+ str(max_difference)+")")
    print("Greatest Decrease in Revenue: " +str(min_date)+"  ($"+ str(min_difference)+")")

output=os.path.join('raw_data', 'budget_PyBank.txt')

with open(output,'w') as text:
    text.write("Financial Analysis")
    text.write("\n------------------------------------")
    text.write("\nTotal Dates: " + str(row_count))
    text.write("\nTotal Revenue: $"+ str(total_revenue))
    text.write("\nAverage Revenue Change: $"+str(round(difference_count/row_count)))
    text.write("\nGreatest Increase in Revenue: " +str(max_date)+"  ($"+ str(max_difference)+")")
    text.write("\nGreatest Decrease in Revenue: " +str(min_date)+"  ($"+ str(min_difference)+")")

filepath1=os.path.join('raw_data', 'budget_data_2.csv')

with open(filepath1) as csv2:
    csvreader2 = csv.reader(csv2)
    next(csvreader2, None)
    print("Financial Analysis")
    print("------------------------------")
    total_revenue=0
    row_count = 0
    difference_count = 0
    prev_revenue = 0
    min_difference = 0
    min_date = 0
    max_difference = 0
    max_date = 0
    #min_difference, max_difference = 0, 0
    for row in csvreader2:
        total_revenue +=int(row[1])
        if row_count == 0:
            prev_revenue = int(row[1])
            min_difference, max_difference = 0, 0
        else:
            difference_count += int(row[1]) - prev_revenue
            if int(row[1]) - prev_revenue < min_difference:
                min_difference = int(row[1]) - prev_revenue
                #min_value = row[1]
                min_date = row[0]
            if int(row[1]) - prev_revenue > max_difference:
                max_difference = int(row[1]) - prev_revenue
                #max_value = row[1]
                max_date = row[0]
            prev_revenue = int(row[1])
        row_count += 1
    print ("Financial Analysis")
    print("------------------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total Revenue: {total_revenue}")
    print("Average Revenue Change: ${0}".format(round(difference_count/row_count)))
    print("Greatest Increase in Revenue: " +str(max_date)+"  ($"+ str(max_difference)+")")
    print("Greatest Decrease in Revenue: " +str(min_date)+"  ($"+ str(min_difference)+")")

output1=os.path.join('raw_data', 'budget_PyBank_2.txt')

with open(output1,'w') as text:
    text.write("Financial Analysis")
    text.write("\n------------------------------------")
    text.write("\nTotal Dates: " + str(row_count))
    text.write("\nTotal Revenue: $"+ str(total_revenue))
    text.write("\nAverage Revenue Change: $"+str(round(difference_count/row_count)))
    text.write("\nGreatest Increase in Revenue: " +str(max_date)+"  ($"+ str(max_difference)+")")
    text.write("\nGreatest Decrease in Revenue: " +str(min_date)+"  ($"+ str(min_difference)+")")