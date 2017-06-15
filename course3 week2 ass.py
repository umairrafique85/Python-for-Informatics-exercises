import re
filehandle = open('regex_sum_308898.txt')
accumulator = list()
for line in filehandle:
    linedata = re.findall('[0-9]+', line)
    linedataconv = list()
    for number in linedata:
        number = int(number)
        accumulator.append(number)

print sum(accumulator)
