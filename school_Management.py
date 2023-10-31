from calendar import c
from tkinter import *
# from PIL import Image, ImageTk
import tkinter.messagebox as msg
from tkinter import ttk
# import openpyxl



root = Tk()

# specify the window size
root.geometry("1200x700")
root.state('zoomed')
root.title("notepad")

# ********************************* variable ******************************
var_cls = StringVar()

# *************** billion variable ************************
var = IntVar()
var.set(True)

# ***************** student variable ********************
s_name = StringVar()
s_admin = StringVar()
s_father = StringVar()
s_mother = StringVar()
s_contact = StringVar()
s_address = StringVar()
s_email = StringVar()
s_cast = StringVar()
s_blood = StringVar()
s_class = StringVar()
s_gender = StringVar()
# student dob
s_date = StringVar()
s_month = StringVar()
s_year = StringVar()
s_stream = StringVar()

# *************** teacher variable ***************
t_name = StringVar()
t_id = StringVar()
t_father = StringVar()
t_mother = StringVar()
t_contact = StringVar()
t_address = StringVar()
t_email = StringVar()
# joining date
t_j_date = StringVar()
t_j_month = StringVar()
t_j_year = StringVar()
t_blood = StringVar()
t_education = StringVar()
t_gender = StringVar()
# dob
t_date = StringVar()
t_month = StringVar()
t_year = StringVar()

# ************** worker variable ****************8888
w_name = StringVar()
w_id = StringVar()
w_father = StringVar()
w_mother = StringVar()
w_contact = StringVar()
w_address = StringVar()
w_email = StringVar()
# joining date
w_j_date = StringVar()
w_j_month = StringVar()
w_j_year = StringVar()
w_blood = StringVar()
w_gender = StringVar()
# dob date
w_date = StringVar()
w_month = StringVar()
w_year = StringVar()

# check button fuctioning
def check():
    fr = Frame(root)
    fr.place(x=300, y=100, width=400, height=400)
    num = str(s_date.get()) + " - " + s_month.get() + " - " + str(s_year.get())
    Label(fr, text=num, font="lucida 12 bold").pack()

# student info saving button function
def saving_s():
    return

# student info editing button function
def editing_s():
    return

# student info deleting button function
def deleting_s():
    return

# student info searching button
def searching_s():
    return

# student image input button
def image_input_s():
    return


# ----------------- teacher --------------------
# teacher info saving function
def saving_t():
    return

# teacher info editing function
def editing_t():
    return

# teacher info deleting function
def deleting_t():
    return

# teacher info seaching function
def searching_t():
    return

# teacher image input function
def image_input_t():
    return

# --------------------------- worker --------------------
# worker info saving function
def saving_w():
    return

# worker info editing function
def editing_w():
    return

# worker info deleting function
def deleting_w():
    return

# worker info searching function
def searching_w():
    return

# worker image input function
def image_input_w():
    return


# function or button operation
def change():
    msg.showinfo("error", "not available now")


# checkbutton function
def select():
    # money frame
    money_frame = Frame(root)
    money_frame.place(x=654, y=214, width=400, height=210)

    choice = var.get()
    if choice == 0:
        rec_b = Label(money_frame, text='Amount Received : ', font='lucida 10 bold')
        rec_b.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        rec_amo_b = Entry(money_frame, width=25, font='lucida 10 bold')
        rec_amo_b.grid(row=0, column=1)
        # due amount
        due_b = Label(money_frame, text='Due Amount :', font='lucida 10 bold')
        due_b.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        due_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        due_entry_b.grid(row=1, column=1)
        # balance amount
        bal_b = Label(money_frame, text='Balance Amount :', font='lucida 10 bold')
        bal_b.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        bal_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        bal_entry_b.grid(row=2, column=1)
    elif choice == 2:
        rec_b = Label(money_frame, text='Amount Received : ', font='lucida 10 bold')
        rec_b.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        rec_amo_b = Entry(money_frame, width=25, font='lucida 10 bold')
        rec_amo_b.grid(row=0, column=1)

        bank_b = Label(money_frame, text='Bank Name :', font='lucida 10 bold')
        bank_b.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        bank_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        bank_entry_b.grid(row=1, column=1)

        no_b = Label(money_frame, text='Cheque No : ', font='lucida 10 bold')
        no_b.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        no_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        no_entry_b.grid(row=2, column=1)

        che_date = Label(money_frame, text='Cheque date : ', font='lucida 10 bold')
        che_date.grid(row=3, column=0, sticky='w', padx=10, pady=5)
        che_date_entry = Entry(money_frame, width=25, font='lucida 10 bold')
        che_date_entry.grid(row=3, column=1)
        # due amount
        due_b = Label(money_frame, text='Due Amount :', font='lucida 10 bold')
        due_b.grid(row=4, column=0, sticky='w', padx=10, pady=5)
        due_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        due_entry_b.grid(row=4, column=1)
        # balance amount
        bal_b = Label(money_frame, text='Balance Amount :', font='lucida 10 bold')
        bal_b.grid(row=5, column=0, sticky='w', padx=10, pady=5)
        bal_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        bal_entry_b.grid(row=5, column=1)
    elif choice == 4:

        rec_b = Label(money_frame, text='Amount Received : ', font='lucida 10 bold')
        rec_b.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        rec_amo_b = Entry(money_frame, width=25, font='lucida 10 bold')
        rec_amo_b.grid(row=0, column=1)

        bank_b = Label(money_frame, text='Bank Name :', font='lucida 10 bold')
        bank_b.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        bank_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        bank_entry_b.grid(row=1, column=1)
        # id_no_b.config(text="Transaction Id")
        id_b = Label(money_frame, text='Cheque No : ', font='lucida 10 bold')
        id_b.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        id_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        id_entry_b.grid(row=2, column=1)
        # due amount
        due_b = Label(money_frame, text='Due Amount :', font='lucida 10 bold')
        due_b.grid(row=3, column=0, sticky='w', padx=10, pady=5)
        due_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        due_entry_b.grid(row=3, column=1)
        # balance amount
        bal_b = Label(money_frame, text='Balance Amount :', font='lucida 10 bold')
        bal_b.grid(row=4, column=0, sticky='w', padx=10, pady=5)
        bal_entry_b = Entry(money_frame, width=25, font='lucida 10 bold')
        bal_entry_b.grid(row=4, column=1)


