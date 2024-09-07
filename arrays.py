


# get the sum of the array 
def targeted_sum(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == target:
                    return [i, j, k]
                


array = [12,3,4,1,6,9]
target = 24
result = targeted_sum(array, target)
print(result)                



