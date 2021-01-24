from time import sleep


def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {arq} criado com sucesso.')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print('------- PROCESSOS CADASTRADOS -------')
        for linha in a:
            dado = linha.split()
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]}{dado[1]}{dado[2]}')
    finally:
        a.close()


def cadastrar(arq, processo, ano, local):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{processo}/{ano} - {local}\n')
        except:
            print('Houve um ERRO na hora de ler os dados.')
        else:
            print(f'Novo processo {processo}/{ano} adicionado.')
            a.close()


def excluir(processo, ano, local):
    try:
        a = open(arq, 'r+')
        a.truncate(0)

    except:
        print('Houve um ERRO na exclusão do arquivo')
    else:
        print(f'Processo {processo}/{ano} - {local}, excluido.')


def menu(lista):
    print('---------- MENU PRINCIPAL -----------')
    c = 1
    for item in lista:
        print(f' \033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    opc = int(input("Sua opção: "))
    return opc


arq = 'processos.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

print("PROCESSOS DE VIABILIDADE")

while True:
    opc = menu(['Ver processos', 'Cadastrar processo', 'Excluir processo', 'Sair do sistema'])
    if opc == 1:
        # Listar processos
        lerArquivo(arq)
    elif opc == 2:
        # Opção cadastrar novo processo
        print('---------- NOVO PROCESSO ----------')
        processo = int(input("Informe o número do processo: "))
        ano = int(input("Informe o ano do processo: "))
        local = str(input("Informe o local aonde está o processo: "))
        cadastrar(arq, processo, ano, local)
    elif opc == 3:
        # excluir processo
        print('---------- EXCLUIR PROCESSO ----------')
        processo = int(input("Informe o número do processo: "))
        ano = int(input("Informe o ano do processo: "))
        local = str(input("Informe o local aonde está o processo: "))
        excluir(processo, ano, local)
    elif opc == 4:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro. Digite uma opção valida!')
    sleep(3)
