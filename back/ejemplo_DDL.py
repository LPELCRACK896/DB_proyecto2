from hbase import Master

def main():
    #Instanciacion de cluster
    hbase = Master()
    
    """
    Create
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
    List
    Inputs ejemplos (FRONTEND):
        - (nada)
        - <palabra_con_la_que_inicia_la_tabla_que_desea_listar>
    Parametros de funcion:
        - starts_with: String con el que empieza las tablas que desean listar
    Return: 
        List: Nombres de tablas en DB
    """
    print(hbase.ddl_list())
    print(hbase.ddl_list("tabla"))
    
    """
    Disable
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
    Enable
    Inputs ejemplos (FRONTEND):
        - <table_name>
    Parametros de funcion:
        - table_name: Nombre de tabla que se desea habilitar
    Return: 
        - Tuple: CODE, message
    """
    print(hbase.enable("tabla_ejemplo2"))
    
    """
    Is_Enabled
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
    Alter
    """
    
    """
    Drop
    """
    
    """
    Drop All
    """

    
    """
    Describe
    """


if __name__ == "__main__":
    main()
