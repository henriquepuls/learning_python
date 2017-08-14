# 2018 NRMP Price Calculator

while True:
    total = int(input("How many residency programs will you apply?"))
    
    def price(total):
        if total <= 0:
            return 0
        elif total > 0 and total < 11:
            price = 99
            return price
        elif total >= 11 and total < 21:
            price = 99 + ((total - 10) * 13)
            return price
        elif total >= 21 and total < 31:
            price = 99 + (10 * 13) + ((total - 20) * 17)
            return price
        else:
            price = 99 + (10 * 13) + (10 * 17) + ((total - 30) * 26) 
            return price

    print ('You will pay USD', price(total), 'to apply for', total, 'residency programs')