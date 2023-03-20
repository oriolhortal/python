import sys

kata = (0, 4, 132.42222, 10000, 12345.67)

module = str(kata[0]).zfill(2)
ex = str(kata[1]).zfill(2)
deci1 = round(kata[2], 2)
integer = "{:.2e}".format(kata[3])
deci2 = "{:.2e}".format(kata[4])

print("module_",module,", ex_",ex," : ",deci1,", ",integer,", ",deci2, sep="") 
