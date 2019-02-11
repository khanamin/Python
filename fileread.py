#def my():
#    fname = input('Enter the file name: ')
#    fhand = open (fname)
#    count = 0
#    for line in fhand :
#        if line.startswith('Subject:') :
#            count = count + 1
#    print('There were', count,'subject lines in', fname)
#my()
fname =  input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File Does not exist:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count,'subject lines in', fname)
        
