from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from pymongo import MongoClient, InsertOne
from bson.objectid import ObjectId
import json
from hbase import Master

master = Master()
master.load_data_from_json("Sales", "./back/purchases.json")
master.load_data_from_json("Games", "./back/games.json")

app = Flask(__name__)

# http://localhost:5000/create?<query>


@app.route("/create", methods=["GET"])
def create():
    try:

        input_str = request.args.get('param1')

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
        master.create_table(table_name, column_families)

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

# http://localhost:5000/List>


@app.route("/List", methods=["GET"])
def List():
    try:

        list = master.ddl_list()

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

        value = master.disable(inputNombre)

        return value

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

        value = master.enable(inputNombre)

        return value

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

        value = master.is_enabled(inputNombre)

        return value

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error

# http://localhost:5000/Alter?param1=<query>


@app.route("/Alter", methods=["GET"])
def Is_Enabled():
    try:

        input_str = request.args.get('param1')
        parts = input_str.split(',')

        # Extract the table name
        table_name = parts.pop(0).strip()

        for i in range(0, len(parts), 2):
            column_family = parts[i].strip().strip('{}')
            column_family_name = column_family.split(':')[0].strip()
            column_family_value = column_family.split(':')[1].strip()

            column_family_new = parts[i+1].strip().strip('{}')
            new_family_accion = column_family_new.split(':')[0].strip()
            column_family_value_new = column_family_new.split(':')[1].strip()

            if(new_family_accion == 'NEW_NAME'):
                master.alter_table(
                    table_name, column_family_name, column_family_value_new
                )
            elif(new_family_accion == 'METHOD'):
                master.delete_alter(
                    table_name, column_family_name
                )

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error


# http://localhost:5000/Describe?param1=<table_name>


@app.route("/Describe", methods=["GET"])
def Describe():
    try:

        input_str = request.args.get('param1')

        value = master.describe(input_str)

        return value

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error


# http://localhost:5000/Drop?param1=<table_name>


@app.route("/Drop", methods=["GET"])
def Describe():
    try:

        input_str = request.args.get('param1')

        value = master.drop(input_str)

        return value

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error


# http://localhost:5000/DropAll


@app.route("/DropAll", methods=["GET"])
def Describe():
    try:

        master.drop()

        value = {
            200,
            'All tables dropped successfully'
        }

        return value

    except Exception as e:
        # Return error message if any exception occurs
        error = {
            '400',
            ('error: ' + str(e))
        }
        return error


if __name__ == '__main__':
    app.run(debug=True)
