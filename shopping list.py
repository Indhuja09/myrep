print("Shopping List")


shoppingList = []
finished = False
while not finished:
        Item = input("Please enter an item for your list: ")
        if len(Item) == 0:
            finished = True
        else:
             shoppingList.append(Item)

print(item)
