from heapq import heappush, heappop

fruits = []
heappush(fruits, "mango")
heappush(fruits, "orange")
heappush(fruits, "apple")

# heap allows for quick lookup
# python heap are min-heaps meaning the 1st element has the smallest
# value
print(fruits)

print("*****************POP*******************")
# popping element will remove the 1st one and remaining elements might
# shuffle a little bit
heappop(fruits)

# orange and mango trade places so that the 1st element is the smallest
print(fruits)
