

def q1(): 
  #Write Assignment code here
  word = input("In: ")
  if word[-3:] == "ife":
    print("-ives")
  elif word[-2:] == "ey":
    print ("-eys")
  elif word[-1:] == "y":
    print ("-ies")
  else:
    print ("-s")



def q2(): 
  #Write Assignment code here
  num = int(input("In: "))
  if num == 0:
    ()
  elif num > 0:
    print(f"{num} is positive")
  else:
    print (f"{num} is negative")




def q3(): 
  tri1 = float(input("Input a number: "))
  tri2 = float(input("Input a number: "))
  tri3 = float(input("Input a number: "))
  if tri1+tri2<tri3 or tri2+tri3<tri1 or tri3+tri1<tri2:
    print("No Triangle") 
  elif tri1 == tri2 and tri1 == tri3 and tri2 == tri3:
    print ("Equilateral")
  elif tri1==tri2 or tri2==tri3 or tri3==tri1:
    print("Isosceles")
  elif tri1!=tri2 and tri2!=tri3 and tri2!=tri3:
    print ("Scalene")
  

#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()