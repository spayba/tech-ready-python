import turtle

turtle.speed(0)
turtle.setup(width=1280,height=960,startx=0,starty=0)
checkers= ['C','H','E','C','K','E','R','S']
turtle.penup()
turtle.goto(-225,-400)
turtle.pendown()
for x in range(8):
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.write(checkers[x], False, align = "center", font= ("Rockwell", 42, "normal"))
turtle.penup()
turtle.goto(-300,300)
turtle.pendown()
for x in range(4):
  turtle.fd(600)
  turtle.rt(90)

def lines():
  for x in range(8):
      turtle.fd(75)
      turtle.rt(90)           
      turtle.fd(600)
      turtle.back(600)
      turtle.left(90)
lines()

turtle.rt(90)

lines()

turtle.penup()
turtle.goto(-335,300)
turtle.pendown()

letters=['0','1','2', '3', '4', '5', '6', '7']

def sideletters():
  for x in range(8):
      turtle.penup()
      turtle.fd(75)
      turtle.pendown()
      turtle.write(letters[x], False, align = "center", font= ("Lato", 42, "normal"))

sideletters()

turtle.penup()
turtle.goto(-337.5,302)
turtle.pendown()
turtle.left(90)

sideletters()

redpieces=[[],[]]
blackpieces=[[],[]]


turtle.penup()
turtle.goto(-300,300)
turtle.pendown()

z=1
v=0
for x in range(3):
   for x in range(4):
       if z%2 == 1:
           redpieces[0].append(turtle.xcor()+(3*37.5)+(v*4*37.5) )
           redpieces[1].append(turtle.ycor()-37.5)
           v += 1
       else:
           redpieces[0].append(turtle.xcor()+(37.5 +(v*4*37.5)))
           redpieces[1].append(turtle.ycor()-37.5)
           v += 1
   z += 1
   v=0
   turtle.penup()
   turtle.goto(-300,turtle.ycor()-75)
   turtle.pendown()

turtle.penup()
turtle.goto(-300,-75)
turtle.pendown()

z=1
v=0
for x in range(3):
   for x in range(4):
       if z%2 == 1:
           blackpieces[0].append(turtle.xcor()+(37.5 +(v*4*37.5)))
           blackpieces[1].append(turtle.ycor()-37.5)
           v += 1
       else:
           blackpieces[0].append(turtle.xcor()+(3*37.5)+(v*4*37.5) )
           blackpieces[1].append(turtle.ycor()-37.5)
           v += 1
   z += 1
   v=0
   turtle.penup()
   turtle.goto(-300,turtle.ycor()-75)
   turtle.pendown()

for x in range(12):
  turtle.penup()
  turtle.goto(redpieces[0][x],redpieces[1][x])
  turtle.pendown()
  turtle.pencolor('red')
  turtle.dot(52)

for x in range(12):
  turtle.penup()
  turtle.goto(blackpieces[0][x],blackpieces[1][x])
  turtle.pendown()
  turtle.pencolor('black')
  turtle.dot(52)

##################################################################################################

"""u =[]
for x in range (12):   #For a winner
   u[x] = " " """
