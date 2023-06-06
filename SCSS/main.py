import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
import matplotlib.animation as animation
import numpy as np
import server
import client
import networklink
import visualize

server1= server.server("s1")
client1= client.client("c1")
networklink=networklink.networklink(client1, server1)
visualize.visualize(networklink)