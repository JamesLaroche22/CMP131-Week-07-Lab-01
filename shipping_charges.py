#James Laroche
#CMP131 
#Week07 
#Lab01 
#shipping_charges
#10/14/26 
weight=float(input("Enter the weight of the package in Kilograms: "))
while(weight<=0 or weight>20):    
    weight=float(input("Please enter a value between 1 to 20: ")) 
distance=int(input("Enter the distance the package is to be shipped in Miles: ")) 
while(distance<10 or distance>3000): 
    distance=int(input("Please enter a value between 10 to 3000: ")) 
if weight<=2:
    rate=1.10 

elif weight>2 and weight<=6:
    rate=2.20 
elif weight>6 and weight<=10: 
    rate=3.70 
elif weight>10 and weight<=20: 
    rate=4.80 
charge = rate * (distance/500) 
