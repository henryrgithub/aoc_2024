def issafe(report):
    increasing = None
    prev = None
    for i in report:
        if prev is None:
            prev = i
            continue
        if increasing is None:
            increasing = (i > prev)
        if (i > prev) != increasing:
            return False
        diff = abs( i- prev)
        if diff < 1:
            return False
        if diff > 3:
            return False
        prev = i
    return True


with open("reports.txt") as file:
    numsafe = 0
    for report in file:
        numreport = list(map(int,report.split()))
        safe = issafe(numreport)
        if not safe:
            for i in range(len(numreport)):
                stripped = numreport.copy()
                stripped.pop(i)
                safe = issafe(stripped)
                if safe:
                    break


        if safe:
            numsafe += 1
    print(numsafe)

