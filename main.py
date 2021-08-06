# Challenge user puts string check number/letter count
stringCheck = "CAAB"

for i in stringCheck:
    count = 0
    for l in stringCheck:
        if i == l:
            count += 1
            if count >= 2:
                print("Duplicate number found")
                break
    print(i)



