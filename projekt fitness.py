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
        self.register = Tk()
        self.register.title("Registration")
        
        
        self.name = Label(self.register, text="register", font=("Arial", 20))
        self.Registration = Button(self.register, text="register", width=15, command = self.register)
        self.login = Button(self.register, text="Already have an account? Login here", width=30, command = self.)
        

        self.Email = Label(self.register, text="Email:")
        self.Password = Label(self.register, text="Password:")
        self.Passwordrep = Label(self.register, text="Repeat Password:")
        self.email2 = Entry(self.register)
        self.password2 = Entry(self.register, show="*")  
        self.passwordrep2 = Entry(self.register, show="*")  
        

        self.name.grid(row=0, column=1, pady=10)
        self.Registration.grid(row=5, column=1, pady=10)
        self.login.grid(row=6, column=1, pady=10)
        
        self.Email.grid(row=2, column=0, padx=10)
        self.Password.grid(row=4, column=0, padx=10)
        self.passwordrep2.grid(row=4, column=0, padx=10)

        self.email2.grid(row=2, column=1, padx=10, pady=5)
        self.password2.grid(row=4, column=1, padx=10, pady=5)
        self.passwordrep2.grid(row=4, column=0, padx=10)
        register.title("Register")
        
        conn = sqlite3.connect('table.db')
        connection.execute(''' CREATE TABLE mydatabase
         FIND INT PRIMARY KEY,
         Name TEXT NOT NULL,
         weight  INT  NOT NULL,
         height    INT; age INT NOT NULL''')
         
        


        self.register.mainloop()

    def reset(self):
        self.fenster.destroy()


Fitness()
