import re
filehandle = open('regex_sum_308898.txt')
accumulator = list()
intaccumulator = list()
accumulator = (re.findall('[0-9]+', filehandle.read()))
for num in accumulator:
    intaccumulator.append(int(num))
print sum(intaccumulator)
