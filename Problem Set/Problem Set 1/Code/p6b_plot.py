import matplotlib.pyplot as plt

filename = "/home/santa/Dropbox/NAM/Problem Set 1/Code/data.txt"
lines = [line.rstrip('\n') for line in open(filename)]
names = ["Reed","Bucknell", "Mississippi", "Virginia", "Berkeley"]

for line in lines:
    pts = line.split(",")
    if pts[0] in names:
        plt.annotate(pts[0], xy=(float(pts[1]),float(pts[2])))
        plt.plot(float(pts[1]),float(pts[2]),'*',color='red')
    else:
        plt.plot(float(pts[1]),float(pts[2]),'.',color='black')

plt.annotate("no paradox line",xy=(70,1.1))
plt.plot([30,130],[1,1])
plt.axis([30,130,0.5,3])
plt.xlabel(r'$<k_u>$')
plt.ylabel(r'$<k_v>/<k_u>$')
plt.show()