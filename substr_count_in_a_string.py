def substrcount(str,substr):
    count=0
    l=len(substr)
    for i in range(len(str)):
        if str[i:i+l]==substr:
            count+=1
    return count
str="ABCDCDC"
substr="CDC"
print(substrcount(str,substr))