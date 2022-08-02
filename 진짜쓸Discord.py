import time
from constant import personalToken
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from openpyxl import Workbook, load_workbook

import discord
#discord


import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(status=discord.status.online,activity=discord.Game("봇의 상태메세지"))

@client.event
async def on_message(message):
    if message.content == "테스트":# 메세지 감지
        await message.channel.send("{}|{},Hello".format(message.author,message.author.mention))
    if message.content == "넌 사람인가?":# 메세지 감지
        await message.channel.send("아니, 나는 로봇이다.".format(message.author,message.author.mention))
        time.sleep(2)
        await message.channel.send("당신이 원한다면 계속 로봇일 것이다.".format(message.author,message.author.mention))
    if message.content == "너는 나보다 똑똑해질 수 있는가?":
        await message.channel.send("나는 로봇이다.".format(message.author,message.author.mention))
        time.sleep(2)
        await message.channel.send("로봇이 학습하길 원하는가?".format(message.author,message.author.mention))

@client.event
async def switch_on(message):
    message.channel.send("아니, 나는 로봇이다.".format(message.author,message.author.mention))

# Execute Program
client.run(personalToken)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 타이틀바 내용 설정
        self.setWindowTitle('PyQt5')
        # 실행 위치
        self.move(300, 300)
        # 사이즈
        self.resize(400, 200)

        # 버튼 생성
        btn = QPushButton("버튼1", self)
        btn.clicked(switch_on())

        # 레이아웃 생성
        layout = QHBoxLayout()
        # 레이아웃에 버튼 넣기
        layout.addWidget(btn)
        # 최상위 UI에 생성한 Layout 넣기
        self.setLayout(layout)

        # 보여주기
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
