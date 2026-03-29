import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x430")
        
        # Calculator
        
        self.expression = ""
        self.width = 10
        self.height = 4
        
        #expression display
        
        self.calc_label = tk.Label(self, text=" ", font=("Arial", 16), bg="white", width=24, height=2)
        self.calc_label.pack(pady=10)
        
        #frames for buttons
        
        self.frame1=tk.Frame(self,bg="lightgrey")
        self.frame1.pack(pady=0)
        self.frame2=tk.Frame(self,bg="lightgrey")
        self.frame2.pack(pady=0)
        self.frame3=tk.Frame(self,bg="lightgrey")
        self.frame3.pack(pady=0)
        self.frame4=tk.Frame(self,bg="lightgrey")
        self.frame4.pack(pady=0)
        self.frame5=tk.Frame(self,bg="lightgrey")
        self.frame5.pack(pady=0)
        
        #buttons
        
        self.b_clear_all = tk.Button(self.frame1, text="AC",command=self.clear_all, width=self.width, height=self.height)
        self.b_clear_all.pack(side=tk.LEFT)
        self.b_bracket = tk.Button(self.frame1, text="( )",command=self.bracket, width=self.width, height=self.height)
        self.b_bracket.pack(side=tk.LEFT)
        self.b_percent = tk.Button(self.frame1, text="%",command=lambda: self.append_expression("%"), width=self.width, height=self.height)
        self.b_percent.pack(side=tk.LEFT)
        self.b_divide = tk.Button(self.frame1, text="÷",command=lambda: self.append_expression("/"), width=self.width, height=self.height)
        self.b_divide.pack(side=tk.LEFT)
        self.b7 = tk.Button(self.frame2, text="7",command=lambda: self.append_expression("7"), width=self.width, height=self.height)
        self.b7.pack(side=tk.LEFT)
        self.b8 = tk.Button(self.frame2, text="8",command=lambda: self.append_expression("8"), width=self.width, height=self.height)
        self.b8.pack(side=tk.LEFT)
        self.b9 = tk.Button(self.frame2, text="9",command=lambda: self.append_expression("9"), width=self.width, height=self.height)
        self.b9.pack(side=tk.LEFT)
        self.b_plus = tk.Button(self.frame2, text="+",command=lambda: self.append_expression("+"), width=self.width, height=self.height)
        self.b_plus.pack(side=tk.LEFT)
        self.b4 = tk.Button(self.frame3, text="4",command=lambda: self.append_expression("4"), width=self.width, height=self.height)
        self.b4.pack(side=tk.LEFT)
        self.b5 = tk.Button(self.frame3, text="5",command=lambda: self.append_expression("5"), width=self.width, height=self.height)
        self.b5.pack(side=tk.LEFT)
        self.b6 = tk.Button(self.frame3, text="6",command=lambda: self.append_expression("6"), width=self.width, height=self.height)
        self.b6.pack(side=tk.LEFT)
        self.b_minus = tk.Button(self.frame3, text="-",command=lambda: self.append_expression("-"), width=self.width, height=self.height)
        self.b_minus.pack(side=tk.LEFT)
        self.b1 = tk.Button(self.frame4, text="1",command=lambda: self.append_expression("1"), width=self.width, height=self.height)
        self.b1.pack(side=tk.LEFT)
        self.b2 = tk.Button(self.frame4, text="2",command=lambda: self.append_expression("2"), width=self.width, height=self.height)
        self.b2.pack(side=tk.LEFT)
        self.b3 = tk.Button(self.frame4, text="3",command=lambda: self.append_expression("3"), width=self.width, height=self.height)
        self.b3.pack(side=tk.LEFT)
        self.b_mul = tk.Button(self.frame4, text="*",command=lambda: self.append_expression("*"), width=self.width, height=self.height)
        self.b_mul.pack(side=tk.LEFT)
        self.b0 = tk.Button(self.frame5, text="0",command=lambda: self.append_expression("0"), width=self.width, height=self.height)
        self.b0.pack(side=tk.LEFT)
        self.b_dot = tk.Button(self.frame5, text=".",command=lambda: self.append_expression("."), width=self.width, height=self.height)
        self.b_dot.pack(side=tk.LEFT)
        self.b_equal = tk.Button(self.frame5, text="=",command=self.calculate, width=self.width, height=self.height)
        self.b_equal.pack(side=tk.LEFT)
        self.b_clear = tk.Button(self.frame5, text="C",command=self.clear_expression, width=self.width, height=self.height)
        self.b_clear.pack(side=tk.LEFT)
        
    #functions
    def percent(self):
        if "%" in self.expression:
            self.expression = self.expression.replace('%', '/100*')
    def append_expression(self, value):
        self.expression += value
        self.calc_label.config(text=self.expression)
    def calculate(self):
        try:
            if "%" in self.expression:
                self.percent()
            result = str(eval(self.expression))
            self.calc_label.config(text=result)
            self.expression = result
            if self.expression.endswith('.0'):
                self.expression = self.expression[:-2]
            self.calc_label.config(text=self.expression)
        except Exception as e:
            self.calc_label.config(text="Error")
            self.expression = ""
    def clear_expression(self):
        self.expression = self.expression[:-1]
        self.calc_label.config(text=self.expression)
    def clear_all(self):
        self.expression = ""
        self.calc_label.config(text=self.expression)
    def bracket(self):
        if self.expression.count('(') == self.expression.count(')'):
            self.expression += '('
        else:
            self.expression += ')'
        self.calc_label.config(text=self.expression)
if __name__ == "__main__":
    app = App()
    app.title("Calculator App")
    app.config(bg="lightblue")
    app.mainloop()