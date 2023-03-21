'''
2 TABLES IN DATABASE (myDiscord)

first table: users

second table: messages

'''

import sqlite3
import datetime

class SQL_manager:
  def __init__(self, db_name):
    self.db_name = db_name
    self.conn = sqlite3.connect(self.db_name)
    self.cursor = self.conn.cursor()
    self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, discriminator TEXT, avatar TEXT, bot INTEGER, created_at TEXT, joined_at TEXT, roles TEXT)")
    self.cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, author_id INTEGER, content TEXT, created_at TEXT, FOREIGN KEY(author_id) REFERENCES users(id))")
    self.conn.commit()

  def add_user(self, user):
    self.cursor.execute("SELECT * FROM users WHERE id=%s", (user.id,))
    if self.cursor.fetchone() is None:
      self.cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (user.id, user.name, user.discriminator, user.avatar, user.bot, user.created_at, user.joined_at, user.roles))
      self.conn.commit()

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