# ******************************************** Bills frame ******************************
def billing():

    main_frame = Frame(root, relief="ridge", bd=4, bg='blue')
    main_frame.place(x=200, y=100, width=1080, height=600)
    # Label(main_frame, text='hello', font='lucida 20').pack()
    # entry frame
    entry_frame = Frame(main_frame)
    entry_frame.place(x=50, y=10, width=400, height=550)
    # side frame
    side_frame = Frame(root)
    side_frame.place(x=654, y=114, width=400, height=100)

    bills_frame = Frame(main_frame)
    bills_frame.place(x=890, y=10, width=170, height=230)

    # billing fee checking button
    check_fee_button = Button(bills_frame, text='FEE', width=20, height=2, relief=RIDGE)
    check_fee_button.grid(row=0, column=0, padx=10, pady=10)

    # billing save button
    bills_button = Button(bills_frame, text='SAVE', width=20, height=2, relief=RIDGE)
    bills_button.grid(row=1, column=0, padx=10, pady=10)

    # billing print button
    free_space = Label(bills_frame)
    free_space.grid(row=2, column=0, padx=10, pady=10)
    print_button = Button(bills_frame, text='PRINT', width=20, height=2, relief=RIDGE)
    print_button.grid(row=3, column=0, padx=10, pady=10)

    # entry name for bills
    name_b = Label(entry_frame, text="Name :  ", font="lucida 10 bold")
    name_b.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    entry_name_b = ttk.Entry(entry_frame, width=25, font="lucida 10 bold")
    entry_name_b.grid(row=0, column=1)

    # entry class for bills
    class_b = Label(entry_frame, text="Class :  ", font="lucida 10 bold")
    class_b.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    entry_classes_b = ttk.Combobox(entry_frame, font="lucida 10", width=22, state='readonly')
    entry_classes_b["value"] = ('nursery', 'L kg', 'prep', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                                '12')
    entry_classes_b.current(0)
    entry_classes_b.grid(row=1, column=1)

    # entry month for bills
    name_b = Label(entry_frame, text="Month :  ", font="lucida 10 bold")
    name_b.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    entry_month_b = ttk.Entry(entry_frame, width=25, font="lucida 10 bold")
    entry_month_b.grid(row=2, column=1)

    # entry admission number for bills
    name_b = Label(entry_frame, text="Admission No. :  ", font="lucida 10 bold")
    name_b.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    entry_admin_b = ttk.Entry(entry_frame, width=25, font="lucida 10 bold")
    entry_admin_b.grid(row=3, column=1)

    # entry date number for bills
    name_b = Label(entry_frame, text="Date :  ", font="lucida 10 bold")
    name_b.grid(row=4, column=0, padx=10, pady=5, sticky='w')

    date_frame_b = Frame(entry_frame)
    date_frame_b.place(x=148, y=130, width=183, height=22)
    date_b = ttk.Combobox(date_frame_b, font="lucida 10", width=3, state='readonly', textvariable=s_date)
    date_b["value"] = ([i for i in range(1, 32)])
    date_b.current(0)
    date_b.grid(row=0, column=0)
    month_b = ttk.Combobox(date_frame_b, font="lucida 10", width=8, state='readonly', textvariable=s_month)
    month_b["value"] = ('January', 'February', 'March', 'April' 'May', 'June', 'July', 'August',
                                   'September', 'October', 'November', 'December')
    month_b.current(0)
    month_b.grid(row=0, column=1, padx=4)
    year_b = ttk.Combobox(date_frame_b, font="lucida 10", width=4, state='readonly', textvariable=s_year)
    year_b["value"] = ([j for j in range(2000, 2050)])
    year_b.current(0)
    year_b.grid(row=0, column=2)

    # enter the stream
    stream_b = Label(entry_frame, text='only for class 11 and 12', fg='red')
    stream_b.grid(row=5, column=0, sticky='w', padx=10, pady=5)
    stream_b = Label(entry_frame, text="Stream :  ", font="lucida 10 bold")
    stream_b.grid(row=6, column=0, padx=10, pady=5, sticky='w')
    entry_stream_b = ttk.Combobox(entry_frame, font="lucida 10", width=23, state='readonly')
    entry_stream_b["value"] = ('Science', 'Commerce')
    entry_stream_b.current(0)
    entry_stream_b.grid(row=6, column=1)

    # blank
    Label(entry_frame).grid(row=7, column=0, pady=10)

    # tution fee
    tut_fee_b = Label(entry_frame, text='Tution Fee', font="lucida 10 bold")
    tut_fee_b.grid(row=8, column=0, sticky='w', padx=10, pady=5)
    entry_fee_b = ttk.Entry(entry_frame, width=25, font="lucida 10 bold")
    entry_fee_b.grid(row=8, column=1)

    # bus fee
    bus_fee_b = Label(entry_frame, text='Bus Fee', font="lucida 10 bold")
    bus_fee_b.grid(row=9, column=0, sticky='w', padx=10, pady=5)
    entry_bus_b = ttk.Entry(entry_frame, width=25, font="lucida 10 bold")
    entry_bus_b.grid(row=9, column=1)

    # spf fee
    spf_fee_b = Label(entry_frame, text='SPF Fee', font="lucida 10 bold")
    spf_fee_b.grid(row=10, column=0, sticky='w', padx=10, pady=5)
    entry_spf_b = ttk.Entry(entry_frame, width=25, font="lucida 10 bold")
    entry_spf_b.grid(row=10, column=1)

    # total amount
    total = 7300
    tot_b = Label(entry_frame, text='Total Amount : ', font='lucida 10 bold')
    tot_b.grid(row=11, column=0, padx=10, pady=10, sticky='w')
    tot_amo_b = Label(entry_frame, text=f"{total}", font='lucida 12 bold')
    tot_amo_b.grid(row=11, column=1, sticky='w')

    # amount in words
    word_b = Label(entry_frame, text='Amount In Words : ', font='lucida 10 bold', fg='red')
    word_b.grid(row=12, column=0, padx=10, pady=10, sticky='w')
    word_entry_b = ttk.Entry(entry_frame, width=25, font="lucida 10 bold")
    word_entry_b.grid(row=12, column=1)

    # ************ side frame money **********
    number = 10118
    recp_b = Label(side_frame, text='Receipt No. : ', font='lucida 10 bold')
    recp_b.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    recp_number = Label(side_frame, text=f"{number}", font='lucida 10 bold')
    recp_number.grid(row=0, column=1, padx=10)

    # payment mode
    pay_b = Label(side_frame, text='Payment Mode :', font='lucida 10 bold')
    pay_b.grid(row=1, column=0, sticky='w', padx=10, pady=5)

    # checkbox money
    cash_b = Checkbutton(side_frame, variable=var, text="Cash", onvalue=0, offvalue=1, font="lucida 10 bold",
                         command=select)
    cash_b.grid(row=2, column=0, sticky='w', padx=10, pady=5)

    # cheque money
    cheque_b = Checkbutton(side_frame, variable=var, text="Cheque", onvalue=2, offvalue=3, font="lucida 10 bold",
                           command=select)
    cheque_b.grid(row=2, column=1, sticky='w', padx=10, pady=5)

    # card/online
    card_online_b = Checkbutton(side_frame, variable=var, text="Card/Online", onvalue=4, offvalue=5,
                                font="lucida 10 bold", command=select)
    card_online_b.grid(row=2, column=3, sticky='w', padx=15, pady=5)


