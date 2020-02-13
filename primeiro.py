import sqlite3

conector = sqlite3.connect('academia.db')
cursor = conector.cursor()

try:
    sql = '''
        create table cadastro
        (codigo integer, nome text, idade integer)
    '''
    cursor.execute(sql)

except: 
    print('tabela já existe')


sql = '''
    insert into cadastro
    (codigo, nome, idade) values (1284, 'Pedro de Oliveira', 32)
'''
cursor.execute(sql)

sql = '''
    insert into cadastro
    (codigo, nome, idade) values (1309, 'Maria lucia Machado', 37)
'''
cursor.execute(sql)

conector.commit()
cursor.close()

print('Abra a pasta programa e veja se o arquivo está la')
print('fim do progrma')