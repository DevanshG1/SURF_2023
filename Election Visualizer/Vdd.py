import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Process:
    def __init__(self, id):
        self.id = id
        self.dead = False

    def getID(self):
        return self.id

    def __str__(self):
        return 'p' + str(self.id)

class visualizer:
    adjlist = {}
    pro = []
    discover = []
    coord = 0
    labels = {}
    elist = []

    def __init__(self, n, defunct):
        self.graph = nx.DiGraph()
        self.defunct = defunct
        self.n = n
        self.coord = n - 1
        self.fig, self.ax = plt.subplots(figsize=(8, 8))

    def generate_process(self, n):
        for i in range(n):
            self.pro.append(Process(i))
            self.labels[i] = i
        return self.pro

    def Add_Discoverer(self, a):
        self.discover.append(a)

    def Add_Coordinater(self, c):
        self.coord = c
        if c not in self.adjlist.keys():
            self.adjlist[c]=[]

    def add_link(self, a, b):
        self.elist.append((a, b))
        if a not in self.adjlist.keys():
            self.adjlist[a] = []
            self.adjlist[a].append(b)
        else:
            self.adjlist[a].append(b)
            self.algotype = 1
        a = a.id
        b = b.id
        self.graph.add_edge(a, b)

    def visualize(self, pro):
        if not self.pro:
            self.pro = pro
        for i in range(len(self.pro)):
            self.labels[pro[i].getID()] = pro[i].getID()
            self.graph.add_node(self.pro[i].id)

        pos = nx.circular_layout(self.graph)
        gnodes = nx.draw_networkx_nodes(self.graph, pos=pos, node_size=800, ax=self.ax, node_color='grey')
        #nx.draw_networkx_edges(self.graph, pos=pos, edge_color='black', ax=self.ax, arrows=True)
        nx.draw_networkx_labels(self.graph, pos=pos, labels=self.labels, font_color='black')
        #gnodes.set_edgecolor("black")
        temp = [i.id for i in self.defunct]
        nx.draw_networkx_nodes(self.graph, pos=pos, node_size=800, ax=self.ax, node_color='red', nodelist=temp)
        temp_dis=[]
        temp_dis.append(self.discover[0].getID())
        nx.draw_networkx_nodes(self.graph, pos=pos, node_color='Blue', node_size=800, edgecolors='black', ax=self.ax,nodelist=temp_dis)
        self.ax = plt.gca()
        x, y = pos[temp_dis[0]]
        text = 'Conducts Election'
        self.ax.text(x, y-0.1, text, horizontalalignment='center')
        plt.margins(0.1)  # Add a margin to the plot
        plt.axis('off')
        plt.tight_layout()  # Adjust the layout to fit all elements within the figure

        def update(frames):
            nonlocal self,pos
            #print(frames)
            if frames!=0:
                i=(frames//2)%len(self.discover)
                cur=self.discover[i]
                nodal_list=[]
                for j in self.discover:
                    for k in self.adjlist.keys():
                        if j.getID()==k.getID():
                            nodal_list.append(self.adjlist[k])
                if frames%2==0:
                    self.ax.clear()
                    pos = nx.circular_layout(self.graph)
                    gnodes = nx.draw_networkx_nodes(self.graph, pos=pos, node_size=800, ax=self.ax, node_color='grey')
                    #nx.draw_networkx_edges(self.graph, pos=pos, edge_color='black', ax=self.ax, arrows=True)
                    nx.draw_networkx_labels(self.graph, pos=pos, labels=self.labels, font_color='black')
                    gnodes.set_edgecolor("black")
                    temp = [i.id for i in self.defunct]
                    nx.draw_networkx_nodes(self.graph, pos=pos, node_size=800, ax=self.ax, node_color='red', nodelist=temp)
                    temp_dis=[]
                    temp_dis.append(self.discover[i].getID())
                    nx.draw_networkx_nodes(self.graph, pos=pos, node_color='Blue', node_size=800, edgecolors='black', ax=self.ax,nodelist=temp_dis)
                    self.ax = plt.gca()
                    x, y = pos[cur.getID()]
                    text = 'Conducts Election'
                    self.ax.text(x, y-0.1, text, horizontalalignment='center')
                    plt.margins(0.1)  # Add a margin to the plot
                    plt.axis('off')
                    plt.tight_layout()
                elif (frames)%2==1:
                    self.ax.clear()
                    gnodes = nx.draw_networkx_nodes(self.graph, pos=pos, node_size=800, ax=self.ax, node_color='grey')
                    if(self.coord.getID()==cur.getID()):
                        temp_nodes=[]
                        temp_nodes.append(cur.getID())
                        self.ax = plt.gca()
                        x, y = pos[cur.getID()]
                        text = 'New Coordinator'
                        self.ax.text(x, y-0.1, text, horizontalalignment='center')
                        nx.draw_networkx_nodes(self.graph, pos=pos, node_color='yellow', node_size=800, edgecolors='black', ax=self.ax,nodelist=temp_nodes)
                    else:
                        green_nodes=[j.id for j in nodal_list[i] if j not in self.defunct]
                        green_edges=[(cur.id,j.id)  for j in nodal_list[i] if j not in self.defunct]
                        nx.draw_networkx_nodes(self.graph, pos=pos, node_size=800, ax=self.ax, node_color='green', nodelist=green_nodes)
                        nx.draw_networkx_edges(self.graph, pos=pos, edge_color='green', ax=self.ax, arrows=True,edgelist=green_edges)
                        for i in green_nodes:
                            self.ax = plt.gca()
                            x, y = pos[i]
                            text = 'Receives Message\nSends a Ping'
                            self.ax.text(x, y-0.15, text, horizontalalignment='center')
                    red_nodes=[j.id for j in self.defunct]
                    nx.draw_networkx_nodes(self.graph, pos=pos, node_size=800, ax=self.ax, node_color='red', nodelist=red_nodes)
                    nx.draw_networkx_labels(self.graph, pos=pos, labels=self.labels, font_color='black')
                    plt.margins(0.1)  # Add a margin to the plot
                    plt.axis('off')
                    plt.tight_layout()
        anime=animation.FuncAnimation(self.fig,update,frames=(2*len(self.discover)),interval=1000,repeat=True)
        plt.tight_layout()
        plt.show()
