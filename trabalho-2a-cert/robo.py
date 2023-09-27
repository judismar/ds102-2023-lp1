from mundo import printm

def efetua_passo(pos, mundo, passo):
	if passo == 0:
		return -1
	n = len(mundo)
	printm(pos, mundo, -1)
	for _ in range(abs(passo)): #repete 'passo' vezes
		k = (1 if passo > 0 else -1)
		if pos + k < 0 or pos + k == n:
			return (-2 if pos + k < 0 else -3)
		if mundo[pos + k] == 1:
			printm(pos, mundo, pos+k)
			return pos + k
		else:
			pos += k
		printm(pos, mundo, -1)
	return -1

def cratera_na_esquerda(pos, mundo):
	return pos == 0

def cratera_na_direita(pos, mundo):
	return pos == len(mundo) - 1
