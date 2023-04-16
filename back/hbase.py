from collections import defaultdict
import json 
import re
import time

class Master:
    def __init__(self):
        self.tables = defaultdict(Table)

    def insert(self, table_name, row_key, column_family, column, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time() * 1000)
        self.tables[table_name].insert(row_key, column_family, column, value, timestamp)

    def __filtr_ddl_list(self, prefix=None):
        filtered_tables = dict(self.tables)

        if prefix:
            starts_pattern = re.compile(fr'^{prefix}')
            filtered_tables = {k: v for k, v in filtered_tables.items() if starts_pattern.match(k)}
        
        return filtered_tables
    
    def ddl_list(self, prefix = None):
        filtred_tables = self.__filtr_ddl_list(prefix)
        """
        Seccion para parsear la info de las tablas en un solo string. 
        """
        return list(filtred_tables.keys())

    def get(self, table_name, row_key, column_family, column):
        try:
            data = self.tables[table_name].get(row_key, column_family, column)
            return 200, data
        except:
            return 500, "Error on server."
    
    def create_table(self, table_name: str, column_families:list = ["cf"]):
        column_families = list(set(column_families))
        if table_name in self.tables:
            return 404, f"Table '{table_name}' already exists."
        try:
            self.tables[table_name] = Table(column_families)
            return 200, "Success on creating table."
        except:
            return 500, "Error on server."
        
    def is_enable(self, table_name):
        if table_name in self.tables:
            return 200, f"Table {table_name} is enable." if self.tables[table_name].isable else f"Table {table_name} is disabled."
        else:
            return 404, f"Table {table_name} doesn't exist"
        
    def enable(self, table_name):
        if table_name in self.tables:
            self.tables[table_name].enable()
            return 200, "Succesfully enable table."
        return 404, "Table doesn't exist"

    def disable(self, table_name):
        if table_name in self.tables:
            self.tables[table_name].disable()
            return 200, "Succesfully disable table."
        return 404, "Table doesn't exist"

    def load_data_from_json(self, table_name, json_file_path):
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        for record in data:
            for row_key, column_families in record.items():
                for column_family, columns in column_families.items():
                    for column, value in columns.items():
                        self.insert(table_name, row_key, column_family, column, value)
    
    def rename_alter(self, table_name, column_family, new_name):
        return self.tables[table_name].rename_column_family(column_family, new_name)

    def delete_alter(self, table_name, column_family):
        return self.tables[table_name].drop_column_family(column_family)

    def all_alters(self, table_name, alters):
        if table_name not in self.tables:
            return 404, "Table doesn't exist."
        # Expects alter to have a list of dictionaries structure like this: {NAME: column_family_name, NEW_NAME: new_column_family_name} or {NAME: column_family_name, METHOD: delete} 
        log = []
        code = 200
        for alter in alters:
            if len(alter)==2:
                if "NAME" in alter:
                    column_family = alter["NAME"]
                    if "NEW_NAME" in alter:
                        new_name = alter.get("NEW_NAME")
                        log.append(self.rename_alter(table_name, column_family, new_name))
                    elif "METHOD" in alter:
                        method = alter.get("METHOD")
                        if method=="delete":
                            log.append(self.delete_alter(table_name, column_family))
                        else:
                            code = 404
                            log.append(404, f"No method allowed: {method}")
                    else:
                        log.append(404, "Expects column_name")

                else:
                    code = 404
                    log.append(404, "Expects column_name")
            else:
                code = 404
                log.append(404, "Expects only two parameters in alter action.") 
        return code, log

    def drop(self, table_name):
        if table_name not in self.tables:
            return 404, "Table doesn't exist."
        del self.tables[table_name]
        return 200, "Table {table_name} dropped correctly."
            
    def drop_all(self):
        self.tables.clear()
        return 200, "All tables droped"

    def describe(self, table_name) -> dict:
        if table_name not in self.tables:
            return 400, {"name": table_name, "state": None, "column_families": None}
        table: Table  = self.tables[table_name]
        return 200, {"name": table_name, "state": table.isable, "column_families": table.column_families}

class Table:
    def __init__(self, column_families=None):
        self.region = Region()
        self.column_families = column_families or []
        self.isable = True
        #Estos valores solo son simbolicos no afectan nada sobre la arquitectura simulada. 
        self.commpresion = None
        self.versions = 1
        self.ttl = float('inf')
        self.block_size = '1MB'
        self.in_memory = True
        self.bloom_filter = None
        

    def insert(self, row_key, column_family, column, value, timestamp):
        self.region.insert(row_key, column_family, column, value, timestamp)

    def get(self, row_key, column_family, column):
        if self.isable:
            return self.region.get(row_key, column_family, column)
        return 404, "Enable table to get, table is disable."

    def enable(self):
        self.isable = True
        return True
        
    def disable(self):
        self.isable = False
        return True

    def is_enable(self):
        return self.isable

    def rename_column_family(self, old_name, new_name):
        if old_name not in self.column_families:
            return 404, f"Column family '{old_name}' does not exist."
        if new_name in self.column_families:
            return 404, f"Column family '{new_name}' already exists."
            
        self.column_families[self.column_families.index(old_name)] = new_name

        for row in self.region.rows.values():
            if old_name in row.column_families:
                row.column_families[new_name] = row.column_families.pop(old_name)
        return 200, f"Succesfully rename column family {old_name}->{new_name}"
    
    def drop_column_family(self, column_family):
        if column_family not in self.column_families:
            return 404, f"Column family '{column_family}' does not exist."
            
        self.column_families.remove(column_family)

        for row in self.region.rows.values():
            if column_family in row.column_families:
                del row.column_families[column_family]
        return 200, f"Successfully delete column-family: {column_family}"

class Region:
    def __init__(self):
        self.rows = defaultdict(Row)

    def insert(self, row_key, column_family, column, value, timestamp):
        self.rows[row_key].insert(column_family, column, value, timestamp)

    def get(self, row_key, column_family, column):
        return self.rows[row_key].get(column_family, column)

class Row:
    def __init__(self):
        self.column_families = defaultdict(lambda: defaultdict(Cell))

    def insert(self, column_family, column, value):
        self.column_families[column_family][column].insert(value)

    def get(self, column_family, column):
        return self.column_families[column_family][column].get()

class Cell:
    def __init__(self):
        self.versions = []

    def put(self, value, timestamp):
        self.versions.append({"value": value, "timestamp": timestamp})
        self.versions.sort(key=lambda x: x["timestamp"], reverse=True)

    def get(self, timestamp=None):
        if not self.versions:
            return None
        if timestamp is None:
            return self.versions[0]["value"]
        for version in self.versions:
            if version["timestamp"] <= timestamp:
                return version["value"]
        return None


class KeyValue:
    def __init__(self, value):
        self.value = value
