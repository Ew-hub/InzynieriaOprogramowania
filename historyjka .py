import matplotlib as mpl
import networkx as nx
from tkinter import *
from tkinter import filedialog
calls = []
calls_counter = 0
def open_file():

   result =  filedialog.askopenfile(initialdir="/", title="wybierz plik", filetypes=(("text files", ".txt"), ("all files", "*.*")))
   print(result)
   safe_tab = [] #tablica która przechowuje poszczególne wyrazy z każdej linijki using
   for c in result:
        safe_tab = c.split()
        is_quotation = 0
        for i in safe_tab:
            if '"' in (i) and is_quotation == 0:
                is_quotation = 1
            elif '"' in (i) and is_quotation == 1:
                is_quotation = 0
            if is_quotation == 0:
                if i == "import" or i == "using" or i == "include" or i == "open":
                    global calls_counter
                    calls.append(c) #dodanie linijki w której jest dodawany plik to tablicy
                    calls_counter = calls_counter + 1
                if "#" in (i):
                    break
   for i in range (0, calls_counter):
       print("wywolanie numer ", i + 1, "zawiera: ", calls[i])

def exit() :
    sys.exit()
root = Tk()
button = Button(root, text="wczytaj plik", command=open_file)
button1= Button(root, text="koniec", command=exit)
button.pack()
button1.pack()
root.mainloop()

def DiGraphs(relationshipMap):
    G = nx.DiGraph()
    G.add_nodes_from(relationshipMap.items())
    pairNode = []

    for k, v in relationshipMap.items():
        for key, value in v.items():
            G.add_edges_from([(k, key)], weight=value)
            pairNode.append((k, key))

    pairWeight =dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color = 'black', node_size = 250)
    nx.draw_networkx_labels(G, pos)

    nx.draw_networkx_edges(G, pos, edgelist=pairNode, edge_color='blue', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pairWeight)
    plt.savefig("graph.png")
    plt.show()
