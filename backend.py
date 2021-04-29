import database
import os

def login():
    os.system('cls')

    print("=========== Login ===========")
    user = input("Username: ")
    password = input("Senha: ")

    database.cursor.execute("""
        SELECT * FROM users
        WHERE (username = ? and password = ?)
    """, (user, password))

    verify_login = database.cursor.fetchone()

    try:
        if (user in verify_login and password in verify_login):
            print("Acesso Confirmado. Bem-vindo!")
        os.system('pause')
        main()
    except:
        print("Acesso Negado. Verifique os dados inseridos.")
        os.system('pause')
        login()


def register():
    os.system('cls')

    print("=========== Register ===========")
    nome = input("Nome: ")
    email = input("Email: ")
    user = input("Username: ")
    password = input("Senha: ")

    if (nome == "" or email == "" or user == "" or password == ""):
        print("Preencha todos os campos!")
        os.system('pause')
        register()
    else:
        database.cursor.execute("""
            INSERT INTO users (name, email, username, password) VALUES(?, ?, ?, ?)
        """, (nome, email, user, password))

        database.db.commit()

        print("Conta cadastrada com sucesso!")
        os.system('pause')
        main()


def main():
    os.system('cls')

    print("=========== Menu ===========")
    opcao = int(input("[1] Login \n[2] Register \n[3] Sair \n"))

    if (opcao == 1):
        login()
    elif (opcao == 2):
        register()
    elif (opcao == 3):
        exit()
    else:
        print("Digite uma opcao valida")
        main()


if __name__ == '__main__':
    main()
