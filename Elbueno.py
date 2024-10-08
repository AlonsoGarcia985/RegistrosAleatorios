from faker import Faker
import mysql.connector  

 
db = mysql.connector.connect(
    host="localhost",       
    user="USER",      
    password="PASSWORD", 
    database="NAME"
)

cursor = db.cursor()

fake = Faker()

def insert_Departamentos(n):
    print('entra')
    for i in range(n):
        nombre=fake.first_name()
        
        cursor.execute(f"INSERT INTO Departamentos (Nombre) VALUES ('{nombre}')")

def insert_empleados(n):
    for i in range(n):
        nombre = fake.first_name()
        apellido = fake.last_name()
        email = fake.unique.email()
        telefono = fake.phone_number()
        fecha_contratacion = fake.date_between(start_date='-5y', end_date='today')
        
        cursor.execute(f"insert into Empleados (Nombre, Apellido, Email, Telefono, Fecha_Contratacion) Values ('{nombre}','{apellido}','{email}','{telefono}','{fecha_contratacion}')") 


#insert_Departamentos(50000)
insert_empleados(50000) 
db.commit()
cursor.close()
db.close()
