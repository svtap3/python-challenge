import os
import csv


filepath = os.path.join("Resources", "election_data.csv")
outfile = os.path.join("analysis", "testing.txt")



# Open the CSV
with open(filepath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


#Create candidate variables

    candidate1 = "Charles Casper Stockham"
    candidate2 = "Diana DeGette"
    candidate3 = "Raymon Anthony Doane"

    #Define Starting number of votes
    initialvotes1 = 0
    initialvotes2 = 0
    initialvotes3 = 0


    # Loop through looking for the video
    for row in csvreader:
        if row[2] == candidate1:
            initialvotes1 = initialvotes1 + 1
        elif row[2] == candidate2:
            initialvotes2 = initialvotes2 + 1
        elif row[2] == candidate3:
            initialvotes3 = initialvotes3 + 1


    #define total votes

    totalvotes = initialvotes1 + initialvotes2 + initialvotes3

    #define percentages

    stockhampercentage = round((initialvotes1/totalvotes)*100,3)
    degettepercentage = round((initialvotes2/totalvotes)*100,3)
    doanepercentage = round((initialvotes3/totalvotes)*100,3)

    
    #print results
    print ("Election Results:")
    print("Total Votes:" + str(totalvotes))
    print("Charles Casper Stockham:" + str(stockhampercentage) + '%' + ' ' + '(' + str(initialvotes1) + ')')
    print("Diana DeGette:" + str(degettepercentage) + '%' + ' ' + '(' + str(initialvotes2) + ')')
    print("Raymon Anthony Doane:" + str(doanepercentage) + '%' + ' ' + '(' + str(initialvotes3) + ')')

    if initialvotes1 > initialvotes2 and initialvotes1 > initialvotes3:
        print ("Winner: Charles Caspar Stockham")
    elif initialvotes2 > initialvotes1 and initialvotes2 > initialvotes3:
        print ("Winner: Diana DeGette")
    elif initialvotes3 > initialvotes1 and initialvotes3 > initialvotes2:
        print ("Winner: Raymon Anthony Doane")
txtfile.write("Charles Casper Stockham:" + str(stockhampercentage) + '%' + ' ' + '(' + str(initialvotes1) + '))\n')
