import mysql.connector
from CarDao import carDao

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="vehicles"
)

# Create a suppliers table
cursor = db.cursor()
sql="CREATE TABLE suppliers (`supplierID` int NOT NULL AUTO_INCREMENT,\
`name` varchar(50) DEFAULT NULL,\
`location` varchar(50) DEFAULT NULL,\
`phone` varchar(12) DEFAULT NULL,\
PRIMARY KEY (`supplierID`),\
KEY `supplierID` (`supplierID`))"
cursor.execute(sql)

# Create a cars table
cursor = db.cursor()
sql="CREATE TABLE cars (`cid` int NOT NULL AUTO_INCREMENT,\
`kind` enum('new','used') NOT NULL,\
`chassisID` varchar(20) NOT NULL,\
`manu_code` varchar(3) DEFAULT NULL,\
`manu_model` varchar(12) DEFAULT NULL,\
`year` int DEFAULT NULL,\
`mileage` int DEFAULT NULL,\
`price` int NOT NULL,\
`colour` varchar(20) DEFAULT NULL,\
`fuel` enum('petrol','diesel') DEFAULT NULL,\
`supplierID` int DEFAULT NULL,\
PRIMARY KEY (`cid`,`chassisID`),\
KEY `supplierID` (`supplierID`),\
CONSTRAINT `cars_ibfk_1` FOREIGN KEY (`supplierID`) REFERENCES `suppliers` (`supplierID`) ON DELETE SET NULL)"
cursor.execute(sql)

# Populate table with initial data for suppliers and cars
supplier1 = {
    'name': 'Barry Clarke',
    'location': 'Dundalk',
    'phone': '042_9312345'
}

supplier2 = {
    'name': 'Jimmy Murphy',
    'location': 'Swords',
    'phone': '01_6534271'
}

supplier3 = {
    'name': 'John Burke',
    'location': 'Drogheda',
    'phone': '041_9256381'
}

car1 = {
    'kind': 'new',
    'chassisID': '1234567',
    'manu_code': 'TOY',
    'manu_model': 'Corolla',
    'year': 2020,
    'mileage': 0,
    'price': 35000,
    'colour': 'silver',
    'fuel': 'petrol',
    'supplierID': 1
}

car2 = {
    'kind': 'new',
    'chassisID': '1234568',
    'manu_code': 'TOY',
    'manu_model': 'Avensis',
    'year': 2020,
    'mileage': 0,
    'price': 42000,
    'colour': 'blue',
    'fuel': 'petrol',
    'supplierID': 1
}

car3 = {
    'kind': 'used',
    'chassisID': '1234569',
    'manu_code': 'FOR',
    'manu_model': 'Focus',
    'year': 2018,
    'mileage': 18354,
    'price': 10000,
    'colour': 'Black',
    'fuel': 'Petrol',
    'supplierID': 3
}

car4 = {
    'kind': 'used',
    'chassisID': '1234570',
    'manu_code': 'FOR',
    'manu_model': 'Focus',
    'year': 2019,
    'mileage': 11000,
    'price': 15000,
    'colour': 'black',
    'fuel': 'petrol',
    'supplierID': 2
}

# Use functions in CarDao.py to populate the tables with the above initial supplier and car details
carDao.createSupplier(supplier1)
carDao.createSupplier(supplier2)
carDao.createSupplier(supplier3)

carDao.createCar(car1)
carDao.createCar(car2)
carDao.createCar(car3)
carDao.createCar(car4)
