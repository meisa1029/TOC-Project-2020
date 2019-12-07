from transitions.extensions import GraphMachine

from utils import send_text_message

import random


meat = ["雞肉", "牛肉", "豬肉"]
meat_cnt = 3

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, meat[random.randint(0, meat_cnt--)])
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def is_going_to_try(self, event):
        text = event.message.text
        return text.lower() == "try"

    def on_enter_try(self, event):
        print("enter tring state")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger try")
        self.go_back()

    def on_exit_try(self):
        print("leave try")
