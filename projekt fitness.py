from tkinter import Tk, Label, Button, Entry
from tkinter import messagebox
class Fitness:
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title("Fitness App")
        
        
        self.name = Label(self.fenster, text="Stepup", font=("Arial", 20))
        self.Login = Button(self.fenster, text="Login", width=15, command = self.login)
        self.register = Button(self.fenster, text="Dont have an account? Register here", width=30, command = self.gotoregister)
        

        self.Email = Label(self.fenster, text="Email:")
        self.Password = Label(self.fenster, text="Password:")
        self.email1 = Entry(self.fenster)
        self.password1 = Entry(self.fenster, show="*")  
        

        self.name.grid(row=0, column=1, pady=10)
        self.Login.grid(row=5, column=1, pady=10)
        self.register.grid(row=6, column=1, pady=10)
        
        self.Email.grid(row=2, column=0, padx=10)
        self.Password.grid(row=4, column=0, padx=10)
        
        self.email1.grid(row=2, column=1, padx=10, pady=5)
        self.password1.grid(row=4, column=1, padx=10, pady=5)
        
    def login(self):
        
        if self.email1.get() == "izbushkatv@gmail.com" and self.password1.get() == "123456789":
            print("login successful")
            messagebox.showinfo("Login Status", "Login successful")
            self.fenster.destroy()
            main = Tk()
            
        else:
            email1.delete(0, 'end')
            password1.delete(0, 'end')
            messagebox.showerror("Login Status", "login unsuccessful")
        
            
    def gotoregister(self):
        self.fenster.destroy()
        register = Tk()
        register.title("Register")
        

        self.fenster.mainloop()

    def reset(self):
        self.fenster.destroy()


Fitness()
