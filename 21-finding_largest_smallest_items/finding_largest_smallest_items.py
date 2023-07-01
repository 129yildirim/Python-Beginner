import heapq

grades = [32, 43, 654, 34, 312, 78, 215]
print(heapq.nlargest(2, grades))

stocks = [
    {'key11':'value11', 'price':12},
    {'key11':'value21', 'price':22},
    {'key11':'value31', 'price':32},
    {'key11':'value41', 'price':42}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))