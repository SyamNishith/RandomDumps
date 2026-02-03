from _functools import *
nums=[1,2,3,4,5,6,7,8,9,10]
evenlist=list(filter(lambda nums:nums%2==0,nums))
oddlist=list(filter(lambda nums:nums%2!=0,nums))
print("filter:",evenlist)
print("filter:",oddlist)
doublelist=list(map(lambda n:n*2,evenlist))
print("map:",doublelist)
reducelist=reduce(lambda a,b:a+b,doublelist)
print("reduce:",reducelist)