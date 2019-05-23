def isPossible(word):
    i = 0
    j = len(word) - 1
    while i <= j:
        if word[i] != word[j]:
            if word[i] < word[j]:
                if chr(ord(word[i]) + 1) != chr(ord(word[j]) - 1):
                    return False
            else:
                if chr(ord(word[i]) - 1) != chr(ord(word[j]) + 1):
                    return False
        i += 1
        j -= 1

    return True

n = int(raw_input())
testCases = []
for i in range(n):
    lengthTest = int(raw_input())
    testCases.append("YES" if isPossible(raw_input()) else "NO")

print "\n".join(testCases)