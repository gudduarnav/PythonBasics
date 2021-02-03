
salary = float(input("Enter your Annual Income:"))

totaltax = 0
if salary>0:
    taxableamount = min([salary, 350000])
    tax = taxableamount *  0/100
    totaltax = totaltax + tax
    salary = salary - taxableamount
    print(taxableamount," taxed at 0 %. Tax = Rs.", tax)

if salary>0:
    taxableamount = min([salary, 200000])
    tax = taxableamount*10/100
    totaltax = totaltax + tax
    salary = salary - taxableamount
    print(taxableamount, "taxed at 10 % = Rs.", tax)

if salary>0:
    taxableamount = min([salary, 200000])
    tax = taxableamount*20/100
    totaltax = totaltax + tax
    salary = salary - taxableamount
    print(taxableamount, "taxed at 20 % = Rs.", tax)

if salary>0:
    tax = salary*30/100
    totaltax = totaltax + tax
    print(salary, "taxed at 30 % = Rs.", tax)

print("Total Tax is Rs.", totaltax)
