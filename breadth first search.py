
'''
my_dict = {'key1': [3, 8], 'key2': [6, 5], 'key3': [8, 2], 'key4': [4, 9]}

sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1][0])}

print(sorted_dict)
'''

'''
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = {}
    l = [[] for r in range(len(nums))]
    for ele in nums:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    for x, y in d.items():
        l[y - 1].append(x)
    print(l)
    r = []
    for i in range(len(l) - 1, -1, -1):
        if len(r) < k and l[i] != []:
            r.extend(l[i])
    print(r[:k])
topKFrequent([1,1,1,2,2,3,4,4,5,6,2,2,2,2,3,1],3)
'''
######################################################

'''d = {}
l = [1,1,1,2,2,3,4,4,5,6]
for i in l:
    d[i] = d.get(i, 0) +1
print(d)'''
#################################################################################

'''from numpy import unique

my_array = [1, 2, 3, 2, 1, 2, 4, 5, 4, 2]
unique_elements, element_counts = unique(my_array, return_counts=True)

result = {element: count for element, count in zip(unique_elements, element_counts)}

print(result)
'''

##################################################################################

