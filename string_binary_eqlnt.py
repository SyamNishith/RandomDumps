s="syam_nishith"
binary_string=" "
for i in s:
    if i in ['a','e','i','o','u']:
        binary_string+='0'
    else:
        binary_string+='1'
print(int(binary_string,2))