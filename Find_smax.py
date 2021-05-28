def find_smax(list):
    temp = list[:]
    temp.sort()
    print(list)
    print("The second largest element in the list is ", temp[-2])


list = []
num = int(input("Enter number of elements to add in list: "))
for i in range(1, num + 1):
    print("Enter {} elements: ". format(i))
    element = int(input())
    list.append(element)

find_smax(list)