u=0
w=0
q=0
t=0
while u < 30:
   if w == 0:
       print("\n**********Black Pieces Player's Turn**********\n")
       print("**********Choosing Piece to Move**********")

       y=0
       v=0
       z=0
       while y == 0:
           turtle.penup()
           turtle.goto(-300,300)
           leftnumber = int(input("\nPlease choose a left number:    "))
           topnumber= int(input("Please choose a top number:    "))

           if leftnumber < 0 or leftnumber > 8:
               print("\nleft number out of range. please try again.\n")
           else:
               if topnumber < 0 or topnumber > 8:
                   print("\ntop number is out of range. please try again.\n")
               else:
                   if leftnumber > 0 and leftnumber < 8:
                       turtle.goto(-300,300-37.5-(75*leftnumber))
                   else:
                       turtle.goto(-300,300-37.5)

                   if topnumber > 0 and topnumber < 8:
                       turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                   else:
                       turtle.goto(-300 + 37.5,turtle.ycor())
                      
                   for x in range (12):
                       if blackpieces[0][x] == turtle.xcor() and blackpieces[1][x] == turtle.ycor():
                           print("\nValid\n")
                           y=1
                           v=x
                       elif x == 11 and y!=1:
                           print("\nInvalid. Please Try Again\n")

                   if topnumber == 0:
                       for x in range(12):
                           if blackpieces[0][x] == turtle.xcor()+75 and blackpieces[1][x] == turtle.ycor()+75:
                               print("However, this piece is unable to move. Please try again.")
                               y=0

                   elif topnumber == 7:
                       for x in range(12):
                           if blackpieces[0][x] == turtle.xcor()-75 and blackpieces[1][x] == turtle.ycor()+75:
                               print("However, this piece is unable to move. Please try again.")
                               y=0
                   else:
                       for x in range(12):
                           if blackpieces[0][x] == turtle.xcor()-75 and blackpieces[1][x] == turtle.ycor()+75:
                               for x in range(12):
                                   if blackpieces[0][x] == turtle.xcor()+75 and blackpieces[1][x] == turtle.ycor()+75:
                                       print("However, this piece is unable to move. Please try again.")
                                       y=0



       print("**********Choosing Destination**********")

       turtle.penup()

       y = 0

       while y == 0:

           dleftnumber = int(input("\nPlease choose a left number:    "))
           dtopnumber= int(input("Please choose a top number:    "))


           if dleftnumber < 0 or dleftnumber > 8:
               print("\nleft number out of range. please try again.\n")
           else:
               if dtopnumber < 0 or dtopnumber > 8:
                   print("\ntop number is out of range. please try again.\n")
               else:
                   if dleftnumber != leftnumber - 1:
                       print ("Invalid left number. Please try again")
                   else:
                       if dtopnumber == topnumber-1 or dtopnumber == topnumber +1:

                           if dleftnumber > 0 and dleftnumber < 8:
                               turtle.goto(-300,300-37.5-(75*dleftnumber))
                           else:
                               turtle.goto(-300,300-37.5)
                          
                           if dtopnumber > 0 and dtopnumber < 8:
                               turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                           else:
                               turtle.goto(-300 + 37.5,turtle.ycor())

                           for x in range(12):
                               if redpieces[0][x] == turtle.xcor() and redpieces[1][x] == turtle.ycor():
                                   if dtopnumber == 0 or dtopnumber == 7:
                                       print("You cannot take this piece")
                                   else:
                                       if dtopnumber < topnumber:
                                           for x in range(12):
                                               if redpieces[0][x] == turtle.xcor() -150 and redpieces[1][x] == turtle.ycor() +150:
                                                   print("You cannot take this piece.") 
                                                   t=0
                                                   break                                                
                                               else:
                                                   t=1
                                           if t ==1:
                                               print("You have taken this piece")
                                               if leftnumber > 0 and leftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)

                                               if topnumber > 0 and topnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())

                                               turtle.penup()                                                
                                               turtle.goto(turtle.xcor(),turtle.ycor())
                                               turtle.pendown()
                                               turtle.pencolor("white")
                                               turtle.dot(52)

                                               if dleftnumber > 0 and dleftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*dleftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)
                                              
                                               if dtopnumber > 0 and dtopnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())
                                               for x in range(12):
                                                   if redpieces[0][x] ==turtle.xcor() and redpieces[1][x] == turtle.ycor():
                                                       redpieces[0][x] = " "
                                                       redpieces[1][x] = " "

                                               turtle.penup()
                                               turtle.goto(turtle.xcor(),turtle.ycor())
                                               turtle.pendown()
                                               turtle.pencolor('white')
                                               turtle.dot(52)

                                               turtle.penup()
                                               turtle.goto(turtle.xcor()-75,turtle.ycor()+75)            
                                               turtle.pencolor("black")
                                               turtle.dot(52)
                                               turtle.penup()    

                                               if leftnumber > 0 and leftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)

                                               if topnumber > 0 and topnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())   

                                               for x in range (12):
                                                   if blackpieces[0][x] == turtle.xcor() and blackpieces[1][x] == turtle.ycor():

                                                       if dleftnumber > 0 and dleftnumber < 8:
                                                           turtle.goto(-300,300-37.5-(75*dleftnumber))
                                                       else:
                                                           turtle.goto(-300,300-37.5)
                                                      
                                                       if dtopnumber > 0 and dtopnumber < 8:
                                                           turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                                       else:
                                                           turtle.goto(-300 + 37.5,turtle.ycor())       

                                                       blackpieces[0][x] = turtle.xcor() - 75
                                                       blackpieces[1][x] = turtle.ycor() + 75                                                                                                                                                                                    
                                               q=1
                                               y=1
                                               t=0

                                               break
                                       else:
                                           for x in range(12):
                                               if redpieces[0][x] == turtle.xcor() +150 and redpieces[1][x] == turtle.ycor() +150:
                                                   print("You cannot take this piece.")
                                                   t=0
                                                   break
                                               else:
                                                   t=1
                                           if t == 1:
                                               print("You have taken this piece")
                                               if leftnumber > 0 and leftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)

                                               if topnumber > 0 and topnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())  
                                               turtle.penup()                                                
                                               turtle.goto(turtle.xcor(),turtle.ycor())
                                               turtle.pendown()
                                               turtle.pencolor("white")
                                               turtle.dot(52)

                                               if dleftnumber > 0 and dleftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*dleftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)
                                              
                                               if dtopnumber > 0 and dtopnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())
                                               for x in range(12):
                                                   if redpieces[0][x] ==turtle.xcor() and redpieces[1][x] == turtle.ycor():
                                                       redpieces[0][x] = " "
                                                       redpieces[1][x] = " "

                                               turtle.penup()
                                               turtle.goto(turtle.xcor(),turtle.ycor())
                                               turtle.pendown()
                                               turtle.pencolor('white')
                                               turtle.dot(52)

                                               turtle.penup()
                                               turtle.goto(turtle.xcor()+75,turtle.ycor()+75)            
                                               turtle.pencolor("black")
                                               turtle.dot(52)
                                               turtle.penup()    

                                               if leftnumber > 0 and leftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)

                                               if topnumber > 0 and topnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())   

                                               for x in range (12):
                                                   if blackpieces[0][x] == turtle.xcor() and blackpieces[1][x] == turtle.ycor():

                                                       if dleftnumber > 0 and dleftnumber < 8:
                                                           turtle.goto(-300,300-37.5-(75*dleftnumber))
                                                       else:
                                                           turtle.goto(-300,300-37.5)
                                                      
                                                       if dtopnumber > 0 and dtopnumber < 8:
                                                           turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                                       else:
                                                           turtle.goto(-300 + 37.5,turtle.ycor())       

                                                       blackpieces[0][x] = turtle.xcor() + 75
                                                       blackpieces[1][x] = turtle.ycor() + 75                                                                                                                                                                                    
                                               q=1
                                               y=1
                                               t=0

                                               break

                           if q == 0:
                               turtle.penup()
                               turtle.pendown()
                               turtle.pencolor('black')
                               turtle.dot(52)
                               turtle.penup()

                               blackpieces[0][v] = turtle.xcor()
                               blackpieces[1][v] = turtle.ycor()

                               if leftnumber > 0 and leftnumber < 8:
                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                               else:
                                   turtle.goto(-300,300-37.5)

                               if topnumber > 0 and topnumber < 8:
                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                               else:
                                   turtle.goto(-300 + 37.5,turtle.ycor())

                               y = 1
                               turtle.penup()
                               turtle.pendown()
                               turtle.pencolor('white')
                               turtle.dot(52)
                               turtle.penup()

                               for x in range(12):
                                       if blackpieces[0][x] == turtle.xcor() and blackpieces[1][x] == turtle.ycor():
                                           if dleftnumber > 0 and dleftnumber < 8:
                                               turtle.goto(-300,300-37.5-(75*dleftnumber))
                                           else:
                                               turtle.goto(-300,300-37.5)
                                          
                                           if dtopnumber > 0 and dtopnumber < 8:
                                               turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                           else:
                                               turtle.goto(-300 + 37.5,turtle.ycor())

                                           blackpieces[0][x] = turtle.xcor()
                                           blackpieces[1][x] = turtle.ycor()


                       else:         
                            print ("Invalid top number. Please try again")

       u+=1                   
       w+=1
       q=0
       t=0
   else: #########################################################################################
       print("\n**********Red Pieces Player's Turn**********\n")
       print("**********Choosing Piece to Move**********")
       y=0
       v=0
       z=0
       while y == 0:
           turtle.penup()
           turtle.goto(-300,300)
           leftnumber = int(input("\nPlease choose a left number:    "))
           topnumber= int(input("Please choose a top number:    "))

           if leftnumber < 0 or leftnumber > 8:
               print("\nleft number out of range. please try again.\n")
           else:
               if topnumber < 0 or topnumber > 8:
                   print("\ntop number is out of range. please try again.\n")
               else:
                   if leftnumber > 0 and leftnumber < 8:
                       turtle.goto(-300,300-37.5-(75*leftnumber))
                   else:
                       turtle.goto(-300,300-37.5)

                   if topnumber > 0 and topnumber < 8:
                       turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                   else:
                       turtle.goto(-300 + 37.5,turtle.ycor())
                      
                   for x in range (12):
                       if redpieces[0][x] == turtle.xcor() and redpieces[1][x] == turtle.ycor():
                           print("\nValid\n")
                           y=1
                           v=x
                       elif x == 11 and y!=1:
                           print("\nInvalid. Please Try Again\n")

                   if topnumber == 0:
                       for x in range(12):
                           if redpieces[0][x] == turtle.xcor()+75 and redpieces[1][x] == turtle.ycor()-75:
                               print("However, this piece is unable to move. Please try again.")
                               y=0

                   elif topnumber == 7:
                       for x in range(12):
                           if redpieces[0][x] == turtle.xcor()-75 and redpieces[1][x] == turtle.ycor()-75:
                               print("However, this piece is unable to move. Please try again.")
                               y=0
                   else:
                       for x in range(12):
                           if redpieces[0][x] == turtle.xcor()-75 and redpieces[1][x] == turtle.ycor()-75:
                               for x in range(12):
                                   if redpieces[0][x] == turtle.xcor()+75 and redpieces[1][x] == turtle.ycor()-75:
                                       print("However, this piece is unable to move. Please try again.")
                                       y=0



       print("**********Choosing Destination**********")

       turtle.penup()

       y = 0

       while y == 0:

           dleftnumber = int(input("\nPlease choose a left number:    "))
           dtopnumber= int(input("Please choose a top number:    "))


           if dleftnumber < 0 or dleftnumber > 8:
               print("\nleft number out of range. please try again.\n")
           else:
               if dtopnumber < 0 or dtopnumber > 8:
                   print("\ntop number is out of range. please try again.\n")
               else:
                   if dleftnumber != leftnumber + 1:
                       print ("Invalid left number. Please try again")
                   else:
                       if dtopnumber == topnumber-1 or dtopnumber == topnumber +1:

                           if dleftnumber > 0 and dleftnumber < 8:
                               turtle.goto(-300,300-37.5-(75*dleftnumber))
                           else:
                               turtle.goto(-300,300-37.5)
                          
                           if dtopnumber > 0 and dtopnumber < 8:
                               turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                           else:
                               turtle.goto(-300 + 37.5,turtle.ycor())

                           for x in range(12):
                               if blackpieces[0][x] == turtle.xcor() and blackpieces[1][x] == turtle.ycor():
                                   if dtopnumber == 0 or dtopnumber == 7:
                                       print("You cannot take this piece")
                                   else:
                                       if dtopnumber < topnumber:
                                           for x in range(12):
                                               if blackpieces[0][x] == turtle.xcor() -150 and blackpieces[1][x] == turtle.ycor() -150:
                                                   print("You cannot take this piece.")
                                                   t=0
                                                   break
                                               else:
                                                   t=1
                                           if t ==1:
                                               print("You have taken this piece")
                                               if leftnumber > 0 and leftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)

                                               if topnumber > 0 and topnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())

                                               turtle.penup()                                                
                                               turtle.goto(turtle.xcor(),turtle.ycor())
                                               turtle.pendown()
                                               turtle.pencolor("white")
                                               turtle.dot(52)

                                               if dleftnumber > 0 and dleftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*dleftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)
                                              
                                               if dtopnumber > 0 and dtopnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())
                                               for x in range(12):
                                                   if blackpieces[0][x] ==turtle.xcor() and blackpieces[1][x] == turtle.ycor():
                                                       blackpieces[0][x] = " "
                                                       blackpieces[1][x] = " "

                                               turtle.penup()
                                               turtle.goto(turtle.xcor(),turtle.ycor())
                                               turtle.pendown()
                                               turtle.pencolor('white')
                                               turtle.dot(52)

                                               turtle.penup()
                                               turtle.goto(turtle.xcor()-75,turtle.ycor()-75)            
                                               turtle.pencolor("red")
                                               turtle.dot(52)
                                               turtle.penup()    

                                               if leftnumber > 0 and leftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)

                                               if topnumber > 0 and topnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())   

                                               for x in range (12):
                                                   if redpieces[0][x] == turtle.xcor() and redpieces[1][x] == turtle.ycor():
                                                       if dleftnumber > 0 and dleftnumber < 8:
                                                           turtle.goto(-300,300-37.5-(75*dleftnumber))
                                                       else:
                                                           turtle.goto(-300,300-37.5)
                                                      
                                                       if dtopnumber > 0 and dtopnumber < 8:
                                                           turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                                       else:
                                                           turtle.goto(-300 + 37.5,turtle.ycor())       

                                                       redpieces[0][x] = turtle.xcor() - 75
                                                       redpieces[1][x] = turtle.ycor() - 75                                                                                                                                                                                    
                                               q=1
                                               y=1
                                               t=0

                                               break
                                       else:
                                           for x in range(12):
                                               if blackpieces[0][x] == turtle.xcor() +150 and blackpieces[1][x] == turtle.ycor() -150:
                                                   print("You cannot take this piece.")
                                                   t=0
                                                   break
                                               else:
                                                   t=1
                                           if t==1:
                                               print("You have taken this piece")
                                               if leftnumber > 0 and leftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)

                                               if topnumber > 0 and topnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())

                                               turtle.penup()                                                
                                               turtle.goto(turtle.xcor(),turtle.ycor())
                                               turtle.pendown()
                                               turtle.pencolor("white")
                                               turtle.dot(52)

                                               if dleftnumber > 0 and dleftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*dleftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)
                                              
                                               if dtopnumber > 0 and dtopnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())
                                               for x in range(12):
                                                   if blackpieces[0][x] ==turtle.xcor() and blackpieces[1][x] == turtle.ycor():
                                                       blackpieces[0][x] = " "
                                                       blackpieces[1][x] = " "

                                               turtle.penup()
                                               turtle.goto(turtle.xcor(),turtle.ycor())
                                               turtle.pendown()
                                               turtle.pencolor('white')
                                               turtle.dot(52)

                                               turtle.penup()
                                               turtle.goto(turtle.xcor()+75,turtle.ycor()-75)            
                                               turtle.pencolor("red")
                                               turtle.dot(52)
                                               turtle.penup()    

                                               if leftnumber > 0 and leftnumber < 8:
                                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                                               else:
                                                   turtle.goto(-300,300-37.5)

                                               if topnumber > 0 and topnumber < 8:
                                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                                               else:
                                                   turtle.goto(-300 + 37.5,turtle.ycor())   

                                               for x in range (12):
                                                   if redpieces[0][x] == turtle.xcor() and redpieces[1][x] == turtle.ycor():
                                                       if dleftnumber > 0 and dleftnumber < 8:
                                                           turtle.goto(-300,300-37.5-(75*dleftnumber))
                                                       else:
                                                           turtle.goto(-300,300-37.5)
                                                      
                                                       if dtopnumber > 0 and dtopnumber < 8:
                                                           turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                                       else:
                                                           turtle.goto(-300 + 37.5,turtle.ycor())       

                                                       redpieces[0][x] = turtle.xcor() + 75
                                                       redpieces[1][x] = turtle.ycor() - 75                                                                                                                                                                                    
                                               q=1
                                               y=1
                                               t=0

                                               break
                           if q == 0:
                               turtle.penup()
                               turtle.pendown()
                               turtle.pencolor('red')
                               turtle.dot(51)
                               turtle.penup()

                               redpieces[0][v] = turtle.xcor()
                               redpieces[1][v] = turtle.ycor()

                               if leftnumber > 0 and leftnumber < 8:
                                   turtle.goto(-300,300-37.5-(75*leftnumber))
                               else:
                                   turtle.goto(-300,300-37.5)

                               if topnumber > 0 and topnumber < 8:
                                   turtle.goto(-300 + 37.5 + (75*topnumber),turtle.ycor())
                               else:
                                   turtle.goto(-300 + 37.5,turtle.ycor())

                               y = 1
                               turtle.penup()
                               turtle.pendown()
                               turtle.pencolor('white')
                               turtle.dot(52)
                               turtle.penup()

                               for x in range(12):
                                       if redpieces[0][x] == turtle.xcor() and redpieces[1][x] == turtle.ycor():
                                           if dleftnumber > 0 and dleftnumber < 8:
                                               turtle.goto(-300,300-37.5-(75*dleftnumber))
                                           else:
                                               turtle.goto(-300,300-37.5)
                                          
                                           if dtopnumber > 0 and dtopnumber < 8:
                                               turtle.goto(-300 + 37.5 + (75*dtopnumber),turtle.ycor())
                                           else:
                                               turtle.goto(-300 + 37.5,turtle.ycor())

                                           redpieces[0][x] = turtle.xcor()
                                           redpieces[1][x] = turtle.ycor()
                       else:
      
                           print ("Invalid top number. Please try again")

       u+=1                   
       w-=1
       q=0
       t=0
turtle.mainloop()

