#------------------------CAJERO AUTOMATICO-----------------------------#
# 18/07/2021
# Santiago, Chile
# Eddie Casañas
# JAVA PORT
#----------------------------------------------------------------------#

saldo = 100000
salida = 0

while True:
	while True:
		print("\nBIENVENIDO AL CAJERO AUTOMATICO")
		print("(1): Consultar saldo")
		print("(2): Hacer retiro")
		print("(3): Hacer deposito")
		print("(4): Salir")
		
		opcion = input()
		if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
			continue
			
		if opcion == "1":
			print("\nCONSULTA DE SALDO")
			print("Su saldo es de: " + str(saldo) + "\n")
			
		elif opcion == "2":
			while True:
				print("\nELIJA EL MONTO A RETIRAR\n")
				print("(1): 1000")
				print("(2): 5000")
				print("(3): 10000")
				print("(4): 50000")
				print("(5): Ingrese un monto")
				print("(6): Volver")
				
				opcion = input()
				if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6":
					continue
					
				if opcion == "1":
					if saldo < 1000:
						print("\nSaldo insuficiente\n")
					else:
						saldo -= 1000
						print("RETIRO: 1000")
						print("SALDO: " + str(saldo) + "\n")
						
				elif opcion == "2":
					if saldo < 5000:
						print("\nSaldo insuficiente\n")
					else:
						saldo -= 5000
						print("RETIRO: 5000")
						print("SALDO: " + str(saldo) + "\n")
						
				elif opcion == "3":
					if saldo < 10000:
						print("\nSaldo insuficiente\n")
					else:
						saldo -= 10000
						print("RETIRO: 10000")
						print("SALDO: " + str(saldo) + "\n")
						
				elif opcion == "4":
					if saldo < 50000:
						print("\nSaldo insuficiente\n")
					else:
						saldo -= 50000
						print("RETIRO: 50000")
						print("SALDO: " + str(saldo) + "\n")
						
				elif opcion == "5":
					try:
						print("Ingrese un monto: ")
						monto = int(input())
						if saldo < monto:
							print("\nSaldo insuficiente\n")
						elif monto < 0:
							print("\nNo se puede retirar un monto negativo\n")
						else:
							saldo -= monto
							print("RETIRO: " + str(monto))
							print("SALDO: " + str(saldo) + "\n")
					except:
						print("\nIngrese un monto valido\n")
						
				elif opcion == "6":
					break
					
		elif opcion == "3":
			while True:
				print("\n(1): Ingresar el monto a depositar")
				print("(2): Volver")
				opcion = input()
				if opcion != "1" and opcion != "2":
					continue
				elif opcion == "1":
					try:
						print("\nINGRESAR EL MONTO: ")
						deposito = int(input())
						if deposito < 0:
							print("\nIngrese un monto valido\n")
						else:
							saldo += deposito
							print("\nDEPOSITO REALIZADO: " + str(deposito))	
							print("SALDO: " + str(saldo) + "\n")
					except:
						print("\nIngrese un monto valido\n")
						
					
					
				elif opcion == "2":
					break
						
		elif opcion == "4":
			salida = 1
			break
			
	if salida != 0:
		break	
