def test(a,list1=[1,2]):
    if a not in list1:
        list1.append(a)
    return list1
print(test(3))  # 输出: [1, 2, 3]
print(test(4))
print(test(9,[3,5,6]))
print(test(11,[3,5,6]))