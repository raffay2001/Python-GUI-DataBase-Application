#IMPORTING TKINTER AND PILLOW AND MESSAGE BOX:-
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk


#INITIALIZING AN EMPTY LIST:-
main_list=[]


#FUNCTION FOR BUTTON_1:-
def butt_1():
    r=Tk()
    r.title("MENU AND INSTRUCTIONS")
    r.geometry("1300x600+30+50")
    r.configure(bg="#26001b")

    #MAKING FUNCTIONS FOR ALL 5 BUTTONS:-

    #FUNCTION TO ADD A RECORD i.e BUTTON_2:-
    def butt_2():
        r=Tk()
        r.title("REGISTRATION PORTAL")
        r.geometry("1300x600+30+50")
        r.configure(bg="#26001b")

        #FUNCTION FOR CALCULATING THE MONTHLY SALARY OF THE DRIVER BASED UPON HIS DAILY WAGE i.e BUTTON_7(RUN-TIME CALCULATION):-
        def butt_7():
            global Total_Salary
            Total_Salary=0
            Daily_wage_for_X=5000.0
            Daily_wage_for_PREMIUM=3000.0
            Daily_wage_for_GO=2000.0

            if (e6.get())=="X":
                Total_Salary+=Daily_wage_for_X*30
                lab_6=Label(r,text=f"The Monthly Salary Of Mr.{e1.get()} Is {Total_Salary} Rs.",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
                lab_6.place(x=700,y=305)

            
            elif (e6.get())=="PREMIUM":
                Total_Salary+=Daily_wage_for_PREMIUM*30
                lab_6=Label(r,text=f"The Monthly Salary Of Mr.{e1.get()} Is {Total_Salary} Rs.",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
                lab_6.place(x=700,y=305)


            elif (e6.get())=="GO":
                Total_Salary+=Daily_wage_for_GO*30
                lab_6=Label(r,text=f"The Monthly Salary Of Mr.{e1.get()} Is {Total_Salary} Rs.",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
                lab_6.place(x=700,y=305)


        #FUNCTION FOR SAVING THE RECORD IN A FILE AND EXIT FROM THE WINDOW i.e BUTTON_8:-
        def butt_8():
            #APPENDING ALL THE DATA OF THE FORM IN THE MAIN_LIST:-
            main_list.append([e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),str(Total_Salary),e7.get()])
            
            #OPENING THE FILE DB_FILE.txt TO SAVE THE CURRENT RECORDS:-
            infile=open("E:/DATABASE PROJECT/DB_FILE.txt","w")
            infile.write('{:15}'.format('NAME'))
            infile.write('{:18}'.format('NIC-NUMBER'))
            infile.write('{:18}'.format('PHONE-NUMBER'))
            infile.write('{:30}'.format('E-MAIL-ADDRESS'))
            infile.write('{:20}'.format("CAR'S-NO.PLATE"))
            infile.write('{:15}'.format('CAR-CLASS'))
            infile.write('{:20}'.format("DRIVER'S-SALARY"))
            infile.write('{:8}'.format("4-DIGIT-ID"))
            infile.write(f'\n')

            
            #ITERATING THROUGH THE MAIN LIST OF RECORDS TO WRITE EACH RECORD IN THE FILE DB_FILE.txt:-
            for record in range(len(main_list)):
                infile.write('{:15}'.format(main_list[record][0]))
                infile.write('{:18}'.format(main_list[record][1]))
                infile.write('{:18}'.format(main_list[record][2]))
                infile.write('{:40}'.format(main_list[record][3]))
                infile.write('{:30}'.format(main_list[record][4]))
                infile.write('{:25}'.format(main_list[record][5]))
                infile.write('{:30}'.format(main_list[record][6]))
                infile.write('{:8}'.format(main_list[record][7]))
                infile.write(f'\n')

            infile.close()

            showinfo(message="♦ Your Response Has Been Submitted ♦")
            r.destroy()
        

        #MAKING THE SECOND WINDOW:-

        #MAIN HEADING:-
        lab=Label(r,text="DRIVER'S REGISTRATION FORM:-",font=('Elephant',20,'bold'),bg="#26001b",fg="white")
        lab.pack()

        #FULL NAME ENTRY:-
        lab1=Label(r,text="Full Name:",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
        lab1.place(x=100,y=65)
        e1=Entry(r,font=('Bahnschrift',12),bg="#fcf8ec")
        e1.place(x=270,y=70)
    
        #NIC-NUMBER ENTRY:-
        lab2=Label(r,text="NIC Number:",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
        lab2.place(x=100,y=115)
        e2=Entry(r,font=('Bahnschrift',12),bg="#fcf8ec")
        e2.place(x=270,y=117)

        #PHONE-NUMBER ENTRY:-
        lab3=Label(r,text="Phone Number:",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
        lab3.place(x=100,y=160)
        e3=Entry(r,font=('Bahnschrift',12),bg="#fcf8ec")
        e3.place(x=270,y=165)

        #E-MAIL ADDRESS ENTRY:-
        lab4=Label(r,text="E-Mail Address:",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
        lab4.place(x=100,y=205)
        e4=Entry(r,font=('Bahnschrift',12),bg="#fcf8ec")
        e4.place(x=270,y=210)

        #CARS"S NUMBER PLATE ENTRY:-
        lab5=Label(r,text=f"Car's No. Plate:",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
        lab5.place(x=100,y=255)
        e5=Entry(r,font=('Bahnschrift',12),bg="#fcf8ec")
        e5.place(x=270,y=260)

        #CAR CLASS ENTRY:-
        lab6=Label(r,text=f"Car's Class\nIncludes:\n(X,PREMIUM,GO)",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
        lab6.place(x=100,y=305)
        e6=Entry(r,font=('Bahnschrift',12),bg="#fcf8ec")
        e6.place(x=270,y=310)

        #CREATING A BUTTON WHICH SHOWS THE RUN TIME CALCULATION i.e DRIVER's SALARY BASED ON THE CAR CLASS:-
        Button_7=Button(r,text="CLick Here To See Driver's Salary..",font=('Bahnschrift',13,'bold'),bg="#fcf8ec",command=butt_7,borderwidth=5)
        Button_7.place(x=270,y=345)
        
        #UNIQUE 4-DIGIT ID NUMBER ENTRY:-
        lab7=Label(r,text=f"Unique 4-digit id:",font=('Bahnschrift',15,'bold'),bg="#fcf8ec")
        lab7.place(x=100,y=405)
        e7=Entry(r,font=('Bahnschrift',12),bg="#fcf8ec")
        e7.place(x=270,y=410)



        #CREATING A BUTTON FOR THE SUBMISSION OF FORM AND SAVE THE RECORD INTO A FILE:-
        Button_8=Button(r,text="SUBMIT RESPONSE",font=('Bahnschrift',13,'bold'),bg="#fcf8ec",command=butt_8,borderwidth=5)
        Button_8.place(x=400,y=500)



        r.mainloop()

    #FUNCTION FOR DISPLAYING THE CURRENT RECORDS IN A LISTBOX:-
    def butt_3():
        r=Tk()
        r.title("CURRENT RECORDS")
        r.geometry("1300x600+30+50")
        r.configure(bg="#26001b")

        #DISPLAYING THE CURRENT RECORDS FROM THE FILE DB_FILE.txt:-
        box=Listbox(r,width=1300,height=600,bg="#26001b",fg="white",font=('helvetica',12))

        infile=open("E:/DATABASE PROJECT/DB_FILE.txt","r")
        for i in infile:
            box.insert("end",i)
        box.pack()

        infile.close()

        r.mainloop()

    #FUNCTION FOR DISPLAYING ALL THE RECORDS IN A LISTBOX:-
    def butt_4():
        r=Tk()
        r.title("ALL RECORDS")
        r.geometry("1300x600+30+50")
        r.configure(bg="#26001b")

        #DISPLAYING ALL THE RECORDS FROM THE FILE MAIN_DB.txt:-
        box=Listbox(r,width=1300,height=600,bg="#26001b",fg="white",font=('helvetica',12))

        infile_1=open("E:/DATABASE PROJECT/MAIN_DB.txt","r")
        for i in infile_1:
            box.insert("end",i)
        box.pack()

        infile_1.close()

        r.mainloop()

    #FUNCTION FOR SEARCHING THE RECORDS BY A FOUR DIGIT UNIQUE ID:-
    def butt_5():


        #FUNCTION FOR THE SEARCH BUTTON:-
        def search_button():
            infile_1=open("E:/DATABASE PROJECT/MAIN_DB.txt","r")
            content=infile_1.read()
            content=content.split()
            infile_1.close()
            a=15
            

            for record in range(len(content)):
                if e.get()==content[a]:
                    lab_3=Label(r,text="The Record having ID:"+e.get()+f" is:\n\n"+f'Name: {content[a-7]}\nNIC-No: {content[a-6]}\nPhone-No.: {content[a-5]}\nE-mail: {content[a-4]}\nCar-No.Plate: {content[a-3]}\nCar-Class: {content[a-2]}\nSalary: {content[a-1]}\nID: {content[a]}',font=('helvetica',15,"bold"),bg="#1c1427",fg="white")
                    lab_3.place(x=300,y=200)
                
                else:
                    a+=8
                    continue


        r=Tk()
        r.title("SEARCH A RECORD")
        r.geometry("1300x600+30+50")
        r.configure(bg="#26001b")

        lab_1=Label(r,text="SEARCH FOR A RECORD",font=('Elephant',20,'bold'),bg="#26001b",fg="white")
        lab_1.pack()

        lab_2=Label(r,text="Enter the Four-digit Unique ID Number to Search for a Record:",font=('helvetica',15,"bold"),bg="#fcf8ec",fg="black")
        lab_2.place(x=100,y=100)
        e=Entry(r,font=('Bahnschrift',12),bg="#fcf8ec")
        e.place(x=705,y=102)

        button_1=Button(r,text="Search The Record",font=('Bahnschrift',13,'bold'),bg="#fcf8ec",borderwidth=5,command=search_button)
        button_1.place(x=705,y=135)




        r.mainloop()
        


    #FUNCTION FOR SAVING ALL THE RECORDS IN THE FILE MAIN_DB.TXT AND EXITING FROM THE APP:-
    def butt_6():
        infile=open("E:/DATABASE PROJECT/DB_FILE.txt","r")
        infile_1=open("E:/DATABASE PROJECT/MAIN_DB.txt","a")
        content=infile.read()
        infile_1.write(f"{content}\n")
        infile.close()
        infile_1.close()

        r.destroy()
        main_r.destroy()




    #CREATING BUTTONS FOR THE OPEARTIONS MENU:-
    
    #OPERATIONS MENU:-
    lab_1=Label(r,text="|--OPERATIONS MENU--|",font=('Elephant',19,'bold'),fg="white",bg="#26001b")
    lab_1.place(x=100,y=50)

    #CREATING ALL THE BUTTONS OF THE OPERATIONS MENU:-

    #BUTTON FOR ADD A NEW RECORD:-
    button_2=Button(r,text="ADD A RECORD",font=('helvetica',15,'bold'),fg='white',bg='#26001b',relief='raised',borderwidth=9,command=butt_2)
    button_2.place(x=110,y=110)

    #BUTTON FOR VIEW THE CURRENT RECORDS:-
    button_3=Button(r,text="VIEW CURRENT RECORDS",font=('helvetica',15,'bold'),fg='white',bg='#26001b',relief='raised',borderwidth=9,command=butt_3)
    button_3.place(x=110,y=190)

    #BUTTON FOR VIEW ALL THE RECORDS:-
    button_4=Button(r,text="VIEW ALL RECORDS",font=('helvetica',15,'bold'),fg='white',bg='#26001b',relief='raised',borderwidth=9,command=butt_4)
    button_4.place(x=110,y=270)

    #BUTTON FOR SEARCH FOR A SPECIFIC RECORD:-
    button_5=Button(r,text="SEARCH FOR A RECORD",font=('helvetica',15,'bold'),fg='white',bg='#26001b',relief='raised',borderwidth=9,command=butt_5)
    button_5.place(x=110,y=350)

    #BUTTON TO EXIT THE APPLICATION:-
    button_6=Button(r,text="EXIT AND SAVE ALL RECORDS",font=('helvetica',15,'bold'),fg='white',bg='#26001b',relief='raised',borderwidth=9,command=butt_6)
    button_6.place(x=110,y=430)


    #WRITING INSTRUCTIONS:-
    lab_2=Label(r,text="|--ELIGIBILITY CRITERIA--|",font=('Elephant',19,'bold'),fg="white",bg="#26001b")
    lab_2.place(x=700,y=50)

    #WRITING POINTS FOR INSTRUCTIONS:-
    lab_3=Label(r,text=f"1-DRIVER MUST BE A MALE.\n2-DRIVER'S AGE SHOULD BE IN BETWEEEN 18-50.\n3-DRIVER'S NATIONALITY SHOULD BE PAKISTANI.\n4-DRIVER'S DAILY WAGE DEPENDS UPON THE CLASS OF HIS CAR i.e:\n♦ FOR CLASS X:WAGE IS 5000.0 Rs.\n ♦ FOR CLASS PREMIUM:WAGE IS 3000.0 Rs.\n♦ FOR CLASS GO:WAGE IS 2000.0 Rs.\n5-DRIVER'S MONTHLY SALARY IS CALCULATED FROM HIS DAILY WAGE.",font=('helvetica',14,'bold'),fg="white",bg="#1c1427")
    lab_3.place(x=600,y=100)


    r.mainloop()





#MAIN FUNCTION:-
def main_window():
    # INSTANTIATING THE MAIN WINDOW
    global main_r
    main_r=Tk()
    main_r.title("HOME")
    main_r.geometry("1300x600+30+50")
    main_r.configure(bg="#26001b")

    #MAKING A FRAME_1 FOR IMAGE:-
    frame_1=Frame(main_r)

    # RESIZING THE IMAGE AND PUTTING IT IN THE FRAME_1:-
    img=Image.open("E:/DATABASE PROJECT/IMAGES/car.jpg")
    resized=img.resize((400,800))
    updated_pic=ImageTk.PhotoImage(resized)
    lab=Label(frame_1,image=updated_pic)
    lab.pack(side='left')
    frame_1.pack(side='left')


    #PUTTING ANOTHER IMAGE IN THE MAIN WINDOW:-
    img_1=Image.open("E:/DATABASE PROJECT/IMAGES/car_1.jpg")
    resized_1=img_1.resize((398,150))
    updated_pic_1=ImageTk.PhotoImage(resized_1)
    lab_1=Label(main_r,image=updated_pic_1)
    lab_1.place(x=700,y=100)

    #PLACING THE TEXT:-
    lab_2=Label(main_r,text="WELCOME TO UBER DRIVER REGISTRATION PORTAL",font=('Elephant',19,'bold'),bg='#26001b',fg='white')
    lab_2.pack()

    #PLACING A BUTTON WHICH TAKES THE USER TO THE NEXT WINDOW OF OPERATIONS MENU AND ELIGIBILITY CRITERIA:-
    button_1=Button(main_r,text="CLICK HERE TO CONTINUE..",font=('helvetica',19,'bold'),fg='white',bg='#26001b',relief='raised',borderwidth=9,command=butt_1)
    button_1.place(x=710,y=300)


    main_r.mainloop()

main_window()
