def plot_histogram(dict, design = '===', hide_freq = False, align_freq = False):
    design = '==='
    hide_freq = False
    align_freq = False


    max_length = 0
    for freq in dict.values():
        if freq> max_length: 
            max_length = freq

    design = design + ' '

    for key,freqeuncy in dict.items():
        print(f'{key} | ', end=' ')

        align_val = ' '

        if align_freq == True:
            align_val = ' '*(max_length - freqeuncy) * len(design)
        print(design*freqeuncy, end=align_val)

        if hide_freq == False:
            print(f'{freqeuncy}')
        else:
            print()

dict = {2:3,1:6, 9:2,4:3,3:1}


plot_histogram(dict, design='+++', hide_freq=False, align_freq= False)
plot_histogram(dict, design='+++', hide_freq=True, align_freq= False)
plot_histogram(dict, design='+++', hide_freq=False, align_freq= True)


