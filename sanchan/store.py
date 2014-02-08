import sqlite3
import sanchan.options

class DataStore():
	def __init__(self):
		self.db = sqlite3.connect('database.db')
		self.db.execute('CREATE TABLE IF NOT EXISTS "sanchan" ("status_id" INTEGER, "text" TEXT, "count" INTEGER, "latitude" REAL, "longitude" REAL)')

	def put(self, status, count):
		c = self.db.cursor()
		c.execute('INSERT INTO sanchan(status_id, text, count) VALUES ?, ?, ?, ?, ?', status.id, status,text, count)
