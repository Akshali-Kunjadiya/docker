
import streamlit as st
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='mysql',
                                     database='my_db',
                                     user='akshali',
                                     password='Akshali3208')
cursor=connection.cursor()

def add(id,name,price):
    cursor=connection.cursor()
    insert_query="""INSERT INTO product(Id,Name,Price) VALUES(%s,%s,%s)"""
    val=[(id,name,price)]
    cursor.executemany(insert_query,val)
    connection.commit()

def delete(id):
    cursor=connection.cursor()
    delete_query="""DELETE FROM product WHERE Id=%s"""
    val=[(id)]
    cursor.execute(delete_query,val)
    connection.commit()

def update(id,name,price):
    cursor=connection.cursor()
    update_query=f"UPDATE  product SET Name='{name}',Price='{price}' WHERE Id={id}"
    cursor.execute(update_query)
    connection.commit()

try:

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        st.header("Product Details")
        id=st.number_input('ID',step=1)
        name=st.text_input('Name')
        price=st.number_input('Price')
        st.button('ADD',on_click=add,args=[id,name,price])

        delete_id=st.number_input('DELETE_ID',step=1)
        st.button('DELETE',on_click=delete,args=[delete_id])

        id=st.number_input('UID',step=1)
        name=st.text_input('UName')
        price=st.number_input('UPrice')
        st.button('UPDATE',on_click=update,args=[id,name,price])
        cursor=connection.cursor()
        result_query="""SELECT * FROM product"""
        cursor.execute(result_query)
        result=cursor.fetchall()
        st.dataframe(result)
        print("display")
        cursor.close()
except Error as e:
    print("Error while connecting to MySQL", e)

