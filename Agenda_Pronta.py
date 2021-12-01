import os
os.system('cls') #limpar o terminal

#funções para base do sistema de escrita e configuração:

listacontatos = []
def salvarcontatos(listacontatos): #salvar contato no documento txt
    with open("agenda.txt","w") as agenda:
        for contatos in listacontatos:
            agenda.write("{}|{}|{}\n".format(contatos["email"], contatos["nome"], contatos["tel"]))

def carregarcontatos(): #carregar contatos para lista
    listacontatos = []
    with open("agenda.txt", "r") as agenda:
        for linhas in agenda.readlines():
            colunas = linhas.strip().split("|")

            contatos = {
                "email": colunas[0], "nome": colunas[1], "tel": colunas[2]
                }
            listacontatos.append(contatos)
    return listacontatos

def existenciacontato(listacontatos, email): #existencia do contato
    if len(listacontatos) > 0:
        for contato in listacontatos:
            if contato["email"] == email:
                return True
    return False

#FUNÇÕES BASICAS

def insere(listacontatos): #vou usar email como forma de chave para achar o contato
    while True:

        email = input("Digite o e-mail do contato: ").lower()
        if not existenciacontato(listacontatos, email):
            break
        else:
            print("Email já utilizado.")
            print("Tente novamente, insira outro email.")
    contatos = {
            "email": email, "nome": input("Digite o nome: ").strip(), "tel": input("Digite o telefone: ").strip()
        }
    listacontatos.append(contatos)
    print("O contato {} foi salvo.\n". format(contatos["nome"]))

def remove(listacontatos): #remover contatos
    print("============Excluir Contatos============")
    if len(listacontatos) > 0:
        email = input("Digite o e-mail do contato que você deseja apagar: ")
        if existenciacontato(listacontatos ,email):
            for i, contatos in enumerate(listacontatos):
                if contatos["email"] == email:
                    print("Segue as informações deste contato: ")
                    print("\tNome: {}".format(contatos["nome"]))
                    print("\tE-mail: {}".format(contatos["email"]))
                    print("\tTelefone: {}".format(contatos["tel"]))
                    print("==============================")
                    del listacontatos[i]
                    print("contato apagado com email {}.".format(contatos["email"]))
                    break
        else:
            print("Não há contatos com o email: {}.".format(email))
    else:
        print("Ainda não há contatos nesta agenda.")

def edita(listacontatos): #editar contatos
    print("============Editar Contatos============")
    if len(listacontatos) > 0:
        email = input("Digite o contato que você busca: ")
        if existenciacontato(listacontatos ,email):
            for contatos in listacontatos:
                if contatos["email"] == email:
                    print("Segue as informações deste contato: ")
                    print("\tNome: {}".format(contatos["nome"]))
                    print("\tE-mail: {}".format(contatos["email"]))
                    print("\tTelefone: {}".format(contatos["tel"]))
                    print("==============================")

                    contatos["nome"] = input("Digite o novo nome do contato: ")
                    contatos["tel"] = input("Digite o novo telefone do contato: ")
    
                    print("O contato com email {} foi alterado com sucesso".format(contatos["email"]))
                    break
        else:
            print("Não há contatos com o email: {}.".format(email))
    else:
        print("Ainda não há contatos nesta agenda.")

def buscar(listacontatos): #procurar contatos
    print("============Busca de Contatos============")
    if len(listacontatos) > 0:
        email = input("Digite o contato que você busca: ")
        if existenciacontato(listacontatos ,email):
            for contatos in listacontatos:
                if contatos["email"] == email:
                    print("Segue as informações deste contato: ")
                    print("\tNome: {}".format(contatos["nome"]))
                    print("\tE-mail: {}".format(contatos["email"]))
                    print("\tTelefone: {}".format(contatos["tel"]))
                    print("==============================")
                    break
        else:
            print("Não há contatos com o email: {}.".format(email))
    else:
        print("Ainda não há contatos nesta agenda.")



def listar(listacontatos): #mostrar contatos
    if len(listacontatos) > 0:
        print("============Listar contatos============")
        for i, contatos in enumerate(listacontatos):
            print("Contato {}".format(i+1))
            print("\tNome: {}".format(contatos["nome"]))
            print("\tE-mail: {}".format(contatos["email"]))
            print("\tTelefone: {}".format(contatos["tel"]))
            print("==============================")
    else:
            print("não há contatos")

def principal(): #Função principal (para cada condição que o documento.txt terá uma função para salvar o documento alterado)
    listacontatos = carregarcontatos()
    escolha = 0
    while escolha != 6:
        print('____Agenda Telefonica___')
        print(' 1 - Adicionar contado')
        print(' 2 - Editar contato')
        print(' 3 - Excluir contato')
        print(' 4 - Buscar contato')
        print(' 5 - Listar contatos')
        print(' 6 - Sair')
        escolha = int(input(''))

        if escolha == 1:
            insere(listacontatos)
            salvarcontatos(listacontatos)

        elif escolha == 2:
            edita(listacontatos)
            salvarcontatos(listacontatos)

        elif escolha == 3:
            remove(listacontatos)
            salvarcontatos(listacontatos)

        elif escolha == 4:
            buscar(listacontatos)
            
        elif escolha == 5:
            listar(listacontatos)

        elif escolha == 6:
            print("Obrigado por utilizar o editor de agendas, até mais tarde")
principal()
