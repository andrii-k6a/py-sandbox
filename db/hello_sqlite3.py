import sqlite3

conn = sqlite3.connect('hello_sqlite.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS People')

cur.execute('CREATE TABLE People (email TEXT, age INTEGER)')

while input('Do you want to add a user? (yes/no) ') == 'yes':
    email = input('Enter email: ')
    age = input('Enter age: ')

    cur.execute('SELECT email FROM People WHERE email = ? ', (email,))
    row = cur.fetchone()

    if row is not None:
        print('There is an existing user with email', email, '- updating the data')
        cur.execute('UPDATE People SET age = ? WHERE email = ?', (age, email))
    else:
        print('Inserting a new user')
        cur.execute('INSERT INTO People (email, age) VALUES (?, ?)', (email, age))

    conn.commit()

select_people_sql = 'SELECT email, age FROM People ORDER BY age DESC LIMIT 10'
for row in cur.execute(select_people_sql):
    print(row)  # row is a tuple

cur.close()
conn.close()
print('Goodbye!')
