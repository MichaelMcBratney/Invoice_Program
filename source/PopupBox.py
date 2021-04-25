import tkinter as tk


class PopupBox:
    def __init__(self):
        self.btn_txt = ""
        self.root = tk.Tk()

        self.w = 400
        self.h = 300

        self.ws = self.root.winfo_screenwidth()  # width of the screen
        self.hs = self.root.winfo_screenheight()  # height of the screen

        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)

        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

        self.label1 = tk.Label(self.root, text='Enter the Category:'
                                               '(CS, DG, M, PR, etc.')
        self.canvas1 = tk.Canvas(self.root, width=self.w, height=self.h)
        self.canvas1.pack()

        self.entry1 = tk.Entry(self.root)
        self.entry1.bind("<Return>", (lambda event: self.check_cat()))
        self.entry1.pack(side=tk.TOP)

    def set_active(self):
        self.root.lift()
        self.root.focus_force()
        self.root.grab_set()
        self.root.grab_release()

    def check_cat(self):
        x1 = self.entry1.get()
        self.btn_txt = x1
        self.root.destroy()

    def make_window(self, decr):

        label1 = tk.Label(text="Enter a category for:\n" + decr + ":\n(CS, DG, M, PR, Etc..")
        cat = button1 = tk.Button(text='Enter Category:', command=self.check_cat)
        self.root.title("Invoice Prog")

        btn = tk.Button(self.root, text="Enter Category", command=(lambda: self.check_cat()))
        btn.pack(side=tk.LEFT)

        self.canvas1.create_window(200, 180, window=button1)
        self.canvas1.create_window(200, 100, window=label1)
        self.canvas1.create_window(200, 140, window=self.entry1)

        self.set_active()

        self.entry1.focus()

        self.root.mainloop()
        return self.btn_txt
