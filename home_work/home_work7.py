# Step 1: Create the Empty List
inventory = []


# Step 2: Function to Add Items
def add_item(item):
    """Adds a pet supply item to the inventory list."""
    inventory.append(item)


# Step 3: Recursive Function to Count Items
def count_items(items):
    """Counts the number of items in the list using recursion."""
    # Base Case: If the list is empty
    if not items:
        return 0
    # Recursive Step: Count 1 for current item + count of remaining items
    return 1 + count_items(items[1:])


# Step 4: Main Function
def main():
    # Add items to inventory
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    # Lambda function to display each item
    show_item = lambda item: print(f"Item in Stock: {item}")

    # Display all items
    for item in inventory:
        show_item(item)

    # Count total items using recursion
    total = count_items(inventory)
    print(f"\nTotal number of items in stock: {total}")


# Step 5: Run the Program
main()
