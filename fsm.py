from transitions.extensions import GraphMachine

from utils import send_text_message

import random


meat = ["三杯雞", "牛肉", "炒豬肉片", "鮭魚", "比目魚", "香腸"]
veg = ["炒高麗菜", "水煮青花椰菜", "地瓜葉", "空心菜"]
side_dish = ["玉米炒蛋", "蔥蛋", "杏鮑菇", "洋蔥炒蛋", "馬鈴薯燉肉"] 
soup = ["蛤蜊湯", "大黃瓜湯", "蘿蔔湯"]
other = ["部隊鍋", "火鍋", "大阪燒", "櫻花蝦炒飯", "炒泡麵"]
#to_do_list = []

meat_cnt = 6
veg_cnt = 4
side_cnt = 5
soup_cnt = 3
other_cnt = 5

t = []
state = 0	#1: random 2:select/delete

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    #is_going_state

    def is_going_to_menu(self, event):
        text = event.message.text
        return (state != 0 and text.lower() == "結束")

    def is_going_to_random(self, event):
        text = event.message.text
        return (state == 0 and text.lower() == "1")
    
    def is_going_to_meat(self, event):
        text = event.message.text
        #return (state == 1 and text.lower() == "肉")
        return text.lower() == "肉"

    def is_going_to_veg(self, event):
        text = event.message.text
        return (state == 1 and text.lower() == "菜")

    def is_going_to_side_dish(self, event):
        text = event.message.text
        return (state == 1 and text.lower() == "配菜")

    def is_going_to_soup(self, event):
        text = event.message.text
        return (state == 1 and text.lower() == "湯")

    def is_going_to_other(self, event):
        text = event.message.text
        return (state == 1 and (text.lower() == "其它" or text.lower() == "其他"))

    def is_going_to_add(self, event):
        text = event.message.text
        t = text.split(" ")
        return t[0].lower() == "新增"

    # on_enter_state

    def on_enter_menu(self, event):
        print("menu")
        state = 0
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入\"1\": 進入選擇模式\n輸入\"2\": 進入輸入刪除模式")
        self.go_back()

    def on_enter_random(self, event):
        print("random")
        state = 1
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入想選擇的類別\n類別: 肉、菜、配菜、湯、其它")
        #self.go_back()

    def on_enter_meat(self, event):
        print("choosing meat")
        reply_token = event.reply_token
        reply = meat[random.randint(0, meat_cnt-1)] + "\n繼續選擇請輸入選擇類別  如：菜、肉\n結束選擇請輸入\"結束\"\n"+str(state)
        send_text_message(reply_token, reply)
        #self.go_back()

    def on_enter_veg(self, event):
        print("choosing vegetable")
        reply_token = event.reply_token
        send_text_message(reply_token, veg[random.randint(0, veg_cnt-1)])
        self.go_back()

    def on_enter_side_dish(self, event):
        print("choosing side dish")
        reply_token = event.reply_token
        send_text_message(reply_token, side_dish[random.randint(0, side_cnt-1)])
        self.go_back()

    def on_enter_soup(self, event):
        print("choosing soup")
        reply_token = event.reply_token
        send_text_message(reply_token, soup[random.randint(0, soup_cnt-1)])
        self.go_back()

    def on_enter_other(self, event):
        print("choosing other")
        reply_token = event.reply_token
        send_text_message(reply_token, other[random.randint(0, other_cnt-1)])
        self.go_back()

    def on_enter_add(self, event):
        print("add")
        reply_token = event.reply_token
        reply = t[2] + " 新增成功"
        send_text_message(reply_token, reply)
        self.go_back()

    # on_exit

    def on_exit_menu(self):
        print("Leaving menu")

    def on_exit_random(self):
        print("Leaving random")

    def on_exit_meat(self):
        print("Leaving meat")

    def on_exit_veg(self):
        print("Leaving vegetable")

    def on_exit_side_dish(self):
        print("Leaving side dish")

    def on_exit_soup(self):
        print("leaveing soup")

    def on_exit_other(self):
        print("Leaving other")

