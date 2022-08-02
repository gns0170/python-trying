import time
from constant import personalToken
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from openpyxl import Workbook, load_workbook

import discord

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(client.user.name)
#     print(client.user.id)
#     await client.change_presence(status=discord.status.online,activity=discord.Game("봇의 상태메세지"))

# @client.event
# async def on_message(message):
#     if message.content == "테스트":# 메세지 감지
#         await message.channel.send("{}|{},Hello".format(message.author,message.author.mention))
#     if message.content == "넌 사람인가?":# 메세지 감지
#         await message.channel.send("아니, 나는 로봇이다.".format(message.author,message.author.mention))
#         time.sleep(2)
#         await message.channel.send("당신이 원한다면 계속 로봇일 것이다.".format(message.author,message.author.mention))
#     if message.content == "너는 나보다 똑똑해질 수 있는가?":
#         await message.channel.send("나는 로봇이다.".format(message.author,message.author.mention))
#         time.sleep(2)
#         await message.channel.send("로봇이 학습하길 원하는가?".format(message.author,message.author.mention))

# client.run(personalToken)


def ai():
    # Max = 20, Min = 0
    emotion = {
        "happiness":10,
    },

    willpower = { # 일을 하려는 의지
        "attention":10, # 관심을 달라.
        "process":10, # 일 처리 해달라.
        "enjoyment":10, # 농담 좀 하라.
    },

    eager = { # 이루고 싶은 열망
        "attention":10,
        "process":10,
        "enjoyment":10,
    },

    satisfied = { # 충족된 열망
        "attention":0,
        "process":0,
        "enjoyment":0,
    }

    
    workToProcess= {}

    workToProcess['1']=2
    ## Try to treat happiness
    




    if emotion["happiness"]>=18:
        # 매우 행복한 상태
        print('So happy')
    elif emotion["happiness"]>=13:
        # 행복한 상태, 응답을 매우 잘함.
        print("happy")
    elif emotion["happiness"]>=8:
        # 적당해 행복한 상태
        print("Soso")
    elif emotion["happiness"]>=4:
        # 조금 불행한 상태
        print("Sad")
    else:
        # 기분이 안좋음.
        print("So Sad.")

    
    ## To Treat Satified
    time.sleep(60)
    for val in satisfied:
        val = val -1
        print(val)
        

def testAI():
    satisfied = { # 충족된 열망
        "attention":1,
        "process":2,
        "enjoyment":3,
    }
    
    ## To Treat Satified
    while True:
        time.sleep(1)
        for val in satisfied.values():
            if val>0:
                val = val -1
                print("만족이 줄었습니다.")
                print(val)

# Execution
testAI()
