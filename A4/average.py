def var_sum(*args):
    sum = 0

    for i in args:
        sum += i
    return sum

def var_avg(*args):
    return var_sum(*args)/len(args)


print(var_avg(1,2,3))

