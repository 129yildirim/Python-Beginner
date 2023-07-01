
# list = ['December 13 2023', 'red tv', 18]

# date, obj, time =  ['December 13 2023', 'red tv', 18]

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65, 76, 98, 54, 21])
drop_first_last([65, 76, 98, 54, 21, 54, 78, 96, 21, 34])



