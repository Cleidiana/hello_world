from python_opcua.opcua import Client
from random import randint
import datetime
import time


url = "opc.tcp://192.168.60.112:4840"

client = Client(url)
client.connect()
print("Cliente conectado")

while True:
	Temp = client.get_node("ns=2;i=2")
	Temperature = Temp.get_value()
	print(Temperature)
	
	Press = client.get_node("ns=2;i=3")
	Pressure = Press.get_value()
	print(Pressure)
	
	Time = client.get_node("ns=2;i=4")
	TIME_Value = Time.get_value()
	print(TIME_Value)
	time.sleep(1)
