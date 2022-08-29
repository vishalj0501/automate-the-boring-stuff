def displayInventory(inventory):
    print('Inventory:')
    items=0
    for k,v in inventory.items():
        print(str(v)+" "+k)
        items+=v
    print('Total number of items: '+str(items))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i]+=1
        
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)