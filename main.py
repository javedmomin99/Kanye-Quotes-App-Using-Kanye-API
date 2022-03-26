import tkinter
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    #print(quote)
    canvas.itemconfig(quote_text, text=quote)
    
window = tkinter.Tk()
window.title("Kanye Says...")
window.config(padx=10, pady=10)

canvas = tkinter.Canvas(width=500, height=500)
background_img = tkinter.PhotoImage(file="background.png")
canvas.create_image(250, 250, image=background_img)
quote_text = canvas.create_text(250, 250, text="Kanye Quote Goes HERE", width=290, font=("Arial", 20, "bold"), fill="black")
#250,250 are width and height of text created and width = 290 is width of screen
canvas.grid(row=0, column=0)

kanye_img = tkinter.PhotoImage(file="kanye.png")
kanye_button = tkinter.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()