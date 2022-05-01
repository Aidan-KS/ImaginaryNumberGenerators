# Code by Aidan Kirby-Smith

# imports 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button

def createComplexNumber(re,img):

    # Create the complex number
    num = complex(float(re), float(img))
    print("------------------------------------------------")
    print("                 Infomation")
    print("  Absolute Value of starting number:", abs(num))
    print("------------------------------------------------")
    return num

def createSequence(num,power):
    sequence = []
    for x in range(1,int(power)+1):
        newNum = pow(num,x)
        sequence.append(newNum)
    return sequence

def getCords(sequenceList):
    x = []
    y = []
    for z in sequenceList:
        x.append(z.real)
        y.append(z.imag)
    return x,y

def main(numPower):
    # Create sub plot
    fig, ax = plt.subplots()

    limit=10
    plt.xlim((-limit,limit))
    plt.ylim((-limit,limit))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.axhline(y=0,color='black')
    plt.axvline(x=0, color='black')
    
    l, = plt.plot((1,2,3,4), (1,2,3,4), color='red', marker='.', linestyle='-', linewidth=2, markersize=12)
    
    # Create Space at the bottom
    plt.subplots_adjust(bottom=0.35)
    
    # Reset labels 
    plt.axes([0, 10, 0, 10])
    
    # Slider1
    axSlider1 = plt.axes([0.1, 0.2, 0.8, 0.1])
    slider1 = Slider(axSlider1, 'RE', valmin=-3, valmax=3, valinit=0)
    
    # Slider2
    axSlider2 = plt.axes([0.1, 0.1, 0.8, 0.1])
    slider2 = Slider(axSlider2, 'IMG', valmin=-3, valmax=3, valinit=0)
    
    
    def update(val):
        num = createComplexNumber(slider1.val, slider2.val)
        sequenceList = createSequence(num,numPower)
        xvalues, yvalues = getCords(sequenceList)
        l.set_xdata(xvalues)
        l.set_ydata(yvalues)
        print("Last Value in the sequence",xvalues[-1], " ",yvalues[-1],"i")
        
    
    slider1.on_changed(update)
    slider2.on_changed(update)
    
    plt.show()

    



if __name__ == "__main__":
    numPower = input("Power raised: ")
    main(numPower)

    






# def plotData(x,y):
#     # Create sub plot
#     fig, ax = plt.subplots()
    
#     limit=10
#     plt.xlim((-limit,limit))
#     plt.ylim((-limit,limit))
#     plt.ylabel('Imaginary')
#     plt.xlabel('Real')
#     plt.axhline(y=0,color='black')
#     plt.axvline(x=0, color='black')

    
#     # Create Space at the bottom
#     plt.subplots_adjust(bottom=0.35)
    
#     # Reset labels 
#     plt.axes([0, 10, 0, 10])
    
#     # Plot
#     line, = plt.plot(x, y)
    
#     # Slider
#     axSlider1 = plt.axes([0.1, 0.2, 0.8, 0.1])
#     slider1 = Slider(axSlider1, 'RE', valmin=-3, valmax=3, valinit=0)
    
    
#     axSlider2 = plt.axes([0.1, 0.1, 0.8, 0.1])
#     slider2 = Slider(axSlider2, 'IMG', valmin=-3, valmax=3, valinit=0)
    
#     # The function to be called anytime a slider's value changes
#     def update(val):
#         line.set_xdata()
#         line.set_ydata()
#         fig.canvas.draw_idle()


#     # register the update function with each slider
#     slider1.on_changed(update)
#     slider2.on_changed(update)
    
#     plt.show()
