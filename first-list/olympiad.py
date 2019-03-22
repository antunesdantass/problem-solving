quantidadeDePessoas = int(raw_input())
pontuacao = set((raw_input()).split())
print (len(pontuacao) - 1) if "0" in pontuacao else (len(pontuacao))
