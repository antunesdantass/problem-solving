vowel = set(['a', 'e', 'i', 'o', 'u'])
word = str(raw_input())
isIt =  True
for i in range(1, len(word)):
    prev = word[i - 1]
    if prev not in vowel:
        if prev != 'n' and word[i] not in vowel:
            isIt = False
            break
    if i == len(word) -1 and word[i] != 'n' and word[i] not in vowel:
        isIt = False

if len(word) == 1 and word not in vowel and word != 'n':
    isIt = False

print "YES" if isIt else "NO"         