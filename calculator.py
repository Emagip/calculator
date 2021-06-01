#!/usr/bin/env python
# encoding: utf-8

import npyscreen as gui
class TestApp(gui.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = gui.Form(name = "Welcome to Npyscreen",)
        s  = F.add(gui.TitleSlider, out_of=100, name = "Slider")
        s2 = F.add(gui.TitleSlider, out_of=100, name = "Slider2")
        ms = F.add(gui.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
                values = ["add","multiply","divide","subtract"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        user_input = ms.get_value()
        num1 = s.get_value()
        num2 = s2.get_value()
        if user_input== [0]:
        	result= (num1 +num2)
        	print(result)
        	
        elif user_input== [1]:
        	result=(num1*num2)
        	print(result)
        	
        elif user_input== [2]:
        	result=(num1 //num2)
        	print(result)
     
        elif user_input== [3]:
        	result=(num1 - num2)
        	print(result)
            
if __name__ == "__main__":
    App = TestApp()
    App.run()
