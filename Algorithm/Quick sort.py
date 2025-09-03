import random
def quick_sort(array):
    if len(array)<=1:
        return array
    pivot=random.choice(array)
    right=[i for i in array if i<pivot ]
    left=[i for i in array if i>pivot]
    middle=[i for i in array if i==pivot]
    result=quick_sort(right)+middle+quick_sort(left)
    return result


array=[34,23,56,76,89]
print(quick_sort(array))