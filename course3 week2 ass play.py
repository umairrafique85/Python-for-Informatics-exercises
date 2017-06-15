import re
#filehandle = open('regex_sum_308898.txt')
print sum([int(number) for number in re.findall('[0-9]+', open('regex_sum_308898.txt').read())])
