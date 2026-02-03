'''The function accepts two integers n, m as arguments
 Find the sum of all numbers in range from 1 to m(both inclusive)
 that are not divisible by n. Return difference
 between sum of integers not divisible by n with sum of numbers divisible by n.'''
def find(n,m):
    sum_div=0
    sum_notdiv=0
    for i in range(1,m+1):
        if i%n!=0:
            sum_notdiv+=i
        if i%n==0:
            sum_div+=i
    return (sum_notdiv-sum_div)
print(find(4,20))

