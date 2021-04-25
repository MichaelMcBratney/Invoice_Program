import tkinter as tk


class EndPage:

    def __init__(self):
        self.root = tk.Tk()
        self.label1 = tk.Label(self.root, text='Done!')

        self.w = 400
        self.h = 300

        self.ws = self.root.winfo_screenwidth()  # width of the screen
        self.hs = self.root.winfo_screenheight()  # height of the screen

        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)

        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

        self.canvas1 = tk.Canvas(self.root, width=self.w, height=self.h)
        self.canvas1.pack()
        self.canvas1.create_window(200, 140, window=self.label1)

    def btn_press(self):
        self.root.destroy()

    def make_window(self):

        label1 = tk.Label(text="Done!")
        next_btn = button3 = tk.Button(text="Quit", command=self.btn_press)
        self.root.title("Invoice Program")
        self.canvas1.create_window(200, 195, window=button3)
        self.canvas1.create_window(200, 100, window=label1)
        self.root.mainloop()