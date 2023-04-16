from hbase import Master

def main():
    #Instanciacion de cluster
    hbase = Master()
    
    """
    DDL
    Create
    Inputs ejemplos (FRONTEND):
        - <nombre_tabla>
        - <nombre_tabla>, {NAME => <nombre_family_column_1>}, {NAME => <nombre_family_column_2>}, ..., {NAME => <nombre_family_column_n>} 
    Parametros de funcion:
        - table_name: String con nombre de tablas  
        - column_families: Lista con los nombre de las familias de columnas
    """

    """
    List
    """
    
    """
    Disable
    """
    
    """
    Is_Enabled
    """
    
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
    
    
    hbase.create_table("table1", ["customer info", "purchase info", "product info"])
    hbase.create_table("table1", ["customer info", "purchase info", "product info"])

    hbase.drop_all()
    hbase.insert("table1", "7512", "customer info", "Name", "Jeremy Garcia")
    print(hbase.get("table1", "7512", "customer info", "Name"))  # Output: Jeremy Garcia

    # Rename column family
    hbase.tables["table1"].rename_column_family("customer info", "client info")
    print(hbase.get("table1", "7512", "client info", "Name"))  # Output: Jeremy Garcia

    # Drop column family
    hbase.tables["table1"].drop_column_family("client info")
    print(hbase.get("table1", "7512", "client info", "Name"))  # Output: None

if __name__ == "__main__":
    main()
