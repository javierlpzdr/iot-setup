import paho.mqtt.client as mqtt
import os

# Variables

broker_address="localhost"
option1="true" # Variable that determines if the first dish is available
option2="false" # Variable that determines if the second dish is availble


# Functions

"""
Determine if there are enough ingredients to make the order. If not, It prints a message.
"""
def check_on_stock(order, option, client):
	print("Comprando si hay stock...")
	if option == 'true':
		client.publish("restaurant/orders/order", order)
		print ("Orden hecha!")
	else:
		print ("ups, parece que no queda!")

"""

"""
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("restaurant/dishes/dish/#")

def on_message(client, user_data, message):
	if message.topic=="restaurant/dishes/dish/1":
		option1=message.payload
	elif message.topic=="restaurant/dishes/dish/2":
		option2=message.payload

# Starting the program...

print("Creating a new instance")
client = mqtt.Client("iot-restaurant")
client.on_connect = on_connect
client.on_message = on_message

print("connecting to broker")
client.connect(broker_address, 1883, 60)

client.loop_start()
def menu():

	"""

	Menu to show

	"""

	os.system('clear')

	print ("Selecciona una opción")

	print ("\t1 - Slow Cooker Texas Pulled Pork")

	print ("\t2 - Slow Cooker Pork Ramen")

	print ("\t9 - salir")



while True:

	# Mostramos el menu

	menu()

	# solicituamos una opción al usuario

	opcionMenu = input("inserta un numero valor >> ")


	if opcionMenu=="1":

		print ("Has seleccionado Slow Cooker Texas Pulled Pork")

		check_on_stock(opcionMenu, option1, client)

		input("Has pulsado la opción 1...\npulsa una tecla para continuar")

	elif opcionMenu=="2":

		print ("Has seleccionado Slow Cooker Pork Ramen")

		check_on_stock(opcionMenu, option2, client)

		input("Has pulsado la opción 2...\npulsa una tecla para continuar")

	elif opcionMenu=="9":

		break

	else:

		print ("")

		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")