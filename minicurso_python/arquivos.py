##################################
# r -> somente leitura
# w -> escrita (se o arquivo ja existir
#               será apagado e um novo 
#               vazio será criado)
# a -> leitura e escrita (adiciona o
#               novo conteúdo no fim 
#               do arquivo)
# r+ -> leitura e escrita
# w+ -> escrita (tambem apaga o conteúdo)
# a+ -> leitura e escrita (abre o arquivo
#               para atualização)

arq = open("arquivo.txt")

#linhas = arq.readlines()
#print(linhas)

texto_completo = arq.read()
print(texto_completo)

##########################################
arq2 = open("arquivo2.txt", "a")
arq2.write("Escrevendo no arquivo 2\nEsse é meu arquivo\n")
arq2.close()