import tkinter as tk
import smtplib

class MailApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mail Application")

        self.label_to = tk.Label(self.window, text="To:")
        self.label_to.grid(row=0, column=0)

        self.entry_to = tk.Entry(self.window)
        self.entry_to.grid(row=0, column=1)

        self.label_subject = tk.Label(self.window, text="Subject:")
        self.label_subject.grid(row=1, column=0)

        self.entry_subject = tk.Entry(self.window)
        self.entry_subject.grid(row=1, column=1)

        self.label_body = tk.Label(self.window, text="Body:")
        self.label_body.grid(row=2, column=0)

        self.entry_body = tk.Text(self.window, height=10, width=50)
        self.entry_body.grid(row=2, column=1)

        self.button_send = tk.Button(self.window, text="Send", command=self.send_mail)
        self.button_send.grid(row=3, column=1)

        self.window.mainloop()

    def send_mail(self):
        recipient = self.entry_to.get()
        subject = self.entry_subject.get()
        body = self.entry_body.get("1.0", tk.END)

        try:
            # create SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("sender_email_address", "sender_email_password")

            # message to be sent
            message = f"Subject: {subject}\n\n{body}"

            # sending the mail
            s.sendmail("sender_email_address", recipient, message)

            # terminating the session
            s.quit()

            tk.messagebox.showinfo("Success", "Mail sent successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

mail_app = MailApp()
