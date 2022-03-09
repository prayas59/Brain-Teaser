import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
num = random.randint(1,100)
num2 = random.randrange(2,100,2)
num2=int(num2)
annum=num2/2
annum=int(annum)
num2=str(num2)
annum=str(annum)
point=0
count=0
no=8
def save():
    name1 = username.get()
    name2 = username0.get()
    file = open('Your Data.txt','a')
    file.write('\nName: '+name1+'\nBranch: '+name2+'\n')
    file.close()

    
def onclick1():
    global num
    def onclick4(): 
        import random
        screen = Tk()
        screen.title('Guess A Number')
        screen.geometry('1200x1400')
        screen.configure(bg='#ab7976')
       
        Label(screen,text= """ 8 Chance Left""",bg='#ab7976',fg='#FFFDD0',font=('Times new roman',18)).place(x=10,y=10)
        tk.Button(screen,text='Exit This Window',bg='white',fg='black',font=('Times new roman',18),command = screen.withdraw).place(x=10,y=100)
        Label(screen,text= """Try Your Number from 1 To 100""",bg='#ab7976',fg='#FFFDD0',font=('Times new roman',24,'bold')).pack(pady=10)
        n =Entry(screen,bg='white',fg='blue',font=('Times new roman',18))
        n.pack()
        count=0
        
       
  
        def onclick1():
            global no
            global count
            
            global num
            if n.get()=="":
                print("no input")
                Label(screen,text= """Please Enter A Number""",bg='#ab7976',fg='white',font=('Times new roman',20)).pack(pady=10)
                
            else:
                
                if (int (n.get()) == num) :
                 
                    Label(screen,text= """Yipee You Win""",bg='#ab7976',fg='white',font=('Times new roman',20)).pack(pady=10)
                else:
                    
                    if(int (n.get())>num):
                       
                        if(int(n.get())-num >10):
                            Label(screen,text= """Oops You Are Wrong! You have guessed a Higher Number &  Far! Try Again""",bg='#ab7976',fg='#402191',font=('Times new roman',18,'bold')).pack(pady=10)
                            no=no-1
                            count=count+1
                        else:
                            Label(screen,text= """Oops You Are Wrong! You have guessed a Higher Number & near by! Try Again""",bg='#ab7976',fg='#402191',font=('Times new roman',18,'bold')).pack(pady=10)
                            no=no-1
                            count=count+1
                    else:
                        
                        if(num - int (n.get())>10):
                            Label(screen,text= """Oops You Are Wrong! You have guessed a Lower Number & Far! Try Again""",bg='#ab7976',fg='#402191',font=('Times new roman',18,'bold')).pack(pady=10)
                            no=no-1
                            count=count+1
                        else:
                            Label(screen,text= """Oops You Are Wrong! You have guessed a Lower Number & near by! Try Again""",bg='#ab7976',fg='#402191',font=('Times new roman',18,'bold')).pack(pady=10)
                            no=no-1
                            count=count+1
        def onclick48():
            global count
            global no
            Label(screen,text= str(no)+""" Chance Left""",bg='#ab7976',fg='#FFFDD0',font=('Times new roman',20)).place(x=10,y=10)
            
            if(count==8):
                b2.configure(state=DISABLED)
                Label(screen,text= """No more Chances""",bg='#ab7976',fg='#FFFDD0',font=('Times new roman',20)).pack(pady=10)
                
            
            
            
        def onclick54():
               
            global num
            tk1.Label(screen,text= num,bg='#07f5c9',fg='Black',font=('Times new roman',20)).pack(pady=10)
        
        
        b2=tk.Button(screen,text='Submit',bg='#FFFDD0',fg='black',font=('Times new roman',18),command = lambda:[ onclick1(), onclick48()])
        b2.pack(pady = 10)
        buttonDraw=Button(screen,text='Show Number',bg='#FFFDD0',fg='black',font=('Times new roman',18),command=onclick54).pack(pady = 10)

        screen.mainloop()
    def onclick5():
        global num2
        global annum
        import tkinter as tk1
        from tkinter import messagebox
        screen = tk1.Tk()
        screen.title('Magic Question')
        screen.geometry('1200x1400')
        screen.configure(bg='teal')
        def onclick6():
            def onclick8():
                def onclick10():
                    def onclick12():
                        def onclick14():
                            tk1.Label(screen,text= """Your Answer is """+annum,bg='#FFFDD0',fg='black',font=('Times new roman',20)).pack(pady=10)
                        
                        tk1.Label(screen,text= """Subtract Number You Thought At Starting""",bg='#07f5c9',fg='Black',font=('Times new roman',20)).pack(pady=10)
                        tk.Button(screen,text='DONE',bg='#f58e07',fg='white',font=('Times new roman',18),command = onclick14).pack(pady = 1)
                        tk.Button(screen,text='NO , Exit',bg='#f58e07',fg='white',font=('Times new roman',18),command=screen.withdraw).pack(pady = 1)
                    
                    tk1.Label(screen,text= """Divide By 2""",bg='#07f5c9',fg='Black',font=('Times new roman',20)).pack(pady=10)
                    tk.Button(screen,text='DONE',bg='#f58e07',fg='white',font=('Times new roman',18),command = onclick12).pack(pady = 1)
                    tk.Button(screen,text='NO , Exit',bg='#f58e07',fg='white',font=('Times new roman',18),command = screen.withdraw).pack(pady = 1)
            
                tk1.Label(screen,text= """Add """+num2,bg='#07f5c9',fg='Black',font=('Times new roman',20)).pack(pady=10)
                tk.Button(screen,text='DONE',bg='#f58e07',fg='white',font=('Times new roman',18),command = onclick10).pack(pady = 1)
                tk.Button(screen,text='NO , Exit',bg='#f58e07',fg='white',font=('Times new roman',18),command = screen.withdraw).pack(pady = 1)
           
            tk1.Label(screen,text= """Double Your Number""",bg='#07f5c9',fg='Black',font=('Times new roman',20)).pack(pady=10)
            tk.Button(screen,text='DONE',bg='#f58e07',fg='white',font=('Times new roman',18),command = onclick8).pack(pady = 1)
            tk.Button(screen,text='NO , Exit',bg='#f58e07',fg='white',font=('Times new roman',18),command = screen.withdraw).pack(pady = 1)

    
        tk1.Label(screen,text= """Think A Number""",bg='#07f5c9',fg='black',font=('Times new roman',20)).pack(pady=10)
        tk.Button(screen,text='DONE',bg='#f58e07',fg='white',font=('Times new roman',18),command = onclick6).pack(pady = 1)
        tk.Button(screen,text='NO , Exit ',bg='#f58e07',fg='white',font=('Times new roman',18),command = screen.withdraw).pack(pady = 1)
        screen.mainloop()
        
    import tkinter as tk1
    from tkinter import messagebox
    screen = tk1.Tk()
    screen.title('Play')
    screen.geometry('1200x1400')
    screen.configure(bg='teal')
    tk1.Label(screen,text= 'Wow,Lets Play!',bg='teal',fg='#FFFDD0',font=('Times new roman',30)).pack(pady=10)
    tk1.Button(screen,text='Guess A Number',bg='#FF7F50',fg='black',font=('Times new roman',20),command = onclick4).pack(pady = 40)
    tk1.Button(screen,text='Magic Question',bg='#FF7F50',fg='black',font=('Times new roman',20),command = onclick5).pack(pady = 40)
    tk1.Button(screen,text='Exit This Window',bg='white',fg='black',font=('Times new roman',18),command = screen.withdraw).place(x=10,y=10)
    screen.mainloop()
