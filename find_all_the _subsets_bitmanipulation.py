A=[1,2,3]
n=len(A)
print(n)
main_list=[]
for i in range(2**n):
    my_list=[]
    for j in range(n):
        if (i &(1<<j)):
            my_list.append(A[j])
    main_list.append(my_list)
print(main_list)