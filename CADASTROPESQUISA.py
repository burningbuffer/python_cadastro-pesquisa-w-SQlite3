import sqlite3, time
from datetime import datetime

conn = sqlite3.connect('agenda.db')
c = conn.cursor()
now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

def criar_db():
    c.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, telefone varchar, email text, data text)')


d = now.strftime('%d/%m/%Y')

def inserir_db(n, t, e):
    
    c.execute('INSERT INTO cadastro VALUES(?,?,?,?)',(n, t, e, d))
    conn.commit()

def pesquisar_db(p):
    sql = 'SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql,(p,)):
        print(row)

def pesquisar_todos_db():
    todos = 'SELECT * FROM cadastro'
    for row2 in c.execute(todos):
        print(row2)
    

"""
try:
    criar_db()
except:
    print('Erro ao criar o banco de dados ')
else:
    print('Banco de dados criado com sucesso !')
"""

print("1 - Cadastrar")
print("2 - Pesquisar")
print("3 - Visualizar todos")
question = int(input("O que deseja fazer ?: "))

# CADASTRO
if question == 1:
    try:
        print("Cadastro Agenda")
        time.sleep(2)
        n = str(input("Digite seu nome: "))
        t = int(input("Digite um telefone: "))
        e = str(input("Digite seu email: "))
        inserir_db(n, t, e)
    except:
        print("Erro ao cadastrar")
    else:
        print("Cadastrado com sucesso")

# PESQUISA
elif(question == 2):
    try:
        print("Pesquisa Agenda")
        time.sleep(2)
        p = str(input("Digite para pesquisar: "))
        pesquisar_db(p)
    except:
        print("Erro ao pesquisar")
        
elif(question == 3):
    try:
        print("Todos")
        time.sleep(2)
        pesquisar_todos_db()
    except:
        print("Erro ao visualizar")

    
