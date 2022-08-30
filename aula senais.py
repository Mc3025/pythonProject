import sqlite3

conexão = sqlite3.connect('dbsenai.db')
cursor= conexão.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS cliente('
               'id INETEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'idade INTEGER'
               ')')
cursor.execute('INSERT INTO cliente ( nome, idade') VALUES ("Marco")'')
    