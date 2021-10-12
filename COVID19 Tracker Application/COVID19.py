from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = Tk()
root.iconphoto(False, tk.PhotoImage(file='b.png'))

root.geometry("750x550")
root.title("Covid-19 Country Status")
root['background'] = 'LIGHTSTEELBLUE'
canvas = Canvas(width=596, height=296)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("z.jpg"))
canvas.create_image(1, 1, anchor=NW, image=img)


def showdata():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid
    covid = Covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    try:
        root.update()
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")

        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
        for y in cases:
            confirmed.append(y["confirmed"])
            active.append(y["active"])
            deaths.append(y["deaths"])
            recovered.append(y["recovered"])

        confirmed_patch = mpatches.Patch(color='black', label='Confirmed')
        recovered_patch = mpatches.Patch(color='green', label='Recovered')
        active_patch = mpatches.Patch(color='red', label='Active')
        deaths_patch = mpatches.Patch(color='orange', label='Deaths')
        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])

        for x in range(len(country_names)):
            plt.bar(country_names[x], confirmed[x], color='black')
            if recovered[x] > active[x]:
                plt.bar(country_names[x], recovered[x], color='green')
                plt.bar(country_names[x], active[x], color='red')
            else:
                plt.bar(country_names[x], active[x], color='red')
                plt.bar(country_names[x], recovered, color='green')
        plt.bar(country_names[x], deaths[x], color='orange')
        plt.title('Current Covid Cases')
        plt.xlabel('Country Name')
        plt.ylabel('cases(in Millions)')
        plt.show()
    except Exception as e:
        print("Enter Correct Details")


Label(root, text="Enter the name of the Country\nto get its Covid-19 Data", font="Consolas 15 bold",
      bg='LIGHTSTEELBLUE').pack()
Label(root, text="\n Enter Country Name", font="Consolas 16 bold", bg='LIGHTSTEELBLUE').pack()
data = StringVar()
data.set("")
entry = Entry(root, textvariable=data, font="calibre 20 normal", width=30).pack()
Label(root, bg='LIGHTSTEELBLUE').pack()
Button(root, text="Get Data", font="Consolas 15 bold", height=2, width=10, command=showdata).pack()

root.mainloop()