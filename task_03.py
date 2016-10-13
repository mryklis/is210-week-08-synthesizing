
import decimal

PROD1 = [xrange(0, 199999), xrange(1, 15), 'y', decimal.Decimal(3.63) ]
PROD2 = [xrange(0, 199999), xrange(1, 15), 'n', decimal.Decimal(4.65)]
PROD3 = [xrange(0, 199999), xrange(16, 20), 'y', decimal.Decimal(4.04)]
PROD4 = [xrange(0, 199999), xrange(16, 20), 'n', decimal.Decimal(4.98)]
PROD5 = [xrange(0, 199999), xrange(21, 30), 'y', decimal.Decimal(5.77)]
PROD6 = [xrange(0, 199999), xrange(21, 30), 'n', decimal.Decimal(6.39)]
PROD7 = [xrange(200000, 999999), xrange(1, 15), 'y', decimal.Decimal(3.02)]
PROD8 = [xrange(200000, 999999), xrange(1, 15), 'n', decimal.Decimal(3.98)]
PROD9 = [xrange(200000, 999999), xrange(16, 20), 'y', decimal.Decimal(3.27)]
PROD10 = [xrange(200000, 999999), xrange(16, 20), 'n', decimal.Decimal(4.08)]
PROD11 = [xrange(200000, 999999), xrange(21, 30), 'y', decimal.Decimal(4.66)]
PROD12 = [xrange(1000000, ), xrange(1, 15), 'y', decimal.Decimal(2.05)]
PROD13 = [xrange(1000000, ), xrange(16, 20), 'y', decimal.Decimal(2.62)]

N = 12

NAME = raw_input('what is your name?')



AMOUNT = int(raw_input('What is the amount of your principal (the amount being borrowed)?'))
if AMOUNT in PROD1[0] or PROD2[0] or PROD3[0] or PROD4[0] or PROD5[0] or PROD6[0]:
    YEARS = int(raw_input('For how many years is this loan being borrowed?'))
    if YEARS in PROD1[1] or PROD2[1]:
        QUAL = raw_input('Are you pre-qualified for this loan?').decode('utf-8').lower()
        if QUAL in PROD1[2]:
            RATE = PROD1[3]
        elif QUAL in PROD2[2]:
        	RATE = PROD2[3]
    elif YEARS in PROD3[1] or PROD4[1]:
        QUAL = raw_input('Are you pre-qualified for this loan?').decode('utf-8').lower()
        if QUAL in PROD3[2]:
            RATE = PROD3[3]
        elif QUAL in PROD4[2]:
        	RATE = PROD4[3]
    elif YEARS in PROD5[1] or PROD6[1]:
    	QUAL = raw_input('Are you pre-qualified for this loan?').decode('utf-8').lower()
    	if QUAL in PROD5[2]:
        	RATE = PROD5[3]
        elif QUAL in PROD6[2]:
        	RATE = PROD6[3]
elif AMOUNT in PROD7[0] or PROD8[0] or PROD9[0] or PROD10[0] or PROD11[0]:
    YEARS = int(raw_input('For how many years is this loan being borrowed?'))
    if YEARS in PROD7[1] or PROD8[1]:
        QUAL = raw_input('Are you pre-qualified for this loan?').decode('utf-8').lower()
        if QUAL in PROD7[2]:
            RATE = PROD7[3]
        elif QUAL in PROD8[2]:
        	RATE = PROD8[3]
    elif YEARS in PROD9[1] or PROD10[1]:
        QUAL = raw_input('Are you pre-qualified for this loan?').decode('utf-8').lower()
        if QUAL in PROD9[2]:
            RATE = PROD9[3]
        elif QUAL in PROD10[2]:
        	RATE = PROD10[3]
    elif YEARS in PROD11[1]:
    	QUAL = raw_input('Are you pre-qualified for this loan?').decode('utf-8').lower()
    	if QUAL in PROD11[2]:
        	RATE = PROD11[3]
elif AMOUNT in 
