'''
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.textinput import TextInput
Window.clearcolor = "#FABF0E"
Window.size=(360,600)
st = "hello world"


class SampleAppApp(App):
    def build(self):

        layout=BoxLayout(orientation="vertical",padding=30,spacing=20)
        #label = Button(text=st, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5},on_press=self.pressing)
        #layout.add_widget(label)
        #layout.add_widget(button)
        """
        layout=GridLayout(cols=2,row_force_default=True , row_default_height=50,padding=100)
        but1 = Button(text=st,size_hint=(None,None),height=200,width=200,pos_hint={'center_x': 0.5, 'center_y': 0.5})
        but2 = Button(text=st, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        but3 = Button(text=st, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        but4 = Button(text=st, size_hint=(1, 1),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(but1)
        layout.add_widget(but2)
        layout.add_widget(but3)
        layout.add_widget(but4)
        :return:
        """
        self.num=TextInput(hint_text="enter")
        but1 = Button(text="click me!!",on_press=self.pressing)
        layout.add_widget(num)
        layout.add_widget(but1)
        return layout

    def pressing(self, obj):
        n

        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)
        num = TextInput(text="enter a number2:")
        but1 = Button(text="click me!!@@@@                                                                                                ", on_press=self.pressing)
        layout.add_widget(num)
        layout.add_widget(but1)
        return layout




SampleAppApp().run()

'''
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from random import randint
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.theme_style = "Dark"
        screen = MDScreen()
        label1 = MDLabel(text="Stone Paper Scissor", pos_hint={'center_y': 0.8}, halign='center', font_style='H2')
        self.user_name = "hemanth"
        label2 = MDLabel(text=f"{self.user_name.capitalize()}'s Choice:", pos_hint={'center_y': 0.7}, halign='center', font_style='H4')
        self.button1 = MDRectangleFlatButton(text="Stone", pos_hint={'center_x': 0.4, 'center_y': 0.5},
                                             on_press=lambda *args: self.Game('stone', 1))
        self.button2 = MDRectangleFlatButton(text="Paper", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                             on_press=lambda *args: self.Game('paper', 2))
        self.button3 = MDRectangleFlatButton(text="Scissor", pos_hint={'center_x': 0.6, 'center_y': 0.5},
                                             on_press=lambda *args: self.Game('scissor', 3))
        screen.add_widget(self.button1)
        screen.add_widget(self.button2)
        screen.add_widget(self.button3)

        screen.add_widget(label1)
        screen.add_widget(label2)
        return screen

    def Game(self, obj, num):
        user_choice=obj
        li = ["stone","paper","scissor"]
        computer_choice= li[randint(0, 2)]
        but1 = MDRectangleFlatButton(text="back", on_press=self.back)
        result = 1 if user_choice == computer_choice else 0 if user_choice == 'stone' and  computer_choice != 'paper' else 0 if user_choice == 'paper' and computer_choice != 'scissor' else 0 if user_choice == 'scissor' and computer_choice != 'stone'  else 2
        display_result="match tie" if result == 1 else self.user_name+"win" if result == 0 else "computer win"
        self.dialog=MDDialog(title="Stone Paper Scissor",text=self.user_name+"'s choice: "+user_choice+"\nComputer's  Choice: "+computer_choice+"\n"+display_result.center(20),buttons=[but1])
        self.dialog.open()
    def back(self,obj):
        self.dialog.dismiss()




DemoApp().run()
