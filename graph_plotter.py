print("""Refer 'Readme' file for solutions of some common issues
You are free to contact me :
  Discord:Loki_Laufeyson#2473 
  Telegram:https://t.me/Loki_Laufeyson_2473 
  Email: manwiththegoldengun837@gmail.com
if you find more issues/errors. """)
from colorama import Fore, Back, Style
import matplotlib.pyplot as plt
import numpy as np 
print(Fore.BLUE + 'Graph-- Plotter \u00A92022'), print('V 0.1.0')
print(Fore.WHITE + 'Graph-- Plotter made by HydroApps')
print("Give the graphsize/ width and height of the graph[in inches]. NOTE:By default they are 6.4 and 4.8 respectively : ")
m=int(input('Enter width:'))
n=int(input('Enter height:' ))
print("Enter the x values [min 5 values]:--")
print(Fore.GREEN + """Example: 
    input:1
          2
          3
          4
          5
          stop
    output: [1,2,3,4,5]  """
)
# try block to handle the exception
try:
	xv_list = []
	
	while True:
		xv_list.append(int(input()))
		
# if the input is not-integer, just print the list
except:
	print(Fore.WHITE +"Your x values",xv_list)
print("Enter the y values [min 5 values]:--")
print(Fore.GREEN + """Example: 
    input:9
          8
          7
          6
          4
          stop 
    output: [9,8,7,6,4]  """
)
# try block to handle the exception
try:
	xc_list = []
	
	while True:
		xc_list.append(int(input()))
		
# if the input is not-integer, just print the list
except:
    print(Fore.WHITE +"Your y values",xc_list) 
       
plt.figure(figsize=(m,n))
plt.plot(xv_list,xc_list)
print("Enter name for x and y axis ")
nax=input("Name of x axis: ")
nay=input("Name of y axis: ")
print("Enter fontsize of x and y variables")
fox=int(input("Enter fontsize of x variables: "))
foy=int(input("Enter fontsize of y variables: "))
print("Enter title for the graph")
tit=input("Title: ")
plt.xlabel(nax, fontsize=fox)
plt.ylabel(nay,fontsize=foy)
plt.title(tit)
print("Enter the degree of rotation of x and y labels:--")
print(Fore.GREEN + """Example:
           Input: 30
           Output: #The x or y label will rotate 30 degree
        Note: Enter zero for no rotation
""")
nod=int(input(Fore.WHITE+ "Enter degree of rotation for x variables: "))
nob=int(input("Enter degree of rotation for y variables: "))
plt.xticks(rotation=nod)
plt.yticks(rotation=nob)
plt.show()
print("Thank u for using Graph--plotter app!!:)")
k=input("press Enter to close or exit")