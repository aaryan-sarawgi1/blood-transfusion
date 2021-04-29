from tkinter import *
import sqlite3
db=sqlite3.connect("test.db")
cursor=db.cursor()
print("Successfully Connected to SQLite")
root = Tk()
root.title("BLOOD BANK")
root.geometry("1920x1080")
root.iconbitmap('C:/Users/Samir/Desktop/icon_img_1.ico')

background_image=PhotoImage(file='C:/Users/Samir/Desktop/bloodpic1.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
l3=Label(root,text="BLOOD BANK SYSTEM",bg='white',font = "Helvetica 15 bold").place(x=550,y=40,w=350,h=50)
l1=Label(root,text="Click to enter the details of the DONOR",bg='white',font="Helvetica 12").place(x=350,y=200,w=300,h=40)
b1=Button(root,text="Donor Details",command=lambda : donordetails()).place(x=450,y=250)
l3=Label(root,text="Click to make a request for BLOOD",bg='white',font="Helvetica 12").place(x=350,y=300,w=300,h=40)
b3=Button(root,text="Blood Request",command=lambda : requestblood()).place(x=450,y=350)
b2=Button(root,text="Exit",padx=20,pady=7,command=lambda : stop(root)).place(x=350,y=410)


v = StringVar()

def insertDonor(name,age,gender,address,contactno,bloodgroup,platelet,rbc,date):
	try:
		cursor.execute("INSERT INTO donor (name,age,gender,address,contactno,bloodgroup,platelet,rbc,date) VALUES(?, ?, ?, ?, ? ,?, ?, ?, ?)", (name,age,gender,address,contactno,bloodgroup,platelet,rbc,date)) 
		db.commit()
		root=Toplevel()
		root.title("BLOOD BANK")
		root.iconbitmap('C:/Users/Samir/Desktop/icon_img_1.ico')
		root.geometry("720x450")
		background_image=PhotoImage(file='C:/Users/Samir/Desktop/thank_img.png')
		background_label = Label(root, image=background_image)
		background_label.place(x=0, y=0, relwidth=1, relheight=1)
		l=Label(root,text="Hiie  "+name,padx=50,pady=10).place(x=300,y=65)
		b2=Button(root,text="Back",padx=25,pady=8,command=lambda : stop(root)).place(x=330,y=250)
		background_label.image = background_image
		root.mainloop()
	except:
		db.rollback()

	
def retrieve(bg):
	request="select * from donor  where bloodgroup='"+bg+"'"
	
	try:
		cursor.execute(request)		
		rows=cursor.fetchall()		
		db.commit()
		print ((rows))
		return rows
	except:
		db.rollback() 
 

def donordetails():
	e3=StringVar()
	root=Toplevel()
	root.title("BLOOD BANK")
	root.geometry("1920x1080")
	root.iconbitmap('C:/Users/Samir/Desktop/icon_img_1.ico')
	background_image=PhotoImage(file='C:/Users/Samir/Desktop/blood_img.png')
	background_label = Label(root, image=background_image)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)
	l1=Label(root,text="Name:",bg='white',font="Helvetica 12").place(x=450,y=40)
	l2=Label(root,text="Age:",bg='white',font="Helvetica 12").place(x=450,y=80)
	l3=Label(root,text="Gender:",bg='white',font="Helvetica 12").place(x=450,y=120)
	l4=Label(root,text="Address:",bg='white',font="Helvetica 12").place(x=450,y=220)
	l5=Label(root,text="Contact:",bg='white',font="Helvetica 12").place(x=450,y=260)
	l6=Label(root,text="Blood Group:",font="Helvetica 12").place(x=450,y=300)
	l7=Label(root,text="PLatetelet count (in 100 thousands):",font="Helvetica 12").place(x=450,y=340)
	l8=Label(root,text="RBC count (in millions):",font="Helvetica 12").place(x=450,y=380,w=250,h=20)
	l9=Label(root,text="Date Of Entry count:").place(x=450,y=420)
	e1=Entry(root)
	e1.place(x=530,y=40)
	e2=Entry(root)
	e2.place(x=530,y=80)
	r1=Radiobutton(root,text="Male",variable=e3,value="Male").place(x=530,y=120)
	r2=Radiobutton(root,text="Female",variable=e3,value="Female").place(x=530,y=150)
	r3=Radiobutton(root,text="Other",variable=e3,value="Other").place(x=530,y=180)
	e4=Entry(root)
	e4.place(x=530,y=220)
	e5=Entry(root)
	e5.place(x=530,y=260)
	e6=Entry(root)
	e6.place(x=730,y=300)
	e7=Entry(root)
	e7.place(x=730,y=340)
	e8=Entry(root)
	e8.place(x=730,y=380)
	e9=Entry(root)
	e9.place(x=730,y=420)

	
	b2=Button(root,text="BACK",bg="red",fg="white",padx=25,pady=8,command=lambda : stop(root)).place(x=600,y=460)
	
	b1=Button(root,text="SUBMIT",bg="green",fg="white",padx=25,pady=8,command=lambda : insertDonor(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())).place(x=450,y=460)
	
	
	root.mainloop()

	
def grid1(bg):
	root=Toplevel()
	root.title("LIST OF MATCHING DONORS")
	root.geometry("1150x619")
	root.iconbitmap('C:/Users/Samir/Desktop/icon_img_1.ico')
	background_image=PhotoImage(file='C:/Users/Samir/Desktop/match1_img.png')
	background_label = Label(root, image=background_image)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)
	rows=retrieve(bg)
	x=0
	for row in rows:
		l1=Label(root,text=row[0],bg="#E0EEEE",font = "Verdana 15 bold").grid(row=x,column=0,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l2=Label(root,text=row[1],bg="#E0EEEE",font = "Verdana 15 bold").grid(row=x,column=1,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l3=Label(root,text=row[2],bg="#E0EEEE",font = "Verdana 15 bold").grid(row=x,column=2,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l4=Label(root,text=row[3],bg="#E0EEEE",font = "Verdana 15 bold").grid(row=x,column=3,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l5=Label(root,text=row[4],bg="#E0EEEE",font = "Verdana 15 bold").grid(row=x,column=4,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l6=Label(root,text=row[5],bg="#E0EEEE",font = "Verdana 15 bold").grid(row=x,column=5,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l7=Label(root,text=row[6],bg="#E0EEEE",font = "Verdana 15 bold").grid(row=x,column=6,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l8=Label(root,text=row[7],bg="#E0EEEE",font = "Verdana 15 bold").grid(row=x,column=7,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l9=Label(root,text=row[8],bg="#E0EEEE",font = "Verdana 15 bold").grid(row=x,column=8,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		x=x+1
	root.mainloop()

def requestblood():
	root=Toplevel()
	root.title("BLOOD BANK")
	root.geometry("900x500")
	root.configure(background='rosybrown1')
	root.iconbitmap('C:/Users/Samir/Desktop/icon_img_1.ico')
	l=Label(root,text="Enter the blood group").place(x=50,y=50,w=400,h=40)
	e=Entry(root)
	e.place(x=500,y=50)
	b2=Button(root,text="BACK",command=lambda : stop(root)).place(x=600,y=100)
	b1=Button(root,text="ENTER",command=lambda : grid1(e.get())).place(x=500,y=100)
	root.mainloop()

def stop(root):
	root.destroy()

background_label.image = background_image
root.mainloop()
