# Program Q5 updated header
# 5. Write a function to print all keys and values from a dictionary in separate lists.
def print_dict(d):
    keys = list(d.keys())
    values = list(d.values())
    print("Keys:", keys)
    print("Values:", values)

data = {"a": 1, "b": 2, "c": 3}
print_dict(data)
# Small improvement
