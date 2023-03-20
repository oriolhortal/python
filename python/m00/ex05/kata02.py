import sys

kata = (2019, 9, 25, 3, 30)

year = str(kata[0]).zfill(4)
month = str(kata[1]).zfill(2)
day = str(kata[2]).zfill(2)
hour = str(kata[3]).zfill(2)
minute = str(kata[4]).zfill(2)

print (f"{month}/{day}/{year} {hour}:{minute}")
