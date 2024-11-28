from collections import defaultdict
def isanagram(strs: list[str]) -> list[str]:
    anagrams_s = defaultdict(list)
    result = []
    
    for s in strs:
      sorted_s = tuple(sorted(s))
      anagrams_s[sorted_s].append(s)
    
    for values in anagrams_s.values():
      result.append(values)
    return result

print(isanagram(['cat','tac','hell','heck']))
print(isanagram(['eat','tea','tan','ate','nat','bat']))
print(isanagram(['aaac']))

