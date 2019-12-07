from transitions.extensions import GraphMachine

from utils import send_text_message

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
            return flag
    return flag

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    #is_going_state

    def is_going_to_menu(self, event):
        text = event.message.text
#        state = read_txt("state")
#        if state == -1:
#            return True
#        else:        
        return (text.lower() == "開始" or text.lower() == "結束")

    def is_going_to_random(self, event):
        text = event.message.text
        return text.lower() == "1"

    def is_going_to_change(self, event):
        text = event.message.text
        return text.lower() == "2"

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

    # on_enter_state

    def on_enter_menu(self, event):
        print("menu")
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入\"1\": 進入選擇模式\n輸入\"2\": 進入輸入/刪除模式")
       # self.go_back()

    def on_enter_random(self, event):
        print("random")
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入想選擇的類別\n類別: 肉、青菜、配菜、湯、其它")
        #self.go_back()

    def on_enter_change(self, event):
        print("change")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入：\"新增\"/\"刪除\" 類別 品名\nex: 新增 肉 雞肉\n     刪除 湯 蘿蔔湯\n類別：肉、青菜、配菜、湯、其他")
        #self.go_back()

    def on_enter_meat(self, event):
        print("choosing meat")
        reply_token = event.reply_token
        read = read_txt("meat.txt")
        meats = read.split(" ")
        meat_cnt = len(meats)
        reply = meats[random.randint(0, meat_cnt-1)] + "\n繼續選擇請輸入選擇類別  類別：肉、青菜、配菜、湯、其他\n結束選擇請輸入\"結束\""
        send_text_message(reply_token, reply)
#        self.go_back()

    def on_enter_veg(self, event):
        print("choosing vegetable")
        reply_token = event.reply_token
        read = read_txt("veg.txt")
        vegs = read.split(" ")
        veg_cnt = len(vegs)
        reply = vegs[random.randint(0, veg_cnt-1)] + "\n繼續選擇請輸入選擇類別  類別：肉、青菜、配菜、湯、其他\n結束選擇請輸入\"結束\""
        send_text_message(reply_token, reply)
#        self.go_back()

    def on_enter_side_dish(self, event):
        print("choosing side dish")
        reply_token = event.reply_token
        read = read_txt("side_dish.txt")
        side_dishes = read.split(" ")
        side_cnt = len(side_dishes)
        reply = side_dishes[random.randint(0, side_cnt-1)] + "\n繼續選擇請輸入選擇類別  類別：肉、青菜、配菜、湯、其他\n結束選擇請輸入\"結束\""
        send_text_message(reply_token, reply)
#       self.go_back()

    def on_enter_soup(self, event):
        print("choosing soup")
        reply_token = event.reply_token
        read = read_txt("soup.txt")
        soups = read.split(" ")
        soup_cnt = len(soups)
        reply = soups[random.randint(0, soup_cnt-1)] + "\n繼續選擇請輸入選擇類別  類別：肉、青菜、配菜、湯、其他\n結束選擇請輸入\"結束\""
        send_text_message(reply_token, reply)
#        self.go_back()

    def on_enter_other(self, event):
        print("choosing other")
        reply_token = event.reply_token
        read = read_txt("other.txt")
        others = read.split(" ")
        other_cnt = len(others)
        reply = others[random.randint(0, other_cnt-1)] + "\n繼續選擇請輸入選擇類別  類別：肉、青菜、配菜、湯、其他\n結束選擇請輸入\"結束\""
        send_text_message(reply_token, reply)
#        self.go_back()

    def on_enter_add(self, event):
        print("add")
        reply_token = event.reply_token
        read = read_txt("change.txt")
        t = read.split(" ")
        t_name = get_t_name(t[0])
        if t_name == "0":
            reply = "格式錯誤\n結束新增\刪除請輸入\"結束\""
        else:
            if check(t_name, t[1]) == -1:
                read = read_txt(t_name)
                read = read + " " + t[1]
                write_txt(t_name, read)
                reply = t[1] + " 新增成功\n結束新增\刪除請輸入\"結束\""
            else:
                reply = "該品項已經存在\n結束新增\刪除請輸入\"結束\""
        send_text_message(reply_token, reply)
#        self.go_back()

    def on_enter_delete(self, event):
        print("delete")
        reply_token = event.reply_token
        read = read_txt("change.txt")
        t = read.split(" ")
        t_name = get_t_name(t[0])
        if t_name == "0":
            reply = "格式錯誤\n結束新增\刪除請輸入\"結束\""
        else:
            if check(t_name, t[1]) != -1:
                read = read_txt(t_name)
                r = read.split(" ")
                r.remove(t[1])
                write = ""
                for i in range(len(r)):
                    write = write + r[i]
                write_txt(t_name, write)
                reply = t[1] + " 新增成功\n結束新增\刪除請輸入\"結束\""
            else:
                reply = "該品項已經存在\n結束新增\刪除請輸入\"結束\""
        send_text_message(reply_token, reply)
#        self.go_back()
    # on_exit

#    def on_exit_menu(self):
#        print("Leaving menu")

#    def on_exit_random(self):
#        print("Leaving random")

#    def on_exit_meat(self):
#       print("Leaving meat")

#    def on_exit_veg(self):
#        print("Leaving vegetable")

#    def on_exit_side_dish(self):
#        print("Leaving side dish")

#    def on_exit_soup(self):
#        print("leaveing soup")

#    def on_exit_other(self):
#        print("Leaving other")

