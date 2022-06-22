import string

class ContadorDePalavras:
    """Contador de palavras em arquivos .txt"""

    def __init__(self):
        """
        Faz a contagem e mostra as dez palavras mais frequentes no texto.
        Permite a pesquisa de pelavras específicas.
        """
        self.boas_vindas()
        self.abrir_arquivo()
        self.contagem = {}
        self.contar_palavras()
        self.montar_lista_decrescente()
        self.pesquisar_palavra()
        self.adeus()

    def boas_vindas(self):
        titulo = "Contador de palavras"
        print('\n\n{:-^80}\n'.format(titulo))
        mensagem = "Instruções: \n-Somente para arquivos .txt.\n-Há distinção "\
            f"entre letras minúsculas e maiúsculas. Pesquise suas palavras\n" \
            f"utilizando sempre letras minúsculas para um melhor resultado."
        print(mensagem)


    def abrir_arquivo(self):
        while True:
            filename = input('\nDigite o nome completo do arquivo (.txt): ')
            if filename == 'q':
                exit()
            try:
                self.arquivo = open(filename, encoding='utf-8')
                break
            except:
                mensagem = '\nO arquivo não pode ser aberto.\nVerifique o ' \
                    'nome do arquivo e tente novamente ou pressione "q" ' \
                    'para sair.\n'
                print(mensagem)
                continue

    def contar_palavras(self):
        for linha in self.arquivo:
            linha = linha.translate(str.maketrans('', '', string.punctuation))
            linha = linha.lower()
            palavras = linha.split()
            for palavra in palavras:
                self.contagem[palavra] = self.contagem.get(palavra, 0) + 1

    def montar_lista_decrescente(self):
        lst = []
        for key, val in list(self.contagem.items()):
            lst.append((val, key))
        lst.sort(reverse=True)
        mensagem = '\nAs dez palavras que mais aparecem no arquivo são: \n'
        print(mensagem)
        for key, val in lst[:10]:
            print(key, val)

    def pesquisar_palavra(self):
        pergunta = input("\nDeseja pesquisar uma palavra específica? (S/n): ")
        while True:
            if pergunta == 'S':
                palavra = input("Digite a palavra: ")
                contagem = self.retornar_palavra(palavra)
                print(f"Foram encontradas {contagem} palavras '{palavra}'")
                pergunta = input("\nDeseja pesquisar outra palavra? (S/n): ")
            elif pergunta == 'n':
                break
            else:
                continue

    def retornar_palavra(self, palavra):
        try:
            contagem_palavra = self.contagem[palavra]
        except:
            contagem_palavra = 0
        return contagem_palavra

    def adeus(self):
        titulo = "Obrigado e até logo"
        print('\n\n{:-^80}\n\n'.format(titulo))


if __name__ == '__main__':
    run = ContadorDePalavras()
