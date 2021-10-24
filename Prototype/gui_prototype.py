import tkinter as tk
from decimal import Decimal, Context


# W = Width, H = Height, X/Y = X/Y coordinate, C = Count
WINDOW_W = 550
WINDOW_H = 305
Projct_X = 20
Projct_Y = 20
FINDER_X = 20
FINDER_Y = 150 
OUTPUT_C = 0  # for the mnimum finder


# Each Widget Class can locate itself, and Some have an identical method
# [CLASS] Label
class Label(tk.Label):
    def __init__(self, root, text, font, x, y):
        super().__init__(
            root, text=text, font=(f"{font[0]}", font[1])
        )
        self.place(x=x, y=y)
        
    def txt_update(self, txt):
        self.config(text=txt)


# [CLASS] Button
class Button(tk.Button):
    def __init__(self, root, text, w, x, y, c=None, s="normal"):
        super().__init__(
            root, text=text, width=w, font=("", 12), command=c, state=s
        )
        self.place(x=x, y=y)


# [CLASS] Text box 
class TxtBox(tk.Entry):
    def __init__(self, w, x, y):
        super().__init__(width=w)
        self.place(x=x, y=y)
        
    def get_txt(self):
        return self.get()


# [CLASS] Program for receiving and displaying user input
class TxtProjector():
    def __init__(self, root):
        self.lbl_title = Label(root, "Text Projector", ("bold", 18), Projct_X, Projct_Y)
        self.lbl_text = Label(root, "TEXT :", ("bold", 14), Projct_X+235, Projct_Y)
        self.lbl_txt = Label(root, "", ("", 14), Projct_X+235, Projct_Y+35)

        self.txt_box = TxtBox(20, Projct_X, Projct_Y+35)
        self.sbmt_btn = Button(root, "Submit", 6, Projct_X, Projct_Y+70, self.txt_project)

    def txt_project(self):
        txt = self.txt_box.get_txt()
        self.lbl_txt.txt_update(txt)


# [CLASS] Program for reflecting numbers a user inputs in ascending order
class MinFinder():
    def __init__(self, root):
        self.root = root
        self.content = []
        self.boxes = []

        # Creates text boxes each with a default value
        for i in range(10):
            if i < 5:
                self.boxes.append(TxtBox(2, FINDER_X+30*i, FINDER_Y+35))
            else:
                self.boxes.append(TxtBox(2, FINDER_X+30*(i-5), FINDER_Y+70))
            self.boxes[i].insert(0, i)

        # Labels for a title, a warning for wrong input, and computer output
        self.lbl_title = Label(root, "Minimum Finder", ("bold", 18), FINDER_X, FINDER_Y)
        self.lbl_warning = Label(root, "", ("", 14), FINDER_X+200, FINDER_Y)
        self.lbl_pos = Label(self.root, "", ("bold", 16), FINDER_X+230, FINDER_Y+35)
        self.lbl_num = Label(self.root, "", ("bold", 16), FINDER_X+230, FINDER_Y+60)

        # Buttons for a user to submit and check sorted numbers
        self.sbmt_btn = Button(
            root, "Submit", 6, FINDER_X, FINDER_Y+110, self.process_request
        )
        self.min_btn = Button(
            self.root, "Pending", 6, FINDER_X+230, FINDER_Y+90, self.display_sorted, "disabled"
        )

    # Handle the whole flow of user input and computer output
    def process_request(self):
        self.content.clear()
        self.get_content()
        if self.validate_content():
            self.input_toggle()
            self.content = list(map(decimal_normalize, self.content))
            self.content.sort()
            self.display_sorted()

    # Transfer values from text boxes to a list
    def get_content(self):
        for b in self.boxes:
            self.content.append(b.get_txt())

    # Recursively works to show a sorted numbers in ascending order
    def display_sorted(self, evnt=None):
        global OUTPUT_C
        if OUTPUT_C < 10:
            if OUTPUT_C == 0:
                pos_txt = "The Minimum :"
                btn_txt = "-> 2nd"
            elif OUTPUT_C == 1:
                pos_txt = "The 2 nd :"
                btn_txt = "-> 3rd"
            elif OUTPUT_C == 2:
                pos_txt = "The 3 rd :"
                btn_txt = "-> 4th"
            else:
                pos_txt = f"The {OUTPUT_C+1} th :"
                if OUTPUT_C == 9:
                    btn_txt = "-> back"
                else:
                    btn_txt = f"-> {OUTPUT_C + 2}th"
            self.lbl_pos.txt_update(pos_txt)
            self.lbl_num.txt_update(self.content[OUTPUT_C])
            self.min_btn.config(text=btn_txt, state="normal")
            OUTPUT_C += 1
        else:
            self.lbl_pos.txt_update("")
            self.lbl_num.txt_update("")
            self.min_btn.config(text="pending", state="disabled")
            self.input_toggle()
            OUTPUT_C = 0
            return

    # Examines if user input is erroneous (not a number or blanks)
    def validate_content(self):
        if "" in self.content or False in list(map(is_float, self.content)):
            self.lbl_warning["text"] = "*Please fill all boxes in number."
            return False
        else:
            return True

    # Switch availability of user inputs
    def input_toggle(self):
        if self.sbmt_btn["state"] == "normal":
            self.sbmt_btn.config(state="disabled")
        else:
            self.sbmt_btn.config(state="normal")
        for b in self.boxes:
            b.config(state=self.sbmt_btn["state"])


# [CLASS] Provide a GUI window and two main objects
class Prototype(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg="orange")
        self.geometry(f"{WINDOW_W}x{WINDOW_H}")
        self.title("GUI Prototype")
        self.projector = TxtProjector(self)
        self.finder = MinFinder(self)


# [FUNCTION] Check if a string can be changed in a float form
def is_float(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True


# [FUNCTION] Return a normalized number
def decimal_normalize(n):
    def _remove_exponent(n_exp):
        return n_exp.quantize(Decimal(1)) if n_exp == n_exp.to_integral() else n_exp.normalize()
    n_exp = Decimal.normalize(Decimal(str(n)))
    n_norm = _remove_exponent(n_exp)
    return n_norm


# [FUNCTION] Create GUI application
def main():
    app = Prototype()
    app.mainloop()


if __name__ == "__main__":
    main()