# ************************************** student frame ***********************************
def student():
    frame_1_s = Frame(root, relief="ridge", bd=4, bg='red')
    frame_1_s.place(x=200, y=100, width=1080, height=600)

    # ****************************** student column ******************************
    add_std_info = LabelFrame(frame_1_s, text="Add Student Details", bd=2, font='consolas 14 bold', fg='red',
                              bg="lightgrey")
    add_std_info.place(x=5, y=4, width=350, height=560)

    # student name
    add_name_s = Label(add_std_info, text="Student Name : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_name_s.grid(row=0, column=0, sticky='w')
    add_entry1_s = ttk.Entry(add_std_info, width=30, textvariable=s_name)
    add_entry1_s.grid(row=0, column=1)

    # student admission number
    add_admin_s = Label(add_std_info, text="Admission No. :", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_admin_s.grid(row=1, column=0, sticky='w')
    add_entry2_s = ttk.Entry(add_std_info, width=30, textvariable=s_admin)
    add_entry2_s.grid(row=1, column=1)

    # student father name
    add_father_s = Label(add_std_info, text="Fathers Name :", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_father_s.grid(row=2, column=0, sticky='w')
    add_entry3_s = ttk.Entry(add_std_info, width=30, textvariable=s_father)
    add_entry3_s.grid(row=2, column=1)

    # student mother name
    add_mother_s = Label(add_std_info, text="Mother Name : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_mother_s.grid(row=3, column=0, sticky='w')
    add_entry4_s = ttk.Entry(add_std_info, width=30, textvariable=s_mother)
    add_entry4_s.grid(row=3, column=1)

    # student contact number
    add_contact_s = Label(add_std_info, text="Contact Number : ", font="lucida 10 bold", pady=5, padx=4,
                          bg="lightgrey")
    add_contact_s.grid(row=4, column=0, sticky='w')
    add_entry5_s = ttk.Entry(add_std_info, width=30, textvariable=s_contact)
    add_entry5_s.grid(row=4, column=1)

    # student address
    add_address_s = Label(add_std_info, text="Address : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_address_s.grid(row=5, column=0, sticky='w')
    add_entry6_s = ttk.Entry(add_std_info, width=30, textvariable=s_address)
    add_entry6_s.grid(row=5, column=1)

    # student email address
    add_email_s = Label(add_std_info, text="Email : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_email_s.grid(row=6, column=0, sticky='w')
    add_entry7_s = ttk.Entry(add_std_info, width=30, textvariable=s_email)
    add_entry7_s.grid(row=6, column=1)

    # student cast
    add_cast_s = Label(add_std_info, text="Cast : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_cast_s.grid(row=7, column=0, sticky='w')
    entry_cast_s = ttk.Combobox(add_std_info, font="lucida 10", width=23, state='readonly', textvariable=s_cast)
    entry_cast_s["value"] = ('Gen', 'OBD', 'SC', 'ST')
    entry_cast_s.current(0)
    entry_cast_s.grid(row=7, column=1)

    # student blood group
    add_blood_group_s = Label(add_std_info, text="Blood Group : ", font="lucida 10 bold", pady=5, padx=4,
                              bg="lightgrey")
    add_blood_group_s.grid(row=8, column=0, sticky='w')
    entry_blood_s = ttk.Combobox(add_std_info, font="lucida 10", width=23, state='readonly', textvariable=s_blood)
    entry_blood_s["value"] = ('B+', 'O+', 'AB', 'AB+', 'O-')
    entry_blood_s.current(0)
    entry_blood_s.grid(row=8, column=1)

    # student class
    add_class_s = Label(add_std_info, text="Class : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_class_s.grid(row=9, column=0, sticky='w')
    entry_classes = ttk.Combobox(add_std_info, font="lucida 10", width=23,
                                 state='readonly', textvariable=s_class)
    entry_classes["value"] = ('nursery', 'L kg', 'prep', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                              '12')
    entry_classes.current(0)
    entry_classes.grid(row=9, column=1)

    # student Gender
    add_gender_s = Label(add_std_info, text="Gender : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_gender_s.grid(row=10, column=0, sticky='w')
    entry_gender_s = ttk.Combobox(add_std_info, font="lucida 10", width=23, state='readonly', textvariable=s_gender)
    entry_gender_s["value"] = ('Male', 'Female', 'Other')
    entry_gender_s.current(0)
    entry_gender_s.grid(row=10, column=1)

    # Student date of birth
    add_birth_s = Label(add_std_info, text="DOB : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_birth_s.grid(row=11, column=0, sticky='w')

    dob_date_frame_s = Frame(add_std_info, bg='lightgrey')
    dob_date_frame_s.place(x=143, y=336, width=185, height=22)
    entry_dob_date_s = ttk.Combobox(dob_date_frame_s, font="lucida 10", width=3, state='readonly', textvariable=s_date)
    entry_dob_date_s["value"] = ([i for i in range(1, 32)])
    entry_dob_date_s.current(0)
    entry_dob_date_s.grid(row=0, column=0, padx=2)
    entry_dob_month_s = ttk.Combobox(dob_date_frame_s, font="lucida 10", width=8, state='readonly', textvariable=s_month)
    entry_dob_month_s["value"] = ('January', 'February', 'March', 'April' 'May', 'June', 'July', 'August',
                                  'September', 'October', 'November', 'December')
    entry_dob_month_s.current(0)
    entry_dob_month_s.grid(row=0, column=1, padx=2)
    entry_dob_year_s = ttk.Combobox(dob_date_frame_s, font="lucida 10", width=4, state='readonly', textvariable=s_year)
    entry_dob_year_s["value"] = ([j for j in range(2000, 2050)])
    entry_dob_year_s.current(0)
    entry_dob_year_s.grid(row=0, column=2, padx=2)

    # stream info
    add_stream = Label(add_std_info, text='Only For Class 11 and 12', font="lucida 8 bold", pady=5, padx=4,
                       bg="lightgrey", fg='red')
    add_stream.grid(row=12, column=0)

    # student stream (only for class 11 and 12)
    sel_stream_s = Label(add_std_info, text="Stream : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    sel_stream_s.grid(row=13, column=0, sticky='w')
    entry_stream_s = ttk.Combobox(add_std_info, font="lucida 10", width=23, state='readonly', textvariable=s_stream)
    entry_stream_s["value"] = ('Science', 'Commerce')
    entry_stream_s.current(0)
    entry_stream_s.grid(row=13, column=1)

    # ******************************** student Info button ********************************
    frame_2_s = Frame(add_std_info, relief=FLAT, bg="lightgrey")
    frame_2_s.place(x=0, y=490, width=350, height=60)

    # student information saving button
    save_button = Button(frame_2_s, command=saving_s, text="Save", width=10, height=1, font="lucida 12 bold", bg='red', fg="goldenrod")
    save_button.grid(row=0, column=0, padx=3)

    # student information edition button
    edit_button = Button(frame_2_s, command=editing_s, text="Edit", width=10, height=1, font="lucida 12 bold", bg='red', fg="goldenrod")
    edit_button.grid(row=0, column=2, padx=3)

    # student information deleting button
    delete_button = Button(frame_2_s, command=deleting_s, text="Delete", width=10, height=1, font="lucida 12 bold", bg='red',
                           fg="goldenrod")
    delete_button.grid(row=0, column=3, padx=3)

    # *********************************** searching info for student ***********************************

    ser_info_s = LabelFrame(frame_1_s, text='Search Student Information', fg='red', font="consolas 12", bg='lightgrey')
    ser_info_s.place(x=360, y=4, width=710, height=80)

    # student name for search
    stud_name = Label(ser_info_s, text='Student Name : ', font="lucida 10 bold", bg='lightgrey')
    stud_name.grid(row=0, column=0, padx=10)
    add_entry_ser1 = ttk.Entry(ser_info_s, width=20, font="lucida")
    add_entry_ser1.grid(row=1, column=0, padx=10)

    # student admission number for search
    stud_admin = Label(ser_info_s, text='Admission Number : ', font="lucida 10 bold", bg='lightgrey')
    stud_admin.grid(row=0, column=1, padx=10)
    ser_info_s2 = ttk.Entry(ser_info_s, width=15, font="lucida")
    ser_info_s2.grid(row=1, column=1, padx=10)

    # student classes for search
    stud_class = Label(ser_info_s, text='Class : ', font="lucida 10 bold", bg='lightgrey')
    stud_class.grid(row=0, column=2, padx=10)
    ser_info_s3 = ttk.Combobox(ser_info_s, font="lucida 10", width=8, state='readonly')
    ser_info_s3["value"] = ('Nursery', 'lkg', 'prep', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
    ser_info_s3.current(0)
    ser_info_s3.grid(row=1, column=2)

    # search student info button
    search_button = Button(ser_info_s, command=searching_s, width=18, height=1, bg="red", fg='goldenrod', text='Search',
                           font="lucida 12 bold")
    search_button.grid(row=1, column=3, padx=10)

    # ****************************** showing student info *********************************

    info_frame_s = Frame(frame_1_s, bd=5, relief=RIDGE)
    info_frame_s.place(x=360, y=89, width=710, height=475)

    # details frame
    details_frame_s = Frame(info_frame_s, relief=RIDGE, bg='lightgrey')
    details_frame_s.place(x=0, y=0, width=699, height=180)

    # student image frame
    image_frame_s = Frame(details_frame_s, relief=RIDGE, bd=5)
    image_frame_s.place(x=580, y=0, width=119, height=150)

    # student image input button
    image_button_s = Button(details_frame_s, command=image_input_s, text="Select Image", bd=3, bg='goldenrod', fg='red', font="lucida 8 bold")
    image_button_s.place(x=580, y=152, width=119)

    # student name
    det_name_s = Label(details_frame_s, text="Student Name : ", background='lightgrey')
    det_name_s.place(x=0, y=0)
    name_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    name_input_s.place(x=90, y=0)

    # student father name
    det_father_s = Label(details_frame_s, text="Father Name : ", background='lightgrey')
    det_father_s.place(x=0, y=30)
    father_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    father_input_s.place(x=90, y=30)

    # student mother name
    det_mother_s = Label(details_frame_s, text="Mother Name : ", background='lightgrey')
    det_mother_s.place(x=0, y=60)
    mother_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    mother_input_s.place(x=90, y=60)

    # student classes
    det_cls_s = Label(details_frame_s, text="Class : ", background='lightgrey')
    det_cls_s.place(x=0, y=90)
    cls_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    cls_input_s.place(x=50, y=90)

    # student date of birth
    det_dob_s = Label(details_frame_s, text="DOB : ", background='lightgrey')
    det_dob_s.place(x=0, y=120)
    dob_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    dob_input_s.place(x=50, y=120)

    # student address
    det_address_s = Label(details_frame_s, text="Address : ", background='lightgrey')
    det_address_s.place(x=0, y=150)
    address_input_s = Label(details_frame_s, text="-------", bg='lightgrey')
    address_input_s.place(x=60, y=150)

    # next side
    # student admission number
    det_admin_s = Label(details_frame_s, text="Admission No : ", background='lightgrey')
    det_admin_s.place(x=290, y=0)
    admin_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    admin_input_s.place(x=380, y=0)

    # student blood group
    det_blood_s = Label(details_frame_s, text="Blood Group : ", background='lightgrey')
    det_blood_s.place(x=290, y=30)
    blood_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    blood_input_s.place(x=380, y=30)

    # student contact
    det_cont_s = Label(details_frame_s, text="Contact No. : ", background='lightgrey')
    det_cont_s.place(x=290, y=60)
    cont_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    cont_input_s.place(x=380, y=60)

    # student Cast details
    det_cast_s = Label(details_frame_s, text="Cast : ", background='lightgrey')
    det_cast_s.place(x=290, y=85)
    cast_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    cast_input_s.place(x=380, y=85)

    # student Gender
    det_gender_s = Label(details_frame_s, text="Gender : ", background='lightgrey')
    det_gender_s.place(x=290, y=106)
    gender_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    gender_input_s.place(x=380, y=106)

    # student streams details
    det_streams_s = Label(details_frame_s, text="Stream : ", background='lightgrey')
    det_streams_s.place(x=290, y=128)
    streams_input_s = Label(details_frame_s, text="----", bg='lightgrey')
    streams_input_s.place(x=380, y=128)

    # student fee showing box
    info_show_s = LabelFrame(info_frame_s, bd=2)
    info_show_s.place(x=1, y=180, width=700, height=285)

    # scroll bar for the box
    scroll_bar_x_s = Scrollbar(info_show_s, orient=HORIZONTAL)
    scroll_bar_y_s = Scrollbar(info_show_s, orient=VERTICAL)
    table_s = ttk.Treeview(info_show_s, column=("sno", "moth", "email"),
                           xscrollcommand=scroll_bar_x_s, yscrollcommand=scroll_bar_y_s)
    scroll_bar_x_s.pack(side=BOTTOM, fill=X)
    scroll_bar_y_s.pack(side=RIGHT, fill=Y)
    scroll_bar_x_s.config(command=table_s.xview)
    scroll_bar_y_s.config(command=table_s.yview)

    # to show heading
    table_s.heading("sno", text="S.no")
    table_s.heading("moth", text="Month")
    table_s.heading("email", text="Email")

    table_s["show"] = "headings"

    # show column width
    table_s.column('sno', width=50)
    table_s.column('moth', width=600)
    table_s.column('email', width=300)
    table_s.pack(fill=BOTH, expand=1)


# ******************************************** Teacher column *******************************************
def teach():
    frame3_t = Frame(root, relief="ridge", bd=4, bg='green')
    frame3_t.place(x=200, y=100, width=1080, height=600)

    # information adding frame
    add_col_t = LabelFrame(frame3_t, text="Add Teacher Details", bd=2, font='consolas 14 bold', fg='red',
                           bg="lightgrey")
    add_col_t.place(x=5, y=4, width=350, height=560)

    # teacher name
    add_name_t = Label(add_col_t, text="Teacher Name : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_name_t.grid(row=0, column=0, sticky='w')
    add_entry1_t = ttk.Entry(add_col_t, width=30, textvariable=t_name)
    add_entry1_t.grid(row=0, column=1)

    # teacher id number
    add_id_t = Label(add_col_t, text="Teacher Id No. : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_id_t.grid(row=1, column=0, sticky='w')
    add_entry2_t = ttk.Entry(add_col_t, width=30, textvariable=t_id)
    add_entry2_t.grid(row=1, column=1)

    # teacher father name
    add_father_t = Label(add_col_t, text="Fathers Name : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_father_t.grid(row=2, column=0, sticky='w')
    add_entry3_t = ttk.Entry(add_col_t, width=30, textvariable=t_father)
    add_entry3_t.grid(row=2, column=1)

    # teacher mother name
    add_mother_t = Label(add_col_t, text="Mother Name : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_mother_t.grid(row=3, column=0, sticky='w')
    add_entry4_t = ttk.Entry(add_col_t, width=30, textvariable=t_mother)
    add_entry4_t.grid(row=3, column=1)

    # teacher contact number
    add_contact_t = Label(add_col_t, text="Contact Number : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_contact_t.grid(row=4, column=0, sticky='w')
    add_entry5_t = ttk.Entry(add_col_t, width=30, textvariable=t_contact)
    add_entry5_t.grid(row=4, column=1)

    # teacher address
    add_address_t = Label(add_col_t, text="Address : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_address_t.grid(row=5, column=0, sticky='w')
    add_entry6_t = ttk.Entry(add_col_t, width=30, textvariable=t_address)
    add_entry6_t.grid(row=5, column=1)

    # teacher email address
    add_email_t = Label(add_col_t, text="Email : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_email_t.grid(row=6, column=0, sticky='w')
    add_entry7_t = ttk.Entry(add_col_t, width=30, textvariable=t_email)
    add_entry7_t.grid(row=6, column=1)

    # teacher joining date
    add_date_t = Label(add_col_t, text="Joining date : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_date_t.grid(row=7, column=0, sticky='w')

    join_date_frame = Frame(add_col_t, bg='lightgrey')
    join_date_frame.place(x=126, y=214, width=185, height=22)
    entry_date_t = ttk.Combobox(join_date_frame, font="lucida 10", width=3, state='readonly', textvariable=t_j_date)
    entry_date_t["value"] = ([i for i in range(1, 32)])
    entry_date_t.current(0)
    entry_date_t.grid(row=0, column=0, padx=2)
    entry_month_t = ttk.Combobox(join_date_frame, font="lucida 10", width=8, state='readonly', textvariable=t_j_month)
    entry_month_t["value"] = ('January', 'February', 'March', 'April' 'May', 'June', 'July', 'August', 'September',
                              'October', 'November', 'December')
    entry_month_t.current(0)
    entry_month_t.grid(row=0, column=1, padx=2)
    entry_year_t = ttk.Combobox(join_date_frame, font="lucida 10", width=4, state='readonly', textvariable=t_j_year)
    entry_year_t["value"] = ([j for j in range(2000, 2050)])
    entry_year_t.current(0)
    entry_year_t.grid(row=0, column=2, padx=2)

    # teacher blood group
    add_blood_group_t = Label(add_col_t, text="Blood Group : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_blood_group_t.grid(row=8, column=0, sticky='w')
    entry_blood1_t = ttk.Combobox(add_col_t, font="lucida 10", width=23, state='readonly', textvariable=t_blood)
    entry_blood1_t["value"] = ('B+', 'O+', 'AB', 'AB+', 'O-')
    entry_blood1_t.current(0)
    entry_blood1_t.grid(row=8, column=1)

    # teacher education
    add_edu_t = Label(add_col_t, text="Education : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_edu_t.grid(row=9, column=0, sticky='w')
    entry_edu_t = ttk.Entry(add_col_t, font="lucida 10", width=25, textvariable=t_education)
    entry_edu_t.grid(row=9, column=1)

    # teacher Gender
    add_gender_t = Label(add_col_t, text="Gender : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_gender_t.grid(row=10, column=0, sticky='w')
    entry_gender_t = ttk.Combobox(add_col_t, font="lucida 10", width=23, state='readonly', textvariable=t_gender)
    entry_gender_t["value"] = ('Male', 'Female', 'Other')
    entry_gender_t.current(0)
    entry_gender_t.grid(row=10, column=1)

    # teacher date of birth
    add_birth_t = Label(add_col_t, text="DOB : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_birth_t.grid(row=11, column=0, sticky='w')

    dob_date_frame_t = Frame(add_col_t, bg='lightgrey')
    dob_date_frame_t.place(x=126, y=337, width=185, height=22)
    entry_dob_date_t = ttk.Combobox(dob_date_frame_t, font="lucida 10", width=3, state='readonly', textvariable=t_date)
    entry_dob_date_t["value"] = ([i for i in range(1, 32)])
    entry_dob_date_t.current(0)
    entry_dob_date_t.grid(row=0, column=0, padx=2)
    entry_dob_month_t = ttk.Combobox(dob_date_frame_t, font="lucida 10", width=8, state='readonly', textvariable=t_month)
    entry_dob_month_t["value"] = ('January', 'February', 'March', 'April' 'May', 'June', 'July', 'August',
                                  'September', 'October', 'November', 'December')
    entry_dob_month_t.current(0)
    entry_dob_month_t.grid(row=0, column=1, padx=2)
    entry_dob_year_t = ttk.Combobox(dob_date_frame_t, font="lucida 10", width=4, state='readonly', textvariable=t_year)
    entry_dob_year_t["value"] = ([j for j in range(2000, 2050)])
    entry_dob_year_t.current(0)
    entry_dob_year_t.grid(row=0, column=2, padx=2)

    # ******************************** teacher button ********************************
    frame4_t = Frame(add_col_t, relief=FLAT, bg="lightgrey")
    frame4_t.place(x=0, y=490, width=350, height=60)

    # teacher information saving button
    save_button_t = Button(frame4_t,command=saving_t, text="Save", width=10, height=1, font="lucida 12 bold", bg='red', fg="goldenrod")
    save_button_t.grid(row=0, column=0, padx=3)

    # teacher information editing button
    edit_button_t = Button(frame4_t, command=editing_t, text="Edit", width=10, height=1, font="lucida 12 bold", bg='red', fg="goldenrod")
    edit_button_t.grid(row=0, column=2, padx=3)

    # teacher information deleting button
    delete_button_t = Button(frame4_t, command=deleting_t, text="Delete", width=10, height=1, font="lucida 12 bold", bg='red',
                             fg="goldenrod")
    delete_button_t.grid(row=0, column=3, padx=3)

    # ***********************************teacher search information button ***********************************

    ser_info_t = LabelFrame(frame3_t, text='Search Teacher Information', fg='red', font="consolas 12", bg='lightgrey')
    ser_info_t.place(x=360, y=4, width=710, height=80)

    # teacher name for search
    teacher_name = Label(ser_info_t, text='Teacher Name : ', font="lucida 10 bold", bg='lightgrey')
    teacher_name.grid(row=0, column=0, padx=10)
    entry_teacher1 = ttk.Entry(ser_info_t, width=20, font="lucida")
    entry_teacher1.grid(row=1, column=0, padx=10)

    # teacher id number for search
    teacher_admin = Label(ser_info_t, text='Id No. : ', font="lucida 10 bold", bg='lightgrey')
    teacher_admin.grid(row=0, column=1, padx=10)
    entry_teacher2 = ttk.Entry(ser_info_t, width=15, font="lucida")
    entry_teacher2.grid(row=1, column=1, padx=10)

    # search button
    search_button = Button(ser_info_t, command=searching_t, width=18, height=1, bg="red", fg='goldenrod', text='Search',
                           font="lucida 12 bold")
    search_button.grid(row=1, column=2, padx=10)

    # ************************** showing teacher info *****************************

    info_fame_t = Frame(frame3_t, bd=5, relief=RIDGE)
    info_fame_t.place(x=360, y=89, width=710, height=475)

    # details frame
    det_frame_t = Frame(info_fame_t, relief=RIDGE, bg='lightgrey')
    det_frame_t.place(x=0, y=0, width=699, height=180)

    # image frame
    img_frame_t = Frame(det_frame_t, relief=RIDGE, bd=5)
    img_frame_t.place(x=580, y=0, width=119, height=150)

    # teacher image details
    img_button_t = Button(det_frame_t, command=image_input_t, text="Select Image", bd=3, bg='goldenrod', fg='red', font="lucida 8 bold")
    img_button_t.place(x=580, y=152, width=119)

    # teacher name
    det_name_t = Label(det_frame_t, text="Teacher Name : ", background='lightgrey')
    det_name_t.place(x=0, y=0)
    name_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    name_input_t.place(x=90, y=0)

    # teacher father name
    det_father_t = Label(det_frame_t, text="Father Name : ", background='lightgrey')
    det_father_t.place(x=0, y=30)
    father_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    father_input_t.place(x=90, y=30)

    # teacher mother name
    det_mother_t = Label(det_frame_t, text="Mother Name : ", background='lightgrey')
    det_mother_t.place(x=0, y=60)
    mother_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    mother_input_t.place(x=90, y=60)

    # teacher education
    det_edu_t = Label(det_frame_t, text="Education : ", background='lightgrey')
    det_edu_t.place(x=0, y=90)
    edu_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    edu_input_t.place(x=70, y=90)

    # teacher date of birth
    det_dob_t = Label(det_frame_t, text="DOB : ", background='lightgrey')
    det_dob_t.place(x=0, y=120)
    dob_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    dob_input_t.place(x=50, y=120)

    # teacher address
    det_address_t = Label(det_frame_t, text="Address : ", background='lightgrey')
    det_address_t.place(x=0, y=150)
    address_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    address_input_t.place(x=60, y=150)

    # next side
    # teacher id number
    det_id_t = Label(det_frame_t, text="Id No : ", background='lightgrey')
    det_id_t.place(x=290, y=0)
    id_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    id_input_t.place(x=380, y=0)

    # teacher blood group
    det_blood_t = Label(det_frame_t, text="Blood Group : ", background='lightgrey')
    det_blood_t.place(x=290, y=30)
    blood_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    blood_input_t.place(x=380, y=30)

    # teacher contact
    det_cont_t = Label(det_frame_t, text="Contact No. : ", background='lightgrey')
    det_cont_t.place(x=290, y=60)
    cont_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    cont_input_t.place(x=380, y=60)

    # teacher joining date      (details)
    det_joining_date_t = Label(det_frame_t, text="Joining date : ", background='lightgrey')
    det_joining_date_t.place(x=290, y=90)
    det_cast_t = Label(det_frame_t, text="----", bg='lightgrey')
    det_cast_t.place(x=380, y=90)

    # teacher Gender
    det_gender_t = Label(det_frame_t, text="Gender : ", background='lightgrey')
    det_gender_t.place(x=290, y=120)
    gender_input_t = Label(det_frame_t, text="----", bg='lightgrey')
    gender_input_t.place(x=380, y=120)

    # information showing box
    info_t = LabelFrame(det_frame_t, bd=2)
    info_t.place(x=1, y=180, width=700, height=285)

    # scroll bar
    scroll_bar_x_t = Scrollbar(info_t, orient=HORIZONTAL)
    scroll_bar_y_t = Scrollbar(info_t, orient=VERTICAL)
    table_t = ttk.Treeview(info_t, column=("sno", "moth", "email"),
                           xscrollcommand=scroll_bar_x_t, yscrollcommand=scroll_bar_y_t)
    scroll_bar_x_t.pack(side=BOTTOM, fill=X)
    scroll_bar_y_t.pack(side=RIGHT, fill=Y)
    scroll_bar_x_t.config(command=table_t.xview)
    scroll_bar_y_t.config(command=table_t.yview)


# *********************************************** workers column ***************************************
def stf():
    frame5_w = Frame(root, relief="ridge", bd=4, bg='orange')
    frame5_w.place(x=200, y=100, width=1080, height=600)

    # ************** workers column *************
    add_col_w = LabelFrame(frame5_w, text="Add Worker Details", bd=2, font='consolas 14 bold', fg='red',
                           bg="lightgrey")
    add_col_w.place(x=5, y=4, width=350, height=560)

    # workers name
    add_name_w = Label(add_col_w, text="Worker Name : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_name_w.grid(row=0, column=0, sticky='w')
    add_entry1_w = ttk.Entry(add_col_w, width=30, textvariable=w_name)
    add_entry1_w.grid(row=0, column=1)

    # workers id number
    add_id_w = Label(add_col_w, text="Worker Id No. : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_id_w.grid(row=1, column=0, sticky='w')
    add_entry2_w = ttk.Entry(add_col_w, width=30, textvariable=w_id)
    add_entry2_w.grid(row=1, column=1)

    # workers father name
    add_father_w = Label(add_col_w, text="Fathers Name : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_father_w.grid(row=2, column=0, sticky='w')
    add_entry3_w = ttk.Entry(add_col_w, width=30, textvariable=w_father)
    add_entry3_w.grid(row=2, column=1)

    # workers mother name
    add_mother_w = Label(add_col_w, text="Mother Name : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_mother_w.grid(row=3, column=0, sticky='w')
    add_entry4_w = ttk.Entry(add_col_w, width=30, textvariable=w_mother)
    add_entry4_w.grid(row=3, column=1)

    # workers contact number
    add_contact_w = Label(add_col_w, text="Contact Number : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_contact_w.grid(row=4, column=0, sticky='w')
    add_entry5_w = ttk.Entry(add_col_w, width=30, textvariable=w_contact)
    add_entry5_w.grid(row=4, column=1)

    # workers address
    add_address_w = Label(add_col_w, text="Address : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_address_w.grid(row=5, column=0, sticky='w')
    add_entry6_w = ttk.Entry(add_col_w, width=30, textvariable=w_address)
    add_entry6_w.grid(row=5, column=1)

    # workers address
    add_email_w = Label(add_col_w, text="Email : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_email_w.grid(row=6, column=0, sticky='w')
    add_entry7_w = ttk.Entry(add_col_w, width=30, textvariable=w_email)
    add_entry7_w.grid(row=6, column=1)

    #   workers joining date
    add_date_w = Label(add_col_w, text="Joining date : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_date_w.grid(row=7, column=0, sticky='w')

    join_date_frame_w = Frame(add_col_w, bg='lightgrey')
    join_date_frame_w.place(x=126, y=214, width=185, height=22)
    entry_date_w = ttk.Combobox(join_date_frame_w, font="lucida 10", width=3, state='readonly', textvariable=w_j_date)
    entry_date_w["value"] = ([i for i in range(1, 32)])
    entry_date_w.current(0)
    entry_date_w.grid(row=0, column=0, padx=2)
    entry_month_w = ttk.Combobox(join_date_frame_w, font="lucida 10", width=8, state='readonly', textvariable=w_j_month)
    entry_month_w["value"] = ('January', 'February', 'March', 'April' 'May', 'June', 'July', 'August', 'September',
                              'October', 'November', 'December')
    entry_month_w.current(0)
    entry_month_w.grid(row=0, column=1, padx=2)
    entry_year_w = ttk.Combobox(join_date_frame_w, font="lucida 10", width=4, state='readonly', textvariable=w_j_year)
    entry_year_w["value"] = ([j for j in range(2000, 2050)])
    entry_year_w.current(0)
    entry_year_w.grid(row=0, column=2, padx=2)

    # workers blood group
    add_blood_group_w = Label(add_col_w, text="Blood Group : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_blood_group_w.grid(row=8, column=0, sticky='w')
    entry_blood1_w = ttk.Combobox(add_col_w, font="lucida 10", width=23, state='readonly', textvariable=w_blood)
    entry_blood1_w["value"] = ('B+', 'O+', 'AB', 'AB+', 'O-')
    entry_blood1_w.current(0)
    entry_blood1_w.grid(row=8, column=1)

    # workers Gender
    add_gender_w = Label(add_col_w, text="Gender : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_gender_w.grid(row=9, column=0, sticky='w')
    entry_gender_w = ttk.Combobox(add_col_w, font="lucida 10", width=23, state='readonly', textvariable=w_gender)
    entry_gender_w["value"] = ('Male', 'Female', 'Other')
    entry_gender_w.current(0)
    entry_gender_w.grid(row=9, column=1)

    # worker date of birth
    add_birth_w = Label(add_col_w, text="DOB : ", font="lucida 10 bold", pady=5, padx=4, bg="lightgrey")
    add_birth_w.grid(row=10, column=0, sticky='w')

    dob_date_frame_w = Frame(add_col_w, bg='lightgrey')
    dob_date_frame_w.place(x=126, y=307, width=185, height=22)
    entry_dob_date_w = ttk.Combobox(dob_date_frame_w, font="lucida 10", width=3, state='readonly', textvariable=w_date)
    entry_dob_date_w["value"] = ([i for i in range(1, 32)])
    entry_dob_date_w.current(0)
    entry_dob_date_w.grid(row=0, column=0, padx=2)
    entry_dob_month_w = ttk.Combobox(dob_date_frame_w, font="lucida 10", width=8, state='readonly', textvariable=w_month)
    entry_dob_month_w["value"] = ('January', 'February', 'March', 'April' 'May', 'June', 'July', 'August',
                                  'September', 'October', 'November', 'December')
    entry_dob_month_w.current(0)
    entry_dob_month_w.grid(row=0, column=1, padx=2)
    entry_dob_year_w = ttk.Combobox(dob_date_frame_w, font="lucida 10", width=4, state='readonly', textvariable=w_year)
    entry_dob_year_w["value"] = ([j for j in range(2000, 2050)])
    entry_dob_year_w.current(0)
    entry_dob_year_w.grid(row=0, column=2, padx=2)

    # ******************************** worker Info button ********************************
    frame6_w = Frame(add_col_w, relief=FLAT, bg="lightgrey")
    frame6_w.place(x=0, y=490, width=350, height=60)

    # info adding button
    but_save_w = Button(frame6_w, command=saving_w, text="Save", width=10, height=1, font="lucida 12 bold", bg='red', fg="goldenrod")
    but_save_w.grid(row=0, column=0, padx=3)

    # info edit button
    but_edit_w = Button(frame6_w, command=editing_w, text="Edit", width=10, height=1, font="lucida 12 bold", bg='red', fg="goldenrod")
    but_edit_w.grid(row=0, column=2, padx=3)

    # info delete button
    but_delete_w = Button(frame6_w, command=deleting_w, text="Delete", width=10, height=1, font="lucida 12 bold", bg='red', fg="goldenrod")
    but_delete_w.grid(row=0, column=3, padx=3)

    # *********************************** workers search ***********************************

    ser_w = LabelFrame(frame5_w, text='Search Student Information', fg='red', font="consolas 12", bg='lightgrey')
    ser_w.place(x=360, y=4, width=710, height=80)

    # worker name foe search
    worker_name = Label(ser_w, text='Worker Name : ', font="lucida 10 bold", bg='lightgrey')
    worker_name.grid(row=0, column=0, padx=10)
    entry_worker1 = ttk.Entry(ser_w, width=20, font="lucida")
    entry_worker1.grid(row=1, column=0, padx=10)

    # worker id number for search
    worker_id = Label(ser_w, text='Id No. : ', font="lucida 10 bold", bg='lightgrey')
    worker_id.grid(row=0, column=1, padx=10)
    entry_worker2 = ttk.Entry(ser_w, width=15, font="lucida")
    entry_worker2.grid(row=1, column=1, padx=10)

    # search button
    ser_button_w = Button(ser_w, command=searching_w, width=18, height=1, bg="red", fg='goldenrod', text='Search', font="lucida 12 bold")
    ser_button_w.grid(row=1, column=2, padx=10)

    # ******************************** worker information details *****************************
    in_fame_w = Frame(frame5_w, bd=5, relief=RIDGE)
    in_fame_w.place(x=360, y=89, width=710, height=475)

    # details frame
    det_frame_w = Frame(in_fame_w, relief=RIDGE, bg='lightgrey')
    det_frame_w.place(x=0, y=0, width=699, height=180)

    # image frame
    img_frame_w = Frame(det_frame_w, relief=RIDGE, bd=5)
    img_frame_w.place(x=580, y=0, width=119, height=150)

    # workers image details
    img_button_w = Button(det_frame_w, command=image_input_w, text="Select Image", bd=3, bg='goldenrod', fg='red', font="lucida 8 bold")
    img_button_w.place(x=580, y=152, width=119)

    # workers name
    det_name_w = Label(det_frame_w, text="Worker Name : ", background='lightgrey')
    det_name_w.place(x=0, y=0)
    det_name_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_name_w.place(x=90, y=0)

    # workers father name
    det_father_w = Label(det_frame_w, text="Father Name : ", background='lightgrey')
    det_father_w.place(x=0, y=30)
    det_father_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_father_w.place(x=90, y=30)

    # workers mother name
    det_mother_w = Label(det_frame_w, text="Mother Name : ", background='lightgrey')
    det_mother_w.place(x=0, y=60)
    det_mother_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_mother_w.place(x=90, y=60)

    # worker date of birth
    det_dob_w = Label(det_frame_w, text="DOB : ", background='lightgrey')
    det_dob_w.place(x=0, y=90)
    det_dob_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_dob_w.place(x=70, y=90)

    # worker Gender
    det_gender_w = Label(det_frame_w, text="Gender : ", background='lightgrey')
    det_gender_w.place(x=0, y=120)
    det_gender_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_gender_w.place(x=70, y=120)

    # worker address
    det_address_w = Label(det_frame_w, text="Address : ", background='lightgrey')
    det_address_w.place(x=0, y=150)
    det_address_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_address_w.place(x=70, y=150)

    # next side
    # worker admission number
    det_id_w = Label(det_frame_w, text="Id No : ", background='lightgrey')
    det_id_w.place(x=290, y=0)
    det_id_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_id_w.place(x=380, y=0)

    # worker blood group
    det_blood_w = Label(det_frame_w, text="Blood Group : ", background='lightgrey')
    det_blood_w.place(x=290, y=30)
    det_blood_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_blood_w.place(x=380, y=30)

    # worker contact
    det_cont_w = Label(det_frame_w, text="Contact No. : ", background='lightgrey')
    det_cont_w.place(x=290, y=60)
    det_cont_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_cont_w.place(x=380, y=60)

    # worker Cast details
    det_joining_date_w = Label(det_frame_w, text="Joining date : ", background='lightgrey')
    det_joining_date_w.place(x=290, y=90)
    det_cast_w = Label(det_frame_w, text="----", bg='lightgrey')
    det_cast_w.place(x=380, y=90)

    # search box info
    info_w = LabelFrame(in_fame_w, bd=2)
    info_w.place(x=1, y=180, width=700, height=285)

    # scroll bar
    scroll_bar_x_w = Scrollbar(info_w, orient=HORIZONTAL)
    scroll_bar_y_w = Scrollbar(info_w, orient=VERTICAL)
    table_w = ttk.Treeview(info_w, column=("sno", "moth", "email"),
                           xscrollcommand=scroll_bar_x_w, yscrollcommand=scroll_bar_y_w)
    scroll_bar_x_w.pack(side=BOTTOM, fill=X)
    scroll_bar_y_w.pack(side=RIGHT, fill=Y)
    scroll_bar_x_w.config(command=table_w.xview)
    scroll_bar_y_w.config(command=table_w.yview)


# **************** Menu Bar *********************
my_menu = Menu(root)

inside_menu = Menu(my_menu, tearoff=0)
inside_menu.add_command(label="Teacher Info")
inside_menu.add_command(label="Student Info")
root.config(menu=my_menu)
my_menu.add_cascade(label="File", menu=inside_menu)

# second menu option
my_menu.add_command(label="Student Info")
root.config(menu=my_menu)

# ***************** First Frame for image display ***************
frame1 = Frame(root, bd=2, relief="ridge")
frame1.place(x=0, y=0, width=200, height=100)
# # image = Image.open("download.jpeg")
# image = image.resize((130, 100), Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(image)
# label = Label(frame1, image=photo)
# label.pack()

# ****************** display the school name *********************
frame2 = Frame(root, borderwidth=5, relief="ridge")
frame2.place(x=200, y=0, width=1080, height=100)
label1 = Label(frame2, text="Bhowmik Resort", font="lucida 52 bold", fg="goldenrod", bg="red")
label1.pack(fill="x")

# free frame
# ima = Frame(root, relief="ridge")
# ima.place(x=200, y=100, width=1080, height=800)
# image = Image.open("abc.jpg")
# image = image.resize((1080, 600), Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(image)
# label = Label(ima, image=photo)
# label.pack()

# ********************* Left Side frame ******************
frame3 = Frame(root, relief="ridge", bg="#0f111a")
frame3.place(x=0, y=100, width=200, height=800)

# class changing button
button_cls = Button(frame3, text="Change class", width=20, height=2, bg="blue", fg="powderblue", borderwidth=3,
                    font='lucida 12 bold', command=change)
button_cls.grid(row=0, column=0)

# bills button
button_bill = Button(frame3, text="Bills", width=20, height=2, bg="red", fg="goldenrod", borderwidth=3,
                     command=billing, font='lucida 12 bold')
button_bill.grid(row=1, column=0)

# student button
button_std = Button(frame3, text="Student", width=20, height=2, bg="red", fg="goldenrod", borderwidth=3,
                    font='lucida 12 bold', command=student)
button_std.grid(row=2, column=0)

# teacher button
button_tea = Button(frame3, text="Teacher", width=20, height=2, bg="red", fg="goldenrod", borderwidth=3,
                    command=teach, font='lucida 12 bold')
button_tea.grid(row=3, column=0)

# workers button
button_staff = Button(frame3, text="Workers", width=20, height=2, bg="red", fg="goldenrod", borderwidth=3,
                      command=stf, font='lucida 12 bold')
button_staff.grid(row=4, column=0)

# check button
check_button = Button(frame3, text='check', width=20, height=2, command=check, font=('lucida', 12, 'bold'))
check_button.grid(row=5, column=0)


root.mainloop()
