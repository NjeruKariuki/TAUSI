from PIL import Image
import sys, os


#header & sub-header

print("\n\n\n")
print("%"*88)
print("*"*85)
print("\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
print("\t||||||           |||||  |||||||  |||||||  |||||/      /|||||  |||||||||||")
print("\t|/////////&  &//////// & \////$  |/////|  $///%  //////////|  |/////////|")
print("\t|/////////&  &/////// /_\ \ //$  |//////  $///%  (/////////|  |/////////|")
print("\t|/////////&  &//////  ___  \///$  \////  $////\       \////|  |/////////|")
print("\t|/////////&  &/////  ////\  \///$  \//  $///////////)  ////|  |/////////|")
print("\t|/////////&  &///%  (/////\  \///$     $///////       /////|  |/////////|")
print("\t|/////////(())//////////////////////////////////////////////////////////|")
print("\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
print("*"*85)
print("&"*88)
print("*"*90)

print("\n\t\t\tThis software views images.\n")

#boundary =
print("=" * 100)

#menu
print("\n \t\t\t  MENU")
print("\t\t\t ------")

#VARIABLE
key = input("\n\t1)-> Open_image " + "\n\t2)-> Image Properties" + " \n\t3)-> Filters" + " \n\t4)-> Crop & Resize" + " \n\t99)-> EXIT "+ "\n\n\t Choice: _")

pressed_key = int(key)
#logic
def menu_logic():
	try:
		if pressed_key == '1':
			print("Opening image...")
			return
		elif pressed_key == '2':
			print("Image property loading...")
		elif pressed_key == '3':
			print("Opening Filters...")
		elif pressed_key == '4':
			print("Crop & Resize loading...")
		elif pressed_key == '99':
			print("Exiting Program...")
			sys.exit()
	except:
		print("\a Invalid Choice!, Please Try again \n")

menu_logic()		

message = "\n \t\t Thank you for using my software\n"

#image class
name = input("\n\n\n\t\t Enter name of image you want to view: ")
image_name = str(name) + '.jpg'
image = Image.open(image_name)

class Image():
	def __init__(self):
		global x
	def open_image(self):
		var_key = input(">>>Press 1 to view image:\n")
		if var_key == '1':
			image.show()
		else:
			x.image_property()
	def image_property(self):
		trials = 0
		while trials <= 2:
			print("This shows you image properties: \n")
			key = input("-> Press 1 to see image size\n \n-> Press 2 to see image format\n")
			pressed_key = int(key)
			try:
				if pressed_key == 1:
					print("\n\t>>>image size: {}\n\n".format(image.size))
				elif pressed_key == 2:
					print("\n\t>>>image format: {}\n\n".format(image.format))
			except:
				print("\a\n\t Invalid key!, Try again \n")
			trials += 1
	def exit_program(self):
		ex_key = input("press 99 to exit program:\n ")
		if ex_key == '99':
			print("*"*100)
			print("%"*100)
			print("*"*100)
			print("\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t|||||||||||         |||||  ||||||  |||||||  ||||          |||||  ||||||  ||||||||  ||||||/           |||||||||")
			print("\t|/////////&  &///////////\  \////  //////|  |//////|  ||//////|  |////|   \////||  |/////  //////////////////|")
			print("\t|/////////&  &////////////\  \//  ///////|  |//////|  |///////|  |////|     \///|  |///|  ///////////////////|")
			print("\t|/////////&        |////////>   <//\/////|  |//////|  |///////|  |////|  |\  \//|  |///|  |////    \/////////|") 
			print("\t|/////////&  &/////////////  //\  \//////|  |//////|  |///////|  |////|  |//\  \|  |///|  |//////|  |////////|")
			print("\t|/////////&  &/////%//////  ////\  \/////|  |//////|  |///////|  |////|  |///\__   |///|   \/////   /////////|")
			print("\t|/////////&         |////  //////\  \////|  |//////|  |///////|  |////|  |//////|  |////\          //////////|")
			print("\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )
			print("*"*100)
			print("&"*100)	
			print("*"*100)
			print("\n\n")
			print("="*100)
			print(message.title())
			print("*"*100)
			
			sys.exit()

x = Image()
x.open_image()
x.image_property()
x.exit_program()
