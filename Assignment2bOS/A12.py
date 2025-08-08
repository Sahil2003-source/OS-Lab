words = ["eat", "ate", "tea", "bat", "tab", "tan", "ant", "net", "ten"]

anagrams = {}

for word in words:
    key = ''.join(sorted(word))
    if key in anagrams:
        anagrams[key].append(word)
    else:
        anagrams[key] = [word]

for group in anagrams.values():
    if len(group) > 1:
        print(group)
