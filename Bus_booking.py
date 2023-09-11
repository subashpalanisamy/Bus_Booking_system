from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class BusBooking(Tk):

    def __init__(self):
        super().__init__()

        self.title("BUS BOOKING")
        self.geometry("600x650")
        self.config(bg="pink")

        
        self.login_screen()

    def update_pickup_points(self, *args):
        pickups = pickup_points[self.origin_var.get()]
        self.pickup_var.set('---Select---')
        self.pickup_menu['values'] = pickups

    def update_drop_points(self, *args):
        drops = drop_points[self.dest_var.get()]
        self.drop_var.set('---Select---')
        self.drop_menu['values'] = drops

    def update_price_range(self, *args):
        prices = price_ranges.get(self.drop_var.get(), [])
        self.price_var.set('---Select---')
        self.price_menu['values'] = prices

    def login_screen(self):
        
        for widget in self.winfo_children():
            widget.destroy()

        
        Label(self, text="LOGIN", bg="pink", font=("calibri", 16)).pack(pady=20)
        Label(self, text="Username", bg="pink").pack(pady=10)
        self.username_var = StringVar()
        Entry(self, textvariable=self.username_var).pack(pady=10)

        Label(self, text="Password", bg="pink").pack(pady=10)
        self.password_var = StringVar()
        Entry(self, textvariable=self.password_var, show='*').pack(pady=10)

        Label(self, text="Phone Number", bg="pink").pack(pady=10)
        self.phone_var = StringVar()
        Entry(self, textvariable=self.phone_var).pack(pady=10)

        Button(self, text="Login", command=self.bus_booking_screen).pack(pady=20)

    def bus_booking_screen(self):
        
        for widget in self.winfo_children():
            widget.destroy()

        
        Label(self, text="BUS BOOKING SYSTEM", bg="pink", font=("calibri", 16)).pack(pady=20)

        
        Label(self, text="From",bg="pink", font=("calibri", 12)).place(x=175,y=100)
        self.origin_var = StringVar()
        self.origin_var.trace('w', self.update_pickup_points,)
        ttk.Combobox(self, textvariable=self.origin_var, values=cities).place(x=350,y=95)

        
        Label(self, text="Pick UP Point", bg="pink", font=("calibri", 12)).place(x=175,y=150)
        self.pickup_var = StringVar()
        self.pickup_menu = ttk.Combobox(self, textvariable=self.pickup_var)
        self.pickup_menu.place(x=350,y=150)

        
        Label(self, text="To", bg="pink", font=("calibri", 12)).place(x=175,y=200)
        self.dest_var = StringVar()
        self.dest_var.trace('w', self.update_drop_points)
        ttk.Combobox(self, textvariable=self.dest_var, values=cities).place(x=350,y=200)

        
        Label(self, text="Dropping Point", bg="pink", font=("calibri", 12)).place(x=175,y=250)
        self.drop_var = StringVar()
        self.drop_var.trace('w', self.update_price_range)
        self.drop_menu = ttk.Combobox(self, textvariable=self.drop_var)
        self.drop_menu.place(x=350,y=250)

       
        Label(self, text="Price Range", bg="pink", font=("calibri", 12)).place(x=175,y=300)
        self.price_var = StringVar()
        self.price_menu = ttk.Combobox(self, textvariable=self.price_var)
        self.price_menu.place(x=350,y=300)

        
        Button(self, text="Proceed to Seat Selection", command=self.seat_selection_screen).place(x=215, y=400)  
        
    def seat_selection_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

        Label(self, text="SEAT SELECTION", bg="pink", font=("calibri", 16)).pack(pady=20)
        Label(self,text="seat 1 to 8 sleeper and 9 to 20 sitter",bg="pink").pack(pady=20)
        self.selected_seats = set()  

        
        seat_frame = Frame(self, bg="pink")
        seat_frame.pack(pady=20)

        self.seat_buttons = {}  

        
        for row in range(5):
            for col in range(4):
                seat_num = row * 4 + col + 1
                btn  = Button(seat_frame, text=str(seat_num), command=lambda s=seat_num: self.select_seat(s))
                btn.grid(row=col, column=row, padx=5, pady=5)
                self.seat_buttons[seat_num] = btn
        
        Button(self, text="Confirm Seats", command=self.book_seat).pack(pady=30)
        

    def select_seat(self, seat_num):
        if seat_num in self.selected_seats:
            self.seat_buttons[seat_num].config(bg="SystemButtonFace")  
            self.selected_seats.remove(seat_num)
        else:
            self.seat_buttons[seat_num].config(bg="blue")
            self.selected_seats.add(seat_num)

    def book_seat(self):
        origin = self.origin_var.get()
        pickup = self.pickup_var.get()
        dest = self.dest_var.get()
        drop = self.drop_var.get()
        price = self.price_var.get()

        if not origin or not pickup or not dest or not drop or not price:
            messagebox.showerror("Error", "Please select all the options.")
            return

        self.seat_numbers = ", ".join(map(str, self.selected_seats))
        messagebox.showinfo("Booking Successful", f"You've booked from {pickup} ({origin}) to {drop} ({dest}) for the price {price}!")

        self.show_receipt(pickup, origin, drop, dest, price)

    def show_receipt(self, pickup, origin, drop, dest, price):
        
        for widget in self.winfo_children():
            widget.destroy()

    

        Label(self, text="RECEIPT", bg="pink", font=("calibri", 16)).pack(pady=20)
        Label(self, text=f"Username: {self.username_var.get()}", bg="pink").pack(pady=10)
        Label(self, text=f"Phone: {self.phone_var.get()}", bg="pink").pack(pady=10)
        Label(self, text=f"From: {pickup} ({origin})", bg="pink").pack(pady=10)
        Label(self, text=f"To: {drop} ({dest})", bg="pink").pack(pady=10)
        Label(self, text=f"Price: {price}", bg="pink").pack(pady=10)
        Label(self, text=f"seat_number: {self.seat_numbers}", bg="pink").pack(pady=10)
        Button(self, text="Home", command=self.bus_booking_screen).pack(pady=20)
        Button(self, text="Close", command=self.destroy).pack(pady=20)
    

if __name__ == "__main__":
    cities = ['Chennai', 'Coimbatore', 'Ooty']
    pickup_points = {
        'Chennai': ['koyambedu', 'Tambaram'],
        'Coimbatore': ['singanallur', 'Gandhipuram'],
        'Ooty': ['Ooty', 'Coonoor']
    }
    drop_points = pickup_points
    price_ranges = {
        'koyambedu': ['sitter:Rs.400', 'sleeper:Rs.800'],
        'Tambaram': ['sitter:Rs.400', 'sleeper:Rs.800'],
        'singanallur': ['sitter:Rs.400', 'sleeper:Rs.800'],
        'Gandhipuram': ['sitter:Rs.400', 'sleeper:Rs.800'],
        'Ooty': ['sitter:Rs.400', 'sleeper:Rs.800'],
        'Coonoor': ['sitter:Rs.400', 'sleeper:Rs.800']
    }

app = BusBooking()
app.mainloop()
