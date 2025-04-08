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
                 "VALUES (%s, %s, %s)")
        self.cursor.execute(query, (username, first_name, last_name))
        self.connection.commit()

    def createDriver(self, username, first_name, last_name):
        query = ("INSERT INTO Driver "
                 "(username, firstName, lastName, active) "
                 "VALUES (%s, %s, %s, TRUE)")
        self.cursor.execute(query, (username, first_name, last_name))
        self.connection.commit()

    def signInRider(self, username):
        query = ("SELECT * "
                 "FROM Rider "
                 "WHERE username = %s")
        self.cursor.execute(query, [username])
        self.connection.commit()
        return self.cursor.fetchone()

    def signInDriver(self, username):
        query = ("SELECT * "
                 "FROM Driver "
                 "WHERE username = %s")
        self.cursor.execute(query, [username])
        self.connection.commit()
        return self.cursor.fetchone()

    def viewRating(self, username):
        query = ("SELECT AVG(rating) "
                 "FROM Ride "
                 "WHERE driver = %s")
        self.cursor.execute(query, [username])
        self.connection.commit()
        res = self.cursor.fetchone()[0]
        if res is None:
            return "No ratings yet."
        else:
            return res

    def getIsActive(self, username):
        query = ("SELECT active "
                 "FROM Driver "
                 "WHERE username = %s")
        self.cursor.execute(query, [username])
        self.connection.commit()
        return self.cursor.fetchone()[0]

    def toggleDrivingMode(self, username):
        res = self.getIsActive(username)
        if res == 0:
            query = ("UPDATE Driver "
                     "SET active = TRUE "
                     "WHERE username = %s")
            self.cursor.execute(query, [username])
            self.connection.commit()
            return "Driving mode activated."
        else:
            query = ("UPDATE Driver "
                     "SET active = FALSE "
                     "WHERE username = %s")
            self.cursor.execute(query, [username])
            self.connection.commit()
            return "Driving mode deactivated."

    def viewRidesDriven(self, username):
        query = ("SELECT rider, pickUpLocation, dropOffLocation, rating "
                 "FROM Ride "
                 "WHERE driver = %s")
        self.cursor.execute(query, [username])
        self.connection.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
