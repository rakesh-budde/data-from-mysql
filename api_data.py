from flask import *
import json
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = '10.128.8.5'
app.config['MYSQL_USER'] = 'original'
app.config['MYSQL_PASSWORD'] = 'Original@123'
app.config['MYSQL_DB'] = 'python_api_db'

mysql = MySQL(app)

@app.route('/',methods=['GET'])
def home_page():
	result = []
	cur = mysql.connection.cursor()
	quaries = cur.execute("SELECT * FROM api_data")

	if quaries > 0:
		result = cur.fetchall()
	json_data = json.dumps(result)
	return json_data

if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5002, debug = True)

