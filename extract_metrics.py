import re

def extract_time(filename):
    f = open(filename)
    content = f.readlines()
    content = [x.strip() for x in content]
    ts = []
    for item in content:
        if item.startswith("[CS527 Peifeng]"):
            splitted_item = re.split('\s+', item)
            ts.append(int(splitted_item[8]))
    return ts

def extract_coverage(filename):
    f = open(filename)
    content = f.readlines()
    content = [x.strip() for x in content]
    coverage = []
    for item in content:
        if item.startswith("[CS527 Peifeng]"):
            splitted_item = re.split('[\s+\]\%]', item)
            coverage.append(float(splitted_item[4]))
    return coverage

def printToColumn(arr):
    for item in arr:
        print(item) 

filename = "test.txt"
ts = extract_time(filename)
printToColumn(ts)
coverage = extract_coverage(filename)
printToColumn(coverage)