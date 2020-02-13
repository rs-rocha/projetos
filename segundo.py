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
print('-'*18)
for dado in dados:
    print(f'{dado[0]:<7} {dado[1]:20} {dado[2]:>6}')
print('-'*35)
print(f'Encontrados {len(dados)} registros')
print('\n\nFim do programa.')