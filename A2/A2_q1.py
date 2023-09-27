
def frequency_distribution(seq):
    d = {}
    for i in seq:
        if i in d:
            d[i] += 1
        else: 
            d[i] = 1
    return d        

seq = [2, 2, 9, 1, 2, 2, 1, 4, 2, 2, 3, 1]

d = frequency_distribution(seq)
print(d)
#print_freq_table(d)