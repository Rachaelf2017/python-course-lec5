import sys

in_file = open(sys.argv[1])
indata = in_file.read().split('\n')[1:-1]

# print indata


index = []
for month in indata:
    index.append(month.split(','))
print index

for item in index:
    print "Month: %s YTD: %s" % (item[0], item[2])