def onclick3():
    Queslist=["An IF-ELSE statement is also called ___.","What is the name of << bitwise operator in Java?","If relational operators are present in an expression, what type of other operators may be used?","Byte code is the result of?","What is the output of Compilation of Java Program?","What is a Compiler?","What is an Interpreter?","Computer Viruses and Trojans are often transmitted along with which files?"," Java language was originally developed for operating?","What is the original name of Java Programming language?","Who invented Java language?","Java is a Successor to which programming language?","Who invented C Language.?"," C Language is a successor to which language.?","C is a which level language.?","Low level language is .?","High level language is a .?","C is _______ type of programming language.?"]
    optlist=["1) Branching statement","2) Control statement","3) Block statements","4) All","1) Right Shift Operator","2) Left Shift Operator","3) Left Shift Fill Zero operator","4) Right Shift Fill Zero operator","1) Logical operators","2) Bitwise operators","3) A and B","4) None of the above","1) Compiling a Java file","2) Compiling a Class file","3) Interpreting a Java File","4) Interpreting a Class file","1) .class file","2) .cla file","3) .jc file","4) .javax file","1) A Compiler converts all instructions in one go.","2) A compiler converts source code to low-level code","3) Compilers work fast","4) All the above","1) An interpreter converts instructions line by line","2) An Interpreter converts source code to low-level code","3) Interpreters are slow to execute","4) All the above","1) JPG files","2) TXT files","3) EXE files","4) .ICO files","1) TV","2) TV Set-top box","3) Embedded System equipment","4) All the above","1) J++","2) C++","3) OAK","4) TEAK","1) Dennis Ritchie","2) James Gosling","3) Larry Page","4) Serge Page","1) B","2) C","3) C++","4) D","1) Charles Babbage","2) Grahambel","3) Dennis Ritchie","4) Steve Jobs","1) FORTRAN","2) D Language","3) BASIC","4) B Language","1) Low Level","2) High Level","3) Low + High","4) None","1) Human readable like language.","2) language with big program size.","3) language with small program size.","4) Difficult to understand and readability is questionable.","1) Human readable like language.","2) language with small program size.","3) language with big program size.","4) language which is difficult to understand and not human readable.","1) Object Oriented","2) Procedural","3) Bit level language","4) Functional"]
    Anslist=[4,2,1,1,1,4,4,3,4,3,2,3,3,4,2,4,1,2]
    rano=[]
    listno=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    
    global point
    def save():    
        
        Ans=(randomno*4)+(Anslist[randomno])-1       
        name2 = username7.get()
        if(name2==""):
            print("skipped")
            tk.Label(screen,text= "Please Type Something if You Don't know Type 0",bg='#f7af05',fg='black',font=('Times new roman',18)).pack(pady=5)
        else:          
            b1.configure(state=DISABLED)
            name2 = int(username7.get())
            if(name2==Anslist[randomno]):
                tk.Label(screen,text= 'Correct Ans ',bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                global point
                point+=1
            else:
                tk.Label(screen,text= 'You are Wrong! Correct Ans is '+optlist[Ans],bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
            name2=str(name2)
            file = open('Your Data.txt','a')
            file.write('Ans1: '+name2+' \n')
            file.close()
    
    import tkinter as tk
    from tkinter import messagebox
    def onclick5():
        def save():
            Ans=(randomno*4)+(Anslist[randomno])-1
            name7 = username6.get()
            if(name7==""):
                print("skipped")
                tk.Label(screen,text= "Please Type Something if You Don't know Type 0",bg='#f7af05',fg='black',font=('Times new roman',18)).pack(pady=5)
            else:
                
                b2.configure(state=DISABLED)
                name7 = int(username6.get())
                if(name7==Anslist[randomno]):
                    tk.Label(screen,text= 'Correct Ans ',bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                    global point
                    point+=1
                else:
                    tk.Label(screen,text= 'You are Wrong! Correct Ans is '+optlist[Ans],bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                name7=str(name7)
                file = open('Your Data.txt','a')
                file.write('Ans6: '+name7+'\n')
                file.close()
                tk.Button(screen,text='Veiw Result',bg='#f7af05',fg='white',font=('Times new roman',20),command = lambda:[ onclick22(), screen.withdraw()]).pack(pady = 10)
        import tkinter as tk
        from tkinter import messagebox
        screen = tk.Tk()
        screen.title('Quiz')
        screen.geometry('1200x1400')
        screen.configure(bg='#f7af05')
        def onclick22():
            import tkinter as tk
            from tkinter import messagebox
            screen = tk.Tk()
            screen.title('Quiz')
            screen.geometry('1200x1400')
            screen.configure(bg='black')
            global point
            def save():
                global point
                point=str(point)
                file = open('Your Data.txt','a')
                file.write('You Scored  '+point+'/6 \n')
                file.close()
            point=str(point)
            tk.Button(screen,text='Exit This Window',bg='white',fg='black',font=('Times new roman',18),command = screen.withdraw).place(x=10,y=10)
            tk.Label(screen,text="You Scored "+point+" /6",bg='black',fg='Yellow',font=('Times new roman',24)).pack(pady=30)
            tk.Button(screen,text='Save Result',bg='black',fg='white',font=('Times new roman',20),command = save).pack(pady=20)
            tk.Label(screen,text="""Thank You!
        Creator: Prayas Godara
            Batch : Information Technology 2020
                     """,bg='black',fg='pink',font=('Times new roman',40)).pack(pady=20)
        randomno=random.choice([i for i in listno if i not in rano])
        rano.append(randomno)
        tk.Label(screen,text= 'Your Quiz is here',bg='#f7af05',fg='Black',font=('Times new roman',24)).pack(pady=10)
        tk.Button(screen,text='Exit This Window',bg='white',fg='black',font=('Times new roman',18),command = screen.withdraw).place(x=10,y=10)
        tk.Label(screen,text="Q(6)  "+Queslist[randomno],bg='#f7af05',fg='Black',font=('Times new roman',22)).pack(pady=10)
        tk.Label(screen,text=optlist[randomno*4],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+1],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+2],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+3],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        a1=tk.Label(screen,text= ' Write Your Answer in from of 1 - 4 as Option',bg='#f7af05',fg='Black',font=('Times new roman',20)).pack(pady=10)
        username6 = tk.Entry(screen,bg='#ffe23d',fg='blue',font=('Times new roman',20))
        username6.pack()              
        b2=tk.Button(screen,text='Sumbit',bg='#f7af05',fg='white',font=('Times new roman',20),command = lambda:[save()])
        b2.pack(pady = 10)
     
        
    def onclick4():
        def save():
            Ans=(randomno*4)+(Anslist[randomno])-1
            name6 = username5.get()
            if(name6==""):
                print("skipped")
                tk.Label(screen,text= "Please Type Something if You Don't know Type 0",bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=5)
            else:
                b1.configure(state=DISABLED)
                name6 = int(username5.get())
                if(name6==Anslist[randomno]):
                    tk.Label(screen,text= 'Correct Ans ',bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                    global point
                    point+=1
                else:
                    tk.Label(screen,text= 'You are Wrong! Correct Ans is '+optlist[Ans],bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                name6=str(name6)
                file = open('Your Data.txt','a')
                file.write('Ans5: '+name6+'\n')
                file.close()           
        import tkinter as tk
        from tkinter import messagebox
        screen = tk.Tk()
        screen.title('Quiz')
        screen.geometry('1200x1400')
        screen.configure(bg='#f7af05')
        randomno=random.choice([i for i in listno if i not in rano])
        rano.append(randomno)
        tk.Label(screen,text= 'Your Quiz is here',bg='#f7af05',fg='Black',font=('Times new roman',24)).pack(pady=10)
        tk.Button(screen,text='Exit This Window',bg='white',fg='black',font=('Times new roman',18),command = screen.withdraw).place(x=10,y=10)
        tk.Label(screen,text="Q(5)  "+  Queslist[randomno],bg='#f7af05',fg='Black',font=('Times new roman',24)).pack(pady=10)
        tk.Label(screen,text=optlist[randomno*4],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+1],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+2],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+3],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text= ' Write NO.from 1 to 4 as Option',bg='#f7af05',fg='Black',font=('Times new roman',20)).pack(pady=10)
        username5 = tk.Entry(screen,bg='#ffe23d',fg='blue',font=('Times new roman',20))
        username5.pack()        
        b1=tk.Button(screen,text='save',bg='#f7af05',fg='white',font=('Times new roman',20), command=save)
        b1.pack(pady=50)
        b2=tk.Button(screen,text='Next',bg='#f7af05',fg='white',font=('Times new roman',20),command = lambda:[b2.configure(state=DISABLED), onclick5(), screen.withdraw()])
        b2.pack(pady = 10)
        
    def onclick3():
        
        def save():
            Ans=(randomno*4)+(Anslist[randomno])-1
            name5 = username4.get()
            if(name5==""):
                print("skipped")
                tk.Label(screen,text= "Please Type Something if You Don't know Type 0",bg='#f7af05',fg='black',font=('Times new roman',18)).pack(pady=5)
            else:
                b1.configure(state=DISABLED)
                name5 = int(username4.get())
                if(name5==Anslist[randomno]):
                    tk.Label(screen,text= 'Correct Ans ',bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                    global point
                    point+=1
                else:
                    tk.Label(screen,text= 'You are Wrong! Correct Ans is '+optlist[Ans],bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                name5=str(name5)
                file = open('Your Data.txt','a')
                file.write('Ans4: '+name5+'\n')
                file.close()           
        import tkinter as tk
        from tkinter import messagebox
        screen = tk.Tk()
        screen.title('Quiz')
        screen.geometry('1200x1400')
        screen.configure(bg='#f7af05')
        randomno=random.choice([i for i in listno if i not in rano])
        rano.append(randomno)
        tk.Label(screen,text= 'Your Quiz is here',bg='#f7af05',fg='Black',font=('Times new roman',24)).pack(pady=10)
        tk.Button(screen,text='Exit This Window',bg='white',fg='black',font=('Times new roman',18),command = screen.withdraw).place(x=10,y=10)
        tk.Label(screen,text="Q(4)  "+  Queslist[randomno],bg='#f7af05',fg='Black',font=('Times new roman',22)).pack(pady=10)
        tk.Label(screen,text=optlist[randomno*4],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+1],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+2],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+3],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text= ' Write NO.from 1 to 4 as Option',bg='#f7af05',fg='Black',font=('Times new roman',20)).pack(pady=10)
        username4 = tk.Entry(screen,bg='#ffe23d',fg='blue',font=('Times new roman',20))
        username4.pack()          
        b1=tk.Button(screen,text='save',bg='#f7af05',fg='white',font=('Times new roman',20), command=save)
        b1.pack(pady=50)
        b2=tk.Button(screen,text='Next',bg='#f7af05',fg='white',font=('Times new roman',20),command = lambda:[b2.configure(state=DISABLED), onclick4(), screen.withdraw()])
        b2.pack(pady = 10)
    def onclick2():
        def save():
            Ans=(randomno*4)+(Anslist[randomno])-1
            name4 = username3.get()
            if(name4==""):
                print("skipped")
                tk.Label(screen,text= "Please Type Something if You Don't know Type 0",bg='#f7af05',fg='black',font=('Times new roman',18)).pack(pady=5)
            else:
                b1.configure(state=DISABLED)
                name4 = int(username3.get())
                if(name4==Anslist[randomno]):
                    tk.Label(screen,text= 'Correct Ans ',bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                    global point
                    point+=1
                else:
                    tk.Label(screen,text= 'You are Wrong! Correct Ans is '+optlist[Ans],bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                name4=str(name4)
                file = open('Your Data.txt','a')
                file.write('Ans3: '+name4+'\n')
                file.close()           
        import tkinter as tk
        from tkinter import messagebox
        screen = tk.Tk()
        screen.title('Quiz')
        screen.geometry('1200x1400')
        screen.configure(bg='#f7af05')
        randomno=random.choice([i for i in listno if i not in rano])
        rano.append(randomno)
        tk.Label(screen,text= 'Your Quiz is here',bg='#f7af05',fg='Black',font=('Times new roman',24)).pack(pady=10)
        tk.Button(screen,text='Exit This Window',bg='white',fg='black',font=('Times new roman',18),command = screen.withdraw).place(x=10,y=10)
        tk.Label(screen,text="Q(3)  "+ Queslist[randomno],bg='#f7af05',fg='Black',font=('Times new roman',22)).pack(pady=10)
        tk.Label(screen,text=optlist[randomno*4],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+1],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+2],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+3],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text= ' Write NO.from 1 to 4 as Option',bg='#f7af05',fg='Black',font=('Times new roman',20)).pack(pady=10)
        username3 = tk.Entry(screen,bg='#ffe23d',fg='blue',font=('Times new roman',20))
        username3.pack()      
        b1=tk.Button(screen,text='save',bg='#f7af05',fg='white',font=('Times new roman',20), command=save)
        b1.pack(pady=50)
        b2=tk.Button(screen,text='Next',bg='#f7af05',fg='white',font=('Times new roman',20),command = lambda:[b2.configure(state=DISABLED), onclick3(), screen.withdraw()])
        b2.pack(pady = 10)
        
    def onclick1():       
        def save():
            Ans=(randomno*4)+(Anslist[randomno])-1
            name3 = username2.get()
            if(name3==""):
                print("skipped")
                tk.Label(screen,text= "Please Type Something if You Don't know Type 0",bg='#f7af05',fg='black',font=('Times new roman',18)).pack(pady=5)
            else:
                b1.configure(state=DISABLED)
                name3 = int(username2.get())
                if(name3==Anslist[randomno]):
                    tk.Label(screen,text= 'Correct Ans ',bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                    global point
                    point+=1
                else:
                    tk.Label(screen,text= 'You are Wrong! Correct Ans is '+optlist[Ans],bg='#f7af05',fg='Black',font=('Times new roman',18)).pack(pady=10)
                name3=str(name3)
                file = open('Your Data.txt','a')
                file.write('Ans2: '+name3+'\n')
                file.close()   
        import tkinter as tk
        from tkinter import messagebox
        screen = tk.Tk()
        screen.title('Quiz')
        screen.geometry('1200x1400')
        screen.configure(bg='#f7af05')
        randomno=random.choice([i for i in listno if i not in rano])
        rano.append(randomno)
        
        tk.Label(screen,text= 'Your Quiz is here',bg='#f7af05',fg='Black',font=('Times new roman',24)).pack(pady=10)
        tk.Button(screen,text='Exit This Window',bg='white',fg='black',font=('Times new roman',18),command = screen.withdraw).place(x=10,y=10)
        tk.Label(screen,text= "Q(2)  "+Queslist[randomno],bg='#f7af05',fg='Black',font=('Times new roman',22)).pack(pady=10)
        tk.Label(screen,text=optlist[randomno*4],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+1],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+2],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text=optlist[randomno*4+3],bg='#f7af05',fg='white',font=('Times new roman',20,'bold')).pack(pady = 10)
        tk.Label(screen,text= ' Write NO.from 1 to 4 as Option',bg='#f7af05',fg='Black',font=('Times new roman',20)).pack(pady=10)
        username2 = tk.Entry(screen,bg='#ffe23d',fg='blue',font=('Times new roman',20))
        username2.pack()
        b1=tk.Button(screen,text='save',bg='#f7af05',fg='white',font=('Times new roman',20), command=save)
        b1.pack(pady=50)
        b2=tk.Button(screen,text='Next',bg='#f7af05',fg='white',font=('Times new roman',20),command = lambda:[b2.configure(state=DISABLED), onclick2(), screen.withdraw()])
        b2.pack(pady = 10)

    screen = tk.Tk()
    screen.title('Quiz')
    screen.geometry('1200x1400')
    screen.configure(bg='#f7af05')
    randomno=random.choice([i for i in listno if i not in rano])
    rano.append(randomno)
    tk.Label(screen,text= 'Your Quiz is here',bg='#f7af05',fg='Black',font=('Times new roman',24)).pack(pady=10)
    tk.Button(screen,text='Exit This Window',bg='white',fg='black',font=('Times new roman',18),command = screen.withdraw).place(x=10,y=10)
    tk.Label(screen,text="Q(1)  "+ Queslist[randomno],bg='#f7af05',fg='Black',font=('Times new roman',22)).pack(pady=10)
    tk.Label(screen,text=optlist[randomno*4],bg='#f7af05',fg='#0047AB',font=('Times new roman',20,'bold')).pack(pady = 10)
    tk.Label(screen,text=optlist[randomno*4+1],bg='#f7af05',fg='#0047AB',font=('Times new roman',20,'bold')).pack(pady = 10)   
    tk.Label(screen,text=optlist[randomno*4+2],bg='#f7af05',fg='#0047AB',font=('Times new roman',20,'bold')).pack(pady = 10)
    tk.Label(screen,text=optlist[randomno*4+3],bg='#f7af05',fg='#0047AB',font=('Times new roman',20,'bold')).pack(pady = 10)
    tk.Label(screen,text= ' Write NO.from 1 to 4 as Option',bg='#f7af05',fg='Black',font=('Times new roman',20)).pack(pady=10)
    username7 = tk.Entry(screen,bg='#ffe23d',fg='blue',font=('Times new roman',20))
    username7.pack()
    b1=tk.Button(screen,text='save',bg='#f7af05',fg='white',font=('Times new roman',20), command=save)    
    b1.pack(pady=50)
    b2=tk.Button(screen,text='Next',bg='#f7af05',fg='white',font=('Times new roman',20),command = lambda:[b2.configure(state=DISABLED), onclick1 (), screen.withdraw()])
    b2.pack(pady = 10)
    
        
            
