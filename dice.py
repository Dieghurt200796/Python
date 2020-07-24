import ctypes, random, tkinter as tk, tkinter.messagebox

class DiceRollerGUI:
    def __init__(self):
        user32 = ctypes.windll.user32
        self.screen_width = user32.GetSystemMetrics(0)
        self.screen_height = user32.GetSystemMetrics(1)
        
        self.window = tk.Tk()
        #self.window_size = "400x150"
        #self.window.geometry(self.window_size)
        self.window.wm_title("Dice roller")
        self.font = ("comic sans ms", 20)
        

        self.lbl_welcome = self.create_widget(tk.Label, self.window, text='Welcome to the Dice Rolling Program', font=True, position=(1,0,10,10))
        self.btn_start = self.create_widget(tk.Button, self.window, text='Start', command=self.when_pressed, font=True, position=(2, 0, 10, 10))

        self.lbl_sides = self.create_widget(tk.Label, self.window, text='How many sides do you want your dice to have?', font=True)
        self.frm_roller = self.create_widget(tk.Frame, self.window)
        self.ent_sides = self.create_widget(tk.Entry, self.frm_roller, font=True, position=(2, 2, 5, 0))
        self.btn_roll_dice = self.create_widget(tk.Button, self.frm_roller, text = 'Roll dice', command = self.roll_dice, font=True, position=(2, 3, 5, 0))
        self.lbl_result = self.create_widget(tk.Label, self.window, text = '', font=True)

        # region self.lbl_welcome = tk.Label(self.window, text="Welcome to the dice rolling program")
        # self.set_font(self.lbl_welcome)
        # self.lbl_welcome.grid(row=1, padx=10, pady=10)
        # self.btn_start = tk.Button(self.window, text='Start', command=self.when_pressed)
        # self.btn_start.grid(row=2, padx=10, 
        # endregion self.set_font(self.btn_start)


    #           i can hear you can you hear me?

    def create_widget(self, widget, master, text=None, command=None, font=False, position=None):
        created_widget = widget(master=master, text=text, command = command)
        if font == False:
            pass
        elif font == True:
            self.set_font(created_widget)
        if type(position) == tuple:
            self.display_widget(created_widget,position)
        return created_widget
    def display_widget(self,widget,position):
        widget.grid(row=position[0],column=position[1],padx=position[2],pady=position[3])

    def set_font(self, widget):
        widget.config(font=self.font)


    def roll_dice(self):
        number = int(self.ent_sides.get())
        if number > 1:
            random_number = random.randint(1,number)
            self.display_result(random_number)
        elif number < -1:
            random_number = random.randint(number, -1)
            self.display_result(random_number)
        else:
            tkinter.messagebox.showwarning("Invalid number", "Number must be greater than 1 or less than -1.")

    def display_result(self, number):
        self.lbl_result["text"] = str(number)

#     how do we make it forget last number?

    def when_pressed(self):
        self.lbl_welcome.grid_remove()
        self.btn_start.grid_remove()

        self.display_widget(self.lbl_sides, (1, 0, 10, 10))
        self.display_widget(self.frm_roller, (2, 0, 10, 10))
        self.display_widget(self.lbl_result, (3, 0, 10, 10))

        



    def run(self):

        self.window.mainloop()

GUI = DiceRollerGUI()
GUI.run()
