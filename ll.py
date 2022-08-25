
#     """
#     嵌套for循环实现冒泡排序
#     :param lst:
#     :return:
#     """

# lst = [22,1,31,45,63,95,9,35,62,88]
# def bubble_sort_for(lst):
# for i in range(1, len(lst)):
#     for j in range(0, len(lst) - i):
#         if lst[j] > lst[j + 1]:  # 升序用>，降序用<
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
# print(lst)



# for d in range(1, len(lst)):
#     for e in range(0, len(lst) - 1):
#         if lst[e] < lst[e + 1]:
#             lst[e], lst[e+1] = lst[e+1], lst[e]
# print(lst)








# print(lst)
#
# for x in range(len(lst)):
#     for m in range(len(lst)-1):
#         if lst[m]<lst[m+1]:
#             lst[m],lst[m+1]=lst[m+1],lst[m]
#             print(lst)
# print(lst)






# 冒泡排序
a = [1,2,3,62,56,78,12,43,555]

# for i in range(len(a)):
#     for u in range(len(a)-1):
#         if a[u] < a[u+1]:
#             a[u],a[u+1] = a[u+1],a[u]
#     print(a)




# e = 1
# while e < len(a):
#     r = 0
#     while r < len(a)-1:
#         if a[r] < a[r+1]:
#             a[r],a[r+1] = a[r+1],a[r]
#             print(a)







# for i in range(len(a)):
#     for x in range(len(a)-1):
#         if a[x] > a[x+1]:
#             a[x],a[x+1] = a[x+1],a[x]
#     print(a)





# i = 1
# while i <= 9:
#     j = 1
#     while(j <= i):    # j的大小是由i来控制的
#         print(f'{i}*{j}={i*j}', end='\t')
#         j += 1
#     print('')
#     i += 1


# 实现99乘法表
for i in range(10):
    for j in range(1,i+1):
        print(f'{j}x{i}={i*j}\t', end='')
    print()
