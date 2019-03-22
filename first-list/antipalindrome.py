def antipalindrome(word):
	palindromo = ehPalindromo(word)
	if palindromo and len(word) > 1:
		return antipalindrome(word[:-1])
	elif palindromo and len(word) == 1:
		return 0
	else:
		return len(word)
	
def ehPalindromo(word):
	arrayPalavrasReversas = map(lambda letra: letra, word)
	arrayPalavrasReversas.reverse()
	return ''.join(arrayPalavrasReversas) == word

palavra = raw_input()

print antipalindrome(palavra)
