# this implements sequential search for a sorted array

def seq_search(arr,element):

    index = 0
    

    length = len(arr)

    while index < length:

        if arr[index] == element:

            return True
        else:
            index = index+1
    return
