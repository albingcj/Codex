'''Anagrams'''


def groupAnagrams(strs):
    d = {}
    for i in strs:
        x = "".join(sorted(i))
        if x not in d:
            d[x] = [i]

        else:
            d[x].append(i)
    return list(d.values())


st = ["eat", "tea", "tan", "ate", "nat", "bat"]
a = groupAnagrams(st)
print(a)