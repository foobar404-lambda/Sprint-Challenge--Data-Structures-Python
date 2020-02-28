import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# def binary_search(array, item):
#     high = len(array)
#     low = 0

#     while low < high:
#         middle = (high + low) // 2
#         middle_value = array[middle]

#         if middle_value == item:
#             return middle

#         elif middle_value < item:
#             low = middle + 1
#         else:
#             high = middle - 1

#     return False


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        node = self

        while True:
            if node.value > value:
                if node.left:
                    node = node.left
                else:
                    node.left = Tree(value)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = Tree(value)
                    break

    def contains(self, value, node=0):
        if node == 0:
            node = self

        if node == None:
            return False
        if node.value == value:
            return True

        if value > node.value:
            return self.contains(value, node.right)
        else:
            return self.contains(value, node.left)


tree = Tree(names_2[0])

for name in names_2[1:]:
    tree.insert(name)


# Replace the nested for loops below with your improvements
# ? the old runtime of the code is O(n^2)
for name_1 in names_1:
    if tree.contains(name_1):
        duplicates.append(name_1)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
