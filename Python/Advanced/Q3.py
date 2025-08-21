# 3. Create a program that takes multiple lists as input and calculates the length of each list using a function.
def list_length(lst):
    return len(lst)

list1 = input("Enter elements of list1 (comma separated): ").split(",")
list2 = input("Enter elements of list2 (comma separated): ").split(",")

print("Length of list1:", list_length(list1))
print("Length of list2:", list_length(list2))
# Minor update to Q3
