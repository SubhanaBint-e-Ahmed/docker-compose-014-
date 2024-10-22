from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Example endpoint
@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_db_user",
            password="your_db_password",
            host="db",  # This should match the service name of the database in the docker-compose file
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        return jsonify({'db_version': db_version[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
