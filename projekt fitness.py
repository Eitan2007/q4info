from tkinter import Tk, Label, Button, Entry
from tkinter import messagebox
from sqlite3 import *
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
            self.email1.delete(0, 'end')
            self.password1.delete(0, 'end')
            messagebox.showerror("Login Status", "login unsuccessful")
        
            
    def gotoregister(self):
        self.fenster.destroy()

        register = Tk()
        self.register = Tk()
        self.register.title("Registration")
        
        
        self.name = Label(self.register, text="register", font=("Arial", 20))
        self.Registration = Button(self.register, text="register", width=15, command = self.register)
        self.login = Button(self.register, text="Already have an account? Login here", width=30, command = self)
        

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
        connection.execute(''' CREATE TABLE mydatabase FIND INT PRIMARY KEY, Name TEXT NOT NULL, weight  INT  NOT NULL, eight    INT; age INT NOT NULL''')
         
        


        self.register.mainloop()

        self.register = Tk()
        self.register.title("Register")

        self.name = Label(self.register, text="Stepup", font=("Arial", 20))
        self.login1 = Button(self.register, text="Register", width=15, command = self.register)
        self.login12 = Button(self.register, text="Already have an account? Login here", width=30, command = self.gotologin)
        self.stepup = Label(self.register, text="Stepup", font=("Arial", 20))
        self.height = Label(self.register, text="Height:", font=("Arial", 20))
        self.weight = Label(self.register, text="Weight:", font=("Arial", 20))
        self.password = Label(self.register, text="password:", font=("Arial", 20))
        self.repassword = Label(self.register, text="repeat password:", font=("Arial", 20))
        self.age    = Label(self.register, text = "Age:", font = ("arial", 20))

        self.register1 = Button (self.register, text = "register",font = ("arial", 20), command= self.register)
        self.weight1 = Entry(self.register)
        self.height1 = Entry(self.register,)
        self.password2 = Entry(self.register,text = "password")
        self.password3 = Entry(self.register,text = "repeat password")
        self.email1 = Entry (self.register, text = "enter your email")
        self.email2 = Entry(self.register, text = "repeat Email")
        self.age1 = Entry(self.register, text = "Age:")

        self.name.grid(row=0, column=0)
        self.login1.grid(row=0, column=0)
        self.login12.grid(row=0, column=0)
        self.stepup.grid(row=0, column=0)
        self.height.grid(row=0, column=0)
        self.weight.grid(row=0, column=0)
        self.register1.grid(row=0, column=0)
        self.password2.grid(row=0, column=0)
        self.password2.grid(row=0, column=0)

        self.email2.grid(row=0, column=0)

        
        

        self.fenster.mainloop()
    def gotologin(self):
        self.register.destroy()
        self.fenster = Tk()

    def reset(self):
        self.fenster.destroy()

        def bmi(self):
        BMI = weight/height * 2

         def bmi(self, weight, height):
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi <= 24.9:
                return "Normal weight"
            elif 25 <= bmi <= 29.9:
                return "Overweight"
            elif 30 <= bmi <= 34.9:
                return "Obesity I"
            elif bmi >= 35:
                return "Obesity II"
            else:
                return "Invalid BMI"
        except ZeroDivisionError:
            return "Height cannot be zero"
        except ValueError:
            return "Invalid input"

    def kfa(self): 


    def register(self):

        if self.password2.get() == self.password3.get() and not self.weight1.get() or not self.email1 or not self.email2 or not self.height1.get() or not self.age1.get():
            messagebox.showinfo("Registration Status", "registered successfully")
            self.register.destroy()
            self.home = Tk()
            self.home.title("homepage")

            
        else:
            self.email1.delete(0, 'end')
            self.password1.delete(0, 'end')
            messagebox.showerror("Registration Status", "registered unsuccessfully")
        




Fitness()