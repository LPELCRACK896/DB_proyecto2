from flask import Flask, request, jsonify
from flask_cors import CORS
from hbase import Master
from data_generator import gen_games, gen_purchase

# gen_games("games.json", 20)
#gen_purchase("purchases.json", 20)

master = Master()
master.load_data_from_json("Sales", "./back/purchases.json")
master.load_data_from_json("Games", "./back/games.json")# Create the Flask app
app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes



def process_put(input_str):
    try:
        input_parts = input_str.split(',')
        if len(input_parts) < 4:
            raise ValueError("Input string should have at least 4 values")

        table_name, row_key, column_family_qualifier, value = input_parts[:4]
        timestamp = input_parts[4] if len(input_parts) > 4 else None
        column_family, column_qualifier = column_family_qualifier.split(':')

        timestamp = int(timestamp) if timestamp else None

        print(table_name, row_key, column_family, column_qualifier, value, timestamp)

        status, message = master.put(table_name, row_key, column_family, column_qualifier, value, timestamp)
        return {'status': status, 'message': message}
    except Exception as e:
        return {'status': 400, 'message': str(e)}

def process_get(input_str):
    try:
        input_parts = input_str.split(',')

        if len(input_parts) < 3:
            raise ValueError("Input string should have at least 3 values")

        table_name, row_key, column_family_qualifier = input_parts[:3]
        column_family, column_qualifier = column_family_qualifier.split(':')

        status, message = master.get(table_name, row_key, column_family, column_qualifier)
        return {'status': status, 'message': message}
        
    except Exception as e:
        return {"message": str(e), "status": 400}


def process_scan(input_str):
    try:
        input_parts = input_str.split(',')

        if len(input_parts) < 1:
            raise ValueError("Input string should have at least 1 value")

        table_name = input_parts[0]

        start_row = input_parts[1] if len(input_parts) > 1 else None
        stop_row = input_parts[2] if len(input_parts) > 2 else None

        status, message = master.scan(table_name, start_row, stop_row)
        return {'status': status, 'message': message}
        
    except Exception as e:
        return {"message": str(e), "status": 400}

def process_delete(input_str):
    try:
        input_parts = input_str.split(',')

        if len(input_parts) < 2:
            raise ValueError("Input string should have 3 values: 'table_name','row_key','column_family:column_qualifier'")

        table_name = input_parts[0]
        row_key  = input_parts[1]
        column = input_parts[2] if len(input_parts)==3 else None
        status, message = master.delete(table_name, row_key, column)
        print(message)
        return {'status': status, 'message': message}
        
    except Exception as e:
        return {"message": str(e), "status": 400}

def process_delete_all(input_str):
    try:
        input_parts = input_str.split(',')

        if len(input_parts) < 1:
            raise ValueError("Input string should have at least 1 value")

        table_name = input_parts[0]

        start_row = input_parts[1] if len(input_parts) > 1 else None
        stop_row = input_parts[2] if len(input_parts) > 2 else None

        status, message = master.delete_all(table_name, start_row, stop_row)
        return {'status': status, 'message': message}
        
    except Exception as e:
        return {"message": str(e), "status": 400}
    
def process_count(input_str):
    try:
        input_parts = input_str.split(',')

        if len(input_parts) != 1:
            raise ValueError("Input string should have 1 value: 'table_name'")

        table_name = input_parts[0]

        status, message = master.count(table_name)

        return {'status': status, 'message': message}
        
    except Exception as e:
        return {"message": str(e), "status": 400}

def process_truncate(input_str):
    try:
        input_parts = input_str.split(',')

        if len(input_parts) != 1:
            raise ValueError("Input string should have 1 value: 'table_name'")

        table_name = input_parts[0]
        status, message = master.truncate(table_name)
        return {'status': status, 'message': message} 
        
    except Exception as e:
        return {"message": str(e), "status": 400}

@app.route('/put', methods=['POST'])
def put():
    data = request.get_json()
    input_str = data.get('query')
    result = process_put(input_str)
    return jsonify(result)

@app.route('/get', methods=['POST'])
def get():
    input_str = request.json.get('query', None)
    if input_str:
        response = process_get(input_str)
        return jsonify(response), response.get('status', 200)
    return jsonify({"message": "Input string is missing", "status": 400}), 400


@app.route('/scan', methods=['POST'])
def scan():
    input_str = request.json.get('query', None)
    if input_str:
        response = process_scan(input_str)
        return jsonify(response), response.get('status', 200)
    return jsonify({"message": "Input string is missing", "status": 400}), 400


@app.route('/delete', methods=['POST'])
def delete():
    input_str = request.json.get('query', None)
    if input_str:
        response = process_delete(input_str)
        return jsonify(response), response.get('status', 200)
    return jsonify({"message": "Input string is missing", "status": 400}), 400


@app.route('/delete_all', methods=['POST'])
def delete_all():
    input_str = request.json.get('query', None)
    if input_str:
        response = process_delete_all(input_str)
        return jsonify(response), response.get('status', 200)
    return jsonify({"message": "Input string is missing", "status": 400}), 400


@app.route('/count', methods=['POST'])
def count():
    input_str = request.json.get('query', None)
    if input_str:
        response = process_count(input_str)
        return jsonify(response), response.get('status', 200)
    return jsonify({"message": "Input string is missing", "status": 400}), 400

@app.route('/truncate', methods=['POST'])
def truncate():
    input_str = request.json.get('query', None)
    if input_str:
        response = process_truncate(input_str)
        return jsonify(response), response.get('status', 200)
    return jsonify({"message": "Input string is missing", "status": 400}), 400

if __name__ == "__main__":
    app.run(debug=True)