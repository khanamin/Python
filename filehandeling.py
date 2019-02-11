#fhand  = open('Amin.txt','r')
#print(fhand)
#count = 0
#for x in fhand:
    #print(x)
#    print('Line Count:', count)

#fhand = open('Amin.txt')
#inp = fhand.read()
#print(len(inp))
#print(inp[:999])

#fhand = open('mbox-short.txt')
#for line in fhand:
#    if line.startswith('From:'):
#        print(line)

#fhand = open('mbox-short.txt')
#for line in fhand:
#    line = line.rstrip()
#    if not line.startswith('From:'):
#    print(line)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za'in line :
        continue
    print(line)
