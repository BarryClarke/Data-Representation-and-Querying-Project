import mysql.connector
import dbconfig as cfg

class CarDao:
    db = ""
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host =      cfg.mysql['host'],
            user =      cfg.mysql['user'],
            password =  cfg.mysql['password'],
            database =  cfg.mysql['database']
        )
    
    def __init__(self):
        self.connectToDB()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    
    def getAllSupplier(self):
        cursor = self.getCursor()
        sql = "select * from suppliers"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictSupplier(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray # This will be an array of dict objects
    

    def findByLocation(self, location):
        cursor = self.getCursor()
        sql = "select * from suppliers where location = %s"
        values = [location]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictSupplier(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray # This will be an array of dict objects
    
    def findByIdSupplier(self, supplierID):
        cursor = self.getCursor()
        sql = "select * from suppliers where supplierID = %s"
        values = [supplierID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDictSupplier(result)
    
    def getAllCar(self):
        cursor = self.getCursor()
        #cursor = self.db.cursor()
        sql = "select cars.*, IFNULL(suppliers.name, 0), IFNULL(suppliers.location, 0), IFNULL(suppliers.phone, 0) from cars LEFT JOIN suppliers on cars.supplierID = suppliers.supplierID order by cars.cid"
        #sql = "select cars.*, suppliers.name, suppliers.location, suppliers.phone from cars LEFT JOIN suppliers on cars.supplierID = suppliers.supplierID order by cars.cid"
        #sql = "select * from cars"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictCar1(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray # This will be an array of dict objects
    
    def findByModel(self, model):
        cursor = self.getCursor()
        sql = "select * from cars where manu_model = %s"
        values = [model]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictCar(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray # This will be an array of dict objects
    
    def findByKind(self, kind):
        cursor = self.getCursor()
        sql = "select * from cars where kind = %s"
        values = [kind]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        #print(results) # This is an array of tuples
        for result in results:
            resultAsDict = self.convertToDictCar(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray # This will be an array of dict objects
    
    def findByChassis(self, chassisID):
        cursor = self.getCursor()
        #sql = "select * from cars where chassisID = %s"
        sql = "select cars.*, suppliers.name, suppliers.location, suppliers.phone from cars LEFT JOIN suppliers on cars.supplierID = suppliers.supplierID where cars.chassisID = %s" #order by cars.cid"
        values = [chassisID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDictCar1(result)
    
    def findByIdCar(self, cid):
        cursor = self.getCursor()
        #sql = "select * from cars where cid = %s"
        sql = "select cars.*, suppliers.name, suppliers.location, suppliers.phone from cars INNER JOIN suppliers on cars.supplierID = suppliers.supplierID where cars.cid = %s order by cars.cid"
        values = [cid]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDictCar1(result)

    # Create operations
    # Create Supplier
    def createSupplier(self, supplier):
        cursor = self.getCursor()
        sql = "Insert into suppliers (name, location, phone) values (%s,%s,%s)"
        values= [
            supplier["name"],
            supplier["location"],
            supplier["phone"],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid    
    
    # Create Car
    def createCar(self, car):
        cursor = self.getCursor()
        sql = "Insert into cars (kind, chassisID, manu_code, manu_model, year, mileage, price, colour, fuel, supplierID)\
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values= [
            car["kind"],
            car["chassisID"],
            car["manu_code"],
            car["manu_model"],
            car["year"],
            car["mileage"],
            car["price"],
            car["colour"],
            car["fuel"],
            car["supplierID"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid
    
    # Update operations
    # Update Car
    def updateCar(self, car):
        cursor = self.getCursor()
        sql = "update cars set kind = %s,  manu_code = %s, manu_model = %s, year = %s, mileage = %s, price = %s, colour = %s, fuel = %s, supplierID = %s where chassisID = %s"
        values= [
            car["kind"],
            car["manu_code"],
            car["manu_model"],
            car["year"],
            car["mileage"],
            car["price"],
            car["colour"],
            car["fuel"],
            car["supplierID"],
            car["chassisID"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return car
    
    # Update Supplier
    def updateSupplier(self, supplierID):
        cursor = self.getCursor()
        sql = "update suppliers set name = %s, location = %s, phone = %s where supplierID = %s"
        values= [
            supplierID["name"],
            supplierID["location"],
            supplierID["phone"],
            supplierID["supplierID"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return supplierID
    
    # Delete operations
    # Delete Car
    def deleteCar(self, chassisID):
        cursor = self.getCursor()
        sql = "delete from cars where chassisID = %s"
        values = [chassisID]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid
    
    # Delete Supplier
    def deleteSupplier(self, supplierID):
        cursor = self.getCursor()
        sql = "delete from suppliers where supplierID = %s"
        values = [supplierID]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid


    # function to convert a tuple to a dict object for the suppliers table
    def convertToDictSupplier(self, result):
        colnames = ['supplierID','name', 'location', 'phone']
        supplier = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                supplier[colName] = value
        return supplier
    
    
    # function to convert a tuple to a dict object for the cars table
    def convertToDictCar(self, result):
        colnames = ['cid', 'kind', 'chassisID', 'manu_code', 'manu_model', 'year', 'mileage', 'price', 'colour', 'fuel', 'supplierID']
        car = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                car[colName] = value
        return car
    
    # function to convert a tuple to a dict object for the cars table
    def convertToDictCar1(self, result):
        colnames = ['cid', 'kind', 'chassisID', 'manu_code', 'manu_model', 'year', 'mileage', 'price', 'colour', 'fuel', 'supplierID', 'name', 'location', 'phone']
        car = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                car[colName] = value
        return car

carDao = CarDao()