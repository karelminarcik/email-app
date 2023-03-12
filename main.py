import smtplib
from tkinter import *


# Funkce
def send_mail():
    my_email = sender_entry.get()
    password = password_entry.get()
    to_email = receiver_entry.get()
    message = text_entry.get(1.0, END)
    subject = subject_entry.get()

    with smtplib.SMTP(host="imap.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=f"{my_email}", password=f"{password}")
        connection.sendmail(from_addr=f"{my_email}",
                            to_addrs=f"{to_email}",
                            msg=(f"Subject:{subject}\n\n{message}").encode("utf-8")
                            )
    # deletion of subject and text entry
    text_entry.delete(1.0,END)
    subject_entry.delete(0, END)
# Window
window = Tk()
window.minsize(400, 400)
window.title("Email Client")
window.config(bg="#0A807A")
window.resizable(False, False)
window.iconbitmap("email.ico")

# Framy

input_frame = Frame(window, bg="#0A807A")
text_frame = Frame(window, bg="#0A807A")
button_frame = Frame(window, bg="#0A807A")
input_frame.pack(pady=5)
button_frame.pack(pady=5)
text_frame.pack(pady=5)


# Labels

sender_label = Label(input_frame, text="From address:", width=20, bg="#0A807A", font=("Arial", 12))
sender_label.grid(row=0,column=0, pady=10)

sender_entry = Entry(input_frame, width=25, bg="#CAEDE2", font=("Arial", 12))
sender_entry.grid(row=0,column=1, pady=10, padx=10)

password_label = Label(input_frame, text="Password:", width=20, bg="#0A807A", font=("Arial", 12))
password_label.grid(row=1,column=0, pady=10)

password_entry = Entry(input_frame,show="*", width=25, bg="#CAEDE2", font=("Arial", 12))
password_entry.grid(row=1,column=1, pady=10, padx=10)

receiver_label = Label(input_frame, text="To address:", width=20, bg="#0A807A", font=("Arial", 12))
receiver_label.grid(row=2,column=0, pady=10)

receiver_entry = Entry(input_frame, width=25, bg="#CAEDE2", font=("Arial", 12))
receiver_entry.grid(row=2,column=1, pady=10, padx=10)

text_label = Label(button_frame, text="Text of your email:", width=20, bg="#0A807A", font=("Arial", 12))
text_label.grid(row=2,column=0, pady=10)

subject_label = Label(button_frame, text="Subject:", width=20, bg="#0A807A", font=("Arial", 12))
subject_label.grid(row=3,column=0, pady=10)

subject_entry = Entry(button_frame, width=25, bg="#CAEDE2", font=("Arial", 12))
subject_entry.grid(row=3,column=1, pady=10, padx=10)

text_entry = Text(text_frame, width=46, height=10, bg="#CAEDE2", font=("Arial", 12))
text_entry.grid(row=4,column=0, pady=10)

# button
send_button = Button(button_frame, text="Send", bg="#CAEDE2", font=("Arial", 12), command=send_mail)
send_button.grid(row=2, column=1, padx=10, ipady=5,ipadx=10)

# main loop
window.mainloop()


