import sqlite3
conector = sqlite3.connect('academia.db')
cursor = conector.cursor()
sql = 'select * from cadastro'
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conector.close()

print('\nConsulta ao Banco de Dados "academia.db" \n')
print('Dados da tabela "cadastro"')
print('-'*35)
print(f'{"Código":<7} {"Nome":20} {"Idade":>6}')
