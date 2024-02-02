import psycopg2
cn=None
cur=None
try:
    cn = psycopg2.connect(
        host="localhost",
        database="Hw4",
        user="postgres",
        password=13694774)
    cur=cn.cursor()

    cur.execute('DROP TABLE IF EXISTS Customer')
    
    #Create table
    create_table=''' Create table if Not exists Customer(
                        ID serial primary key ,
                        first_name varchar (200) ,
                        last_name varchar (200) ,
                        phone_number text  )'''
    cur.execute(create_table)

    #insert table
    def insert(id,f_name,l_name,phone):
        insert_tabel='INSERT INTO Customer (ID, first_name , last_name , phone_number ) VALUES(%s,%s,%s,%s)'
        insert_values=(id,f_name,l_name,phone)
        cur.execute(insert_tabel,insert_values)
        print("inserted")
    
    #delete records
    def delete(Id):
        delete_record= 'DELETE FROM Customer WHERE ID=' + str(Id)
        cur.execute(delete_record)
        print("deleted")
    

    #update records
    def update(id , entity , new_entity):
        update_table='UPDATE Customer SET ' + entity +' = %s WHERE ID = %s'
        update_values=(new_entity,id)
        cur.execute(update_table,update_values)
        print("updated")

    

    #read table
    def read(ID):
        cur.execute('select * from Customer')
        for record in cur.fetchall():
            if record[0]==ID :
                print ("ID : ",record[0])
                print ("first name : ",record[1])
                print ("last name : ",record[2])
                print ("phone number : ",record[3])
    #test read
    

    #Test
    insert(1,'ali','alavi','09114608931')
    insert(2,'mohammad','mohammadi','09117685931')
    # insert(3,'sadegh','vahedi','09224490354')
    # delete(1)
    # update(2,  'last_name' , "rahmati")
    # read(2)

    cn.commit()
except Exception as eror:
    print(eror)
finally:
    if cur is not None:
        cur.close
    if cn is not None:
        cn.close
    
