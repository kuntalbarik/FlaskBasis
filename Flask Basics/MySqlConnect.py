####CRUD operations using Mysql+Flask
###C===Create(Create Database,Create Table,Insert)
###R===Read  (Select)
###U===Update(Update)
###D===Delete (Delete)

import mysql.connector
from mysql.connector import Error
import os,json


path="CONFIG/DB_Connection.json"
absfilepath = os.path.abspath(__file__)
fileDir = os.path.dirname(absfilepath)
filename = os.path.join(fileDir, path)
filename = os.path.abspath(os.path.realpath(filename))
readJson = open(filename, "r")
data = json.load(readJson)

class MySqlConnector:

    def ConnectDB(self,dbName:str=None):
        self.__dbName=dbName.lower()
        if(self.__dbName!=None):
            try:
                self.__mydb = mysql.connector.connect(
                    host=data["host"],
                    user=data["user"],
                    password=data["password"],
                    database=self.__dbName
                )
                if self.__mydb.is_connected():
                    return self.__mydb

            except Error as e:
                print("Not able to connect {} database or database does not exists\n".format(self.__dbName),e)
                return False

        else :
            try:
                self.__mydb = mysql.connector.connect(
                    host=data["host"],
                    user=data["user"],
                    password=data["password"]
                )
                if self.__mydb.is_connected():
                    return self.__mydb

            except Error as e:
                print("not able to connect to MySql,check error log\n", e)
                return False

    def CreateDB(self,dbName:str):
        self.__mysqlconnector=MySqlConnector()
        self.__dbName=dbName.lower()
        self.__dbConnectionObject=self.__mysqlconnector.ConnectDB()
        self.__mycursor=self.__dbConnectionObject.cursor()
        self.__mycursor.execute("SHOW DATABASES")
        self.__databaseExists = 0
        for x in self.__mycursor:
            if (str(x[0]) == self.__dbName):
                self.__databaseExists = 1
                break
        if self.__databaseExists == 1:
            print("DataBase {} already exists".format(self.__dbName))
            self.__dbConnection =self.__mysqlconnector.ConnectDB(self.__dbName)
            return self.__dbConnection
        else:
            self.__mycursor.execute("CREATE DATABASE " + self.__dbName)
            print(self.__dbName, "Database created successfully")
            self.__dbConnection = self.__mysqlconnector.ConnectDB(self.__dbName)
            return self.__dbConnection

    def CreateTable(self,dbName:str,tableName:str,sqlQuery:str):
        self.__mysqlconnector = MySqlConnector()
        self.__dbName=dbName.lower()
        self.__tableName=tableName.lower()
        self.__sqlQuery=sqlQuery
        self.__dbConnection=self.__mysqlconnector.ConnectDB(self.__dbName)
        if self.__dbConnection==False:
            print("Not able to connect {} database or database does not exists".format(self.__dbName))
            self.__dbConnection.close()
            return False
        else:
            self.__mycursor=self.__dbConnection.cursor()
            self.__mycursor.execute("SHOW TABLES")
            self.__tableExists = 0
            for x in self.__mycursor:
                if (str(x[0]) == self.__tableName):
                    self.__tableExists = 1
                    break
            if self.__tableExists == 1:
                print("Table {} already exists".format(self.__tableName))
                self.__mycursor.close()
            else:
                self.__mycursor.execute(self.__sqlQuery)
                print("{} table created successfully".format(self.__tableName))
                self.__dbConnection.close()

    def DMF(self,dbName:str,operation:str,sqlQuery:str,values:tuple=None):
        try:
            self.__operation=operation.lower()
            if(self.__operation in ('insert','update','delete')):
                self.__mysqlconnector = MySqlConnector()
                self.__dbName = dbName.lower()
                self.__sqlQuery = sqlQuery
                self.__values =values
                self.__dbConnection =self.__mysqlconnector.ConnectDB(self.__dbName)
                if self.__dbConnection != False:
                    self.__mycursor = self.__dbConnection.cursor()
                    self.__mycursor.execute(self.__sqlQuery,self.__values)
                    self.__dbConnection.commit()
                    self.__dbConnection.close()
                    print("{} record(s) {}ed.".format(self.__mycursor.rowcount,self.__operation.lower()))
            else:
                print("No valid operation selected,Please select a valid operation among Insert,Update,Delete")
        except Error as e:
            print("No valid operation selected,Please select a valid operation among Insert,Update,Delete")

    def SelectData(self,dbName:str,sqlQuery:str,values:tuple=None):
        self.__mysqlconnector = MySqlConnector()
        self.__dbName = dbName.lower()
        self.__sqlQuery = sqlQuery
        self.__values = values
        self.__dbConnection =self.__mysqlconnector.ConnectDB(self.__dbName)

        if self.__dbConnection !=False:
            self.__mycursor = self.__dbConnection.cursor()
            self.__mycursor.execute(self.__sqlQuery,self.__values)
            self.__myresult =self.__mycursor.fetchall()
            # for x in self.__myresult:
            #     print("AuthorID :-",x[0],end=" | ")
            #     print("FirstName :-", x[1],end=" | ")
            #     print("LastName :-", x[2],end=" | ")
            #     print("Country :-", x[3],end="\n")
            self.__dbConnection.close()
            return self.__myresult
        else:
            print("Not able to connect {} database or database does not exists".format(self.__dbName))
            self.__dbConnection.close()


dbName="FlaskBasics"
tableName="Authors"

###Insert
# sqlQuery="insert into FlaskBasics.authors (firstName,Lastname,Country) values (%s,%s,%s)"
# values=("Sudip","Khanra","England")
# DMF(dbName,"insert",sqlQuery,values)

# ##Select from DB ####
sqlQuery="select * from authors where id=%s"
values=(1,)


# ###update
# sqlQuery="update FlaskBasics.Authors set country=%s where id=%s"
# values=("Nepal",2)
# DMF(dbName,"UpdAte",sqlQuery,values)

###Delete
# sqlQuery="delete from FlaskBasics.authors where id=3"
# sqlQuery="delete from FlaskBasics.authors where id=%s"
# values=(2,)
# DMF(dbName,"DELETE",sqlQuery,values)


mysqlconnector=MySqlConnector()
#mysqlconnector.DMF(dbName,"insert",sqlQuery,values)
result=mysqlconnector.SelectData(dbName,sqlQuery,values)
print(result)