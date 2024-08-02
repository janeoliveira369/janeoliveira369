from google.colab import drive
drive.mount('/content/drive')
file = open('Arquivo_tarefas.txt', 'w')
file.write("Olá, mundo!\n")
#Criar lista
lista_de_tarefas = []

#Menu de escolha
def menu():
    print('''
🅻🅸🆂🆃🅰 🅳🅴 🆃🅰🆁🅴🅵🅰🆂
        ''')
    print('''1- Adicionar tarefas''')
    print('''2- Visualizar tarefas''')
    print('''3- Remover tarefas''')
    print('''4 - Sair
          ''')

#Adicionar tarefas
def adicionar_tarefa():
    tarefa = input('\nDigite a tarefa que deseja incluir: ')
    lista_de_tarefas.append(tarefa)
    print (f'\nTarefa {tarefa} incluída com sucesso')
#Visualizar tarefas
def visualizar_tarefas():
    if lista_de_tarefas == []:
        print ('\nNão há tarefas na lista')
    else:
        for tarefa in lista_de_tarefas:
            # o +' na funcao abaixo vai definir que a lisa de tarefas nao comece no 0
            print (f'\n{lista_de_tarefas.index(tarefa) + 1} - {tarefa}')
#Remover tarefas
def remover_tarefa():
    visualizar_tarefas()
    if lista_de_tarefas == []:
       main ()
    else:
        retirar = int(input('Digite a tarefa a retirar: '))-1
        print(f'A tarefa {lista_de_tarefas[retirar]} foi retirada com sucesso! ')
        lista_de_tarefas.pop(retirar) 
        
#Opção de escolha
def main():
    while True:
        try:
            menu()
            opcao = int(input('\nDigite a opção desejada: '))
            print (opcao)
            if opcao == 1:
                print('Adicionar tarefa')
                adicionar_tarefa()
            elif opcao==2:
                print('Visualizar tarefa ')
                visualizar_tarefas()    
            elif opcao==3:
                print('Remover tarefa')
                remover_tarefa()
            elif opcao==4:
                print('Sair')
                break
            else: 
                print('Opção invalida')
        except:
            print ('Digite uma opção valida: ')
main ()