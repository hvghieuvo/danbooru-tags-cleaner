import tkinter
import customtkinter


# ======================== Function ========================

def on_closing(event=0):
    app.destroy()
        
def get_tags():
    f = open("raw_tags.txt", "w")
    print("Raw input get!")
    raw = entry_input.get()
    f.write(raw)
    f.close()
    
def deep_danbooru():
    f = open("raw_tags.txt", "r")
    output_tags = ""
    for x in f:
        if x.strip() == "General Tags":
            continue
        tag = x.split("\t")
        # print(tag[0])
        output_tags += tag[0] + ", "
    f.close()
    # print(output_tags)
    output_dan(output_tags)
    output_tags = ""

def danbooru():
    f = open("raw_tags.txt", "r")
    output_tags = ""
    tags = ""
    for x in f:
        if x.strip() == "General":
            continue
        tag = x.split(" ")
        tag.pop()
        tag.pop(0)
        for i in range(len(tag)):
            tags += str(tag[i]) + " "
        output_tags += str(tags) + ","
        tags = ""
    f.close()
    # print(output_tags)
    output_dan(output_tags)
    output_tags = ""
    
def output_dan(output_tags):
    f = open("cleaned_tags.txt", "w")
    print("Cleaned!")
    f.write(output_tags)
    entry_output.insert(0, output_tags)
    f.close()
    
def clean_button():
    get_tags()
    # radio_choice = str(radio_var.get())
    if radio_var.get() == 0:
        danbooru()
    elif radio_var.get() == 1:
        deep_danbooru()
        

# ======================== GUI ========================

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x450")
app.title("Danbooru get tags - Natakaze")
app.protocol("WM_DELETE_WINDOW", on_closing)  # call .on_closing() when app gets closed


# ======================== create frames ========================

# configure grid layout (2x1)

framemain = customtkinter.CTkFrame(master=app, width=460)
framemain.grid(row=0, sticky="nswe", padx=20, pady=20)


# ======================== framemain ========================

label = customtkinter.CTkLabel(master=framemain,
                                    text="Danbooru Tags Cleaner",
                                    text_font=("Roboto Medium", -16))  # font name and size in px
label.grid(row=1, column=0, sticky="nswe", padx=20, pady=10)


# ======================== Input ========================

entry_input = customtkinter.CTkEntry(master=framemain,
                                            height=75,
                                            corner_radius=6,
                                            width=320,
                                            placeholder_text="Input here...")
entry_input.grid(row=2, column=0, pady=20, padx=20, sticky="nswe")


# ======================== Radio Button ========================

radio_var = tkinter.IntVar(value=0)

radio_button_1 = customtkinter.CTkRadioButton(master=framemain,
                                                    variable=radio_var,
                                                    text="Danbooru",
                                                    value=0)
radio_button_1.grid(row=3, column=0, pady=5, padx=20, sticky="nswe")

radio_button_2 = customtkinter.CTkRadioButton(master=framemain,
                                                   variable=radio_var,
                                                    text="Deep-danbooru",
                                                    value=1)
radio_button_2.grid(row=4, column=0, pady=5, padx=20, sticky="nswe")
        
         
# ======================== Button ========================

button_clean = customtkinter.CTkButton(master=framemain,
                                                text="Clean",
                                                text_font=("Roboto Medium", -16) ,
                                                border_width=2,  # <- custom border_width
                                                command=clean_button)
button_clean.grid(row=5, column=0, columnspan=1, pady=10, padx=20, sticky="we")
        
        
# ======================== Output ========================
        
entry_output = customtkinter.CTkEntry(master=framemain,
                                            height=75,
                                            corner_radius=6,
                                            width=320,
                                            placeholder_text="Ouput here...")
entry_output.grid(row=6, column=0, pady=20, padx=20, sticky="nswe")
    

app.mainloop()