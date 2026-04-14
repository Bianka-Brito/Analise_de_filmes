import unicodedata 

#normaliza o texto 
def remover_acentos(texto):
    texto=unicodedata.normalize('NFD', texto)
    texto= ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

filmes = [ ]

with open("filmes.csv", "r", encoding="utf-8") as arquivo:
    next(arquivo) #pula cabeçalho
    for linha in arquivo: 
        linha= linha.strip()
        
        if not linha: #ignora linha vazia
            continue 

        dados= linha.split(',') #indica que os dados estão separados por virgula 

        if len(dados) < 3: 
            continue 

        #indice de cada dado 
        nome= remover_acentos(dados[0].strip().title())
        genero = remover_acentos(dados[1].lower().strip())
        nota= float(dados[2])

        filmes.append([nome, genero, nota])

#menu principal 
while True:
    print('-'*20, 'Menu', '-'*20)
    print('1- Adicionar filmes \n2- Listar filmes \n3- Buscar \n4- Análises \n5- Sair')
    opcao= int(input('Digite sua escolha: '))
    print(50*'-')

    if opcao == 1: 
        nome = input('Digite o nome do filme: ').strip().title()
        nome= remover_acentos(nome.strip().title())
        genero= input('Digite o gênero do filme: ').strip()
        genero= remover_acentos(genero.lower())
        nota= float(input('Digite a nota do filme(0 a 10): '))
        
        if nota < 0 or nota > 10:
            print('Nota invalida!')
        else: 
            filmes.append([nome,genero,nota])

            with open("filmes.csv", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{nome},{genero},{nota}\n")
            
            print('Arquivo salvo!')
       

    #listar filmes 
    if opcao == 2: 
        #sub menu 
        while True: 
            print(10*'-','Escolha como listar os filmes', 10*'-')
            print('1- Todos \n2- Por gênero \n3- Recomendados (nota =>7) \n4- Voltar')
            escolha=int(input('Como você quer ver: '))
            print(50*'-')

            if escolha == 1:
                for i in filmes:
                    print(f'{i[0]} - {i[1]} - {i[2]}')
            
            elif escolha == 2: 
                    genero_busca=input('Digite o gênero escolhido: ')
                    genero_busca=remover_acentos(genero_busca.lower().strip())
                    encontrou = False
                    
                    for g in filmes: 
                        if g[1] == genero_busca:
                            print(f'{g[0]} - {g[1]} - {g[2]}')
                            encontrou = True #se encontrou o genero para aqui e não executa proxim linha 
                    
                    if not encontrou:
                        print('Genêro invalido!')
            
            #filmes com notas igual ou maiores que 7 
            elif escolha == 3: 
                for f in filmes: 
                    if f[2] >= 7:
                        print(f'{f[0]} - {f[1]} - {f[2]}')
            
            elif escolha == 4:
                break

    #menu para pesquisar o filme 
    if opcao == 3: 
        
            
            nome_filme= input('Digite o nome do filme que você está prourando: ')
            nome_filme= remover_acentos(nome_filme.strip().title())
            encontrou_filme= False 

            for n in filmes:
                if n[0] == nome_filme:
                    print(f'{n[0]} - {n[1]} - {n[2]}')
                    encontrou_filme= True 
        
            if not encontrou_filme:
                print('Filme invalido')

            

    #menu de analises 
    if opcao == 4:
        while True: 
            print('1- Melhor nota \n2- Pior nota \n3- Quantidade por gênero \n4- Top 3 \n5- Voltar')
            selecione= int(input('Digite sua escolha: '))
            print(50*'-')

            #melhor nota
            if selecione == 1:
                maior= filmes[0]
                for c in filmes: 
                    if c[2] > maior[2]: 
                        maior = c
                print(f'O filme com a melhor nota é: {maior[0]} - {maior[1]} - {maior[2]}')
                print(70*'-')
            
            #pior nota
            elif selecione == 2:   
                menor= filmes[0]
                for m in filmes: 
                    if m[2] < menor[2]: 
                        menor = m
                print(f'O filme com a pior nota é: {menor[0]} - {menor[1]} - {menor[2]}')
                print(70*'-')
            
            #quantidade de filmes por genero 
            elif selecione == 3:

                contagem = { }

                for g in filmes: 
                    genero = g[1]
                    if genero in contagem:
                        contagem[genero] += 1
                    else:
                        contagem[genero] = 1
                
                for genero,quantidade in contagem.items(): #mostrar o resultado 
                    print(f'{genero}: {quantidade}')
                print(50*'-')

            #top 3
            elif selecione == 4: 
                nova_lista= sorted(filmes, key=lambda x: x[2], reverse=True)
                print(20*'-','Top 3 filmes',20*'-')
                for n in nova_lista[:3]:
                    print(f'{n[0]}, {n[1]}, {n[2]}')
                print(50*'-')

            elif selecione == 5: 
                break 

    else:
        break 