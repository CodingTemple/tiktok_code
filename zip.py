# don't do this

merch_items = ["T-shirt", "Hoodie", "Sticker"]
prices = [20, 35, 5]
paired_list = []
for i in range(len(merch_items)):
    paired_list.append((merch_items[i], prices[i]))
print(paired_list)

# do this

merch_items = ["T-shirt", "Hoodie", "Sticker"]
prices = [20, 35, 5]
paired_list = list(zip(merch_items, prices))
print(paired_list)
