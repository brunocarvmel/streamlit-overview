import services.database as db
import models.Client as client

def IncludeClient(client):   
    comand = f'INSERT INTO clients (name, age, occupation) VALUES ("{client.name}", "{client.age}", "{client.occupation}")'
    db.cursor.execute(comand)
    db.connection.commit()
   
def EditClient(client):   
    comand = f'UPDATE clients SET name = "{client.name}", age = "{client.age}", occupation = "{client.occupation}" WHERE id = "{client.id}"'
    db.cursor.execute(comand)
    db.connection.commit() 
    
def SelectClientById(id):
    comand = f'SELECT * FROM clients WHERE id = {id}'
    db.cursor.execute(comand)
    costumerList = []
    
    for i in db.cursor.fetchall():
        costumerList.append(client.Client(i[0], i[1], i[2], i[3]))
        
    return costumerList[0]

def ExcludeClient(id): 
    comand = f'DELETE FROM clients WHERE id = {id}'
    db.cursor.execute(comand)
    db.connection.commit() 
    
def SelectAllClients():
    comand = 'SELECT * FROM clients'
    db.cursor.execute(comand)
    costumerList = []
    
    for i in db.cursor.fetchall():
        costumerList.append(client.Client(i[0], i[1], i[2], i[3]))
        
    return costumerList



