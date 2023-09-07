import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import csv

fp_x = "X.csv"
X = []
with open(fp_x, mode="r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        temp = []
        for column in row:
            temp.append(float(column))

        X.append(temp)

fp_y = "Y.csv"
Y = []
with open(fp_y, mode="r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        temp = []
        for column in row:
            temp.append(int(column))

        Y.append(temp)

mayor = 0
for x in X:
    for y in x:
        if y > mayor: 
            mayor = y 


fig, ax = plt.subplots()

carro_1 = ax.plot(X[0][0], Y[0][0], color= "green")[0]
carro_2 = ax.plot(X[8][0], Y[8][0], color= "blue")[0]
carro_3 = ax.plot(X[8][0], Y[8][0], color= "red")[0]
carro_4 = ax.plot(X[8][0], Y[8][0], color= "yellow")[0]
carro_5 = ax.plot(X[8][0], Y[8][0], color= "black")[0]
carro_6 = ax.plot(X[8][0], Y[8][0], color= "magenta")[0]
carro_7 = ax.plot(X[8][0], Y[8][0], color= "cyan")[0]
carro_8 = ax.plot(X[8][0], Y[8][0], color= "purple")[0]
carro_9 = ax.plot(X[8][0], Y[8][0], color= "gray")[0]
carro_10 = ax.plot(X[8][0], Y[8][0], color= "pink")[0]

carros = [carro_1, carro_2, carro_3, carro_4, carro_5, carro_6, carro_7, carro_8, carro_9, carro_10]

ax.set(ylim = [-1, 5])
ax.set(xlim = [0, mayor])

print(type(carro_1))


def update(frame):
    # for each frame, update the data stored on each artist.

    for i, c in enumerate(carros):

        x = X[i][:frame]
        y = Y[i][:frame]
        c.set_xdata(x)
        c.set_ydata(y)

    # update the carro_1 plot:

    return (carro_1)


ani = animation.FuncAnimation(fig=fig, func=update, frames=30, interval=100)
plt.show()