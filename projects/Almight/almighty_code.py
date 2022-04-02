from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
import Library_Backend
import Fee_Backend
root=Tk()
class AlmightyCode:
    def __init__(self,master=None):
        master.geometry("1320x750")
        master.title("TECXON(Jayla)")
        master.config(bg = "lightblue")

        self.Frame1=LabelFrame(height = '14.1111cm',width='9.5833cm', bg = 'white',bd= 2,relief ='ridge')
        self.Frame1.place(x = 500,y =40)

        self.label1 = Label(self.Frame1)
        self.label1.place(relx=0.2, rely=0.02, width='150.606pt', height='140.406 pt')
        self.img = PhotoImage(file="./images/2.png")
        self.label1.configure(image=self.img)

        self.username = Label(self.Frame1, text='Username ', font=('Time_New_Roman', 15), bg='white', fg='blue')
        self.username.place(x=40, y=200)
        self.username= Entry(self.Frame1, font=('Time_New_Roman', 13), fg='black', bd=0, width=30)
        self.username.place(x=40, y=230)
        self.Frame2 = Frame(self.Frame1, width=270, height=1, bg='black')
        self.Frame2.place(x=40, y=250)

        self.password = Label(self.Frame1, text='Password ', font=('Time_New_Roman', 15), bg='white', fg='blue')
        self.password.place(x=40, y=305)
        self.password = Entry(self.Frame1, font=('Time_New_Roman', 13), fg='black', bd=0, width=30, show='*')
        self.password.place(x=40, y=340)

        self.Frame2 = Frame(self.Frame1, width=270, height=1, bg='black')
        self.Frame2.place(x=40, y=360)

        self.button1 = Button(self.Frame1)
        self.button1.place(relx=0.056, rely=0.785, width=330, height=43)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#D2463E")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="blue")
        self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""LOGIN""")
        self.button1.configure(command =self.Login)
    def Login(self,Event = None):
        if self.username.get() == "admin" and self.password.get() =="admin":
            messagebox.showinfo("Message","Login Successful...")
            self.username.delete(0,END)
            self.password.delete(0,END)

            root.withdraw()
            global adm
            global page2
            adm =Toplevel()
            page2=Admin(adm)
            adm.protocol("WM_DELETE_WINDOW",exitt)
            adm.mainloop()
        else:
            messagebox.showinfo("error","you are not an admin")


def student():
    adm.withdraw()
    global std
    global page3
    std=Toplevel()
    page3 = Student(std)
    std.protocol("WM_DELETE_WINDOW", exitt)
    std.mainloop()

def all_student():
    adm.withdraw()
    global all_std
    global page4
    all_std=Toplevel()
    page4 =All_Student(all_std)
    all_std.protocol("WM_DELETE_WINDOW", exitt)
    all_std.mainloop()

def library():
    root.withdraw()
    global lib
    global page4
    lib=Toplevel()
    page4 =Library(lib)
    lib.protocol("WM_DELETE_WINDOW", exitt)
    lib.mainloop()

def exitt():
    Sure = messagebox.askyesno("exit","Are you sure want to Exit",parent =root)
    if Sure == True:
        adm.destroy()
        root.destroy()

class Admin:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("ADMIN Mode")
        self.Frame3 = Frame(adm, width='300pt', height='480pt', bd=3, bg='white', relief='ridge')
        self.Frame3.place(x=10, y=2)

        self.label3 = Label(self.Frame3)
        self.label3.place(relx=0.28, rely=0.05, width=200, height=200)
        self.img = PhotoImage(file="./images/cms_logo4.png")
        self.label3.configure(image=self.img)

        self.Frame4 = Frame(adm, width='650pt', height='480pt', bd=2, bg='navajowhite', relief='ridge')
        self.Frame4.place(x=420, y=2)
        self.label4 = Label(self.Frame4)
        self.label4.place(relx=0, rely=0, width='650pt', height='480pt')
        self.img_4 = PhotoImage(file="./images/bg.png")
        self.label4.configure(image=self.img_4)

        self.btn2 = Button(self.Frame4, text='Log out', font=('Time_New_Roman', 14, 'bold'), bd=0,
                           command='back')
        self.btn2.place(x=750, y=40)

        self.lbl = Label(self.Frame4, text='DASHBOARD', font=('Time_New_Roman', 15, 'bold'), bd=0, fg='red', bg='white')
        self.lbl.place(x=75, y=40)
        self.btn_std = Button(self.Frame4, text='STUDENT', width=20, height=1, bd=0, bg='white', fg='black',
                              font=('Arial', 10, 'bold'), activebackground="blue", command=student)
        self.btn_std.place(relx=0.11, rely=0.349)

        self.btn_sub = Button(self.Frame4, text='ALL STUDENT', width=20, height=1, bd=0, bg='white',
                              fg='black', font=('Arial', 10, 'bold'), activebackground="blue", command=all_student)
        self.btn_sub.place(relx=0.4, rely=0.349)

        self.btn_fee = Button(self.Frame4, text='LIBRARY', width=20, height=1, bd=0, bg='white',
                              fg='black', font=('Arial', 10, 'bold'), activebackground="blue", command=library)
        self.btn_fee.place(relx=0.68, rely=0.349)
        self.btn_std = Button(self.Frame4, text='Fee', width=20, height=1, bd=0, bg='white',
                              fg='black', font=('Arial', 10, 'bold'), activebackground="blue", command='fee')
        self.btn_std.place(relx=0.11, rely=0.8)

        self.btn_std = Button(self.Frame4, text='SETTINGS', width=20, height=1, bd=0, bg='white',
                              fg='black', font=('Arial', 10, 'bold'), activebackground="blue")
        self.btn_std.place(relx=0.41, rely=0.8)

        self.btn_std = Button(self.Frame4, text='TEACHERS', width=20, height=1, bd=0, bg='white',
                              fg='black', font=('Arial', 10, 'bold'), activebackground="blue")
        self.btn_std.place(relx=0.685, rely=0.8)
        # =======================================student==================================================================
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw

class Student:
    def __init__(self,top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Student")
        self.stdf1 = Frame(adm, width=1300, height=650, bd=1, bg='white', relief='ridge')
        self.stdf1.place(x=0, y=0)

        # self.stdf2 = Frame(self.student, width=940, height=60, bd=5, bg='blue',relief ='ridge')
        # self.stdf2.place(x=300, y=10)
        self.stdlbl1 = Label(std, text="STUDENT'S INFORMATION ENTRY", font=('Time_New_Roman', 25, 'bold'),
                             bg='white', fg='red')
        self.stdlbl1.place(x=490, y=15)

        def Exit():
            adm.destroy()

        self.stdf3 = Frame(std, width=250, height=550, bd=5, bg='blue', relief='ridge')
        self.stdf3.place(x=37, y=80)
        self.btn_new = Button(self.stdf3, text='Register New Student', font=('Time_New_Roman', 12, 'bold'), bg='white',
                              fg='red')
        self.btn_new.place(x=25, y=250)

        self.lbl_logo = Label(self.stdf3, text="JAYLA", font=('AZONIX', 25, 'bold'), bg='blue', fg='white')
        self.lbl_logo.place(x=40, y=60)

        self.btn_result = Button(self.stdf3, text='Enter Result', font=('Time_New_Roman', 12, 'bold'), bg='white',
                                 fg='red')
        self.btn_result.place(x=55, y=320)

        self.btn_Exit = Button(self.stdf3, text='Exit', font=('Time_New_Roman', 12, 'bold'), bg='red', fg='white',
                               width=10, height=2, command=Exit)
        self.btn_Exit.place(x=65, y=450)

        self.stdf4 = Frame(std, width=940, height=550, bd=5, bg='white', relief='ridge')
        self.stdf4.place(x=300, y=80)
        # ============================================content frames for entry===========================================
        self.stdf5 = Frame(self.stdf4, width=910, height=520, bd=3, bg='white', relief='ridge')
        self.stdf5.place(x=10, y=10)
        # =========================Label and entry======================================
        self.add_std1 = Label(self.stdf5, text='Student ID ', font=('Time_New_Roman', 15), bg='white', fg='red', bd=0)
        self.add_std1.place(x=10, y=10)
        self.add_ent1 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent1.place(x=200, y=10)
        self.add_std1 = Label(self.stdf5, text='First Name ', font=('Time_New_Roman', 15), bg='white', fg='red', bd=0)
        self.add_std1.place(x=10, y=50)
        self.add_ent1 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent1.place(x=200, y=50)
        self.add_std1 = Label(self.stdf5, text='Last Name ', font=('Time_New_Roman', 15), bg='white', fg='red', bd=0)
        self.add_std1.place(x=10, y=90)
        self.add_ent1 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent1.place(x=200, y=90)

        self.add_std1 = Label(self.stdf5, text='Date Of Birth ', font=('Time_New_Roman', 15), bg='white', fg='red',
                              bd=0)
        self.add_std1.place(x=10, y=130)
        self.add_ent1 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent1.place(x=200, y=130)
        self.add_std4 = Label(self.stdf5, text='Place Of Birth', font=('Time_New_Roman', 15), bg='white', fg='red',
                              bd=0)
        self.add_std4.place(x=10, y=170)
        self.add_ent4 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent4.place(x=200, y=170)
        self.add_std5 = Label(self.stdf5, text='Telephone', font=('Time_New_Roman', 15), bg='white', fg='red', bd=0)
        self.add_std5.place(x=10, y=210)
        self.add_ent5 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent5.place(x=200, y=210)
        self.add_std6 = Label(self.stdf5, text="Father's Name", font=('Time_New_Roman', 15), bg='white', fg='red', bd=0)
        self.add_std6.place(x=10, y=250)
        self.add_ent6 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent6.place(x=200, y=250)
        self.add_std7 = Label(self.stdf5, text="Mother's Name", font=('Time_New_Roman', 15), bg='white', fg='red', bd=0)
        self.add_std7.place(x=10, y=290)
        self.add_ent7 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent7.place(x=200, y=290)
        self.add_std4 = Label(self.stdf5, text='Address ', font=('Time_New_Roman', 15), bg='white', fg='red', bd=0)
        self.add_std4.place(x=10, y=330)
        self.add_ent4 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent4.place(x=200, y=330)
        self.add_std4 = Label(self.stdf5, text='Parent Contact ', font=('Time_New_Roman', 15), bg='white', fg='red',
                              bd=0)
        self.add_std4.place(x=10, y=370)
        self.add_ent4 = Entry(self.stdf5, font=('Time_New_Roman', 14), bg='white', fg='blue', bd=1)
        self.add_ent4.place(x=200, y=370)
        # =========================button=====================================
        # self.passptFrame1 = LabelFrame(self.stdf5, width=1300, height=20,
        #                              bg='white', bd=4)
        # self.passptFrame1.grid(row=11, column=1, padx=10, pady=10)
        self.buttonstd1 = Button(self.stdf5, width=30, height=2, text='ADD DATA',
                                 font=('Time_New_Roman', 15, 'bold'), fg='white', bg='blue')
        self.buttonstd1.place(x=90, y=435)

        self.buttonstd2 = Button(self.stdf5, width=30, height=2, text='RESET DATA',
                                 font=('Time_New_Roman', 15, 'bold'), fg='white', bg='red')
        self.buttonstd2.place(x=500, y=435)
        self.passptFrame = LabelFrame(self.stdf5, text='Upload Passport', width=200, height=230, bg='white', bd=4)
        self.passptFrame.place(x=600, y=10)

        self.button()

    def button(self):
        self.button = Button(self.stdf5, text='Browse a file', fg='blue', width=15, height=2, command=self.fileDialog)
        self.button.place(x=640, y=260)


    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                                   filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.label = Label(self.stdf5, text=" ")
        self.label.place(x=690, y=30)
        self.label.configure(text=self.filename)
        img = Image.open(self.filename)
        photo = ImageTk.PhotoImage(img)
        self.label4 = Label(self.passptFrame, image=photo)
        self.label4.image = photo
        self.label4.place(x=0, y=0)

class All_Student:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("All Student")
        self.allf1 = Frame(all_std, width=250, height=550, bd=5, bg='blue', relief='ridge')
        self.allf1.place(x=37, y=80)
        self.buttonstd1 = Button(self.allf1, width=21, height=2, text='DELETE STUDENT INFO',
                                 font=('Time_New_Roman', 12, 'bold'), fg='red', bg='navajowhite')
        self.buttonstd1.place(x=8, y=320)

        def Exit_P():
            adm.destroy()
            root.mainloop()

        self.buttonstd2 = Button(self.allf1, width=15, height=2, text='EXIT PAGE',
                                 font=('Time_New_Roman', 12, 'bold'), fg='white', bg='red', command=Exit_P)
        self.buttonstd2.place(x=37, y=400)

        search = Entry(self.allf1, font=('Time_New_Roman', 14), width=15, bg='white', fg='blue', bd=2)
        search.place(x=0, y=160)
        self.buttonstd2 = Button(self.allf1, width=7, height=1, text='SEARCH',
                                 font=('Time_New_Roman', 9, 'bold'), fg='white', bg='red')
        self.buttonstd2.place(x=180, y=160)

        self.lbl_logo = Label(self.allf1, text="JAYLA", font=('AZONIX', 30, 'bold'), bg='blue',
                              fg='white')
        self.lbl_logo.place(x=40, y=60)

        self.lbl_logo = Label(self.allf1, text="**ID Search only**", font=('Elephant', 14, 'bold'), bg='blue',
                              fg='white')
        self.lbl_logo.place(x=25, y=200)

        self.stdlbl1 = Label(all_std, text="STUDENT'S INFORMATION DATABASE", font=('Time_New_Roman', 25, 'bold'),
                             bg='white', fg='red')
        self.stdlbl1.place(x=490, y=15)

        self.allf2 = Frame(all_std, width=940, height=550, bd=5, bg='white', relief='ridge')
        self.allf2.place(x=300, y=80)

        # =============================================List box and scrollbar===========================================
        # sb = Scrollbar(self.allf2)
        # sb.grid(row=0, column=1, sticky='ns')

        # self.list = Listbox(self.allf2, font=(
        # 'arial', 13, 'bold'), width=100, height=27)
        # self.list.bind('<<ListboxSelect>>',)
        # self.list.grid(row=0, column=0)
        # sb.config(command=self.list.yview)

        self.scrollbarx = Scrollbar(self.allf2, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.allf2, orient=VERTICAL)
        self.tree = ttk.Treeview(self.allf2)
        self.tree.place(relx=0.002, rely=0.014, width=905, height=500)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", " ")

        self.scrollbary.configure(command=" ")
        self.scrollbarx.configure(command=" ")

        self.scrollbary.place(relx=0.974, rely=0.016, width=21, height=518)
        self.scrollbarx.place(relx=0.007, rely=0.944, width=884, height=22)

        self.tree.configure(
            columns=(
                "ID",
                "Name",
                "DOB",
                "Place Of Birth",
                "Telephone",
                "Father's Name",
                "Mother's Name",
                "Address",
            )
        )

        self.tree.heading("ID", text="STUDENT ID", anchor=W)
        self.tree.heading("Name", text="NAME", anchor=W)
        self.tree.heading("DOB", text="DOB", anchor=W)
        self.tree.heading("Place Of Birth", text="PlACE OF BIRTH", anchor=W)
        self.tree.heading("Telephone", text="TELEPHONE", anchor=W)
        self.tree.heading("Father's Name", text="FATHER'S NAME", anchor=W)
        self.tree.heading("Mother's Name", text="MOTHER'S NAME", anchor=W)
        self.tree.heading("Address", text="ADDRESS", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)
        self.tree.column("#8", stretch=NO, minwidth=0, width=100)

class Library:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Library")
        self.Mtype = StringVar()
        self.refno = StringVar()
        self.fname = StringVar()
        self.surname = StringVar()
        self.address = StringVar()
        self.post = StringVar()
        self.mobno = StringVar()
        self.ID = StringVar()
        self.title = StringVar()
        self.author = StringVar()
        self.borrow = StringVar()
        self.due = StringVar()
        self.loan = StringVar()
        self.yop = StringVar()
        self.edsn = StringVar()

        # ================================================Functions======================================================
        def BookRec(event):

            try:
                global selected_tuple
                index = self.Listbox_2.curselection()[0]
                selected_tuple = self.Listbox_2.get(index)

                self.Entry_0.delete(0, END)
                self.Entry_0.insert(END, selected_tuple[1])
                self.Entry_1.delete(0, END)
                self.Entry_1.insert(END, selected_tuple[2])
                self.Entry_2.delete(0, END)
                self.Entry_2.insert(END, selected_tuple[3])
                self.Entry_3.delete(0, END)
                self.Entry_3.insert(END, selected_tuple[4])
                self.Entry_4.delete(0, END)
                self.Entry_4.insert(END, selected_tuple[5])
                self.Entry_5.delete(0, END)
                self.Entry_5.insert(END, selected_tuple[6])
                self.Entry_6.delete(0, END)
                self.Entry_6.insert(END, selected_tuple[7])
                self.Entry_7.delete(0, END)
                self.Entry_7.insert(END, selected_tuple[8])
                self.Entry_8.delete(0, END)
                self.Entry_8.insert(END, selected_tuple[9])
                self.Entry_9.delete(0, END)
                self.Entry_9.insert(END, selected_tuple[10])
                self.Entry_10.delete(0, END)
                self.Entry_10.insert(END, selected_tuple[11])
                self.Entry_11.delete(0, END)
                self.Entry_11.insert(END, selected_tuple[12])
                self.Entry_12.delete(0, END)
                self.Entry_12.insert(END, selected_tuple[13])


            except IndexError:
                pass

        def Insert():
            if (len(self.refno.get()) != 0):
                Library_Backend.insert(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get() \
                                       , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get() \
                                       , self.title.get(), self.author.get(), self.borrow.get(), self.due.get() \
                                       , self.loan.get())
                self.Listbox_2.delete(0, END)
                self.Listbox_2.insert(END, (
                    self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get() \
                        , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get() \
                        , self.title.get(), self.author.get(), self.borrow.get(), self.due.get() \
                        , self.loan.get()))

        def Display():
            self.Listbox_2.delete(0, END)
            for row in Library_Backend.view():
                self.Listbox_2.insert(END, row, str(' '))

        def Exit():
            Exit = messagebox.askyesno('Library Management System',
                                       'Confirm if you want to Exit')
            if Exit > 0:
                adm.destroy()
                root.mainloop()
                return

        def Reset():
            self.Mtype.set('')
            self.refno.set('')
            self.fname.set('')
            self.surname.set('')
            self.address.set('')
            self.post.set('')
            self.mobno.set('')
            self.ID.set('')
            self.title.set('')
            self.author.set('')
            self.borrow.set('')
            self.due.set('')
            self.loan.set('')
            self.Display.delete('1.0', END)
            self.Listbox_2.delete(0, END)

        def Delete():
            Library_Backend.delete(selected_tuple[0])
            Reset()
            Display()

        def Update():
            Library_Backend.delete(selected_tuple[0])
            Library_Backend.insert(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get() \
                                   , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get() \
                                   , self.title.get(), self.author.get(), self.borrow.get(), self.due.get() \
                                   , self.loan.get())
            self.Listbox_2.delete(0, END)
            self.Listbox_2.insert(END, (
                self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get() \
                    , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get() \
                    , self.title.get(), self.author.get(), self.borrow.get(), self.due.get() \
                    , self.loan.get()))

        def Search():
            self.Listbox_2.delete(0, END)
            for row in Library_Backend.search(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get() \
                    , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get() \
                    , self.title.get(), self.author.get(), self.borrow.get(), self.due.get() \
                    , self.loan.get()):
                self.Listbox_2.insert(END, row, str(' '))

        def Details():
            self.Display.delete('1.0', END)
            self.Display.insert(END, 'Book ID: ' + self.ID.get() + '\n')
            self.Display.insert(END, 'Title: ' + self.title.get() + '\n')
            self.Display.insert(END, 'Author:  ' + self.author.get() + '\n')
            self.Display.insert(END, 'Edition: ' + self.edsn.get() + '\n')
            self.Display.insert(END, 'Year of Publision: \t' + self.yop.get() + '\n')
            self.Display.insert(END, 'Date Borrowed: ' + self.borrow.get() + '\n')
            self.Display.insert(END, 'Date Due:' + self.due.get() + '\n')
            self.Display.insert(END, 'Days in Loan: ' + self.loan.get() + '\n')

        # =====================================================Frames=====================================================
        Main_Frame = Frame(lib, bg='navajowhite')
        Main_Frame.grid()

        Title_Frame_1 = Frame(Main_Frame, width=1350, bg='navajowhite', relief=RIDGE, bd=15,
                              padx=20)
        Title_Frame_1.pack(side=TOP)

        self.lblTitle = Label(Title_Frame_1, font=('arial', 40, 'bold'),
                              text='\tLibrary Management System\t', \
                              bg='navajowhite', padx=13)
        self.lblTitle.grid()

        Button_Frame = Frame(Main_Frame, width=1350, height=50, relief=RIDGE, bd=10,
                             bg='navajowhite')
        Button_Frame.pack(side=BOTTOM)

        Detail_Frame = Frame(Main_Frame, width=1350, height=100, relief=RIDGE, bd=10,
                             bg='navajowhite')
        Detail_Frame.pack(side=BOTTOM)

        Data_Frame = Frame(Main_Frame, width=1350, height=400, relief=RIDGE, bd=15,
                           bg='navajowhite')
        Data_Frame.pack(side=BOTTOM)

        Frame_1 = LabelFrame(Data_Frame, width=800, height=400, relief=RIDGE, bd=10,
                             bg='navajowhite', \
                             text="Library Membership Info:", padx=20,
                             font=('arial', 15, 'bold'))
        Frame_1.pack(side=LEFT, padx=3)

        Frame_2 = LabelFrame(Data_Frame, width=550, height=400, relief=RIDGE, bd=10,
                             bg='navajowhite', \
                             text="Book Details:", padx=20, font=('arial', 15, 'bold'))
        Frame_2.pack(side=RIGHT)

        # ================================================Labels========================================================
        self.Label_1 = Label(Frame_1, text='Member type', font=('arial', 13, 'bold'), pady=2, \
                             bg='navajowhite')
        self.Label_1.grid(row=0, column=0, sticky=W)
        self.Label_2 = Label(Frame_1, text='Reference No.', font=('arial', 13, 'bold'), pady=2, \
                             bg='navajowhite')
        self.Label_2.grid(row=1, column=0, sticky=W)
        self.Label_3 = Label(Frame_1, text='First Name', font=('arial', 13, 'bold'), pady=2, \
                             bg='navajowhite')
        self.Label_3.grid(row=2, column=0, sticky=W)
        self.Label_4 = Label(Frame_1, text='Surname', font=('arial', 13, 'bold'), pady=2, \
                             bg='navajowhite')
        self.Label_4.grid(row=3, column=0, sticky=W)
        self.Label_5 = Label(Frame_1, text='Address', font=('arial', 13, 'bold'), pady=2, \
                             bg='navajowhite')
        self.Label_5.grid(row=4, column=0, sticky=W)
        self.Label_6 = Label(Frame_1, text='Post Code', font=('arial', 13, 'bold'), pady=2, \
                             bg='navajowhite')
        self.Label_6.grid(row=5, column=0, sticky=W)
        self.Label_7 = Label(Frame_1, text='Mobile No.', font=('arial', 13, 'bold'), pady=2, \
                             bg='navajowhite')
        self.Label_7.grid(row=6, column=0, sticky=W)
        self.Label_8 = Label(Frame_1, text='Book ID', font=('arial', 13, 'bold'), pady=2, \
                             bg='navajowhite')
        self.Label_8.grid(row=0, column=2, sticky=W)
        self.Label_9 = Label(Frame_1, text='Book Title', font=('arial', 13, 'bold'), pady=2, \
                             bg='navajowhite')
        self.Label_9.grid(row=1, column=2, sticky=W)
        self.Label_10 = Label(Frame_1, text='Author', font=('arial', 13, 'bold'), pady=2, \
                              bg='navajowhite')
        self.Label_10.grid(row=2, column=2, sticky=W)
        self.Label_11 = Label(Frame_1, text='Date Borrowed', font=('arial', 13, 'bold'), pady=2, \
                              bg='navajowhite')
        self.Label_11.grid(row=3, column=2, sticky=W)
        self.Label_13 = Label(Frame_1, text='Date Due', font=('arial', 13, 'bold'), pady=2, \
                              bg='navajowhite')
        self.Label_13.grid(row=4, column=2, sticky=W)
        self.Label_13 = Label(Frame_1, text='Days in Loan', font=('arial', 13, 'bold'), pady=2, \
                              bg='navajowhite')
        self.Label_13.grid(row=5, column=2, sticky=W)

        # ================================================Entries========================================================
        self.Entry_0 = ttk.Combobox(Frame_1, values=(' ', 'Student', 'Faculty', 'Staff Member'), \
                                    font=('arial', 13, 'bold'), width=23,
                                    textvariable=self.Mtype)
        self.Entry_0.grid(row=0, column=1)
        self.Entry_1 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                             textvariable=self.refno)
        self.Entry_1.grid(row=1, column=1, padx=15)
        self.Entry_2 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                             textvariable=self.fname)
        self.Entry_2.grid(row=2, column=1, padx=15)
        self.Entry_3 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                             textvariable=self.surname)
        self.Entry_3.grid(row=3, column=1, padx=15)
        self.Entry_4 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                             textvariable=self.address)
        self.Entry_4.grid(row=4, column=1, padx=15)
        self.Entry_5 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                             textvariable=self.post)
        self.Entry_5.grid(row=5, column=1, padx=15)
        self.Entry_6 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                             textvariable=self.mobno)
        self.Entry_6.grid(row=6, column=1, padx=15)
        self.Entry_7 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                             textvariable=self.ID)
        self.Entry_7.grid(row=0, column=4, padx=15)
        self.Entry_8 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                             textvariable=self.title)
        self.Entry_8.grid(row=1, column=4, padx=15)
        self.Entry_9 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                             textvariable=self.author)
        self.Entry_9.grid(row=2, column=4, padx=15)
        self.Entry_10 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                              textvariable=self.borrow)
        self.Entry_10.grid(row=3, column=4, padx=15)
        self.Entry_11 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                              textvariable=self.due)
        self.Entry_11.grid(row=4, column=4, padx=15)
        self.Entry_12 = Entry(Frame_1, font=('arial', 13, 'bold'), width=25,
                              textvariable=self.loan)
        self.Entry_12.grid(row=5, column=4, padx=15)

        # =============================================Widgets=========================================================
        self.Display = Text(Frame_2, font=('arial', 13, 'bold'), width=28, height=11)
        self.Display.grid(row=0, column=2)

        List_of_Books = [' C', ' C++', ' Java', ' Python', ' PHP', ' Java Script', ' My SQL',
                         ' Data Structure', ' Linux', \
                         ' Operating System', ' Web Developement', ' Data Science',
                         ' Algorithms', ' Android', \
                         ' VB.net']

        # ===========================================Function for Books Details=========================================
        def SelectedBook(event):
            value = str(self.Listbox_1.get(self.Listbox_1.curselection()))
            v = value

            if (v == ' C'):
                self.ID.set('ISBN 525341')
                self.title.set('Programming using C')
                self.author.set('Yashwant Kanetkar')
                self.yop.set('2019')
                self.edsn.set('5th')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('14')
                self.due.set(d3)
                Details()
            elif (v == ' C++'):
                self.ID.set('ISBN 345687')
                self.title.set('Programming using C++')
                self.author.set('Yashwant Kanetkar')
                self.yop.set('2019')
                self.edsn.set('4th')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=10)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('10')
                self.due.set(d3)
                Details()
            elif (v == ' Java'):
                self.ID.set('ISBN 643842')
                self.title.set('Java Programming')
                self.author.set('Joshua Bloch')
                self.yop.set('2019')
                self.edsn.set('7th')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=13)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('13')
                self.due.set(d3)
                Details()
            elif (v == ' Python'):
                self.ID.set('ISBN 564524')
                self.title.set('Python Programming')
                self.author.set('John Zelle')
                self.yop.set('2019')
                self.edsn.set('3rd')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=13)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('13')
                self.due.set(d3)
                Details()
            elif (v == ' PHP'):
                self.ID.set('ISBN 735893')
                self.title.set('PHP Programming')
                self.author.set('Alan Forbes')
                self.yop.set('2019')
                self.edsn.set('5th')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('15')
                self.due.set(d3)
                Details()
            elif (v == ' Java Script'):
                self.ID.set('ISBN 643842')
                self.title.set('Java Script Programming')
                self.author.set('Jon Duckett.')
                self.yop.set('2019')
                self.edsn.set('4th')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=13)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('13')
                self.due.set(d3)
                Details()
            elif (v == ' My SQL'):
                self.ID.set('ISBN 649635')
                self.title.set('My SQL Programming')
                self.author.set('Groff James')
                self.yop.set('2019')
                self.edsn.set('3rd')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('20')
                self.due.set(d3)
                Details()
            elif (v == ' Data Structure'):
                self.ID.set('ISBN 531588')
                self.title.set('Data Structure')
                self.author.set('Karumanchi Narasimha')
                self.yop.set('2019')
                self.edsn.set('5th')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=11)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('11')
                self.due.set(d3)
                Details()
            elif (v == ' Linux'):
                self.ID.set('ISBN 356853')
                self.title.set('Linux Administration')
                self.author.set('SOYINKA')
                self.yop.set('2019')
                self.edsn.set('1st')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=6)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('6')
                self.due.set(d3)
                Details()
            elif (v == ' Operating System'):
                self.ID.set('ISBN 536453')
                self.title.set('OS Concepts ')
                self.author.set('Silberschatz Abraham')
                self.yop.set('2019')
                self.edsn.set('4th')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=12)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('12')
                self.due.set(d3)
                Details()
            elif (v == ' Web Developement'):
                self.ID.set('ISBN 543548')
                self.title.set('Web Developement ')
                self.author.set('Paul McFedries')
                self.yop.set('2019')
                self.edsn.set('3rd')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('15')
                self.due.set(d3)
                Details()
            elif (v == ' Data Science'):
                self.ID.set('ISBN 835764')
                self.title.set('Data Science Concept ')
                self.author.set('David Stephenson')
                self.yop.set('2019')
                self.edsn.set('3rd')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('15')
                self.due.set(d3)
                Details()
            elif (v == ' Algorithms'):
                self.ID.set('ISBN 535674')
                self.title.set('Basics of Algorithm ')
                self.author.set('Karumanchi Narasimha')
                self.yop.set('2019')
                self.edsn.set('7th')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=10)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('10')
                self.due.set(d3)
                Details()
            elif (v == ' Android'):
                self.ID.set('ISBN 356452')
                self.title.set('Android Programming')
                self.author.set('Harwani B. M')
                self.yop.set('2019')
                self.edsn.set('4th')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=9)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('9')
                self.due.set(d3)
                Details()

        # ===========================================List Box and Scroll Bar==========================================
        sb_1 = Scrollbar(Frame_2)
        sb_1.grid(row=0, column=1, sticky='ns')

        self.Listbox_1 = Listbox(Frame_2, font=('arial', 13, 'bold'), width=20, height=10)
        self.Listbox_1.bind('<<ListboxSelect>>', SelectedBook)
        self.Listbox_1.grid(row=0, column=0)
        sb_1.config(command=self.Listbox_1.yview)

        sb_2 = Scrollbar(Detail_Frame)
        sb_2.grid(row=1, column=1, sticky='ns')

        self.Listbox_2 = Listbox(Detail_Frame, font=('arial', 13, 'bold'), width=144, height=11)
        self.Listbox_2.bind('<<ListboxSelect>>', BookRec)
        self.Listbox_2.grid(row=1, column=0)
        sb_2.config(command=self.Listbox_2.yview)

        for items in List_of_Books:
            self.Listbox_1.insert(END, items)

        # =============================================Buttons=========================================================
        Button_1 = Button(Button_Frame, text='SAVE', font=('arial', 15, 'bold'), width=10,
                          command=Insert)
        Button_1.grid(row=0, column=0, padx=8, pady=5)
        Button_2 = Button(Button_Frame, text='DISPLAY', font=('arial', 15, 'bold'), width=10,
                          command=Display)
        Button_2.grid(row=0, column=1, padx=8)
        Button_3 = Button(Button_Frame, text='RESET', font=('arial', 15, 'bold'), width=10,
                          command=Reset)
        Button_3.grid(row=0, column=2, padx=8)
        Button_4 = Button(Button_Frame, text='UPDATE', font=('arial', 15, 'bold'), width=10,
                          command=Update)
        Button_4.grid(row=0, column=3, padx=8)
        Button_5 = Button(Button_Frame, text='SEARCH', font=('arial', 15, 'bold'), width=10,
                          command=Search)
        Button_5.grid(row=0, column=4, padx=8)
        Button_6 = Button(Button_Frame, text='DELETE', font=('arial', 15, 'bold'), width=10,
                          command=Delete)
        Button_6.grid(row=0, column=5, padx=8)
        Button_7 = Button(Button_Frame, text='EXIT', font=('arial', 15, 'bold'), width=10,
                          command=Exit)
        Button_7.grid(row=0, column=6, padx=8)


obj = AlmightyCode(root)
root.mainloop()



