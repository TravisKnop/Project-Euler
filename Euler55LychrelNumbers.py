counter = 0

def lychrel(number):
    rev_num = int(str(number)[::-1])
    return number + rev_num

def lychrel50(number):
    i = 0
    output = lychrel(number)
    while i < 50:
        if str(output) == str(output)[::-1]:
            #print(number, output, i)
            i += 50
        else:
            output = lychrel(output)
            i += 1
            if i == 49:
                print("LYCHREL! {}".format(number), counter)
                return 1

for x in range(10000):
    if lychrel50(x):
        counter +=1

print(counter)
