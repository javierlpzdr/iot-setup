import paho.mqtt.client as mqtt
import os

# Variables

broker_address="localhost"
option1 = True # Variable that determines if the first dish is available
option2 = True # Variable that determines if the second dish is availble


# Functions

""" Swith functions
Change theirs the variable associated to true/false. Regarding to the stock of the dish, it will
be updated through a message from the broker
"""
def switch1():
	option1 = not option1

def switch2():
	option2 = not option2

"""
Determine if there are enough ingredients to make the order. If not, It prints a message.
"""
def check_on_stock(order, option, client):
	print("Comprando si hay stock...")
	if option == True:
		client.publish("restaurant/orders/order", order)
	else:
		print ("ups, parece que no queda!")

"""

"""
def on_message(client, user_data, message):
    switcher = {
        'restaurant/dishes/1 - switch': switch1,
        'restaurant/dishes/1 - switch': switch2
    }

    func = switcher.get(message.topic + ' - ' + message.payload)

    func(client, message)


# Starting the program...

print("Creating a new instance")
client = mqtt.Client("iot-restaurant")
client.on_message = on_message

print("connecting to broker")
client.connect(broker_address, 1883, 60)

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