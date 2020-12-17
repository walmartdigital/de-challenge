 Instrucciones de despliegue : 

Sera necesario ejecutar un contenedor com docker docker-compose up , dentro hay tres servicios.
  
 - 1) job:Estará calendarizado para ejecutar el etl.py 
 - 2) backend: Se encargara de levantar una pequeña api para consumir los datos del ETL. 
 - 3) api :TODO  Desplegará una vista para los datos.