from hbase import Master


def main():
    # Instanciacion de cluster
    hbase = Master()

    """
    Create REVISION [YES/NO]
    Inputs ejemplos (FRONTEND):
        - <nombre_tabla>
        - <nombre_tabla>, {NAME => <nombre_family_column_1>}, {NAME => <nombre_family_column_2>}, ..., {NAME => <nombre_family_column_n>} 
    Parametros de funcion:
        - table_name: String con nombre de tablas  
        - column_families: Lista con los nombre de las familias de columnas
    Return: 
        Tupla: CODIGO HTTP, Mensaje
    """
    print(hbase.create_table("tabla_ejemplo", ["column_f_1", "column_f_2"]))
    print(hbase.create_table("tabla_ejemplo2", ["column_f_1", "column_f_2"]))
    print(hbase.create_table("table", ["columna_1", "columna_2"]))
    """
    List REVISION [YES/NO]
    Inputs ejemplos (FRONTEND):
        - <nombre del archivo>
        - <palabra_con_la_que_inicia_la_tabla_que_desea_listar>
    Parametros de funcion:
        - starts_with: String con el que empieza las tablas que desean listar
    Return: 
        List: Nombres de tablas en DB
    """
    print(hbase.ddl_list())
    print(hbase.ddl_list("tabla"))

    """
    Disable REVISION [YES/NO]
    Inputs ejemplos (FRONTEND):
        - <table_name>
    Parametros de funcion:
        - table_name: Nombre de tabla que se desea deshabilitar
    Return: 
        - Tuple: CODE, message
    """
    print(hbase.disable("tabla_ejemplo"))
    print(hbase.disable("tabla_ejemplo2"))
    """
    Enable REVISION [YES/NO]
    Inputs ejemplos (FRONTEND):
        - <table_name>
    Parametros de funcion:
        - table_name: Nombre de tabla que se desea habilitar
    Return: 
        - Tuple: CODE, message
    """
    print(hbase.enable("tabla_ejemplo"))

    """
    Is_Enabled REVISION [YES/NO]
    Inputs ejemplos (FRONTEND):
        - <table_name>
    Parametros de funcion:
        - table_name: Nombre de tabla que se desea saber estado.
    Return: 
        - Tuple: CODE, message
    """
    print(hbase.is_enable("tabla_ejemplo"))
    print(hbase.is_enable("tabla_ejemplo2"))
    print(hbase.is_enable("table"))
    """
    Alter REVISION []
    Inputs ejemplos (FRONTEND):
        -   <table_name>, {NAME: <column_family_name>, NEW_NAME: <new_column_family_name>}
        -   <table_name>, {NAME: <column_family_name>, METHOD: delete}
        -   <table_name>, {NAME: <column_family_name>, NEW_NAME: <new_column_family_name>}, {NAME: <column_family_name>, METHOD: delete}
        -   <table_name>,  {NAME: <column_family_name>, METHOD: delete}, {NAME: <column_family_name>, NEW_NAME: <new_column_family_name>}
    Parametros de funcion:
        -   table_name: Nombre da la tabla
        -   alters: Modificaciones a realiazar en forma de diccionarios con dos elementos. 
    Return: 
        - Tuple: Code, lista (contiene los resultados de las operaciones realizadas)
    """
    print(hbase.all_alters("tabla_ejemplo", [{"NAME": "column_f_1", "NEW_NAME": "columna_1"}, {
          "NAME": "column_f_2", "METHOD": "delete"}]))
    # Solo para ver cambios
    """
    Describe REVISION []
    Inputs ejemplos (FRONTEND):
        - <table_name>
    Parametros de funcion:
        - table_name: Nombre de tabla que se desea saber.
    Return: 
        - Tuple: CODE, diccionario con informacio de la tabla
    """
    print(hbase.describe("tabla_ejemplo"))

    """
    Drop REVISION []
    Inputs ejemplos (FRONTEND):
        - <table_name>
    Parametros de funcion:
        - table_name: Nombre de tabla que se desea eliminar.
    Return: 
        - Tuple: CODE, message
    """
    print(hbase.drop("tabla_ejemplo2"))
    """
    Drop All REVISION []
    Inputs ejemplos (FRONTEND):
        - (nada)
    Parametros de funcion:
        -  (nada)
    Return: 
        - Tuple: CODE, message
    """
    print(hbase.drop_all())
    # Comprueba que se borraron
    print(hbase.ddl_list())


if __name__ == "__main__":
    main()
