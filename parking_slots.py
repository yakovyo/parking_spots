import mysql.connector
import random

try:
    runway = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db",
        pool_name="cp",
        pool_size=10
    )
    cursor = runway.cursor()
    # cursor.execute("CREATE TABLE FLIGHTS"
    #                "(id INT(6) PRIMARY KEY,"
    #                "ARRIVAL INT(12),"
    #                "DEPARTURE INT(12))")

    print(runway)
except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")


# please use this class for each incoming plane.
class Airplane:
    def __init__(self, db):
        self.__db = db
        self.__cursor = self.__db.cursor()

    # self.flight_number = flight_number
    # self.arrival = arrival
    # self.departure = departure

    # self.departure = arrival + random.randint(40,80)
    #
    # @property
    # def flight_number(self):
    #     return self.flight_number
    #
    # @property
    # def departure(self, departure):
    #     if self.departure == 0:
    #         return self.arrival + random.randint(40, 80)

    # just making sure the info is collected corectly
    # def __str__(self):
    #     return f"Flight #{self.flight_number}, arrived at: {self.arrival}, and will take off at: {self.departure}."

    def add_flight(self, flight_number, arrival, departure):
        sql = "INSERT INTO FLIGHTS (ID, ARRIVAL, DEPARTURE) VALUES (%s, %s, %s)"
        values = (flight_number, arrival, departure)
        if type(flight_number) is not int or type(arrival) is not int or type(departure) is not int:
            print(f"Error: invalid values")
        try:
            self.__cursor.execute(sql, values)
            self.__db.commit()

        except Exception as error:
            print(f"Error: {error}")


# aa = Airplane('AZ08', 1210, 1325)
# ab = Airplane('LY01', 1600, 1705)
# print(aa)
# print(ab)

a = Airplane(db=runway)
a.add_flight(35, 1630, 1715)
# a.flight_number = 25
# a.arrival = 1600
# a.departure = 1655

a = ("SELECT * FROM db.flights;")
print(a)