'''
2 TABLES IN DATABASE (myDiscord)

first table: users

second table: messages

'''
import pypyodbc as pyodbc
import datetime
connectString = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:testdiscord.database.windows.net,1433;Database=myDiscord;Uid=enzo_azure;Pwd=Enzane0728*;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

# yes, i know that this is not the best way to do it, but it works
class SQL_manager:
  def __init__(self):
    self.conn = pyodbc.connect(connectString)
    self.cursor = self.conn.cursor()
    # self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id VARCHAR(255), name VARCHAR(255), firstname VARCHAR(255), password VARCHAR(255), email VARCHAR(255))")
    # 'IF NOT EXISTS' non supporté sur les serveurs Azure    
    # self.cursor.execute("CREATE TABLE IF NOT EXISTS messages (id VARCHAR(255), author_id VARCHAR(255), content VARCHAR(255), created_at VARCHAR(255))")
    self.conn.commit()
    print('SQL manager initialized')
    
  def create_user(self, name, lastname, password, email ):
    if not self.check_user(email):
        insert_query = "INSERT INTO users (name, firstname, password, email) VALUES (?, ?, ?, ?)"
        values = (name, lastname, password, email)
        self.cursor.execute(insert_query, values)
        self.conn.commit()
        print("User inserted successfully!")
    else:
        print("User already exists.")
  def check_user(self, email):
    print(email)
    self.cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    if self.cursor.fetchone() is not None:
      return True
    else:
      return False
  def login(self, email, password):
    self.cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    if self.cursor.fetchone() is not None:
      return True
    else:
      return False
  
  def add_message(self, message):
    self.cursor.execute("SELECT * FROM messages WHERE id=%s", (message.id,))
    if self.cursor.fetchone() is None:
      self.cursor.execute("INSERT INTO messages VALUES (%s, %s, %s, %s)", (message.id, message.author.id, message.content, message.created_at))
      self.conn.commit()

  def get_user(self, user_id):
    self.cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    return self.cursor.fetchone()

  def get_message(self, message_id):
    self.cursor.execute("SELECT * FROM messages WHERE id=%s", (message_id,))
    return self.cursor.fetchone()

  def get_all_messages(self):
    self.cursor.execute("SELECT * FROM messages")
    return self.cursor.fetchall()

  def get_all_users(self):
    
    self.cursor.execute("SELECT * FROM users")
    return self.cursor.fetchall()

  def get_all_users_messages(self):
    self.cursor.execute("SELECT * FROM users INNER JOIN messages ON users.id = messages.author_id")
    return self.cursor.fetchall()

  def get_all_users_messages(self):
    self.cursor.execute("SELECT * FROM users INNER JOIN messages ON users.id = messages.author_id")
    return self.cursor.fetchall()

  def get_all_users_messages(self):
    self.cursor.execute("SELECT * FROM users INNER JOIN messages ON users.id = messages.author_id")
    return self.cursor.fetchall()

  def get_all_users_messages(self):
    self.cursor.execute("SELECT * FROM users INNER JOIN messages ON users.id = messages.author_id")
    return self.cursor.fetchall()

tests = SQL_manager()

print(tests)
