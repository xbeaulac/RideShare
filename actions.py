import mysql.connector


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="RideShare"
        )
        self.cursor = self.connection.cursor(buffered=True)

    def createRider(self, username, first_name, last_name):
        query = ("INSERT INTO Rider "
                 "(username, firstName, lastName) "
                 "VALUES (%s %s %s)")
        self.cursor.execute(query, (username, first_name, last_name))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
