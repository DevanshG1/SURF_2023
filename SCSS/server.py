import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
import matplotlib.animation as animation
import numpy as np

class server:
    figure=None
    state=0
    def __init__(self, name):
        self.name=name
    
    def attach_figure(self,Circle):
        self.figure=Circle
    def set_state(self,state):
        self.state=state
    