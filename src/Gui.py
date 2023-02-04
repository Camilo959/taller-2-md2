from Lectura import *
from Dijsktra import *
from Floyd import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# Clase muestra la ventana con la información de los grafos.
class Gui:
    def __init__(self):
        self.content = "" 
        self.graph_content = ""

    def config(self, gui):
        self.gui = gui
        self.gui.title("Graphs")
        self.gui.geometry("556x480")
        self.gui.config(bg="green")
        self.font = ("titilitum web", 15, "bold")

        self.general_frame = Frame(gui)
        self.general_frame.config(relief="sunken", bd=25, cursor="")
        self.general_frame.pack(fill="both", expand="yes", padx=10, pady=10)

    def start_gui(self):
        self.window = Tk()
        self.config(self.window)
        self.window.geometry("350x300")
        self.init_components()
        self.window.mainloop()

    def init_components(self):
        self.btn_send = Button(self.general_frame, text="Buscar", command=self.search_file)
        self.btn_send.place(x=75, y=80, height=58, width=120)
        self.btn_send.configure(font=self.font)

        self.lbl_search = Label(self.general_frame, text="Graph search")
        self.lbl_search.place(x=65, y=30 ,width=150 ,height=25)
        self.lbl_search.configure(font=self.font)

    def search_file(self):
        route = filedialog.askopenfilename(initialdir="Grafos",title="Select",filetypes = (
            ("text files", "*.txt"),
            ("All files", ".")))

        objLectura = Lectura()
        self.graph_content = objLectura.read_weighted_graph(route)
        
        self.graph_gui()

    def graph_gui(self):
        self.ventana_2 = Tk()
        self.config(self.ventana_2)
        self.init_gui2_components()
        self.ventana_2.mainloop()

    def init_gui2_components(self):
        self.font = ("Arial", 15, "bold")

        self.entry_graph = Text(self.general_frame,width=50, height=10)
        self.entry_graph.place(x=47, y=20)
        self.entry_graph.delete("1.0", "end")
        self.entry_graph.insert("insert", str(self.graph_content))

        self.lbl_start = Label(self.general_frame, text="Start")
        self.lbl_start.place(x=25, y=210 ,width=50 ,height=25)
        self.lbl_start.configure(font=self.font)

        self.lbl_end = Label(self.general_frame, text="End")
        self.lbl_end.place(x=25, y=260 ,width=50 ,height=25)
        self.lbl_end.configure(font=self.font)

        self.lbd_find = Label(self.general_frame, text="Find Path")
        self.lbd_find.place(x=300, y=205 ,width=100 ,height=25)
        self.lbd_find.configure(font=self.font)

        self.entry_start = Entry(self.general_frame)
        self.entry_start.place(x=80, y=200, width=100, height=45)
        self.entry_start.delete(0, END)

        self.entry_end = Entry(self.general_frame)
        self.entry_end.place(x=80, y=260, width=100, height=45)
        self.entry_end.delete(0, END)

        self.btn_dijkstra = Button(self.general_frame, text="Dijsktra",command=self.djikstra_algorithm)
        self.btn_dijkstra.place(x=240, y=260, width=80, height=40)
        self.btn_dijkstra.configure(font=self.font)     

        self.btn_floyd = Button(self.general_frame, text="Floyd",command=self.floyd_algorithm)
        self.btn_floyd.place(x=360, y=260, width=80, height=40)
        self.btn_floyd.configure(font=self.font)     

        self.btn_exit = Button(self.general_frame, text="Exit",command=self.close_window)
        self.btn_exit.place(x=360, y=320, width=80, height=40)
        self.btn_exit.configure(font=self.font)

    def djikstra_algorithm(self):

        start = self.entry_start.get()
        end = self.entry_end.get()

        try: 
            start_dijkstra = Dijkstra()
            information = start_dijkstra.dijkstra(self.graph_content, start, end)
            menssage_graph = "The shortest path from " + start + " to " + end + " is: " + str(information)
            messagebox.showinfo(message=menssage_graph, title="Dijkstra")
        except:
            messagebox.showerror(message="Enter valid vertices")

    def floyd_algorithm(self):

        start = self.entry_start.get()
        end = self.entry_end.get()

        try:
            start_floyd = Floyd()

            distances = start_floyd.floyd(self.graph_content)

            shortest_path = start_floyd.get_shortest_path(distances, start, end)

            message_graph = "The shortest path from " + start + " to " + end + " is: " + str(shortest_path)
            messagebox.showinfo(message=message_graph, title="Floyd")
        except:
            messagebox.showerror(message="Enter valid vertices")

    def close_window(self):
       self.general_frame.destroy()