textoImpresso = ""

  nome = recuperaValorArquivo("nome.txt")
  nota1 = recuperaValorArquivo("nota-cert-1.txt")
  nota2 = recuperaValorArquivo("nota-cert-1.txt")
  nota3 = recuperaValorArquivo("nota-cert-1.txt")
  
textoImpresso += "Nota de " += nome += float(int(nota1 + nota2 + nota3)/3))
print(textoImpresso))
