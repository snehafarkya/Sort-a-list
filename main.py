# A python script to sort a list of integers as well as strings 
print("Hello, Welcome to SORT STATION! \nEnter integers to get sorted:")

num = list(map(int,input().split()))
print("After sorting in: ")
num.sort()
print("1. Ascending order: ",num)
num.sort(reverse=True)
print("2. Descending order: ",num) 

print("\nEnter strings to get sorted: \n")
num = list(map(str,input().split()))
print("After sorting in: ")
num.sort()
print("1. Ascending order: ",num)
num.sort(reverse=True)
print("2. Descending order: ",num)
