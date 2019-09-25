try:
    #importing modules

    from tkinter import *
    import random
    import time


    root=Tk()
    root.title("Bounce!") #adding the title
    root.geometry("510x500")
    #fixing the window to a particular size
    root.resizable(0,0)



    #fixing the canvas above all other things
    #root.wm_attributes("-topmost",1)

    #setting up the canvas
    canvas=Canvas(root,width=510,height=500,bg="black",bd=0,highlightthickness = 0)
    #bd- border

    canvas.pack(side=LEFT)
    root.update()


    #adding the ball class

    class Ball():
        
        def __init__(self,canvas,paddle,color):
            
            self.canvas=canvas

            self.paddle=paddle

            self.pos=0

            self.count=0
            #count variable stores the score
            
            self.score=canvas.create_text(245,25, text = "SCORE : 0",fill="white",font=("ArcadeClassic",24))
            #initial score is 0
            
            #creating a oval shape with following parameters as learned before these are the coordinates of rectangle in which the oval is inscribed
            self.id=canvas.create_oval(10,10,25,25, fill=color)
            
            self.canvas.move(self.id,245,150)
            #245,100 is appprox. centered

            start=[-3,-2,-1,1,2,3] #creating an array to choose the starting point

            random.shuffle(start)
            #shuffling the array
            
            #creating a starting velocity
            self.x=start[0]
            self.y=-3
            
            self.canvas_height=self.canvas.winfo_height()
            #this function gets the height of the canvas(obviously it is 500)
        
            self.canvas_width=self.canvas.winfo_width()
            #this function gets the width of the canvas(obviously it is 500)

            self.hit_bottom = False
            #adding a variable specifying when the ball hit bottom

        def hit_paddle(self,pos):

            
            paddle_pos=self.canvas.coords(self.paddle.id)
            #getting the coordinates of the paddle
            #returns the array [x1,y1,x2,y2]
            
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            #if x2(ball) >= x1(paddle) and x1(ball) <= x2(paddle)
            #if the ball collide with the paddle from the left and the right side
                
                if pos[3] >= paddle_pos[1] and pos[3 ]<= paddle_pos[3]:
                #if y2(ball) >= y1(paddle) and y2(ball) <= y2(paddle)
                #if the ball collide with the paddle from top to bottom
                    
        
                    

                    
                    return True
                    
                
                return False






        def hit_brick(self,pos):
            global k
            obj=canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])
            t=()
            for i in obj:
                if i!=self.id and i!=self.paddle.id and i!=self.score:
                    t=t+(i,)

      

            for k in t:
                brick_pos=self.canvas.coords(k)
                if pos[2]>=brick_pos[0] and pos[0]<=brick_pos[2]:
                    if pos[3]>=brick_pos[1] and pos[3]<= brick_pos[3]:
                        return True
                    
                    return False
                    
                    

            '''if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            #if x2(ball) >= x1(paddle) and x1(ball) <= x2(paddle)
            #if the ball collide with the paddle from the left and the right side
                
                if pos[3] >= paddle_pos[1] and pos[3 ]<= paddle_pos[3]:
                #if y2(ball) >= y1(paddle) and y2(ball) <= y2(paddle)
                #if the ball collide with the paddle from top to bottom
                    
                    self.count+=1
                    #updating the score after the ball touches the paddle
                    
                    self.canvas.delete(self.score)
                    #deleting the previous text box
                    self.score=canvas.create_text(245,50, text = "SCORE : " + str(self.count),fill="white",font=("ArcadeClassic",24))
                    #adding a new text box with updated score
                    
                    return True
                    
                
                return False'''
            
            
            
        #adding actions on the ball    
        def draw(self):

            global pos

            #moving the ball
            self.canvas.move(self.id,self.x,self.y)
            
            pos= self.canvas.coords(self.id)
            #this function returns the array [x1,y1,x2,y2]

            
            

            #CREATING CONSTRAINTS SO THAT BALL STAY IN THE CANVAS
            
            
            if pos[1] <= 0:
            #if y1 <=0
            #it means that when the ball toches the topmost point of the canvas reverse its direcn
            
                self.y=3
                #reversing the direcn of the ball
                
            if pos[0] <= 0:
            #if x1 <=0
            #it means that when the ball toches the leftmost point of the canvas reverse its direcn
            
                self.x=3
                #reversing the direcn of the ball
                
            if pos[3] >= self.canvas_height:
            #if y2>=0
            #it means that when the ball touches the bottommost point of the canvas, the ball stops
            
                self.hit_bottom = True
                #when the ball hit bottom the hit_bottom variable becomes true
                #while loop stops

                canvas.create_text(250,250, text = "GAME OVER",fill="white",font=("ArcadeClassic",60))


                    

            if pos[2] >= self.canvas_width:
            #if x2>=0
            #it means that when the ball touches the rightmost point of the canvas, it reverses its direcn
            
                self.x=-3
                #reversing the direcn of the ball

            if self.hit_paddle(pos)==True:
            #if the ball hits the paddle, then its direncn will reverse
            #pos-position of the ball
                
                self.y=-3
                #reversing the direcn of the ball

            if self.hit_brick(pos)==True:
                canvas.delete(k)
                self.y=self.y*(-1)
                self.count+=1
                self.canvas.delete(self.score)
                #updating the score after the ball touches the bricks
                self.score=canvas.create_text(245,25, text = "SCORE : " + str(self.count),fill="white",font=("ArcadeClassic",24))
                
                    #deleting the previous text box
        
                    #adding a new text box with updated score

    #creating the class paddle

    class Paddle():
        
        def __init__ (self,canvas,color):

            self.canvas=canvas

            #creating a rectangle with following parameters as the coordinates of opposide points
            self.id=canvas.create_rectangle(0,0,100,10,fill=color)
            
            self.canvas.move(self.id,200,420)
            #moving it to the following location

            self.x=0
            #specifying that the paddle is stationary

            #finding width of the canvas
            self.canvas_width=self.canvas.winfo_width()

            #binding left key to turn left
            self.canvas.bind_all('<Left>',self.turn_left)

            #binding left key to turn left
            self.canvas.bind_all('<Right>',self.turn_right)

        def draw(self):
            #moving the paddle
            self.canvas.move(self.id,self.x,0)
            
            pos= self.canvas.coords(self.id)
            #this function returns the array [x1,y1,x2,y2]
            

            #CREATING CONSTRAINTS SO THAT PADDLE STAY IN THE CANVAS
            
            if pos[0] <= 0:
            #if x1 <=0
            #it means that when the paddle toches the leftmost point of the canvas, it reverses its direction
            
                self.x=2
                #reversing the direcn of the paddle
                

            if pos[2] >= self.canvas_width:
            #if x2>=0
            #it means that when the ball touches the rightmost point of the canvas, it reverses its direction
            
                self.x=-2
                #reversing the direcn of the paddle        
        
        
        #function to turn the paddle left
        def turn_left(self,evt):
            self.x=-2.5
        

        
        #function to turn the paddle right
        def turn_right(self,evt):
            self.x=2.5
        

    #difing a class for bricks
    class Brick():

        def __init__(self,canvas,color,x1_,y1_,x2_,y2_):

            self.canvas=canvas


            self.id=canvas.create_rectangle(x1_,y1_,x2_,y2_, fill=color)
            #creating a brick








            
    #function to display the bricks on the canvas
    def display_brick():
            

        color_list=["yellow","red","cyan"]
        x1=10
        x2=50
        y1=60
        y2=75
        for i in range (3):
            for j in range(10):
            
                brick=Brick(canvas,color_list[i],x1,y1,x2,y2)
                x1+=50
                x2+=50
            x1=10
            x2=50
            y1+=25
            y2+=25      






    #this function starts the countdown and then the game
    def startgame():

       

        ###########test changes################
        #if something goes wrong, try removing it
        display_brick()
        

        
        
        #making a list of colors so that the colors of ball and the paddle can be randomised
        color=["red","blue","orange","pink","magenta","yellow","cyan","gold","lime","coral"]

        #shuffling the list of colors
        random.shuffle(color)

        #calling the paddle
        paddle=Paddle(canvas,color[0])        
                
        #calling the class
        ball=Ball(canvas,paddle,color[1])
       
        
        #creating a loop that count downs from 3 to 1
        for i in range(3,0,-1):

            #creating numbers
            id_=canvas.create_text(250,250, text = str(i),fill="white",font=("ArcadeClassic",60))
            canvas.update()
            #adding 1 sec delay
            time.sleep(1)
            #deleting the numbers
            canvas.delete(id_)
            canvas.update()

        #creating a main loop which always update the canvas so that the ball always appears to be moving    
        while ball.hit_bottom == False:                                 
        #condition that the loop runs until the ball hits the bottom   
                    
            #calling the draw functions
            ball.draw()

            ball.hit_brick(pos)


            paddle.draw()
                            
                        
            root.update_idletasks()
            #updating the background tasks
                        
            root.update()
            #updating the foreground tasks

            object_tuple=canvas.find_all()
            #this func returns the tuple of all the objects present in the canvas

            if len(object_tuple)<=3:
                break
       
            #applying the condition that when the no. of objects in the canvas
            #is less than 3(ball, paddle, and score) the while mainloop will break
            #i.e. all the bricks disappeared


            

            
            time.sleep(0.01)
            #frame time

        

        restart_button()

            

    #this fuction stops the start button from blinking
    #it changes the value of global var. s to False
    #it also clears the canvas and calls the startgame() function
    def stopflashing_start(evt):
        
        global s,r
        
        s=False
        r=False

        canvas.delete("all")
        #clearing the canvas
       
        startgame()



    #creating a function to create the help menu
    def help_menu(evt):

        
        root.geometry("520x500")
        
        global img
        global s

        s=False
        canvas.delete("all")




        canvas.create_text(250,20,text="HELP MENU",fill="white",font=("ArcadeClassic",30))

        screenshot= PhotoImage(file='ss.gif')
        keys_image=PhotoImage(file='keys.gif')

        canvas.create_image(250,50,image=screenshot, anchor=N)

        canvas.create_image(100,250,image=keys_image, anchor=N)

        #canvas.create_text(250,400,text="INSTRUCTIONS",fill="white",font=("ArcadeClassic",20))

        canvas.create_text(250,400,text="Destroy  as  many  bricks  as  you  can  with  the",fill="white",font=("ArcadeClassic",14))

        canvas.create_text(250,440,text="  ball  using  the  paddle",fill="white",font=("ArcadeClassic",14))

        #canvas.create_text(250,590,text="Use  SPACE  BAR  to  start / restart  the  game",fill="white",font=("ArcadeClassic",14))

        #canvas.create_text(250,670,text="Use  the  arrow  keys  to  move  the  paddle",fill="white",font=("ArcadeClassic",14))

        #canvas.create_text(250,750,text="The  score  counter  on  top  shows  how  many  ",fill="white",font=("ArcadeClassic",14))

        #canvas.create_text(250,780,text="bricks  you  have  destroyed",fill="white",font=("ArcadeClassic",14))
        

        #canvas.create_text(250,860,text="Don't  let  the  ball  fall  on  the   ground   or   else   its ",fill="white",font=("ArcadeClassic",14))

        #canvas.create_text(250,890,text="GAME  OVER  !",fill="white",font=("ArcadeClassic",16))

        s=True
        while s==True: 
            start=canvas.create_text(250,1020, text = " START ",fill="white",font=("ArcadeClassic",26))
            canvas.update()
            time.sleep(0.5)
            canvas.delete(start)
            canvas.update()
            time.sleep(0.5)

            canvas.bind_all('<Escape>',close)

            #this statement binds the space bar to stop_flashing function
            canvas.bind_all('<space>',stopflashing_start)

        

        canvas.create_text(450,1290,text="CREATED  BY  -",fill="white",font=("ArcadeClassic",14))

        canvas.create_text(480,1320,text="ABHINAV",fill="white",font=("ArcadeClassic",12))

    def close(evt):
        root.destroy()
        
        
    #this function displays the initial screen
    #it contains the start button which is constantly blinking
    def initialscreen():

        global s

        canvas.create_text(250,50,text=" BOUNCE ",fill="white",font=("ArcadeClassic",52,"bold italic"))
        #these lines create the name of the game 

        #this is the code block which is used to make anything falsh
        #time.sleep is used to add delay bw flashes
        s=True
        while s==True: 
            start=canvas.create_text(250,250, text = " START ",fill="white",font=("ArcadeClassic",30))
            help_bttn=canvas.create_text(60,480,text = "HELP [ H ]",fill="white",font=("ArcadeClassic",22))
            quit_bttn=canvas.create_text(440,480,text = " QUIT [ESC]",fill="white",font=("ArcadeClassic",21))
            canvas.update()
            time.sleep(0.5)
            canvas.delete(start)
            canvas.update()
            time.sleep(0.5)

            canvas.bind_all('<h>',help_menu)
            canvas.bind_all('<Escape>',close)

            #this statement binds the space bar to stop_flashing function
            canvas.bind_all('<space>',stopflashing_start)




    def restart_button():

        global r
        r=True
        while r==True:
    #################################CHANGE THIS LINE
            

        
            restart=canvas.create_text(250,450, text = " RESTART ",fill="white",font=("ArcadeClassic",26))
            canvas.update()
            time.sleep(0.5)
            canvas.delete(restart)
            canvas.update()
            time.sleep(0.5)
            canvas.bind_all('<space>',stopflashing_start)

    #calling the initial screen function
    initialscreen()

    mainloop()

    ##########################################################################
    '''restart=canvas.create_text(250,450, text = " RESTART ",fill="white",font=("ArcadeClassic",26))
        canvas.update()
        time.sleep(0.5)
        canvas.delete(restart)
        canvas.update()
        time.sleep(0.5)
        canvas.bind_all('<space>',startgame)'''

        

        


except:
    pass
    
