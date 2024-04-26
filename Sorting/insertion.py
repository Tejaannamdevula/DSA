def insertion_sort(arr):
    comparisions = 0
    n = len(arr)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
            comparisions +=1
    print(comparisions)
    return arr

arr = [160,120,180,155,452]
print(insertion_sort(arr))

#better when array is almost sorted
#take more comparisions when smallest number are at end