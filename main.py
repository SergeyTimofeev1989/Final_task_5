purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

min_price = float(input())


def total_revenue(purchases):
    revenue = 0
    for purchase in purchases:
        revenue += purchase["price"] * purchase["quantity"]
    return revenue


def items_by_category(purchases):
    items = dict()
    for purchase in purchases:
        if purchase["category"] in items:
            items[purchase["category"]].append(purchase["item"])
        else:
            items[purchase["category"]] = [purchase["item"]]
    return items


def expensive_purchases(purchases, min_price):
    items = list()
    for purchase in purchases:
        if purchase["price"] >= min_price:
            items.append(purchase)
    return items


def average_price_by_category(purchases):
    items = dict()
    for purchase in purchases:
        if purchase["category"] in items:
            items[purchase["category"]].append(purchase["price"])
        else:
            items[purchase["category"]] = [purchase["price"]]

    for item in items:
        items[item] = sum(items[item]) / len(items[item])
    return items


def most_frequent_category(purchases):
    items = dict()
    for purchase in purchases:
        if purchase["category"] in items:
            items[purchase["category"]].append(purchase["quantity"])
        else:
            items[purchase["category"]] = [purchase["quantity"]]

    for item in items:
        items[item] = sum(items[item])

    return max(items)


print(F"Общая выручка: {total_revenue(purchases)}")
print(F"Товары по категориям: {items_by_category(purchases)}")
print(F"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
print(F"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(F"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")
