f1 = open("linear-relationship.csv", mode='w',)
for x in range (1,10000):
    wnp = str(x) + "," + str(2*x+5) + "\n"
    f1.write(wnp)
f1.close()