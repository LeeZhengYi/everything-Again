import tkinter
import tkinter.messagebox
import customtkinter


import csv
import numpy as np
import pandas as pd


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="PWB2000v \n Configuration selection : ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.label_1 = customtkinter.CTkLabel(master=self, text="Select a standard: ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_1.grid(row=0, column=1, padx=0, pady=(10, 2))

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master = self, dynamic_resizing=False,
                                                        values=["PWB2000V-S01", "PWB2000V-S02", "PWB2000V-S03","PWB2000V-S04",
                                                        "PWB2000V-S05","PWB2000V-S06","PWB2000V-S07","PWB2000V-S08","PWB2000V-S09","PWB2000V-S10"])
        self.optionmenu_1.grid(row=0, column=1, padx=0, pady=(75, 2))


        self.optionmenu_1.set("Pick a standard: ")


        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="green", text = "Submit", border_width=2, text_color=("gray10", "#DCE4EE"), command = self.check_all)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")



        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=1 , padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame,command = self.checkbox_1_event, text="PWB20-MCRSET")
        self.checkbox_1.grid(row=1, column=0,padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, command = self.checkbox_2_event, text = "PWB20-STBPHV3")
        self.checkbox_2.grid(row=2, column=0, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-PUNCHVA")
        self.checkbox_3.grid(row=3, column=0, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_4 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame,text="PWB20-VEPUNCHV01")
        self.checkbox_4.grid(row=4, column=0,padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_5 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-STBPHV1")
        self.checkbox_5.grid(row=5, column=0, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_6 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-STBPHV2")
        self.checkbox_6.grid(row=6, column=0, padx=(0, 0), pady=(0, 0), sticky="n")

        self.checkbox_7 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-STBDSV1")
        self.checkbox_7.grid(row=1, column=1, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_8 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-FBLSCUT")
        self.checkbox_8.grid(row=2, column=1, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_9 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-BCRSET")
        self.checkbox_9.grid(row=3, column=1,padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_10 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-FMKITS")
        self.checkbox_10.grid(row=4, column=1,padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_11 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-MGID")
        self.checkbox_11.grid(row=5, column=1, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_12 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-HDD")
        self.checkbox_12.grid(row=6, column=1, padx=(0, 0), pady=(0, 0), sticky="n")

        self.checkbox_13 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-HDD2")
        self.checkbox_13.grid(row=1, column=2, padx=(0, 0), pady=(0, 0),sticky="n")
        self.checkbox_14 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-BSECSGEM")
        self.checkbox_14.grid(row=2, column=2,padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_15 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-ASECSGEM")
        self.checkbox_15.grid(row=3, column=2, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_16 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-HPC")
        self.checkbox_16.grid(row=4, column=2, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_17 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-WIN10")
        self.checkbox_17.grid(row=5, column=2, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_18 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-VPC")
        self.checkbox_18.grid(row=6, column=2, padx=(0, 0), pady=(0, 0), sticky="n")

        self.checkbox_19 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-MPLATE")
        self.checkbox_19.grid(row=1, column=3, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_20 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-DIESETV1")
        self.checkbox_20.grid(row=2, column=3, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_21 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-PUNCH")
        self.checkbox_21.grid(row=3, column=3, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_22 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-PUNCHVAC")
        self.checkbox_22.grid(row=4, column=3, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_23 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-HBSC1")
        self.checkbox_23.grid(row=5, column=3,padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_24 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-PUNCHVA2")
        self.checkbox_24.grid(row=6, column=3, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_25 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-VEPUNCH")
        self.checkbox_25.grid(row=7, column=3, padx=(0, 0), pady=(0, 0), sticky="n")
        self.checkbox_26 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="PWB20-STMPHV1")
        self.checkbox_26.grid(row=8, column=3, padx=(0, 0), pady=(0, 0), sticky="n")


        # writes a line of standard chosen and add ons
        self.textBox1 = customtkinter.CTkTextbox(master=self, width=100, height=1 )
        self.textBox1.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")


        # have a new frame showing 
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color = "white", width = 1000, height = 1000 )
        self.main_frame.grid_columnconfigure(0, weight=1 )
        self.main_label = customtkinter.CTkLabel(self.main_frame, text="Configuration: \n standard \n add on",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"),text_color="black")
        self.main_label.grid(row=0, column=1, padx=30, pady=(2, 2))

        self.textbox2 = customtkinter.CTkTextbox(self.main_frame, width=100, height=200 )
        self.textbox2.grid(row=2, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=4, column=2, padx=30, pady=(50, 150))

       

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

      
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def checkbox_1_event(self):

        if self.checkbox_1.get(): 
            print("checkbox_1 is checked")


    def checkbox_2_event(self):
        if self.checkbox_2.get():
            print("checkbox_2 click")

    def check_all (self):
        input = []
        if self.checkbox_1.get():
            input = input + ["PWB20-MCRSET"]
        if self.checkbox_2.get():
            input = input + ["PWB20-STBPHV3"]
        if self.checkbox_3.get():
            input = input + ["PWB20-PUNCHVA"]
        if self.checkbox_4.get():
            input = input + ["PWB20-VEPUNCHV01"]
        if self.checkbox_5.get():
            input = input + ["PWB20-STBPHV1"]
        if self.checkbox_6.get():
            input = input + ["PWB20-STBPHV2"]
        if self.checkbox_7.get():
            input = input + ["PWB20-STBDSV1"]
        if self.checkbox_8.get():
            input = input + ["PWB20-FBLSCUT"]
        if self.checkbox_9.get():
            input = input + ["PWB20-BCRSET"]
        if self.checkbox_10.get():
            input = input + ["PWB20-FMKITS"]
        if self.checkbox_11.get():
            input = input + ["PWB20-MGID"]
        if self.checkbox_12.get():
            input = input + ["PWB20-HDD"]
        if self.checkbox_13.get():
            input = input + ["PWB20-HDD2"]
        if self.checkbox_14.get():
            input = input + ["PWB20-BSECSGEM"]
        if self.checkbox_15.get():
            input = input + ["PWB20-ASECSGEM"]
        if self.checkbox_16.get():
            input = input + ["PWB20-HPC"]
        if self.checkbox_17.get():
            input = input + ["PWB20-WIN10"]
        if self.checkbox_18.get():
            input = input + ["PWB20-VPC"]
        if self.checkbox_19.get():
            input = input + ["PWB20-MPLATE"]
        if self.checkbox_20.get():
            input = input + ["PWB20-DIESETV1"]
        if self.checkbox_21.get():
            input = input + ["PWB20-PUNCH"]
        if self.checkbox_22.get(): 
            input = input + ["PWB20-PUNCHVAC"]
        if self.checkbox_23.get():
            input = input + ["PWB20-HBSC1"]
        if self.checkbox_24.get():
            input = input + ["PWB20-PUNCHVA2"]
        if self.checkbox_25.get():
            input = input + ["PWB20-VEPUNCH"]
        if self.checkbox_26.get():
            input = input + ["PWB20-STMPHV1"]
        print(input)


        standard = self.optionmenu_1.get()  # get selected value from combobox
        

        
        #show main frame 
        self.label_1.grid_forget()  # remove label_1
        self.optionmenu_1.grid_forget()  # remove combobox
        self.checkbox_slider_frame.grid_forget()  # remove checkbox_slider_frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100, pady = 100, columnspan=3, rowspan=3)
        self.textbox2.insert("0.0", "\n" + standard)
        self.textbox2.insert("1.0", "\n"+ str(input) )

        self.run_event()
        
        return input

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.label_1.grid(row=0, column=1, padx=0, pady=(10, 2)) # show label_1
        self.optionmenu_1.grid(row=0, column=1, padx=0, pady=(75, 2))  # show combobox
        self.checkbox_slider_frame.grid(row=1, column=1 , padx=(0, 0), pady=(0, 0), sticky="nsew") # show checkbox_slider_frame


    index_pos_list = []

    def get_index_positions_2(list_of_elems, element):
        ''' Returns the indexes of all occurrences of give element in
        the list- listOfElements '''
        index_pos_list = []
        for i in range(len(list_of_elems)):
            if list_of_elems[i] == element:
                index_pos_list.append(i)
        return index_pos_list

        



    def run_event(self):

        standard = [self.optionmenu_1.get()]  # get selected value from combobox

        thisCompareMatch = compare(standard, configCodedataArray)
        print("thisCompareMatch", thisCompareMatch)


    

def compare (userInput, dataArray):
    #compare and count the number of standards in the config Database array
    #finding the standard by comparing it to the array 
    n = 0 
    count = 0 
    standard = userInput

    for y in dataArray[:,1]:
                
        if  userInput[0] == dataArray[n,1]:
            print("Standard found")
            print("-------------------------------------")  
            flag = True
            count += 1 
        n+=1
                
    my_string = f'There is {count} iterations of {standard}'
    if count == 0: 
        print("there is no such standard ")
        print ("--------------------------------------------------")
        flag = False
        return flag
    print(my_string) #prints out the standard found and the number of iterations in the database 
    return flag 


ff = pd.read_csv(r'C:\Users\60111\Testing\PWB_database.csv', header=0)
configCodedataArray = ff.to_numpy()

ee = pd.read_csv(r'C:\Users\60111\Coding project\dataBases\standardDatabase.csv', header=0)
DataArray2 = ee.to_numpy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

