import sqlite3
connect = sqlite3.Connection("Bus_Booking_System.db")
c = connect.cursor()

#c.execute("""CREATE TABLE IF NOT EXISTS BUS(Bus_ID int, Type text, Capacity int, Fare int, Route_ID int, Operator_ID int, PRIMARY KEY(BUS_ID),
#FOREIGN KEY(Operator_ID) references OPERATOR(Operator_ID), FOREIGN KEY(Route_ID) references Route(Route_ID))""")
#c.execute("""CREATE TABLE IF NOT EXISTS OPERATOR(Operator_ID int, Opt_Name text, Address text, Email_ID text,Phone_no int, PRIMARY KEY(OPERATOR_ID),
#FOREIGN KEY(Operator_ID) references BUS(Operator_Id))""")
c.execute("""CREATE TABLE IF NOT EXISTS ROUTE(Route_ID int , Station_id int,Station_Name text, PRIMARY KEY(Route_ID, Station_id),
FOREIGN KEY(Route_ID) references BUS(Route_ID))""")
#c.execute("""CREATE TABLE IF NOT EXISTS RUN(Bus_ID int, Date date, Seat_Availavle int, PRIMARY KEY(BUS_ID, Date),
#FOREIGN KEY(BUS_ID) references BUS(Bus_ID))""")


#c.execute("""CREATE TABLE IF NOT EXISTS BOOKING_HISTORY(Booking_ID int AUTO INCREMENT, Passengers_Name text, Gender text, No_of_seats int, Mobile_no int,
#Fare int, Bus_ID int, PRIMARY KEY(Booking_ID), FOREIGN KEY(BUS_ID) references BUS(BUS_ID))""")

c.execute("""select b.Bus_Id,ro.route_id, o.opt_name, b.type, r.seat_availavle, b.capacity, b.fare from route as ro, bus as b, operator as o, run as r where ro.route_id = b.route_id and
         b.operator_Id = o.operator_id and b.bus_id = r.bus_id and ro.station_name = "Guna" and ro.station_name = "Bhopal"
         """)  
#c.execute("select * from route")

records = c. fetchall()
print(records)


connect.commit()
connect.close()

#cur.execute('''Select name,bus_type,capacity,fare,bus_id from bus as a,bus_operator as b,route as f, route as t where f.station_name=? and t.station_name=? and
#f.station_id<t.station_id and f.route_id=t.route_id and t.route_id=f.route_id and a.op_id=b.op_id''',(From,To))
