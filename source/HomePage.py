import tkinter as tk
import tkinter.filedialog


class HomePage:
    def __init__(self):
        self.root = tk.Tk()

        self.label1 = tk.Label(self.root, text='Welcome to the invoice program.'
                                               'Please upload your files.')

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

    def on_input_file_button_clicked(self):
        path = tk.filedialog.askopenfilenames(title="Open File")
        for i in path:
            print(i)
        self.all_files = path

    def on_output_file_button_clicked(self):
        path = tkinter.filedialog.askdirectory()
        self.outputDir = path

    def make_window(self):

        label1 = tk.Label(text="Please Upload your files.")
        label2 = tk.Label(text="Choose Files:")
        label3 = tk.Label(text="Output Folder:")
        input_file_button = button1 = tk.Button(text="...", command=self.on_input_file_button_clicked)
        output_folder_button = button2 = tk.Button(text="...", command=self.on_output_file_button_clicked)
        next_btn = button3 = tk.Button(text="Next", command=self.btn_press)
        self.root.title("Invoice Program")
        self.canvas1.create_window(250, 105, window=button1)
        self.canvas1.create_window(250, 145, window=button2)
        self.canvas1.create_window(200, 195, window=button3)
        self.canvas1.create_window(200, 65, window=label1)
        self.canvas1.create_window(190, 105, window=label2)
        self.canvas1.create_window(190, 145, window=label3)

        self.root.mainloop()

    def get_paths(self):
        try:
            return self.all_files
        except:
            return 0

    def get_dir(self):
        return self.outputDir