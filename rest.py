import pymysql, logging
from app import app
from db import mysql
from flask import jsonify
from flask import flash, request

# Create a logger object
logger = logging.getLogger()

# Configure logger
logging.basicConfig(filename="noteapplog.log", format='%(filename)s: %(message)s', filemode='w')

# Setting threshold level
logger.setLevel(logging.DEBUG)
		
@app.route('/add', methods=['POST'])
def add_note():
	conn = None
	cursor = None
	logger.info("Post Request comes for adding note in DB.")
	try:
		_json = request.json
		_note = _json['note']
		# validate the received values
		if _note and request.method == 'POST':
			# save new note data
			sql = "INSERT INTO NoteApp(note) VALUES(%s)"
			data = (_note,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Note added successfully!')
			if resp.status_code == 200:
				logger.info("Note added successfully!")
				return resp
			else:
				logger.error("Note added failure!")
				return ("Note added failure!")
		else:
			logger.error("Note added failure!")
			return not_found()
	except Exception as e:
		print(e)
		logger.error("Error accoured : {}".format(e))
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/data')
def data():
	conn = None
	cursor = None
	logger.info("User request for Get all data from db and show to UI.")
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT user_id id, Note FROM NoteApp")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		if resp.status_code == 200:
			logger.info("Data found")
			return resp
		else:
			logger.error("Data not found")
			return ("Data not found")

	except Exception as e:
		print(e)
		logger.error("Data not found")
		
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/searchnote/<string:note>')
def Search_Note(note):
	conn = None
	cursor = None
	logger.info("User request for Get data from db on user id basis")
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(f"SELECT * FROM NoteApp WHERE note like '%{note}%'")
		row = cursor.fetchall()
		resp = jsonify(row)
		# print(resp.status_code)
		if resp.status_code == 200:
			logger.info("Data found")
			return resp
		else:
			logger.error("Data not found")
			return ("Data not found")
	except Exception as e:
		print(e)
		logger.error("Data not found")
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['PUT'])
def update_Note():
	conn = None
	cursor = None
	logger.info("User request to update data in db.")
	try:
		_json = request.json
		_id = _json['id']
		_note = _json['note']
		# validate the received values
		if _note and _id and request.method == 'PUT':
			# save edits
			sql = "UPDATE NoteApp SET Note=%s WHERE user_id=%s"
			data = (_note, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Note updated successfully!')
			print(resp.status_code)
			if resp.status_code == 200:
				logger.info("Note updated successfully!")
				return resp
			else:
				logger.error("Note updated failure!")
				return ("Note updated failure!")
		else:
			logger.error("Note updated failure!")
			return not_found()
	except Exception as e:
		print(e)
		logger.error("Error accoured : {}".format(e))
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
	conn = None
	cursor = None
	logger.info("User request to delete note data")
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM NoteApp WHERE user_id=%s", id)
		conn.commit()
		resp = jsonify('Note deleted successfully!')
		if resp.status_code == 200:
			logger.info("Note deleted successfully!")
			return resp
		else:
			logger.error("Note deleted failure!")
			return ("Note deleted failure!")
	except Exception as e:
		print(e)
		logger.error("Note deleted failure!")
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
	
    resp = jsonify(message)
    resp.status_code = 404
	
    return resp
		
if __name__ == "__main__":
	logger.info("Application start")
	app.run()
	
