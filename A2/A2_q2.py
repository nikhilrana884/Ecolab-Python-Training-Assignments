
def frequency_distribution(seq):
    d = { }
    for i in seq:
        if i in d:
            d[i] += 1
        else: 
            d[i] = 1
    return d        
    
def print_freq_table(d):
    for item in d.items():
        count = item[1]
        print(item[0],"| ","===" * count, count ,sep=" ")


seq = [2, 2, 9, 1, 2, 2, 1, 4, 9, 2,  2, 3, 1]

d = frequency_distribution(seq)
print_freq_table(d)