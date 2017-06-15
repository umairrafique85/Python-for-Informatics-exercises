def computepay(hours, payrate):
    if hours > 40:
        pay = payrate*40 + (hours-40)*payrate*1.5
    else:
        pay = hours*payrate
    print "Pay:", pay

