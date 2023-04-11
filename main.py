import threading
import time
from pymongo import MongoClient
from random import *

client = MongoClient('mongodb://localhost:27017')

db = client['bancoiot']

sensores = db.sensores


def mudaTemp1(nome, intervalo):
    while True:
        temp = (randint(30, 40))
        print("Temp1 ", temp)
        result = sensores.update_one(
            {"nomeSensor": "Temp1"},
            {
                "$set": {"valorSensor": temp}
            })
        if temp > 38:
            result = sensores.update_one(
                {"nomeSensor": "Temp1"},
                {
                    "$set": {"sensorAlarmado": "true"}
                })
            print("Atenção! Temperatura  muito  alta! Verificar Sensor 1!")
            results = sensores.find()
            for aux in results:
                print(aux)
            break
        time.sleep(intervalo)


def mudaTemp2(nome, intervalo):
    while True:
        temp = (randint(30, 40))
        print("Temp2 ", temp)
        result = sensores.update_one(
            {"nomeSensor": "Temp2"},
            {
                "$set": {"valorSensor": temp}
            })
        if temp > 38:
            result = sensores.update_one(
                {"nomeSensor": "Temp2"},
                {
                    "$set": {"sensorAlarmado": "true"}
                })
            print("Atenção! Temperatura  muito  alta! Verificar Sensor 2!")
            results = sensores.find()
            for aux in results:
                print(aux)
            break
        time.sleep(intervalo)


def mudaTemp3(nome, intervalo):
    while True:
        temp = (randint(30, 40))
        print("Temp3 ", temp)
        result = sensores.update_one(
            {"nomeSensor": "Temp3"},
            {
                "$set": {"valorSensor": temp}
            })
        if temp > 38:
            result = sensores.update_one(
                {"nomeSensor": "Temp3"},
                {
                    "$set": {"sensorAlarmado": "true"}
                })
            print("Atenção! Temperatura  muito  alta! Verificar Sensor 3!")
            results = sensores.find()
            for aux in results:
                print(aux)
            break
        time.sleep(intervalo)


lista = [{
    "nomeSensor": "Temp1",
    "valorSensor": "",
    "unidadeMedida": "ºC",
    "sensorAlarmado": "false"
},
    {
        "nomeSensor": "Temp2",
        "valorSensor": "",
        "unidadeMedida": "ºC",
        "sensorAlarmado": "false"
    },
    {
        "nomeSensor": "Temp3",
        "valorSensor": "",
        "unidadeMedida": "ºC",
        "sensorAlarmado": "false"
    }]

insert = db.sensores.insert_many(lista)

x1 = threading.Thread(target=mudaTemp1, args=('Thread 1', 1))
x1.start()

x2 = threading.Thread(target=mudaTemp2, args=('Thread 2', 1))
x2.start()

x3 = threading.Thread(target=mudaTemp3, args=('Thread 3', 1))
x3.start()
