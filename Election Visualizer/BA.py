from Vdd import Process as Process
import Vdd
import networkx as nx

class Bully:
    dead=[]
    def __init__(self,n,dead):
        self.net = n
        self.processes = [Process(i) for i in range(n)]
        self.defunct=list(dead)
        for i in self.processes:
            if i.id in self.defunct:
                self.dead.append(i)
        self.vis=Vdd.visualizer(n,defunct=self.dead)

        # for i in self.defunct:
        #     i.setwork(); 
    
    def election(self,discover,count =1):
        respond=list()
        while(True):
            respond.clear
            print('-'*50)
            print("Process id "+str(discover.getID())+" will hold election: "+str(count))
            self.vis.Add_Discoverer(discover)

            # count = 1
            index = discover.getID()
            respond = list()          
            for i in range(index+1,self.net):
                print("Process "+str(index)+" is sending a message to process "+str(i)+".")
                self.vis.add_link(self.processes[index],self.processes[i])
            
            for i in range(index+1,self.net):
                if i not in self.defunct:
                    respond.append(i)
                    print("Process "+str(i)+" is responding.")

            if len(respond) == 0:
                print("Process "+str(index)+" is the new coordinator.")
                self.vis.Add_Coordinater(discover)
                self.vis.visualize(self.processes)
                # for i in range(self.net):
                #     print("Sending message to all other processes")
                return
            discover=Process(respond[0])
            count+=1

            
n = int(input("Enter the total number of processes: "))
dead = input("Please enter the list of defunct processes: ").split()
dead = [int(id) for id in dead]

m = int(input("Who discovers the failed coordinator: "))

bully = Bully(n, dead)
bully.election(Process(m))