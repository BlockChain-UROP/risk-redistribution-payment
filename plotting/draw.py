import csv
import glob
import matplotlib.pyplot as plt

def getAve(arr):
    return sum([int(x) for x in arr]) / len(arr)

def getListOfFiles(re, _pre = 7, _post = 4):
    return sorted(glob.glob(re), key=lambda s: int(s[_pre:-1 * _post]))

def getFirstRowOfCsv(file_name):
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        # Retun the first row
        for row in spamreader:
            return row

### Global Variables
ans = []
# fileRE = './Exp3-*.csv'
# fileRE = './Exp1-aws-ganache-done/Exp1-aws2-*.csv'
fileRE = './Exp3-local-ganache-done/Exp3-local-*.csv'
preChar = 26 + 11
postChar = 4

### Main Execution
for file_name in getListOfFiles(fileRE,preChar,postChar):
    row = getFirstRowOfCsv(file_name)    
    ans.append(getAve(row))
    print(file_name, row)

# Plot
plt.plot(ans)
plt.show()
