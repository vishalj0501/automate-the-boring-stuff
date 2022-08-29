def displayInventory(inventory):
    print('Inventory:')
    items=0
    for k,v in inventory.items():
        print(str(v)+" "+k)
        items+=v
    print('Total number of items: '+str(items))

inventory1={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(inventory1)