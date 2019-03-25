# tohle je asi nejvíc debilní způsob jak to dělat vzhledem k tomu,
# že tesuju u každý položky 2 případy (použiju, nepoužiju) a pak to mezi sebou porovnávám...
# opravdu mě ale nenapadá nic lepšího(rychlejšího a jednoduššího) než testovat všechny kombinace
# i když předpokládám, že s tímhle mě asi pošleš doháje...

item_price = [5, 10, 25, 13, 42, 12, 10, 17, 25, 35]
item_weight = [5, 75, 15, 10, 20, 25, 20, 15, 10, 5]

bag_capacity = float(input("enter your bag weight capacity: "))


def max_bag_value(bag_capacity, item_price, item_weight, n = 0):

    if n == len(item_weight) or bag_capacity <= 0:
        return 0

    if item_weight[n] <= bag_capacity:
        n += 1
        return max(item_price[n-1] + max_bag_value(bag_capacity-item_weight[n-1], item_price, item_weight, n),
                   max_bag_value(bag_capacity, item_price, item_weight, n))

    else:
        n += 1
        return max_bag_value(bag_capacity, item_price, item_weight, n)

    
print(max_bag_value(bag_capacity, item_price, item_weight, 0))
