import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', password='root', database='mysql', charset='utf8')
cursor = connection.cursor(dictionary=True)

# CREATE
# cursor.execute("INSERT INTO users(nome, idade) VALUES('Leonardo', 19)")
# cursor.execute("INSERT INTO users(nome, idade) VALUES('Russo', 17)")
# cursor.execute("INSERT INTO users(nome, idade) VALUES('Joao', 18)")
# connection.commit()



# DELETE
# cursor.execute("Delete from users WHERE id='3'")
# connection.commit()


# READ
# cursor.execute("SELECT idade FROM users WHERE nome='Leonardo'")
# users = cursor.fetchall()
# print(users)


# UPDATE
# cursor.execute("SELECT * from users WHERE id='1'")
# cursor.execute("UPDATE users SET nome='Jonaxx' WHERE id=1 ")
# connection.commit()