screen = tk.Tk() 
screen.title('Brain Teaser') 
screen.geometry('1200x1400') 
screen.configure(bg='#ceb4db')
tk.Label(screen,text= 'Hey! Write Your Name',bg='#ceb4db',fg='black',font=('Helvetica',24)).pack(pady=10)
username = tk.Entry(screen,bg='pink',fg='blue',font=('Times new roman',18))
username.pack()
tk.Label(screen,text= 'Branch Name',bg='#ceb4db',fg='black',font=('Helvetica',24)).pack(pady=10)
username0 = tk.Entry(screen,bg='Pink',fg='Blue',font=('Times new roman',18))
username0.pack()
tk.Button(screen,text='Submit Info',bg='#ceb4db',fg='white',font=('Times new roman',16),command = save).pack(pady = 30)
tk.Label(screen,text= 'What make you Crazy , Choose',bg='#ceb4db',fg='black',font=('Helvetica',24)).pack(pady=10)
tk.Button(screen,text='Play',bg='#ceb4db',fg='White',font=('Times new roman',20,'bold'),command = onclick1).pack(pady = 40)
tk.Button(screen,text='Quiz',bg='#ceb4db',fg='White',font=('Times new roman',20,'bold'),command = onclick3).pack(pady = 30)
tk.Button(screen,text='Exit',bg='#ceb4db',fg='white',font=('Times new roman',18,'bold'),command=quit).pack(pady = 50)

screen.mainloop()
     
