def my():
    fname = input("Enter file name: ")
    fhand = open(fname)
    for line in fhand :
        line = line.strip()
        line =
        print(line.upper())
my()
