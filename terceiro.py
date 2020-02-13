import sqlite3

def exibe_dados(lista):
    '''Exibe uma saida formatada dos dados contidos na Lista'''
    print('\nConsulta ao Banco de Dados "academia.db"\n')
    print('Dados da tabela "cadastro"')
    print('-'*35)

    print(f'{"Código":7} {"Nome":20} {"Idade":>6}')
    print('- '*18)
    for d in lista:
        print(f"{d[0]:<7} {d[1]:20} {d[2]:>6}")
    print('-'*35)
    print(f'Encontrados {len(dados)} registros')

conector = sqlite3.connect('academia.db')
cursor = conector.cursor()
sql = '''
    insert into cadastro
    (codigo, nome, idade) values (?, ?, ?)
'''
print('Digite os dados separados por vígulas')
print('Código, Nome, Idade')

Ler = input()
while Ler !='':
    D = Ler.split(',')
    try:
        cursor.execute(sql, D)
        conector.commit()
    except:
        print(f'{D} Dados inválidos')
    else:
        print('.'*30, '...dados inseridos com sucesso')
    finally:
        print('Codigo, Nome, idade')
    Ler = input()

sql = 'select * from cadastro'
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close
conector.close

exibe_dados(dados)
print('\n\nFim do programa')

