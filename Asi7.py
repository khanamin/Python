fname =  input("Enter the file name : ")
count = 0
tot = 0
ans = 0
fhand = open(fname)
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.strip()
        count += 1
        pos = line.find(":");
        num = line[pos+1:]
        num = float(num)
        tot = num+tot
ans = tot/count
print("Average spam Confidence:",ans)
