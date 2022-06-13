
list1 = []
def min_num(array):

    return min(array)

def second_min_num(array):

    min = array[0]
    min2 = None
    for item in array[1:]:
        if item < min:
            min2 = min
            min = item
        elif min2 is None or min2 > min:
            min2 = item
    return min2

def nth_min_num(array, n):
    length = len(array)
    if n > length :
        return "n is smaller than length of array or n =0"
    elif n <= 0 :
        return "n should be greater than 0"
    else:
        array.sort()
        return array[n-1]


if __name__ == "__main__":
    num = int(input("enter number of elements"))
    nth_smallest = int(input("enter nth smallest element"))
    for i in range(1, num+1):
        element = int(input("enter elements"))
        list1.append(element)
    min_num = min_num(list1)
    second_min_num = second_min_num(list1)

