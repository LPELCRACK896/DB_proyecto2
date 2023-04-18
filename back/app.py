from flask import Flask, request, jsonify
from flask_cors import CORS
from hbase import Master
from data_generator import gen_games, gen_purchase
import re

# gen_games("games.json", 20)
#gen_purchase("purchases.json", 20)

master = Master()
master.load_data_from_json("Sales", "./back/purchases.json")
master.load_data_from_json(
    "Games", "./back/games.json")  # Create the Flask app
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

        print(table_name, row_key, column_family,
              column_qualifier, value, timestamp)

        status, message = master.put(
            table_name, row_key, column_family, column_qualifier, value, timestamp)
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
        print(table_name, row_key, column_family, column_qualifier)
        status, message = master.get(
            table_name, row_key, column_family, column_qualifier)
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
            raise ValueError(
                "Input string should have 3 values: 'table_name','row_key','column_family:column_qualifier'")

        table_name = input_parts[0]
        row_key = input_parts[1]
        column = input_parts[2] if len(input_parts) == 3 else None
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
    print(input_str)
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

# http://localhost:5000/create?<query>
# ejemplo: "7777, {NAME => 'value1'}, {NAME => 'value2'}


@app.route("/create", methods=["POST"])
def create():
    try:
        input_str = request.json.get('query')
        print(input_str)

        # Split the input string into parts
        parts = input_str.split(',')
        table_name = parts.pop(0)
        column_families = []

        # Regular expression to match column family
        cf_pattern = re.compile(r'{NAME=>([^}]+)}')

        # Extract column families
        for part in parts:
            cf_match = cf_pattern.match(part.strip())
            if cf_match:
                column_families.append(cf_match.group(1))
            else:
                response = {"status": 400,
                            "message": f"Invalid column family format: {part}"}
                return jsonify(response), response.get('status', 200)

        if not column_families:
            column_families = ["cf"]
        print(type(table_name), type(column_families))

        # Create a dictionary with the table name and column families
        status_code, success_message = master.create_table(
            table_name, column_families)
        response = {"status": status_code, "message": success_message}
        return jsonify(response), response.get('status', 200)
    except Exception as e:
        response = {"status": 400, "message": f"Error: {str(e)}"}
        return jsonify(response), response.get('status', 200)

# http://localhost:5000/List>
# ejemplo: 8329


@app.route("/list", methods=["POST"])
def List():
    try:

        status, message = master.ddl_list()
        response = {"status": status, "message": message}
        return jsonify(response), response.get('status', 200)

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error


# http://localhost:5000/Disable?param1=<table_name>
# ejemplo: 8329

@app.route("/disable", methods=["POST"])
def Disable():

    inputNombre = request.json.get('query', None)
    if inputNombre is None:
        return jsonify({"Message": "Input string is missing", "status": 400}), 400
    else:
        try:
            input_parts = inputNombre.split(',')

            if len(input_parts) != 1:
                raise ValueError(
                    "Input string should have 1 value: 'table_name'")

            table_name = input_parts[0]
            status, message = master.disable(table_name)
            return {'status': status, 'message': message}

        except Exception as e:
            return {"message": str(e), "status": 400}


# http://localhost:5000/Enable?param1=<table_name>
# ejemplo: 8329


@app.route("/enable", methods=["POST"])
def Enable():
    inputNombre = request.json.get('query', None)
    if inputNombre is None:
        return jsonify({"Message": "Input string is missing", "status": 400}), 400
    else:
        try:
            input_parts = inputNombre.split(',')

            if len(input_parts) != 1:
                raise ValueError(
                    "Input string should have 1 value: 'table_name'")

            table_name = input_parts[0]
            status, message = master.enable(table_name)
            return {'status': status, 'message': message}

        except Exception as e:
            return {"message": str(e), "status": 400}

# http://localhost:5000/Is_Enabled?param1=<table_name>
# ejemplo: 8329


@app.route("/is_enable", methods=["POST"])
def Is_Enabled():
    inputNombre = request.json.get('query', None)
    if inputNombre is None:
        return jsonify({"Message": "Input string is missing", "status": 400}), 400
    else:
        try:
            input_parts = inputNombre.split(',')

            if len(input_parts) != 1:
                raise ValueError(
                    "Input string should have 1 value: 'table_name'")

            table_name = input_parts[0]
            status, message = master.is_enable(table_name)
            return {'status': status, 'message': message}

        except Exception as e:
            return {"message": str(e), "status": 400}

# http://localhost:5000/Alter?param1=<query>
# ejemplo: Sales,{NAME:customer info,NEW_NAME:idontknow}


@app.route("/alter", methods=["POST"])
def Alter():
    inputUser = request.json.get('query', None)
    try:
        if(inputUser is None):
            return jsonify({"Message": "Input string is missing", "status": 400}), 400

        parts = inputUser.split(',')
        table_name = parts.pop(0).strip()

        temp = {}
        temp2 = []
        for i in range(0, len(parts), 2):
            column_family = parts[i].strip().strip('{}')
            column_family_name = column_family.split(':')[0].strip()
            column_family_value = column_family.split(':')[1].strip()

            column_family_new = parts[i+1].strip().strip('{}')
            new_family_accion = column_family_new.split(':')[0].strip()
            column_family_value_new = column_family_new.split(':')[1].strip()

            temp = {column_family_name: column_family_value,
                    new_family_accion: column_family_value_new}
            temp2.append(temp)

        status, message = master.all_alters(table_name, temp2)
        return {'status': status, 'message': message}

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error


# http://localhost:5000/Describe?param1=<table_name>
# ejemplo: 8329

@app.route("/describe", methods=["POST"])
def Describe():
    try:

        input_str = request.json.get('query', None)

        status, message = master.describe(input_str)
        response = {"status": status, "message": message}
        print(response)
        return jsonify(response), response.get('status', 200)

    except Exception as e:
        # Return error message if any exception occurs
        response = {"status": 400, "message": "Error on request"}
        return jsonify(response), response.get('status', 200)


# http://localhost:5000/Drop?param1=<table_name>
# ejemplo: 8329

@app.route("/drop", methods=["POST"])
def Drop():
    try:

        input_str = request.json.get('query')

        if(input_str is None):
            return jsonify({"Message": "Input string is missing", "status": 400}), 400

        statusTemp, messageTemp = master.is_enable(input_str)
        temp = messageTemp.split(' ')
        lastTemp = temp[temp.__len__()-1]
        if(lastTemp == 'enable.'):
            status, message = master.drop(input_str)
            response = {"status": status, "message": message}
            return jsonify(response), response.get('status', 200)
        else:
            return jsonify({"status": 400, "message": "Cant drop table, table is disabled"})

    except Exception as e:
        # Return error message if any exception occurs
        response = {"status": 501, "message": "Server error. py"}
        return jsonify(response), response.get('status', 200)


# http://localhost:5000/DropAll
# ejemplo:

@app.route("/dropall", methods=["POST"])
def DropAll():
    try:
        status, message = master.drop_all()
        response = {"status": status, "message": message}
        return jsonify(response), response.get('status', 200)
    except Exception as e:
        # Return error message if any exception occurs
        response = {"status": 500, "message": "message"}
        return jsonify(response), response.get('status', 200)


if __name__ == "__main__":
    app.run(debug=True)
