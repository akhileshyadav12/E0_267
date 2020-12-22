from typing import Deque
import numpy
import ga
import matplotlib.pyplot as plt
import threading
import animation
import queue
import fit
num_generations=10
qx=queue.Queue()
qy=queue.Queue()

anim=threading.Thread(target=fit.calW,args=(qx,qy,num_generations))
anim.start()
animation.animf(qx,qy,num_generations)
anim.join()
