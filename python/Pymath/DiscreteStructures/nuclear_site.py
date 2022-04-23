import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')


def graph(event=None):
    tmptext = entry.get()
    tmptext = "$"+tmptext+"$"

    ax.clear()
    ax.text(0.2, 0.6, tmptext, fontsize=50)
    canvas.draw()


root = tk.Tk()

mainframe = tk.Frame(root)
mainframe.pack()

entry = tk.Entry(mainframe, width=70)
entry.pack()

label = tk.Label(mainframe)
label.pack()

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=label)
canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
canvas._tkcanvas.pack(side="top", fill="both", expand=True)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

entry.insert(0, r"\sum_{i=0}^\infty x_i \frac{y_i}{z_i}")
graph()

root.bind("<Return>", graph)
root.mainloop()
