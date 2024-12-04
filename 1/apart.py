with open("nums.txt") as file:
    firstnum = []
    secnum = []
    for line in file:
        (a,b) = line.split()
        firstnum.append(int(a))
        secnum.append(int(b))

    firstnum.sort()
    secnum.sort()
    off = 0
    for i in range(len(firstnum)):
        off += abs(firstnum[i]-secnum[i])

    print(off)

    sim = 0
    for i in firstnum:
        numinsec = secnum.count(i)
        sim += i*numinsec
    print(sim)
