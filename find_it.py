def find_it(seq):
    new_arr = [seq.count(num)%2 for num in seq]
    return(seq[new_arr.index(1)])


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))