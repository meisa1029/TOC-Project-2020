from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_button_message

import random

def read_txt(file_open):
    f = open(file_open, "r")
    s = f.readline()
    s = s.split("\n")
    f.close()
    return s[0]

def write_txt(file_open, s):
    f = open(file_open, "w")
    f.write(s)
    f.close()

def get_t_name(t):
    if t == "肉":
        return "meat.txt"
    elif t == "青菜":
        return "veg.txt"
    elif t == "配菜":
        return "side_dish.txt"
    elif t == "湯":
        return "soup.txt"
    elif (t == "其他" or t == "其它"):
        return "other.txt"
    else:
        return "0"

def check(t_name, s):
    read = read_txt(t_name)
    r = read.split(" ")
    index = -1
    for i in range(len(r)):
        if r[i] == s:
            return i
    return index

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    #is_going_state

    def is_going_to_menu(self, event):
        text = event.message.text
        return (text.lower() == "開始" or text.lower() == "結束")

    def is_going_to_random(self, event):
        text = event.message.text
        return text.lower() == "煮什麼"

    def is_going_to_change(self, event):
        text = event.message.text
        return text.lower() == "新增/刪除"

    def is_going_to_list(self, event):
        text = event.message.text
        return text.lower() == "列清單"

    def is_going_to_meat(self, event):
        text = event.message.text
        return text.lower() == "肉"

    def is_going_to_veg(self, event):
        text = event.message.text
        return text.lower() == "青菜"

    def is_going_to_side_dish(self, event):
        text = event.message.text
        return text.lower() == "配菜"

    def is_going_to_soup(self, event):
        text = event.message.text
        return text.lower() == "湯"

    def is_going_to_other(self, event):
        text = event.message.text
        return (text.lower() == "其它" or text.lower() == "其他")

    def is_going_to_add(self, event):
        text = event.message.text
        t = text.split(" ", 1)
        write_txt("change.txt", t[1])
        return t[0].lower() == "新增"

    def is_going_to_delete(self, event):
        text = event.message.text
        t = text.split(" ", 1)
        write_txt("change.txt", t[1])
        return t[0].lower() == "刪除"

    def is_going_to_list_food(self, event):
        text = event.message.text
        if text != "結束":
            write_txt("change.txt", text)
            return True
        else:
            return False

    # on_enter_state

    def on_enter_menu(self, event):
        print("menu")
        reply_token = event.reply_token
        text = ["主選單", "煮什麼：幫你選擇菜單\n新增/刪除：新增刪除菜單"]
        buttons = ["煮什麼", "新增/刪除", "列清單"] 
        send_button_message(reply_token, text, buttons)

    def on_enter_random(self, event):
        print("random")
        reply_token = event.reply_token
        text = ["煮什麼", "輸入想選擇的類別\n類別: 肉、青菜、配菜、湯、其它"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)
        

    def on_enter_change(self, event):
        print("change")
        reply_token = event.reply_token
        text = ["新增/刪除", "輸入：\"新增\"/\"刪除\" 類別 品名\nex:新增 肉 三杯雞\n   刪除 湯 蘿蔔湯\n類別: 肉、青菜、配菜、湯、其它"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)

    def on_enter_list(self, event):
        print("change")
        reply_token = event.reply_token
        text = ["列清單", "請輸入類別\n類別：肉、青菜、配菜、湯、其他"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)

    def on_enter_meat(self, event):
        print("choosing meat")
        reply_token = event.reply_token
        read = read_txt("meat.txt")
        meats = read.split(" ")
        meat_cnt = len(meats)
        text = [meats[random.randint(0, meat_cnt-1)], 
"繼續輸入類別或結束\n類別：肉、青菜、配菜、湯、其他"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)

    def on_enter_veg(self, event):
        print("choosing vegetable")
        reply_token = event.reply_token
        read = read_txt("veg.txt")
        vegs = read.split(" ")
        veg_cnt = len(vegs)
        text = [vegs[random.randint(0, veg_cnt-1)], "繼續輸入類別或結束\n類別：肉、青菜、配菜、湯、其他"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)
        #reply = vegs[random.randint(0, veg_cnt-1)] + "\n繼續選擇請輸入選擇類別  類別：肉、青菜、配菜、湯、其他\n結束選擇請輸入\"結束\""

    def on_enter_side_dish(self, event):
        print("choosing side dish")
        reply_token = event.reply_token
        read = read_txt("side_dish.txt")
        side_dishes = read.split(" ")
        side_cnt = len(side_dishes)
        text = [side_dishes[random.randint(0, side_cnt-1)], "繼續輸入類別或結束\n類別：肉、青菜、配菜、湯、其他"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)
        #reply = side_dishes[random.randint(0, side_cnt-1)] + "\n繼續選擇請輸入選擇類別  類別：肉、青菜、配菜、湯、其他\n結束選擇請輸入\"結束\""

    def on_enter_soup(self, event):
        print("choosing soup")
        reply_token = event.reply_token
        read = read_txt("soup.txt")
        soups = read.split(" ")
        soup_cnt = len(soups)
        text = [soups[random.randint(0, soup_cnt-1)], "繼續輸入類別或結束\n類別：肉、青菜、配菜、湯、其他"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)
        #reply = soups[random.randint(0, soup_cnt-1)] + "\n繼續選擇請輸入選擇類別  類別：肉、青菜、配菜、湯、其他\n結束選擇請輸入\"結束\""

    def on_enter_other(self, event):
        print("choosing other")
        reply_token = event.reply_token
        read = read_txt("other.txt")
        others = read.split(" ")
        other_cnt = len(others)
        text = [others[random.randint(0, other_cnt-1)], "繼續輸入類別或結束\n類別：肉、青菜、配菜、湯、其他"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)
        #reply = others[random.randint(0, other_cnt-1)] + "\n繼續選擇請輸入選擇類別  類別：肉、青菜、配菜、湯、其他\n結束選擇請輸入\"結束\""

    def on_enter_add(self, event):
        print("add")
        reply_token = event.reply_token
        read = read_txt("change.txt")
        t = read.split(" ")
        t_name = get_t_name(t[0])
        if t_name == "0":
            reply = "格式錯誤"
        else:
            if check(t_name, t[1]) == -1:
                read = read_txt(t_name)
                read = read + " " + t[1]
                write_txt(t_name, read)
                reply = t[1] + " 新增成功"
            else:
                reply = "該品項已經存在"
        text = [reply, "繼續輸入或結束"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)

    def on_enter_delete(self, event):
        print("delete")
        reply_token = event.reply_token
        read = read_txt("change.txt")
        t = read.split(" ")
        t_name = get_t_name(t[0])
        if t_name == "0":
            reply = "格式錯誤\n"
        else:
            if check(t_name, t[1]) != -1:
                read = read_txt(t_name)
                r = read.split(" ")
                r.remove(t[1])
                w = ""
                for i in range(len(r)):
                    w = w + " " + r[i]
                write = w.split(" ", 1)
                write_txt(t_name, write[1])
                reply = t[1] + " 刪除成功\n"
            else:
                reply = "該品項不存在"
        text = [reply, "繼續輸入或結束"]
        buttons = ["結束"]
        send_button_message(reply_token, text, buttons)

    def on_enter_list_food(self, event):
        print("list food")
        reply_token = event.reply_token
        read = read_txt("change.txt")
        t_name = get_t_name(read)
        if t_name == "0":
            reply = "格式錯誤\n"
        else:
            read = read_txt(t_name)
            l = read.split(" ")
            reply = ""
            for food in l:
                reply = reply + food + "\n"
        reply = reply + "請繼續輸入類別或輸入\"結束\"\n類別: 肉、青菜、配菜、湯、其它"
        send_text_message(reply_token, reply)
