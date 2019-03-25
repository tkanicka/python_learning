prices = [5, 10, 25, 13, 42, 12, 10, 17, 25, 35]
weights = [5, 75, 15, 10, 20, 25, 20, 15, 10, 5]

items = []
ratio = []

for x in range(len(prices)):
    y = prices[x]/weights[x]
    ratio.append((y,x))
ratio.sort(reverse=True)

for x in range(len(ratio)):
    y = ratio[x][1]
    items.append([prices[y], weights[y]])


def dfs_knapsack(capacity, items, current_value = 0, current_weight = 0, index = 0, best = 0, added_items = [], current_items =[]):

    while current_weight < capacity and index < len(items):
        if items[index] not in added_items:
            if current_weight + items[index][1] <= capacity:
                added_items.append(items[index])
                current_items.append(items[index])
                current_weight += items[index][1]
                current_value += items[index][0]
                index += 1
            else:
                index += 1

        else:
            index += 1

    if current_value > best:
        best = current_value

    if len(current_items) == 1:
        return best

    else:
        index = items.index(current_items[-2])
        last_v = current_items[-1][0]
        last_w = current_items[-1][1]
        current_items.pop()
        return dfs_knapsack(capacity, items, current_value - last_v, current_weight - last_w, index, best, added_items, current_items)


bag_capacity = float(input("enter your bag weight capacity: "))
if bag_capacity < min(items[:len(items)][1]):
    print("nothing can be added into your bag")
else:
    print(dfs_knapsack(bag_capacity, items))
