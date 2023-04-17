from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from pymongo import MongoClient, InsertOne
from bson.objectid import ObjectId
import json

app = Flask(__name__)

# http://localhost:5000/create?<query>


@app.route("/create", methods=["GET"])
def create():
    try:

        nameFile = request.args.get('param1')
        nameFile = nameFile + ".json"
        input_str = request.args.get('param2')

        # Split the input string into parts
        parts = input_str.split(',')

        # Extract the table name
        table_name = parts[0].strip()

        # Extract the column families
        column_families = []

        for part in parts[1:]:
            column_family = part.strip().strip('{}')

            if("=>" in column_family):
                column_family_name = column_family.split('=>')[0].strip()
                column_family_value = column_family.split('=>')[1].strip()
                column_families.append(
                    {column_family_name: column_family_value})

            else:
                error = {
                    '400',
                    ('error: no se puede leer el query, revisa que contenga =>')
                }
                return error

        # Create a dictionary with the table name and column families
        hbase_json = {table_name: {"column_families": column_families}}

        # Convert the dictionary to JSON
        json_data = json.dumps(hbase_json, indent=2)

        # Write JSON data to a file
        with open(nameFile, 'w') as file:
            file.write(json_data)

        regresar = {
            200,
            'Data processed successfully'
        }
        return regresar

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error

# http://localhost:5000/List?param1=<archivo>&param2=<palabra a buscar>


@app.route("/List", methods=["GET"])
def List():
    try:

        # searchFile = request.args.get('param1')
        # searchFile = searchFile + ".json"
        # inputNombre = request.args.get('param2')
        # # Open the JSON file in read mode
        # with open(searchFile, 'r') as json_file:
        #     # Load the JSON data from the file
        #     json_data = json.load(json_file)

        inputNombre = request.args.get('param1')
        # Open the JSON file in read mode
        with open("games.json", 'r') as json_file:
            # Load the JSON data from the file
            json_data = json.load(json_file)

        # Alternatively, you can iterate over the keys and values in the JSON dictionary
        list = []
        for key, value in json_data.items():
            print(f"Key: {key}, Value: {value}")

            keyString = key.split(' ')
            if(keyString[0] == inputNombre):
                list.append(key)

        return list

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error


# http://localhost:5000/Disable?param1=<table_name>


@app.route("/Disable", methods=["GET"])
def Disable():
    try:

        inputNombre = request.args.get('param1')
        # Open the JSON file in read mode
        with open('games.json', 'r') as json_file:
            # Load the JSON data from the file
            json_data = json.load(json_file)

        for key, value in json_data.items():

            if(key == inputNombre):
                with open('validator.json', 'r') as json_file:
                    # Load the JSON data from the file
                    validator = json.load(json_file)

                # Add a value to the key
                validator[key] = 'disabled'

                # Write the updated JSON data back to the file
                with open('validator.json', 'w') as f:
                    json.dump(validator, f, indent=4)

                regresar = {
                    200,
                    'Table disabled successfully'
                }
                return regresar
            else:
                error = {
                    '200',
                    ('No se encontro la tabla')
                }
                return error

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error

# http://localhost:5000/Enable?param1=<table_name>


@app.route("/Enable", methods=["GET"])
def Enable():
    try:

        inputNombre = request.args.get('param1')
        # Open the JSON file in read mode
        with open('validator.json', 'r') as json_file:
            # Load the JSON data from the file
            json_data = json.load(json_file)

        for key, value in json_data.items():

            if (key == inputNombre):
                del json_data[key]
                with open('validator.json', 'w') as f:
                    json.dump(json_data, f, indent=4)
                regresar = {
                    '200',
                    ('Table enabled successfully')
                }
                return regresar

        regresar = {
            '200',
            ('Tabla no encontrada como deshabilitada: revisa nombre de la tabla')
        }
        return regresar

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error


# http://localhost:5000/Is_Enabled?param1=<table_name>


@app.route("/Is_Enabled", methods=["GET"])
def Is_Enabled():
    try:

        inputNombre = request.args.get('param1')
        # Open the JSON file in read mode
        with open('games.json', 'r') as json_file:
            # Load the JSON data from the file
            json_data = json.load(json_file)

        for key, value in json_data.items():

            if(key == inputNombre):
                with open('validator.json', 'r') as json_file:
                    # Load the JSON data from the file
                    validator = json.load(json_file)
                flag = False
                for key2, value2 in validator.items():
                    if(key2 == key):
                        flag = True

                if(flag):
                    regresar = {
                        '200',
                        ('Table is disabled')
                    }
                else:
                    regresar = {
                        '200',
                        ('Table is enabled')
                    }
                return regresar

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error


if __name__ == '__main__':
    app.run(debug=True)
