from transitions.extensions import GraphMachine

from utils import send_text_message

import random


meat = ["三杯雞", "牛肉", "炒豬肉片", "鮭魚", "比目魚", "香腸"]
veg = ["炒高麗菜", "水煮青花椰菜", "地瓜葉", "空心菜"]
soup = ["蛤蜊湯", "大黃瓜湯", "蘿蔔湯"]
side_dish = ["玉米炒蛋", "蔥蛋", "杏鮑菇", "洋蔥炒蛋", "馬鈴薯燉肉"] 
#other = ["部隊鍋", "火鍋", "大阪燒", "櫻花蝦炒飯", "炒泡麵"]
#to_do_list = []
meat_cnt = 6
veg_cnt = 4
side_cnt = 5
soup_cnt = 3

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_meat(self, event):
        text = event.message.text
        return text.lower() == "肉"

    def is_going_to_veg(self, event):
        text = event.message.text
        return text.lower() == "菜"

    def is_going_to_soup(self, event):
        text = event.message.text
        return text.lower() == "湯"

    def on_enter_meat(self, event):
        print("choosing meat")
        reply_token = event.reply_token
        send_text_message(reply_token, meat[random.randint(0, meat_cnt-1)])
        self.go_back()

    def on_enter_veg(self, event):
        print("choosing vegetable")
        reply_token = event.reply_token
        send_text_message(reply_token, veg[random.randint(0, veg_cnt-1)])
        self.go_back()

    def on_enter_soup(self, event):
        print("choosing soup")
        reply_token = event.reply_token
        send_text_message(reply_token, soup[random.randint(0, soup_cnt-1)])
        self.go_back()

    def on_exit_meat(self):
        print("Leaving meat")

    def on_exit_veg(self):
        print("Leaving vegetable")

    def on_exit_soup(self):
        print("leaveing soup")
