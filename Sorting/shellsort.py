# gap is taken ad n/2 
# when gap is 1 it is classic insertion sort
# we gradually decrease the distance of between elements 
#works well when smallest numbers are at last optimizes insertion better in this case


# optimization to insertion sort to teduce gaps 
#gap = 1 => insertion sort



def shell_sort(arr):
    comparisons = 0
    n = len(arr)
    gap = n//2
    while (gap>0):
        for i in range(n-gap):
            if arr[i] >arr [i+gap] :
                arr[i],arr[i+gap] = arr[i+gap], arr[i]
            for j in range(i,0,-gap):
                if arr[j-gap ] > arr[i]:
                     arr[j-gap],arr[i] = arr[i], arr[j-gap]
            comparisons+=1
    
        gap //= 2
    print(comparisons)
    return arr 

arr = [160,120,180,155,452]
print(shell_sort(arr))