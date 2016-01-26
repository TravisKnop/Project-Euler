import itertools

ones = range(201)
twos = range(101)
fives = range(41)
tens = range(21)
twentys = range(11)
fiftys = range(5)
hundred = range(3)
two_hun = range(2)

counter = 0
running_total = 0
for a in two_hun:
    running_total = a * 200
    if running_total == 200:
        counter += 1
    elif running_total < 200:
        for b in hundred:
            running_total = a*200 + b*100
            if running_total == 200:
                counter += 1
            elif running_total < 200:
                for c in fiftys:
                    running_total = a*200 + b*100 + c*50
                    if running_total == 200:
                        counter += 1
                    elif running_total < 200:
                        for d in twentys:
                            running_total = a*200 + b*100 + c*50 + d*20
                            if running_total == 200:
                                counter += 1
                            elif running_total < 200:
                                for e in tens:
                                    running_total = a*200 + b*100 + c*50 + d*20 + e*10
                                    if running_total == 200:
                                        counter += 1
                                    elif running_total < 200:
                                        for f in fives:
                                            running_total = a*200 + b*100 + c*50 + d*20 + e*10 + f*5
                                            if running_total == 200:
                                                counter += 1
                                            elif running_total < 200:
                                                for g in twos:
                                                    running_total = a*200 + b*100 + c*50 + d*20 + e*10 + f*5 + g*2
                                                    if running_total == 200:
                                                        counter += 1
                                                    elif running_total < 200:
                                                        for h in ones:
                                                            running_total = a*200 + b*100 + c*50 + d*20 + e*10 + f*5 + g*2 + h*1
                                                            if running_total == 200:
                                                                counter += 1

print(counter)
