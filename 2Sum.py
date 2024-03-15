def TwoSum(arr,N):
    hash_set =set()

    for i in range (0,len(arr)):
        value = N-arr[i]
        if(value in hash_set):
            print("Pairs {} , {} ".format(arr[i],value))
        hash_set.add(arr[i])

arr = [1,2,40,3,9,4,3]
N=3
TwoSum(arr,N)