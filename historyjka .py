from tkinter import *
from tkinter import filedialog
calls = []
calls_counter = 0
def open_file():
    path = filedialog.askopenfilenames(initialdir="/", title="wybierz plik")
    for lines in path:
        file_path = lines
        result = open(file_path)
        file_postion1 = file_path.index(".py")
        file_postion2 = file_path.rindex("/")
        file_name = file_path[file_postion2+1 : file_postion1+3]
        for c in result:
            safe_tab = c.split()
            is_quotation = 0
            for i in safe_tab:
                if '"' in (i) and is_quotation == 0:
                    is_quotation = 1
                elif '"' in (i) and is_quotation == 1:
                    is_quotation = 0
                if is_quotation == 0:
                    if i == "import" or i == "import*":
                        global calls_counter
                        if "from" in c:
                            position1 = c.find(i)
                            position2 = c.find("from")
                            calls.append(
                                [file_name, c[position2 + len("from "):position1]])  # dodanie nazwy pliku to tablicy
                            calls_counter = calls_counter + 1
                        else:
                            position1 = c.find(i)
                            position2 = len(c)
                            calls.append(
                                [file_name, c[position1 + len(i):position2 - 1]])  # dodanie nazwy pliku to tablicy
                            calls_counter = calls_counter + 1
                    if i == "using" or i == "include" or i == "open" or "open(" in i:
                        # global calls_counter
                        position1 = c.find(i)
                        position2 = len(c)
                        calls.append([file_name, c[position1 + len(i):position2 - 1]])  # dodanie nazwy pliku to tablicy
                        calls_counter = calls_counter + 1
                    if "#" in (i):
                        break
        for i in range(0, calls_counter):
            print("wywolanie numer ", i + 1, "zawiera: ", calls[i])
def graph():
    print ("A tu bedzie stal nasz graf")
def exit() :
    sys.exit()
root = Tk()
button_open = Button(root, text="wczytaj plik", command=open_file)
button_graph=Button(root, text="graf", command=graph)
button_exit= Button(root, text="koniec", command=exit)
button_open.pack()
button_exit.pack()
button_graph.pack()
root.mainloop()
