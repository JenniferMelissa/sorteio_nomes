#biblioteca gera numeros aleatorios
import random 

nomes = []

while True:
    print(' 1 - Inserir nome na lista: ')
    print(' 2 - Sortear.')
    print(' 3 - Sair do Programa.')

    opcao = input('Opção desejada: ')

    match opcao:
        case '1':
            nome = input('Insira o nome: ')
            nomes.append(nome)
            print(f'{nome} inserido com sucesso.')
            continue
        case '2':
            #coloca o -1 pois o len vai retornar 1 numero a mais, se o numero da lista foi 10 ele retorna 10, mas nao contabiliza o 0 do indice, por isso o  menos -1, para que fique exato o tanto de nomes cadastrados, e nao um a mais
            indice_sorteado = random.randint(0,len(nomes)-1)
            print(f'Nome sorteado: {nomes[indice_sorteado]}.')
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida!')
            continue
