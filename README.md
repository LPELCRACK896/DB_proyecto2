## Ejemplos inputs

### DML

#### Put
##### Estructura
```
<table_name>,<column_family>:<column>,<value>
```
##### Ejemplo
```
Sales,2321,customer info:Name,Maria W
```
#### Get
##### Estructura
```
<table_name>,<column_family>:<column>
```
##### Ejemplo
```
Sales,2321,customer info:Name
```
#### Scan
##### Estructura
```
<table_name>
```
##### Ejemplo
```
Games
```
Con start-row y stop-row
##### Estructura
```
<table_name>,<start_row>,<end_row>
```
##### Ejemplo
```
Games,1003,8141
```
#### Delete

Registro completo
##### Estructura
```
<table_name>,<row_key>
```
##### Ejemplo
```
Sales,9192
```
##### Estructura --Aun con errores.
```
<table_name>,<row_key>,<column_family>
```
##### Ejemplo
```
Sales,7903,customer info
```
#### Delete all
##### Estructura
```
<table_name>
```
##### Ejemplo
```
Games
```
Con start-row y stop-row
##### Estructura
```
<table_name>,<start_row>,<end_row>
```
##### Ejemplo
```
Games,1003,8141
```
#### Count
##### Estructura
```
<table_name>
```
##### Ejemplo
```
Games
```

#### Truncate
##### Estructura
```
<table_name>
```
##### Ejemplo
```
Sales
```