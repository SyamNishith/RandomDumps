import heapq
heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,1)
heapq.heappush(heap,71)
heapq.heappush(heap,24)
heapq.heappush(heap,31)
heapq.heappush(heap,2)
heapq.heappush(heap,16)
print(heap)
heapq.heappop(heap)#delet the minimum node from tree since it is a min heap
print(heap)
heap2=[12,1,32,45,67,98,61,23,41]#heapify is used to convert given list into min heap
heapq.heapify(heap2)
print("second heap is:",heap2)
heapq.heappushpop(heap2,56)#pushpop will push the given node and also pop the smallest node in the heap
print("after pushpop:",heap2)
heapq.heapreplace(heap2,100)
print("after heapreplace:",heap2)#heapreplace will pop the smallest node and push the given node
print(heapq.nsmallest(2,heap2))# returns the n smallest nodes in the binary heap
print(heapq.nlargest(2,heap2))#returns the n largest nodes in the binary heap