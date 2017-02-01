import matplotlib.pyplot as plt

filename = "/home/santa/Dropbox/NAM/Problem Set 1/Code/ec.txt"
lines = [line.rstrip('\n') for line in open(filename)]

plt.subplot(211)
for line in lines:
    pts = line.split(",")
    plt.plot(float(pts[2]),float(pts[1]),'.',color='black')

plt.axis([0,45000,5,14])
plt.ylabel(r'diameter $<l_{max}>$')
plt.xlabel('network size n')

plt.subplot(212)
for line in lines:
    pts = line.split(",")
    plt.plot(float(pts[4]),float(pts[3]),'.',color='black')

plt.axis([0,45000,2,4])
plt.ylabel(r'mean geodesic distance $<l>$')
plt.xlabel('size of the largest component n')

plt.tight_layout()
plt.show()