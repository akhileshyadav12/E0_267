#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animf(qx,qy,num_generations):
    fig = plt.figure()
    #creating a subplot 
    ax1 = fig.add_subplot(1,1,1)
    xs=[]
    ys=[]
    def animate(i):
        data = open('stock.txt','r').read()
        lines = data.split('\n')
        xs.append(qx.get())
        ys.append(qy.get())
    
        
        #ax1.clear()
        ax1.plot(xs, ys)


        plt.xlabel('iteration')
        plt.ylabel('Value')
        plt.title('Live graph with matplotlib')	
        if num_generations==len(xs):
            print("complete")
            plt.close()
            return
        
        
    ani = animation.FuncAnimation(fig, animate,interval=1) 
    plt.show()
    print("from chiled")
if __name__=='__main__':

    animf(1,2)