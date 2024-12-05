import re

with open("mulnums.txt") as file:
    tot = 0
    active = True
    for i in file:
        matches = re.findall(r"mul\(+[0-9]{1,3},+[0-9]{1,3}\)|do\(\)|don't\(\)",i)
        for j in matches:
            if "do()" in j:
                active = True
            elif "don" in j:
                active = False
            else:
                if active:
                    nums = list(map(int,re.findall(r"[0-9]{1,3}",j)))
            #print(nums[0])
                    tot += nums[0]*nums[1]
    print(tot)
