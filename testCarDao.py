from CarDao import carDao

supplier1 = {
    'name': 'Barry Clarke',
    'location': 'Dundalk',
    'phone': 42_9312345
}

supplier2 = {
    'name': 'Jimmy Murphy',
    'location': 'Swords',
    'phone': 1_6534271
}

supplier2 = {
    'name': 'Johy Murphy',
    'location': 'Drogheda',
    'phone': 41_9256381
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
    'chassisID': '1234569',
    'manu_code': 'TOY',
    'manu_model': 'Avensis',
    'year': 2020,
    'mileage': 0,
    'price': 45000,
    'colour': 'blue',
    'fuel': 'petrol',
    'supplierID': 1
}

car3 = {
    'kind': 'used',
    'chassisID': '1234567',
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
    'chassisID': '1234567',
    'manu_code': 'FOR',
    'manu_model': 'Focus',
    'year': 2019,
    'mileage': 11000,
    'price': 15000,
    'colour': 'black',
    'fuel': 'petrol',
    'supplierID': 2
}






#returnvalue = carDao.createSupplier(supplier1)
#returnvalue = carDao.createSupplier(supplier2)

#print("Get All Suppliers")
#returnvalue = carDao.getAllSupplier()
#print(returnvalue)
#returnvalue = carDao.createCar(car1)
#returnvalue = carDao.createCar(car2)
#returnvalue = carDao.createCar(car3)
#returnvalue = carDao.getAllCar()
#print("Get All Cars")
#print(returnvalue)
#returnvalue = carDao.findByModel(car2['manu_model'])
#print("Find By car Model")
#print(returnvalue)
#returnvalue = carDao.delete(car1['reg'])
#print(returnvalue)
returnvalue = carDao.getAllCar()
print("Get All")
print(returnvalue)



#returnvalue = carDao.updateCar(car2)
#print("Updated car 2")
#print(returnvalue)
#returnvalue = carDao.findByChassis(1234567)
#print("Find By Chassis")
#print(returnvalue)
#returnvalue = carDao.delete(car2['reg'])
#print(returnvalue)
#returnvalue = carDao.getAll()
#print("Get All")
#print(returnvalue)
