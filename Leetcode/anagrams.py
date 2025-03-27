from collections import defaultdict
# def isanagram(strs: list[str]) -> list[str]:

#     anagrams_s = defaultdict(list)
#     result = []
    
#     for s in strs:
#       sorted_s = tuple(sorted(s))
#       print (sorted_s)
#       anagrams_s[sorted_s].append(s)
    
#     for values in anagrams_s.values():
#       result.append(values)
#     return result

def isanagram(strs: list[str]) -> list[str]:
    anagrams_s = defaultdict(list)
    for s in strs:
        sorted_s = "".join(sorted(s))   # sorted(s) returns ['a', 'b', 'c'], while "".join(sorted(s)) returns "abc"
        print (sorted_s)
        anagrams_s[sorted_s].append(s)
    return list(anagrams_s.values())

print(isanagram(['cat','tac','hell','heck']))


# from collections import defaultdict

