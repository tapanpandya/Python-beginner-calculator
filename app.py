from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expressiom
# in the text entry box
def press(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		result.set(total)
		equation.set("")

		# initialze the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


root = Tk()

root.geometry("400x325+200+100")
# StringVar() is the variable class
# we create an instance of this class
equation = StringVar()
result = StringVar()
# Creating frames to divide and creating sections
f1 = Frame(root)
f1.pack()

f2 = Frame(root)
f2.pack()

f3 = Frame(root)
f3.pack()

app_name = Label(f1, text="Basic Calculator")
app_name.config(font=("Courier", 25))
app_name.pack()

#Creating Entry for values and Entry for Answer
query = Entry(f2, textvariable=equation, bd=3, font=("Courier", 19), width=25)
answer = Entry(f2, textvariable=result, bd=3, font=("Courier", 19), width=25, state=DISABLED)
query.grid(row=0, column=0)
answer.grid(row=1, column=0)


# Creating Buttons
seven = Button(f3, text="7", command=lambda: press(7), font=("Courier", 20), height = "1", width = "4")
eight = Button(f3, text="8", command=lambda: press(8), font=("Courier", 20), height = "1", width = "4")
nine = Button(f3, text="9", command=lambda: press(9), font=("Courier", 20), height = "1", width = "4")
divide = Button(f3, text="/", command=lambda: press("/"), font=("Courier", 20), height = "1", width = "4", bg="gray")
four = Button(f3, text="4", command=lambda: press(4), font=("Courier", 20), height = "1", width = "4")
five = Button(f3, text="5", command=lambda: press(5), font=("Courier", 20), height = "1", width = "4")
six = Button(f3, text="6", command=lambda: press(6), font=("Courier", 20), height = "1", width = "4")
multiply = Button(f3, text="*", command=lambda: press("*"), font=("Courier", 20), height = "1", width = "4", bg="gray")
one = Button(f3, text="1", command=lambda: press(1), font=("Courier", 20), height = "1", width = "4")
two = Button(f3, text="2", command=lambda: press(2), font=("Courier", 20), height = "1", width = "4")
three = Button(f3, text="3", command=lambda: press(3), font=("Courier", 20), height = "1", width = "4")
minus = Button(f3, text="-", command=lambda: press("-"), font=("Courier", 20), height = "1", width = "4", bg="gray")
zero = Button(f3, text="0", command=lambda: press(0), font=("Courier", 20), height = "1", width = "4")
point = Button(f3, text=".", command=lambda: press("."), font=("Courier", 20), height = "1", width = "4")
equal = Button(f3, text="=", command=equalpress, font=("Courier", 20), height = "1", width = "4", bg="blue")
plus = Button(f3, text="+", command=lambda: press("+"), font=("Courier", 20), height = "1", width = "4", bg="gray")

seven.grid(row=0, column=0, padx=3, pady=3)
eight.grid(row=0, column=1, padx=3, pady=3)
nine.grid(row=0, column=2, padx=3, pady=3)
divide.grid(row=0, column=3, padx=3, pady=3)
four.grid(row=1, column=0, padx=3, pady=3)
five.grid(row=1, column=1, padx=3, pady=3)
six.grid(row=1, column=2, padx=3, pady=3)
multiply.grid(row=1, column=3, padx=3, pady=3)
one.grid(row=2, column=0, padx=3, pady=3)
two.grid(row=2, column=1, padx=3, pady=3)
three.grid(row=2, column=2, padx=3, pady=3)
minus.grid(row=2, column=3, padx=3, pady=3)
zero.grid(row=3, column=0, padx=3, pady=3)
point.grid(row=3, column=1, padx=3, pady=3)
equal.grid(row=3, column=2, padx=3, pady=3)
plus.grid(row=3, column=3, padx=3, pady=3)

root.mainloop()
