import csv
from datetime import datetime
#This class includes seperating and storing data from each of the 4 categories in the csv file 

class treeNode:
    def __init__(self, date, category, item, price):
        self.date = date
        self.category = category
        self.item = item
        self.price = price
        self.left = None
        self.right = None

class listNode:
    def __init__(self, date, category, item, price):
        self.date = datetime.strptime(date, '%m-%d-%Y')  # Convert date string to datetime object
        self.category = category
        self.item = item
        self.price = price
        self.next = None
        self.prev = None

def extract_data_from_csv(filename: str):
    list_nodes = []
    tree_nodes = []

    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Extract data from each row
                date = row['date'].strip()  # Stripping any extra spaces
                category = row['category'].strip()
                item = row['item'].strip()
                price = float(row['price'])  # Convert price to float

                # Create a listNode instance
                list_node = listNode(date, category, item, price)
                list_nodes.append(list_node)

                # Create a treeNode instance
                tree_node = treeNode(date, category, item, price)
                tree_nodes.append(tree_node)

        print(f"Extracted {(len(list_nodes))} list nodes and {(len(tree_nodes))} tree nodes from {filename}")
        return list_nodes, tree_nodes

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
filename = "October.csv"
list_nodes, tree_nodes = extract_data_from_csv(filename) #Array of all extracted nodes from csv

# def test_tree_node(nodes): #Test if node is valid
#     date = "2024-10-09"
#     category = "entertainment"
#     item = "leagueRP"
#     price = 23.98
#     node = nodes[0]
            
#     # Check if the values are assigned correctly
#     assert node.date == date, f"Expected date to be {date}, but got {node.date}"
#     assert node.category == category, f"Expected category to be {category}, but got {node.category}"
#     assert node.item == item, f"Expected item to be {item}, but got {node.item}"
#     assert node.price == price, f"Expected price to be {price}, but got {node.price}"

#     # Check if left and right pointers are initialized as None
#     assert node.left is None, f"Expected left to be None, but got {node.left}"
#     assert node.right is None, f"Expected right to be None, but got {node.right}"

#     print("All test cases passed!")

# # Run the test function
# test_tree_node(tree_nodes)

# Modify the `dateList` class to use the `datetime` objects for comparison
class dateList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, newNode):
        # Case 1: List is empty, newNode becomes head and tail
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        # Case 2: Insert before the current head if newNode's date is earlier
        elif newNode.date < self.head.date:
            newNode.next = self.head  # newNode now becomes the first node
            self.head.prev = newNode 
            self.head = newNode
        else:
            # Case 3: Traverse the list to find the right insertion point (1 before where the new node should be inserted)
            crawler = self.head
            while crawler.next is not None and crawler.next.date <= newNode.date:
                crawler = crawler.next
            
            # Insert newNode between crawler and crawler.next
            newNode.next = crawler.next
            if crawler.next is not None:
                crawler.next.prev = newNode
            newNode.prev = crawler
            crawler.next = newNode

            # Update the tail if we're inserting at the end
            if newNode.next is None:
                self.tail = newNode

    def traverseList(self, head):
        result = []
        crawler = head

        while crawler is not None:
            result.append(crawler)
            crawler = crawler.next
        return result
 
# def test_dateList_with_extracted_nodes(list_nodes):
#     date_list = dateList()

#     # Insert each node into the priceTree
#     for node in list_nodes:
#         date_list.insert(node)

#     sorted_nodes = date_list.traverseList(date_list.head)

#     result = [f"{node.price}: {node.item} ({node.date}) ({node.category})" for node in sorted_nodes]
#     print(result)

# test_dateList_with_extracted_nodes(list_nodes)


class priceTree: #Use BST for price
    def __init__(self, treeNode=None):
        self.root = treeNode

    def insert(self, newNode):
        if self.root is None:
            self.root = newNode
        else:
            self.insertHelper(self.root, newNode)

    def insertHelper(self, root, newNode):
        while root is not None:
            # Compare prices to determine left or right insertion
            if newNode.price < root.price:
                # Go to the left subtree if the new node's price is less
                if root.left is None:
                    root.left = newNode
                    break
                else:
                    root = root.left
            else:
                # Go to the right subtree if the new node's price is more or equal
                if root.right is None:
                    root.right = newNode
                    break
                else:
                    root = root.right

    def in_order_traversal(self):
        return self._in_order_recursive(self.root)

    def _in_order_recursive(self, current_node):
        result = []
        if current_node is not None:
            result.extend(self._in_order_recursive(current_node.left))
            result.append(current_node)
            result.extend(self._in_order_recursive(current_node.right))
        return result

# def test_priceTree_with_extracted_nodes(extracted_nodes):
#     price_tree = priceTree()

#     # Insert each node into the priceTree
#     for node in extracted_nodes:
#         price_tree.insert(node)

#     sorted_nodes = price_tree.in_order_traversal()

#     result = [f"{node.price}: {node.item} ({node.date}) ({node.category})" for node in sorted_nodes]
#     print(result)

# test_priceTree_with_extracted_nodes(tree_nodes)

class categoriesDict:
    def __init__(self):
        self.categories = {
            "Living": [],
            "Food": [],
            "Entertainment": []
        }

    def addNode(self, newNode):
        if newNode.category in self.categories:
            self.categories[newNode.category].append(newNode)
        else:
            print(f"{newNode.category} not recognized")
    
    def getCategory(self, category):
        return self.categories.get(category, [])

# def test_categoriesDict_with_extracted_nodes(list_nodes):
#     catDict = categoriesDict()

#     # Add each node to the categoriesDict
#     for node in list_nodes:
#         catDict.addNode(node)

#     # Retrieve nodes from each category and print the result
#     for category in ["Living", "Food", "Entertainment"]:
#         category_nodes = catDict.getCategory(category)
#         # Format the date to "MM-DD-YYYY" when printing
#         result = [f"{node.item} - ${node.price} ({node.date.strftime('%m-%d-%Y')})" for node in category_nodes]
#         print(f"{category.capitalize()} Transactions:", result)

# # Example usage: Assuming list_nodes is a list of listNode instances.
# test_categoriesDict_with_extracted_nodes(list_nodes)

class itemsList:
    def __init__(self):
        self.items = []

    def addItem(self, newNode):
        self.items.append(newNode)

    def get_sorted_items(self):
        return sorted(self.items, key=lambda x: x.item)

    def print_sorted_items(self):
        sorted_items = self.get_sorted_items()
        result = [f"{node.item} - ${node.price} ({node.date.strftime('%m-%d-%Y')}) ({node.category})"
                  for node in sorted_items]
        print("Sorted Items A-Z:", result)

# def test_item_sorter_with_extracted_nodes(list_nodes):
#     # Create an instance of ItemSorter
#     item_sorter = itemsList()

#     # Add each node to the ItemSorter
#     for node in list_nodes:
#         item_sorter.addItem(node)

#     # Print the sorted list of items
#     item_sorter.print_sorted_items()

# # Example usage: Assuming list_nodes is a list of listNode instances.
# test_item_sorter_with_extracted_nodes(list_nodes)