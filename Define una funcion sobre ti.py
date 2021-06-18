# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:36:27 2021

@author: sigri
"""

# Escribe aquí tu código

datos={"Nombre":"Sigrid","Mascota":True, "Edad":29, 
       "Peli":"perdona si te llamo amor"}



def muestra_datos(mis_datos):

   print("Nombre:",mis_datos["Nombre"])

   if mis_datos["Mascota"] == True:

       print("Mascota: Si")

   else:

       print("Mascota: No")

   print("Edad:",mis_datos["Edad"])

   print("Libro o peli favorita:",mis_datos["Peli"])

   return



muestra_datos(datos)

    