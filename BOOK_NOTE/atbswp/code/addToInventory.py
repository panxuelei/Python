def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print('Total number of items: ' + str(item_total))

#更新物品清单的函数
def addToInventory(inventory, addedItems):
	for loot in addedItems:
		if loot in inventory:
			inventory[loot] = inventory[loot] + 1
		else:
			inventory[loot] = 1
	return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)