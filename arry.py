'''grcy=[["apple",1.0,5],["orange",10.0,5],["apple",10.0,10]]
item with highest total selling price >> cost*no.of items.
total selling price of all items >> cost*no.of.items for all the items.
average selling price per item. >> no of items sold/total selling price'''
grcy=[["apple",1.0,5],["orange",10.0,5],["apple",10.0,10]]
item1_selling_price=0
item2_selling_price=0
num_of_item1_sold=0
num_of_item2_sold=0
item1_avg_selling_price=0
item2_avg_selling_price=0
selling_price_all_items=0
for i in range(len(grcy)):
    if grcy[i][0]=="apple":
        item1_selling_price+=grcy[i][1]*grcy[i][2]
        num_of_item1_sold+=grcy[i][2]
        item1_avg_selling_price+=item1_selling_price/num_of_item1_sold
    elif grcy[i][0]=="orange":
        item2_selling_price+=grcy[i][1]*grcy[i][2]
        num_of_item2_sold += grcy[i][2]
        item2_avg_selling_price+=item2_selling_price/num_of_item2_sold
selling_price_all_items+=item1_selling_price+item2_selling_price
print("max selling price is:",item1_selling_price)if item1_selling_price>item2_selling_price else item2_selling_price
print(f"total selling price of all items is:{item1_selling_price+item2_selling_price}")
print(f"average selling price of apple is:{item1_avg_selling_price}")
print(f"average selling price of orange is:{item2_avg_selling_price}")