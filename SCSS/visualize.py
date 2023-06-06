import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
import matplotlib.animation as animation
import numpy as np

def visualize(networklink):
    fig, ax = plt.subplots()
    ax.axis('off')
    temp1 = networklink.body1
    temp2 = networklink.body2
    temp1.attach_figure(patches.Circle((0.2, 0.5), radius=0.1, edgecolor='black', facecolor='white'))
    temp2.attach_figure(patches.Circle((0.6, 0.5), radius=0.1, edgecolor='black', facecolor='white'))
    line = lines.Line2D([temp1.figure.center[0] + 0.1, temp2.figure.center[0] - 0.1],
                       [temp1.figure.center[1], temp2.figure.center[1]], color="black")
    ax.add_patch(temp1.figure)
    ax.add_patch(temp2.figure)
    ax.add_line(line)
    text = temp1.name
    plt.text(temp1.figure.center[0], temp1.figure.center[1], text, ha='center', va='center', fontsize=12)
    text = temp2.name
    plt.text(temp2.figure.center[0], temp2.figure.center[1], text, ha='center', va='center', fontsize=12)

    
    def update(frame, temp1, temp2):
        temp_state=frame%4
        if temp1.state == 0:
            temp1.figure.set_facecolor("white")
            temp2.figure.set_facecolor("white")
            line.set_color("black")
        if temp1.state == 1:
            temp1.figure.set_facecolor("red")
            if(temp2.state==0):
                line.set_color("red")
            if(temp2.state==1):
                line.set_color("black")
                temp2.figure.set_facecolor("red")
            if(temp2.state==2):
                temp2.figure.set_facecolor("green")
                print(1)
            if(temp2.state==3):
                line.set_color("green")
                temp1.set_state(3)
                print(2)
            temp2.set_state((temp2.state+1)%4)
        if temp1.state==0:
            temp1.set_state(max(1,min(1,temp_state)))
        if temp1.state == 3:
            temp1.figure.set_facecolor("green")
            temp1.set_state(0)
            temp2.set_state(0)

    anime = animation.FuncAnimation(fig, update, fargs=(temp1, temp2), frames=100, interval=800, repeat=True)
    plt.show()
