try:
    hours = int(raw_input('Enter Hours: '))
    payrate = float(raw_input('Enter Rate: '))
    if hours > 40:
        pay = payrate*40 + (hours-40)*payrate*1.5
    else:
        pay = hours*payrate
    print "Pay:", pay
except:
    print "Error, please enter numeric input"
