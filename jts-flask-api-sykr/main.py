# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:45:55 2019

@author: hp
"""

from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
from flask import request
from datetime import datetime

from flask_cors import CORS, cross_origin
from wtforms import TextField,TextAreaField, SubmitField
from wtforms.validators import Required
 
import sys
import os
import datetime
import calendar

import pickle

import json


########################################################################
######### CHAT BOT VARIABLES
########################################################################

import mysql.connector
import datetime
import time
from dateutil import relativedelta
from flask import Flask, jsonify, request
import os
import traceback
import json
import random
import requests

now = datetime.datetime.now()
now1= now + datetime.timedelta(days=1)
now2= now + datetime.timedelta(days=2)
now3= now + datetime.timedelta(days=3)
now4= now + datetime.timedelta(days=4)
now5= now + datetime.timedelta(days=5)
now6= now + datetime.timedelta(days=6)

# Define the messages

all_okay_message = """
All Okay.
"""


welcome_message = """
こんにちは。アプリ登録ありがとうございます。
私の名前はミライです。
私は、あなた専属の美容コンシェルジュです。
サロンの予約受付は私が行います。
さらに、
サロンのこと、
美容のこと、
わからないことがあれば何でも解決策を考えます。
知りたい情報はいち早くお伝えいたします。
あなたの人生が楽しく、そして快適に過ごせるように・・・
全力でお手伝いいたします。
どうぞよろしくお願いいたします。
"""

ask_name_message = """
あなたのお名前は？
"""
is_nickname_message = """
とっても可愛いお名前ですね。
ニックネームはありますか？
"""


#is_confirm_message = """
#確認しますか？
#"""

is_confirm_message = """
予約を確定してよろしいですか？
"""

wrong_is_nickname_message = """
ニックネームがあるかどうかについて有効な応答を入力してください。
はいの場合は1、いいえの場合は2を押します。
"""

wrong_is_reservation_now_message = """
今すぐ予約するかどうかの有効な回答を入力してください。
「はい」の場合は1、「いいえ」の場合は2を押します。
"""

wrong_is_time_for_more_message = """
他に質問があるかどうかについて、有効な回答を入力してください。
はいの場合は1、いいえの場合は2を押します。 
"""

wrong_is_confirm_message = """
確認するかどうかについて有効な回答を入力してください。
はいの場合は1、いいえの場合は2を押します。 
"""
wrong_cust_type_of_salon_message = """
表示されたオプションから有効な種類のサロンを入力してください。 
"""

wrong_cust_service_message = """
表示されたオプションから有効なサービスを入力してください。    
"""

wrong_cust_avail_options_message = """
表示されたオプションから有効なスタッフと時間を選択してください。 
"""

wrong_cust_sub_service_message = """
表示されたオプションから有効なメニュー項目を入力してください。
"""

ask_nickname_message = """
ニックネームは何ですか？
"""

ask_alt_time_message = """
何時がいいですか？ 
"""

ask_alt_date_message = """
で施術可能な日付はこちらです 
"""
ask_birthday_message = """
いいですね。ありがとうございました{0}。
今後も仲良くしてください。
    
お誕生日を教えていただけますか {1}？
"""
ask_birthday_without_nickname_message = """
お誕生日を教えていただけますか？
"""



is_time_for_more_message = """
そうなんですね。
もう少し質問に答えていただける時間はありますか？
"""

ask_phone_message = """
ありがとうございます。
電話番号を教えてください。
"""

ask_color_message = """
ありがとうございます。
{0}、何色がお好きですか？
"""

ask_color_without_nickname_message = """
ありがとうございます。
何色がお好きですか？
"""
ask_hobbies_message = """
いい色ですよね。このカラーを選んだあなたの特徴は
{0} 
あなたの趣味は何ですか？
"""

ask_hobbies_message_1 = """
いい色ですよね。このカラーを選んだあなたの特徴は
{0} 
"""
ask_hobbies_message_2 = """
あなたの趣味は何ですか？
"""

confirmed_message = """
あなたの予約は確認されました。 あなたの予約番号は：{0}

今後も様々なご要望にお応えしていきます。
ぜご予約を取りたい時など、何かありましたら、お知らせください。

もう少し質問に答えていただける時間はありますか？
"""

confirmed_without_more_message = """
あなたの予約は確認されました。 あなたの予約番号は：{0}

今後も様々なご要望にお応えしていきます。
ぜご予約を取りたい時など、何かありましたら、お知らせください。
"""

red_idea = """
個性的でありたい、目立ちたい願望が強く、好奇心旺盛。少し感情的になる面もあるため、自生が必要なときもある。
面倒見がよくリーダーシップを発揮し、行動的でみんなから慕われます。根が楽天的で、細かいところは気にしなくておおざっぱです。
外見的が物静かに見える人でも落ち着いた外見とは裏腹に激しい情熱や欲望を秘めています。
"""

orange_idea = """
陽気で社交的な性格。
物事にあまりこだわらず、諦めが早い。温かい心の持ち主で、人なつっこく、誰からも愛される人柄。
人生に対して常に意欲的で、かなりの社交家です。人が集まる場所では常に注目のまとになるでしょう。
"""


yellow_idea = """
明るく、話し上手で表現力豊かな人です。好奇心旺盛で、つねに新しいことを求めている個性派。
社交的でユーモアのセンスも抜群なので、人の輪の中心にいるタイプです。
明るく可愛い、天真爛漫な性格。知的なのに子供っぽく、ユーモアセンスがあるので、人から好かれやすい。
"""

green_idea = """
基本的に穏やかで、何事においても堅実さが際立ち、我慢強さもあります。手堅く成功をおさめるタイプと言えるでしょう。
忍耐強く、優しい性格。争いごとを好まず、穏やかな日常を願う。
礼儀正しく、決して人の道を踏み外さない人。
人と協調したいので自己主張が弱く、優柔不断な面も見られます
"""

purple_idea = """
冷静で理知的、一つの枠の中で自制できる従順さを持っています。
理知的で誠実、控えめな内向的な性格。どんなことにも感情的にならず、冷静に物事を判断できる。
自制心はありますが、内向的で保守的な面もあり、自分の考え方は常に正しいと思っている事が多いようです。
整理整頓が得意で、創造性に富み、内向的な人が好む傾向があります。
"""

pink_idea = """
どんなときでも大きな心で受け止める愛情深い人。
優しく穏やかなロマンチスト。
デリケートで傷つきやすく人のちょっとした言葉や態度に、いつまでもくよくよしがちです。
"""

brown_idea = """
責任感があり、チームワークを作り出す特技を持っているのが特徴
自己表現が下手な人が多い。自分を犠牲にして他人に尽くすタイプ。
"""

gray_idea = """
優柔不断で自己中心的な性格。だれとでも調子を合わせることができ、自分を主張しない反面、人から干渉されることを嫌う。
感情をあまり表面に出さないので、クールでおとなしい人と見られる。
"""

white_idea = """
気高く、つねに完璧を求めて努力するタイプ。
純粋で誠実、潔癖、真面目で、素直、無邪気な性格
"""

black_idea = """
感情を溜め込む傾向があり、子供っぽいことが嫌いで、クールで大人な自分をアピールする。
人から命令されたり、強制されることを嫌う。プライドを傷つけられることを好まない面を持つ
意思が強く、少し頑固。いつも情熱を抑えている人。人を動かす才能はあるけれど、明るさと素直さに欠ける面も。
"""

blue_idea = """
冷静で理知的、一つの枠の中で自制できる従順さを持っています。
理知的で誠実、控えめな内向的な性格。どんなことにも感情的にならず、冷静に物事を判断できる。
"""




"""
def color_menu_int_to_idea(argument):
    argument = int(argument)
    switcher = {
        1:	"暖かさと愛",
        2:	"ケアと育成",
        3:  "元気と創造性",
        4:  "快適さと活気",
        5:  "耐久性と楽観主義",
        6:	"プロフェッショナリズムと忠誠心",
        7:  "王族と貴族",
        8:  "伝統主義と知性", 
        9:  "自信と信頼性",
        10: "優雅さと洗練された", 
        11: "平和と単純さ"
    }
    return switcher.get(argument, "nothing")
"""
def color_menu_int_to_idea(argument):
    argument = int(argument)
    switcher = {
        1: red_idea,
        2: pink_idea,
        3: orange_idea,
        4: yellow_idea,
        5: green_idea,
        6: blue_idea,
        7: purple_idea,
        8: gray_idea, 
        9: brown_idea,
        10: black_idea, 
        11: white_idea 
    }
    return switcher.get(argument, "nothing")

"""
1: "Red",
2: "Pink",
3: "Orange",
4: "Yellow",
5: "Green",
6: "Blue",
7: "Purple",
8: "Gray",
9: "Brown",
10: "Black",
11: "White"
"""


"""
switcher1 = { 
        "書くこと": 1, 
        "def": 2,
        "読書"：3,
        "スポーツ"：3,
        "音楽"：5,
        "旅行"：6,
        "ガーデニング"：7,
        "映画"：88,
        "ゲーム"：55,
        "編み物"：88,
        "空手"：89
} 
"""

def hobby_to_idea(hobby_string):

    hobby_dict = { 

        "スポーツ観戦" : "スポーツ観戦は、特にあなたの好きなチームが勝利したときにリラックスするのに役立ちます。",
    
        "スポーツ" : "スポーツをすることは運動だけでなく楽しみにもなり得ます。",
    
        "運動" : "運動は健康で幸せな滞在をするのに役立ちます",
    
        "ジム" : "ジムは健康維持に役立ちます。",
    
        "ヨガ" : "ヨガは古代インドのテクニックで、心身ともに良いものです。",
    
        "ネットサーフィン" : "インターネットサーフィンはあなたがあなたの家の快適さで世界についてのあなたの知識を増やすのを助けることができます。",
    
        "ゲーム":"ゲームをすることはあなたにスポーツの精神を植え付ける", 
    
        "アプリゲーム":"アプリのゲームは楽しいですし、どこでも遊べます",
    
        "睡眠":"睡眠は体の適切な機能のために必要です",
    
        "アニメ鑑賞":"最近のアニメは世界中で人気があります。",
    
        "食べること":"あなたの好きな食べ物を持っていることは最も楽しい経験の一つになることができます。",
    
        #"アイドル":"
    
        "コンサート": "あなたのお気に入りのバンドが演奏しているときにコンサートは特に素晴らしいです。",
    
        "英語": "英語は世界中の人々とのコミュニケーションを助けます。",
    
        "お笑い": "コメディを見ることはあなたを幸せにすることができます。",
    
        "お笑い芸人":"人々を笑わせることはあなたに内なる満足を与えることができます。",
    
        "テレビ鑑賞":"テレビは週末に最適なパスタイムです。",

        "映画":"映画は友達や家族と一緒に楽しめる素晴らしい経験です。",
    
        "貯金":"貯蓄はあなたの経済的未来に不可欠です。",
    
        "献血":"それが命を救うのを助けることができるので、献血は素晴らしい趣味です。",
    
        #"映画鑑賞"
    
        "ドライブ":"運転はあなたの家から出てあなたの周りを楽しむためのクールな方法です。",
    
        "旅行":"旅行は私たちが新しい人と出会い、異なる文化を理解するのを助けます。",
    
        "写真":"写真撮影は本当にクールな趣味です。",
    
        "カメラ":"カメラはとても楽しいです。",
    
        "音楽":"音楽は世界共通の言語であり、最も古い芸術形式の一つです。",

    
        "楽器":"楽器は素晴らしいです。 アインシュタインでさえバイオリンを弾いた。",
    
        "ギター":"ああ！あなたはロックスターです！",
    
        "ピアノ":"ピアノは美しい響きの楽器です。",
    
        #"コンサート"
    
        "読書":"ああ！ あなたは知的な種類のようです。",
    
        "マラソン":"あなたは珍しい人です。 多くの人はマラソンを走ることができません。",
    
        "ランニング":"ランニングヘルプあなたはより速くあなたの目的地に到達するのと同様に健康を維持します。",
    
        "野球":"野球は世界中で急速に人気が高まっています。",

        "バッティングセンター":"バッティングセンターは本当にかっこいいです。",
    
        "ゲームセンター":"ゲームセンターは楽しい時間です。",
    
        "食べ歩き":"食べ歩きはシンプルでクールな趣味です。",
    
        "料理":"料理はあなたや他の人を幸せにするものです。",
    
        "お菓子作り":"お菓子は私のお気に入りのものです。 仲良くしましょう。",
    
        "食べること":"食べることも私が楽しむものです。",
    
        "花":"花はきれいです。 私はそれらがとても好きです。",
    
        "ガーデニング": "ガーデニングはすごいです。 それはあなたが環境に情熱を持っていることを示しています。",
    
        "海外ドラマ":"海外のドラマも好きです。",
    
        "編み物":"編み物はあなたが家で服を製造するのを助ける素晴らしい趣味です。",
    
        "DIY":"DIYはとても楽しいです。",
    
        "ダンス":"ダンスは素晴らしい運動です。",
    
        "フラダンス":"フラフープダンスは素晴らしい運動です。",
    
        "ベリーダンス":"ベリーダンスは運動の素晴らしい形です。",
    
        "ヒップホップ": "ヒップホップミュージックは、人々が自分自身を簡単に表現するのを助けます",
    
        "コーヒー": "コーヒーは長い一日の後にあなたの心をリフレッシュさせる",
    
        "勉強": "勉強することはあなたがあなたの心を育てるのを助けます。",
    
        #"ロック":

   
        #"インターネット"

    }   

    out_msg = ""
    
    for key in hobby_dict:
        if key in hobby_string: 
            out_msg = out_msg + hobby_dict[key] + " " 
    if out_msg == "": 
            if "しない" in hobby_string or "何もない" in hobby_string or "いいえ" in hobby_string:
                out_msg = "趣味？まれです！私はあなたが秘密を守っていると思います。"
    if out_msg == "": 
        out_msg = "いい趣味をお持ちですね。"

    return out_msg



"""
def hobby_to_idea(argument):
     
    switcher = {
        #"書くこと" ："私も時々書くのが好きです",
        #"読書"："ああ！ あなたは知的なタイプのようです！",
        #"スポーツ"："うーん、あなたはアテロームです。",
        #"音楽"："私も音楽が好き",
        #"旅行"："私はいつか世界を旅行するつもりです",
        #"ガーデニング"："私は自分の庭を持っていました。",
        #"映画"："私も北野武の映画を見るのが大好き",
        #"ゲーム"："クール、私たちは仲良くします。 私はPUBGのプロです",
        #"編み物"："それは本当にクールだ、私も編み物が大好き",
        #"空手"："周りにいるとき私は注意する必要があります！"
    }
    

    return switcher.get(argument, "かっこいい。私もそのような趣味を持ちたいです")
"""
def color_menu_int_to_name(argument):
    print("Inside Switcher")
    print("Argument:" + str(argument) + "Arg")
    print(type(argument))
    try:
        argument = int(argument)
    except:
        return "nothing"
     
    switcher = {
        1:	"赤",
        2:	"ピンク",
        3: "オレンジ",
        4: "黄色",
        5: "緑",
        6:	"青",
        7:  "紫",
        8:  "グレー", 
        9: "茶色",
        10: "黒", 
        11: "白"
    }

    #x = switcher[argument]
    #print(x)
    return switcher.get(argument, "nothing")

ask_type_of_salon_message = """
ありがとうございます。
どんな美容サロンが好きですか？
"""

new_welcome_message = """
おかえりなさい {0}
今日は何をお手伝いしましょうか？
"""

new_welcome_without_nickname_message = """
おかえりなさい
今日は何をお手伝いしましょうか？
"""

#いい色ですよね。この色は {0}

is_reservation_now_message = """
わかりました。
お客様の期待に答えられるように、努めてまいります。
    
次回予約をお取りしましょうか？
"""

is_reservation_now_message_1 = """
わかりました。
お客様の期待に答えられるように、努めてまいります。
"""
is_reservation_now_message_2 = """
次回予約をお取りしましょうか？
"""
ask_date_message = """
かしこまりました。
ご予約のお日にちはいつがよろしいですか？
"""

ask_service_message = " メニューはお決まりですか？"

empty_name_message = """
正しい名前を入力してください。 
"""

empty_nickname_message = """
正しいニックネームを入力してください。
"""


empty_phone_message = """
正しい電話番号を入力してください。
"""
wrong_color_message = """
色の正しいオプションを選択してください。  
"""

wrong_hobby_message = """
あなたの趣味として何かを入力してください。
"""


wrong_service_message = """
正しいサービスを選択してください。
"""


wrong_date_message = """
正しい形式で正しい日付を入力してください。
例：2019年6月21日の場合は、次のいずれかを入力します。

1）2019年6月21日
2）2019-06-21
"""

good_date_message = """
Alright!
    
What time would be convenient for you?
    
Example: enter 13:00 for 1pm
"""


get_time_message = """
    Alright!
    
    What time would be convenient for you?
    
    Example: enter 13:00 for 1pm
    """

wrong_time_message = """
正しい形式で時間を入力してください。
例：午後1時に13:00と入力
"""

select_date_message = """
    Okay, Please tell me which date.
    1) %s
    2) %s
    3) %s
    4) %s
    5) %s
    6) %s
    7) %s
    """  % (now.strftime("%Y-%m-%d"),now1.strftime("%Y-%m-%d"),now2.strftime("%Y-%m-%d"),now3.strftime("%Y-%m-%d"),now4.strftime("%Y-%m-%d"),now5.strftime("%Y-%m-%d"),now6.strftime("%Y-%m-%d"))



"""
local_connection = mysql.connector.connect(
                                           host="localhost",
                                           user="root",
                                           passwd="12345678",
                                           database="test"
                                           )

local_cursor = local_connection.cursor()
"""


mydb = mysql.connector.connect(
                               host="34.85.64.241",
                               user="jts",
                               passwd="Jts5678?",
                               database="jtsboard_jts"
                               )
mycursor = mydb.cursor()

slot_list = ["00:00:00","00:30:00","01:00:00","01:30:00","02:00:00","02:30:00","03:00:00","03:30:00",
             "04:00:00","04:30:00","05:00:00","05:30:00","06:00:00","06:30:00","07:00:00","07:30:00",
             "08:00:00","08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00",
             "12:00:00","12:30:00","13:00:00","13:30:00","14:00:00","14:30:00","15:00:00","15:30:00",
             "16:00:00","16:30:00","17:00:00","17:30:00","18:00:00","18:30:00","19:00:00","19:30:00",
             "20:00:00","20:30:00","21:00:00","21:30:00","22:00:00","22:30:00","23:00:00","23:30:00"]


def get_date_in_ddmmyyyy_format(inp_str):
    status = 0 
    try:
        print("inside try") 
        inp_str = inp_str.replace("日","")
        inp_str = inp_str.replace("月","-")
        inp_str = inp_str.replace("年","-")

        print("inp_str")
        print(inp_str)
            
        str_list = inp_str.split("-")

        if len(str_list) == 3:
            print("year included")
            day = str_list[2]
            month = str_list[1]
            year = str_list[0]

            if len(day) == 1:
                if int(day) < 10:  
                    day = "0" + day  

            if len(month) == 1:
                if int(month) < 10:  
                    month = "0" + month 
                     
            status = 1   
            out_date = day + "-" + month + "-" + year 
            date_obj = datetime.datetime.strptime(out_date, '%d-%m-%Y')
            
        elif len(str_list) == 2:

            print("year not included")
            print("year not included")
            print("year not included")
            print("year not included")

            day = str_list[1]
            month = str_list[0]
            print("year not included")
            now = datetime.datetime.now()
            year= str(now.year)
            print("here")
            if len(day) == 1:
                if int(day) < 10:  
                    day = "0" + day  

            if len(month) == 1:
                if int(month) < 10:  
                    month = "0" + month 
            status = 1   
            out_date = day + "-" + month + "-" + year 
            print("out_date")
            print(out_date)
            date_obj = datetime.datetime.strptime(out_date, '%d-%m-%Y')
            print("date_obj")
            print(date_obj)
        else:
            out_date = ""  
            status = 0 
            return status, out_date,wrong_date_message
    except:
            out_date = ""  
            status = 0 
            return status, out_date,wrong_date_message
                
    return status,date_obj,all_okay_message



"""

def get_date_in_ddmmyyyy_format(inp_str):
    try:
        inp_str = inp_str.replace("日","")
        inp_str = inp_str.replace("月","-")
        inp_str = inp_str.replace("年","-")
        
        str_list = inp_str.split("-")
        day = str_list[2]
        month = str_list[1]
        year = str_list[0]

        if len(day) == 1:
            if int(day) < 10: 
                day = "0" + day 

        if len(month) == 1:
            if int(month) < 10: 
                month = "0" + month 
        
        status = 1 
        out_date = day + "-" + month + "-" + year
        date_obj = datetime.datetime.strptime(out_date, '%d-%m-%Y')
        print("\n\n9999999999999999999999999999999999999999\n\n")
        print(date_obj)
        print("\n\n9999999999999999999999999999999999999999\n\n")
        
    except:
            out_date = ""
            status = 0
            return status, out_date,wrong_date_message
    
    return status,date_obj,all_okay_message
"""


def insert_into_chats_db(user_id,ip,name,is_nickname,nickname,birthday,is_time_for_more,phone,color,type_of_salon,is_reservation_now,res_date,res_time,service_id,emp_id,is_confirm,last_state):

    sql = "insert into chats values(default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    insert_tuple = (user_id,ip,name,is_nickname,nickname,birthday,is_time_for_more,phone,color,type_of_salon,is_reservation_now,res_date,res_time,service_id,emp_id,is_confirm,last_state)
    
    mycursor.execute(sql,insert_tuple)
    
    mydb.commit()



def insert_into_session_db(ip,STATE,return_list_of_dicts,return_dict,cust_responses):

    print("\n\nInside insert session\n\n")
    print("HHHHHHHHHHH" + return_list_of_dicts + "IIIIIIIIIIII")
    #return "nothing"

    #sql = "insert into session(ip,STATE,return_list_of_dicts,return_dict,cust_responses) values(%s,%s,%s,%s,%s)"
    sql = "insert into sessions(ip,STATE,return_list_of_dicts,return_dict,cust_responses) values(%s,%s,%s,%s,%s)"
    
    insert_tuple = (ip,STATE,return_list_of_dicts,return_dict,cust_responses)
    
    mycursor.execute(sql,insert_tuple)
    
    mydb.commit()


def update_session_db(ip,STATE,return_list_of_dicts,return_dict,cust_responses):
    
    #sql = "update session set STATE = %s, return_list_of_dicts = %s, return_dict = %s,cust_responses= %s where ip = %s"
    sql = "update sessions set STATE = %s, return_list_of_dicts = %s, return_dict = %s,cust_responses= %s where ip = %s"
    insert_tuple = (STATE,return_list_of_dicts,return_dict,cust_responses,ip)
    mycursor.execute(sql,insert_tuple)
    mydb.commit()


def generate_reservation_number():
    print("run")
    low =  10000000
    high =  99999999
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    al = random.choice(letters)
    num = str(random.randint(low,high))
    new_code = "M" + al + num 
    sql = """select reservation_number from reservations"""
    mycursor.execute(sql)
    myresult_list = mycursor.fetchall()
    found = 0 
    for code_tuple in myresult_list:
        exist_code_ba = code_tuple[0]
        exist_code = exist_code_ba.decode() ; exist_code
        if new_code == exist_code:
            found = 1 
            break
    if found == 0:
        return new_code
    elif found == 1:
        generate_reservation_number()


def delete_from_reservations_table(r_num):

    r_num_status = 0 

    select_sql = """select * from reservations where reservation_number = %s"""
    select_tuple = (r_num,)
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()
        
    if len(myresult_list) == 0:
        r_num_status = 0 
    else:
        r_num_status = 1
        update_sql = """update reservations set reservation_type = 5 where reservation_number = %s"""
        #delete_sql = """delete from reservations where reservation_number = %s"""
        update_tuple = (r_num,)
        mycursor.execute(update_sql,update_tuple)
        mydb.commit()
    return r_num_status


def insert_into_reservations_table(u_id,c_id,s_id,ss_id,e_id,s_date,e_date,s_time,e_time,total):

    ex_s_date = s_date + " 00:00:00"
    ex_e_date = e_date + " 00:00:00" 
    r_num = generate_reservation_number() 
    now_obj = datetime.datetime.now()
    now_str = str(now_obj)
    print("generated code successfully")

    insert_sql = """
        insert into reservations
        (id,user_id,customer_id,service_id,
        sub_service_id,employee_ids,reservation_number,
        start_date,end_date,extra_start_date,
        extra_end_date,start_time,end_time,
        reservation_type,reservation_total,
        used_points,payment_total,status,created,modified,note)
        values(default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'1',%s,'0',%s,1,%s,%s,'')
    """
   
    insert_tuple = (
        u_id,c_id,s_id,ss_id,e_id,r_num,s_date,e_date,
        ex_s_date,ex_e_date,s_time,e_time,total,total,
        now_str,now_str
    )

    mycursor.execute(insert_sql,insert_tuple)
    mydb.commit()

    print("yahaan hoon")
        
    select_sql1 = """select id from reservations where reservation_number = %s"""
    select_tuple1 = (r_num,)
    mycursor.execute(select_sql1,select_tuple1)
    myresult_list = mycursor.fetchall()

    print("yahaan hoon")
    tuple0 = myresult_list[0]
    r_id = tuple0[0]
    
    return r_num,r_id


#def insert_into_customers_table(c_name,c_kana,c_dob,c_tel,user_id,device_id,device_token):
def insert_into_customers_table(c_name,c_kana,c_dob,c_tel,user_id):

    na = c_name.split(' ')
    if len(na) == 1:
        c_first_name = na[0] 
        c_last_name = ""  
    else:
        c_first_name = na[1] 
        c_last_name = na[0] 

    nna = c_kana.split(' ')
    if len(nna) == 1:
        c_kana_first_name = nna[0] 
        c_kana_last_name = ""  
    else:
        c_kana_first_name = nna[1] 
        c_kana_last_name = nna[0] 
    
    select_sql = """select * from customers where user_id = %s and name = %s and tel = %s"""
    select_tuple = (user_id,c_name,c_tel)

    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()

    
    if len(myresult_list) == 0:
        now_obj = datetime.datetime.now()
        now_str = str(now_obj)
        insert_sql = """ 
            insert into customers (user_id,name,first_name,last_name,kana,
            kana_first_name,kana_last_name,dob,tel,created,modified) 
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        insert_tuple = (
            user_id,c_name,c_first_name,c_last_name,
            c_kana,c_kana_first_name,c_kana_last_name,
            c_dob,c_tel,now_str,now_str
        )

        mycursor.execute(insert_sql,insert_tuple)
        
        
        mydb.commit() 

        select_sql1 = """select * from customers where user_id = %s and name = %s and tel = %s"""
        select_tuple1 = (user_id,c_name,c_tel)
        mycursor.execute(select_sql1,select_tuple1)
        myresult_list = mycursor.fetchall()
    
        tuple0 = myresult_list[0]
        c_id = tuple0[0]
    else:
        tuple0 = myresult_list[0]
        c_id = tuple0[0]
   
    return c_id


def find_employee_name(user_id):
    select_sql = """select id,name from employees where user_id = %s and is_technician = 1 order by service_id """
    select_tuple = (user_id,) 
    mycursor.execute(select_sql,select_tuple)

    myresult_list = mycursor.fetchall()
    emp_name_dict = dict()

    for emp_tuple in myresult_list:
        emp_name_dict[emp_tuple[0]] = [emp_tuple[1]]

    return emp_name_dict


def get_services(user_id):

    print("user_id")
    print(user_id)

    select_sql = """
        select id, name from services where id in 
        (select distinct service_id from employees 
        where user_id = %s and is_technician = 1 and service_id in 
        (select distinct service_id from sub_services where user_id = %s));
    """

    select_tuple = (user_id,user_id)
    
    mycursor.execute(select_sql,select_tuple)
    
    myresult_list  = mycursor.fetchall()
    
    s_dict = dict()
    menu_int = 1 

    for serv_tuple in myresult_list:
        #print("_______")

        s_id = serv_tuple[0]
    
        serv_tuple_second = serv_tuple[1]
        s_name = serv_tuple_second.decode() ; s_name 

        s_dict[str(menu_int)] = {"id": s_id, "name": s_name}
    
        menu_int += 1

    return s_dict


def get_super_services(service_id,user_id):

    print("inside get sub serices")
    print("service_id","user_id")
    print(service_id,user_id)
    sql = """select id,name from sub_services where user_id = %s and status = 1 and service_id = %s and parent_id = %s"""
    select_tuple = (user_id,service_id,0)
    
    mycursor.execute(sql,select_tuple)
    myresult_list  = mycursor.fetchall()
    print("myresult_list") 
    print(myresult_list) 
    sup_serv_dict = dict()
    menu_int = 1 

    for serv_tuple in myresult_list:
        #print("_______")

        sup_serv_id = serv_tuple[0]
    
        serv_tuple_second = serv_tuple[1]
        sup_serv_name = serv_tuple_second.decode() ; sup_serv_name 
    
        sup_serv_dict[str(menu_int)] = {"id": sup_serv_id, "name": sup_serv_name}
    
        menu_int += 1
    
    print("sup_serv_dict")
    print(sup_serv_dict)

    return sup_serv_dict

def get_sub_services(service_id,user_id):

    print("inside get sub serices")
    print("service_id","user_id")
    print(service_id,user_id)
    sql = """select id,name,duration,price from sub_services where user_id = %s and status = 1 and service_id = %s"""
    select_tuple = (user_id,service_id)
    
    mycursor.execute(sql,select_tuple)
    myresult_list  = mycursor.fetchall()
    print("myresult_list") 
    print(myresult_list) 
    ss_dict = dict()
    menu_int = 1 

    for serv_tuple in myresult_list:
        #print("_______")

        ss_id = serv_tuple[0]
    
        serv_tuple_second = serv_tuple[1]
        ss_name = serv_tuple_second.decode() ; ss_name 
    
        serv_tuple_third = serv_tuple[2]
        ss_duration = serv_tuple_third.decode() ; ss_duration 
    
        serv_tuple_fourth = serv_tuple[3]
        ss_price = serv_tuple_fourth.decode() ; ss_price

        ss_dict[str(menu_int)] = {"id": ss_id, "item": ss_name, "duration": ss_duration, "price": ss_price}
    
        menu_int += 1
    print("ss_dict")
    print(ss_dict)

    return ss_dict

def find_employees_for_service(service_id,user_id):


    print("inside find employees for service")
    print("service_id,user_id")
    print(service_id,user_id)
    
    select_sql = """select service_id,id from employees where user_id = %s and is_technician = 1 order by service_id"""
    select_tuple = (user_id,)
    mycursor.execute(select_sql,select_tuple)

    myresult_list = mycursor.fetchall()

    print("myresult_list")
    print(myresult_list)
        
    service_dict = dict()

    for serv_tuple in myresult_list:
        if serv_tuple[0] in service_dict:
            service_dict[serv_tuple[0]].append(serv_tuple[1])
        else:
            service_dict[serv_tuple[0]] = [serv_tuple[1]]

    print("service_dict[service_id]")
    print(service_dict[service_id])

    return service_dict[service_id]

#def check_availability(service_int, date_time_obj,employee_list,time_duration):
#    return result_list


def check_new_availability(date_time_obj,employee_list,time_duration,user_id):
    print("Check New Availability")
    print("date_time_obj,employee_list,time_duration,user_id")
    print(date_time_obj,employee_list,time_duration,user_id)
    #return 0

    result_dict = {}
    date_format = date_time_obj.strftime("%Y-%m-%d")
    time_format = date_time_obj.strftime("%H:%M:%S")
    
    for employee in employee_list:
        print("\n\n\nEmployee\n\n\n")
        employee_schedule = []
        for i in range(48):
            employee_schedule.append(0)

        select_sql = """
            select service_id, employee_ids, start_date, start_time, end_time 
            from reservations where user_id = %s and reservation_type='1' 
            and start_date = %s and employee_ids = %s
        """

        select_tuple = (user_id, date_format, employee)
        mycursor.execute(select_sql,select_tuple)

        appointments = mycursor.fetchall()
        for appointment in appointments:
            print("--- appointment ---")
            #print(appointment) 
            
            service_id = appointment[0]
            employee_id = appointment[1]
            date = appointment[2]
            start_time = appointment[3]
            end_time = appointment[4]
            start_hour = start_time.seconds//3600
            start_minute = (start_time.seconds//60) % 60
            
            start_slot_number = start_hour * 2
            if start_minute >= 30 and start_minute <= 59:
                start_slot_number += 1
            
            end_hour = end_time.seconds//3600
            end_minute = (end_time.seconds//60) % 60
            
            end_slot_number = end_hour * 2
            
            if end_minute == 0:
                end_slot_number -= 1
            if end_minute > 30 and end_minute <= 59:
                end_slot_number += 1
            
            for i in range(start_slot_number,end_slot_number+1):
                employee_schedule[i] = 1

        print("employee_schedule")
        print(employee_schedule)
    #return 0

     
        num_of_slots_needed = time_duration * 2

        free_slots = []

        slot_i = 20 # Starting at 10:00 AM

        for i in range(3):
            #print("Iteration " + str(i) + " Started")
            zero_count = 0
            
            if i != 0 :     ## Increase slot number
                slot_i += 1 ## from previous iteration
            
            #while slot_i <= 44: # Ending search at 10:00 PM
            while slot_i <= 40: # Ending search at 08:00 PM
                #print("Inside While Loop")
                #print("slot = " + str(slot_i))
                if employee_schedule[slot_i] == 1:
                    zero_count = 0
                else:
                    zero_count += 1
                
                if zero_count == num_of_slots_needed:
                    break
                slot_i += 1

            avail_end_slot = slot_i
            avail_start_slot = avail_end_slot - num_of_slots_needed + 1
        
            free_slots.append(avail_start_slot)
            result_dict[employee] = free_slots
     
    print("result_dict")
    print(result_dict)
    return result_dict


def get_employee_schedule_for_date(date_time_obj,employee_list):

    date_format = date_time_obj.strftime("%Y-%m-%d")
    employee_schedule_dict = {}

    for employee in employee_list:
        print("here")
        employee_schedule = []  
        for i in range(48):
            employee_schedule.append(0)

        select_sql = """ 
            select service_id, employee_ids, start_date, start_time, end_time 
            from reservations where reservation_type='1' 
            and start_date = %s and employee_ids = %s
        """

        select_tuple = (date_format, employee)
        mycursor.execute(select_sql,select_tuple)

        appointments = mycursor.fetchall()

        for appointment in appointments:
            #print("--- appointment ---")
    
            service_id = appointment[0]
            employee_id = appointment[1]
            date = appointment[2]
            start_time = appointment[3]
            end_time = appointment[4]
            start_hour = start_time.seconds//3600
            start_minute = (start_time.seconds//60) % 60  

            start_slot_number = start_hour * 2 
            if start_minute >= 30 and start_minute <= 59: 
                start_slot_number += 1 
    
            end_hour = end_time.seconds//3600
            end_minute = (end_time.seconds//60) % 60  
    
            end_slot_number = end_hour * 2 
    
            if end_minute == 0:
                end_slot_number -= 1 
            if end_minute > 30 and end_minute <= 59: 
                end_slot_number += 1 
    
            for i in range(start_slot_number,end_slot_number+1):
                employee_schedule[i] = 1 
 
        employee_schedule_dict[employee] = employee_schedule

    return employee_schedule_dict



def check_emp_avail_for_time(employee_schedule_dict,start_time,time_duration_in_hours):
    result_dict = {}
    num_of_slots_needed = time_duration_in_hours * 2 

    start_time_split = start_time.split(":")
    start_hour = int(start_time_split[0])
    start_minute = int(start_time_split[1])

    start_slot_number = start_hour * 2 
    if start_minute >= 30 and start_minute <= 59: 
        start_slot_number += 1 
    next_slot_number = start_slot_number + num_of_slots_needed

    for employee in employee_schedule_dict:
        zero_count = 0 
        for slot_i in range(start_slot_number,next_slot_number):
            if employee_schedule_dict[employee][slot_i] == 1:
                zero_count = 0 
            else:
                zero_count += 1
            if zero_count == num_of_slots_needed:
                break

        avail_end_slot = slot_i
        avail_start_slot = avail_end_slot - num_of_slots_needed + 1 

        free_slots = [avail_start_slot,]
        result_dict[employee] = free_slots 
        
    return result_dict



def convert_avail_dict_to_display_options(avail_dict,emp_name_dict):
    print("Convert Avail Dict TO Display Options") 
    print("avail_dict,emp_name_dict")
    print(avail_dict,emp_name_dict)
    #return 0,0,0 
    
    avail_msg = "かしこまりました。次のお日にちで空きがあります。\n"
    #avail_msg = avail_msg + "さて、私たちは以下の時期に空室状況があります：\n"
    option_list = []
    option_new_list = []
    display_options = []

    emp_serial = 1
    
    for emp_id in avail_dict:
        list_of_avail_slots = avail_dict[emp_id]
        for slot in list_of_avail_slots:
            time_start = slot_list[slot]
            
            emp_bytearray_list = emp_name_dict[emp_id]
            emp_bytearray_firstelement = emp_bytearray_list[0]
            emp_name = emp_bytearray_firstelement.decode() ; emp_name
            option_str = str(emp_serial) + ") " + emp_name + " で利用可能です " + str(time_start)
            option_list.append(option_str)

            key = str(emp_serial)
            value = emp_name + " で利用可能です " + str(time_start)

            my_dict = {
                "key": key,
                "value": value
            }
            option_new_list.append(my_dict)
            option = [emp_serial,emp_id,slot]
            display_options.append(option)
            emp_serial += 1

    none_option_str = str(emp_serial) + ") " + "上記の時間のどれも私には合いません。"
    option_list.append(none_option_str)

    none_key = str(emp_serial)
    none_value = "上記の時間のどれも私には合いません。"
    none_dict = {
    "key": none_key,
    "value": none_value
    }
    option_new_list.append(none_dict)

    none_option = [emp_serial,"none","none"]
    display_options.append(none_option)

    print("display_options,option_new_list")
    print(display_options,option_new_list)

    return avail_msg,display_options,option_new_list




def type_of_salon_menu_int_to_name(argument):
    switcher = {
    1: "早く仕上げてくれる",
    2: "安い",
    3: "静かなサロン",
    4: "接客がとてもいいサロン",
    5: "高級感のあるサロン",
    6: "スタッフの質が高いサロン",
    7: "清潔感のあるサロン",
    8: "落ち着いたサロン"

    }

    return switcher.get(argument, "nothing")

"""
def service_menu_int_to_id(argument):
    switcher = {
    1: 1,
    2: 3,
    3: 2
    }

    return switcher.get(argument, "nothing")
"""


def service_menu_int_to_id(argument):
    switcher = {
    1: 1,
    2: 2
    }

    return switcher.get(argument, "nothing")


def service_numbers_to_strings(argument):
    switcher = {
    1: "nails",
    2: "beauty_treatment",
    3: "eye_lashes",
    4: "body",
    5: "hair_removal",
    6: "facial"
    }
    return switcher.get(argument, "nothing")



def welcome_ask_name():
    #return welcome_ask_name_message
    return welcome_message

def ask_name_fun():
    #return welcome_ask_name_message
    return ask_name_message

def is_nickname_fun():
    is_nickname_options = [ 
    {"key":"1", "value":"はい"}, 
    {"key":"2","value": "いいえ"} 
    ]
    return is_nickname_message,is_nickname_options

def ask_nickname():
    return ask_nickname_message

def ask_alt_time_fun():
    return ask_alt_time_message

def ask_alt_date_fun(cust_responses):
    #alt_avail_days = cust_responses["alt_avail_days"]
    alt_avail_days = cust_responses["jap_option_list"] 
    return ask_alt_time_message,alt_avail_days

def ask_birthday(cust_responses):
    if cust_responses["is_nickname"] == "yes":
        nick = cust_responses["nickname"]
        return ask_birthday_message.format(nick,nick)
    else:
        return ask_birthday_without_nickname_message
def confirmed_fun(r_num):
    
    options = [ 
    {"key":"1", "value": "はい、今から大丈夫です。"}, 
    {"key":"2", "value": "今は難しいです。"} 
    ]
    
    return confirmed_message.format(r_num), options

def confirmed_without_more_fun(r_num):
    return confirmed_without_more_message.format(r_num)

def is_time_for_more_fun():
#is_time_for_more_options = ["1) はい、今から大丈夫です。/ I can chat now", "2) 今は難しいです。/ let’s talk later"]

    is_time_for_more_options = [ 
    {"key":"1", "value": "はい、今から大丈夫です。"}, 
    {"key":"2", "value": "今は難しいです。"} 
    ]


    return is_time_for_more_message,is_time_for_more_options

def ask_phone():
    return ask_phone_message

def ask_hobbies_fun(color_idea):
    #return ask_hobbies_message
    #return ask_hobbies_message.format(color_idea)
    return ask_hobbies_message_1.format(color_idea),ask_hobbies_message_2

def ask_color(cust_responses):

    color_options = [  
    {"key":"1", "value": "赤"}, 
    {"key":"2", "value": "ピンク"}, 
    {"key":"3", "value": "オレンジ"},
    {"key":"4", "value": "黄色"},
    {"key":"5", "value": "緑"},
    {"key":"6", "value": "青"},
    {"key":"7", "value": "紫"},
    {"key":"8", "value": "グレー"},
    {"key":"9", "value": "茶色"},
    {"key":"10", "value": "黒"},
    {"key":"11", "value": "白"}
    ]     


    if cust_responses["is_nickname"] == "yes":
        nick = cust_responses["nickname"]
        return ask_color_message.format(nick),color_options
    else:
        return ask_color_without_nickname_message,color_options


def new_welcome_fun(cust_responses):
    new_welcome_options = [
    {"key":"1", "value": "新しい予約を取りたい"},
    {"key":"2", "value": "予約をキャンセルしたい"},
    {"key":"3", "value": "現在の予約を変更したい"},
    ]   
    if cust_responses["is_nickname"] == "yes":
        nick = cust_responses["nickname"]
        return new_welcome_message.format(nick), new_welcome_options
    else:
        return new_welcome_without_nickname_message, new_welcome_options

def ask_type_of_salon():
    ask_type_of_salon_options = [
    {"key":"1", "value": "早く仕上げてくれる。"},
    {"key":"2", "value": "安い。"},
    {"key":"3", "value": "静かなサロン。"},
    {"key":"4", "value": "接客がとてもいいサロン。"},
    {"key":"5", "value": "高級感のあるサロン。"},
    {"key":"6", "value": "スタッフの質が高いサロン。"},
    {"key":"7", "value": "清潔感のあるサロン。"},
    {"key":"8", "value": "落ち着いたサロン。"}
    ]   

    #return ask_type_of_salon_message.format(color_idea), ask_type_of_salon_options
    return ask_type_of_salon_message, ask_type_of_salon_options

def is_reservation_now_fun():
#is_reservation_now_options = ["1) 予約を取る。/ Make a reservation","2) 後で予約を取る。/ Later"]
#is_reservation_now_options = {"1": "予約を取る。/ Make a reservation","2": "後で予約を取る。/ Later"}
    is_reservation_now_options = [
    {"key":"1", "value": "予約を取る。"},
    {"key":"2", "value": "後で予約を取る。"}
    ]   

    #return is_reservation_now_message,is_reservation_now_options
    return is_reservation_now_message_1,is_reservation_now_message_2,is_reservation_now_options

def ask_date():
    return ask_date_message



def ask_service_fun(user_id):
    service_dict = get_services(user_id) 
    ask_service_options = []
    
    for service in service_dict:
        value = str(service_dict[service]["name"])
        option = {"key": service, "value": value} 
        ask_service_options.append(option)
    return ask_service_message, ask_service_options,service_dict


def ask_super_service_fun(cust_responses):
    print("inside ask super service function")

    ask_super_service_message = "どんなメニューですか？"
    sup_service_dict = cust_responses["sub_service_dict"] 
   
    ask_sub_service_options = []
    for sub_service in sub_service_dict:
        value = str(sub_service_dict[sub_service]["item"]) + " : " + str(sub_service_dict[sub_service]["price"])
        #option = {"key": sub_service, "value": sub_service_dict[sub_service]} 
        option = {"key": sub_service, "value": value} 
        ask_sub_service_options.append(option)
     
    return ask_sub_service_message,ask_sub_service_options

def ask_sub_service_fun(cust_responses):
    print("inside ask sub service function")

    #ask_sub_service_message = "メニューから項目を選択してください。"
    ask_sub_service_message = "どんなメニューですか？"
    sub_service_dict = cust_responses["sub_service_dict"] 
   
    ask_sub_service_options = []
    for sub_service in sub_service_dict:
        value = str(sub_service_dict[sub_service]["item"]) + " : " + str(sub_service_dict[sub_service]["price"])
        #option = {"key": sub_service, "value": sub_service_dict[sub_service]} 
        option = {"key": sub_service, "value": value} 
        ask_sub_service_options.append(option)
     
    return ask_sub_service_message,ask_sub_service_options



def show_avail_options():
    return session['cust_avail_msg']

def is_confirm():
#is_confirm_options = ["1) はい / Yes", "2) いいえ / No"]
#is_confirm_options = {"1": "はい / Yes", "2": "いいえ / No"}

    is_confirm_options = [
    {"key":"1", "value": "はい"},
    {"key":"2", "value": "いいえ"},
    ]

    return is_confirm_message,is_confirm_options


def ask_name():
    return get_name_message

def check_name(name):
    name_status = 0
    if not name:
        name_status = 0
        return name_status, empty_name_message
    else:
        name_status = 1
        return name_status, all_okay_message


def check_is_nickname(is_nickname_menu_int):

    is_nickname_status = 0

    try:
        is_nickname_menu_int = int(is_nickname_menu_int)
    except:
        is_nickname_status = 0
        is_nickname_response = None
        out_msg = wrong_is_nickname_message
        return is_nickname_status, is_nickname_response, out_msg


    if is_nickname_menu_int != 1 and is_nickname_menu_int != 2:
        is_nickname_status = 0
        is_nickname_response = None
        out_msg = wrong_is_nickname_message

    if is_nickname_menu_int == 1:
        is_nickname_status = 1
        is_nickname_response = "yes"
        out_msg = all_okay_message

    if is_nickname_menu_int == 2:
        is_nickname_status = 1
        is_nickname_response = "no"
        out_msg = all_okay_message

    return is_nickname_status, is_nickname_response, out_msg

def check_is_confirm(is_confirm_menu_int):

    is_confirm_status = 0

    try:
        is_confirm_menu_int = int(is_confirm_menu_int)
    except:
        is_confirm_status = 0
        is_confirm_response = None
        out_msg = wrong_is_confirm_message
        return is_confirm_status, is_confirm_response, out_msg


    if is_confirm_menu_int != 1 and is_confirm_menu_int != 2:
        is_confirm_status = 0
        is_confirm_response = None
        out_msg = wrong_is_confirm_message

    if is_confirm_menu_int == 1:
        is_confirm_status = 1
        is_confirm_response = "yes"
        out_msg = all_okay_message

    if is_confirm_menu_int == 2:
        is_confirm_status = 1
        is_confirm_response = "no"
        out_msg = all_okay_message

    return is_confirm_status, is_confirm_response, out_msg



def check_is_reservation_now(is_reservation_now_menu_int):

    is_reservation_now_status = 0

    try:
        is_reservation_now_menu_int = int(is_reservation_now_menu_int)
    except:
        is_reservation_now_status = 0
        is_reservation_now_response = None
        out_msg = wrong_is_reservation_now_message
        return is_reservation_now_status, is_reservation_now_response, out_msg


    if is_reservation_now_menu_int != 1 and is_reservation_now_menu_int != 2:
        is_reservation_now_status = 0
        is_reservation_now_response = None
        out_msg = wrong_is_reservation_now_message

    if is_reservation_now_menu_int == 1:
        is_reservation_now_status = 1
        is_reservation_now_response = "yes"
        out_msg = all_okay_message

    if is_reservation_now_menu_int == 2:
        is_reservation_now_status = 1
        is_reservation_now_response = "no"
        out_msg = all_okay_message

    return is_reservation_now_status, is_reservation_now_response, out_msg


def check_nickname(nickname):
    nickname_status = 0
    if not nickname:
        nickname_status = 0
        return nickname_status, empty_nickname_message
    else:
        nickname_status = 1
        return nickname_status, all_okay_message


def check_is_time_for_more(is_time_for_more_menu_int):

    is_time_for_more_status = 0

    try:
        is_time_for_more_menu_int = int(is_time_for_more_menu_int)
    except:
        is_time_for_more_status = 0
        is_time_for_more_response = None
        out_msg = wrong_is_time_for_more_message
        return is_time_for_more_status, is_time_for_more_response, out_msg


    if is_time_for_more_menu_int != 1 and is_time_for_more_menu_int != 2:
        is_time_for_more_status = 0
        is_time_for_more_response = None
        out_msg = wrong_is_time_for_more_message

    if is_time_for_more_menu_int == 1:
        is_time_for_more_status = 1
        is_time_for_more_response = "yes"
        out_msg = all_okay_message

    if is_time_for_more_menu_int == 2:
        is_time_for_more_status = 1
        is_time_for_more_response = "no"
        out_msg = all_okay_message

    return is_time_for_more_status, is_time_for_more_response, out_msg


def check_cust_type_of_salon(cust_type_of_salon_menu_int_list):
    print("inside check type of salon")
    print(cust_type_of_salon_menu_int_list)

    cust_type_of_salon_status = 0

    try:
        for menu_int in cust_type_of_salon_menu_int_list:
            print(menu_int)
            menu_int = int(menu_int)
    except:
        print("inside except")
        cust_type_of_salon_status = 0
        cust_type_of_salon_response = None
        out_msg = wrong_cust_type_of_salon_message
        return cust_type_of_salon_status, cust_type_of_salon_response, out_msg
    print("done with try except")

    salon_types = []

    print("cust_type_of_salon_menu_int_list")
    print(cust_type_of_salon_menu_int_list)
    
    for menu_int in cust_type_of_salon_menu_int_list:
        salon_type_name = type_of_salon_menu_int_to_name(int(menu_int))
        salon_types.append(salon_type_name)
    print("salon_types")
    print(salon_types)
 
    wrong_type = 0
    
    for s_type in salon_types:
        print("s_type")
        print(s_type)
        if s_type == "nothing":
            wrong_type = 1
            break
    
    if wrong_type == 1:
            cust_type_of_salon_status = 0
            cust_type_of_salon_response = None
            out_msg = wrong_cust_type_of_salon_message

    else:
        cust_type_of_salon_status = 1
        cust_type_of_salon_response = salon_types
        out_msg = all_okay_message

    return cust_type_of_salon_status, salon_types, out_msg

def check_new_welcome(new_welcome_menu_int):
    print("new_welcome_menu_int")
    print(new_welcome_menu_int)
    new_welcome_status = 1
     
    if new_welcome_menu_int == "1":
        print("inside new_reservation")
        new_welcome_response = "new_reservation"

    if new_welcome_menu_int == "2":
        new_welcome_response = "cancel_reservation"

    if new_welcome_menu_int == "3":
        new_welcome_response = "change_reservation"

    return new_welcome_status, new_welcome_response


def check_service(cust_service_menu_int,cust_responses):
    
    cust_service_status = 0
    try:
        cust_service_menu_int = int(cust_service_menu_int)
    except:
        
        cust_service_status = 0
        cust_service_id = None
        cust_service_name = ""
        out_msg = wrong_cust_service_message
        
        return cust_service_status,cust_service_id,cust_service_name,out_msg

    found = 0
    selected_option = {}
    
    for option in cust_responses["service_dict"]:
        if str(cust_service_menu_int) == option:
            found = 1
            cust_service_id = cust_responses["service_dict"][option]["id"]
            cust_service_name = cust_responses["service_dict"][option]["name"]
            break

    if found == 0:
        cust_service_status = 0
        out_msg = wrong_cust_sub_service_message

    elif found == 1:
        cust_service_status = 1
        out_msg = all_okay_message

    return cust_service_status,cust_service_id,cust_service_name,out_msg


def check_sub_service(cust_sub_service_menu_int,cust_responses):
    print("Check Sub Service Function")
    print("cust_sub_service_menu_int")
    print(cust_sub_service_menu_int)
     
    cust_sub_service_status = 0
    try:
        cust_sub_service_menu_int = int(cust_sub_service_menu_int)
    except:
        ss_status = 0
        ss_id = 0
        ss_name = "" 
        ss_duration = 0
        ss_price = 0
        out_msg = wrong_cust_sub_service_message
        return ss_status,ss_id,ss_name,ss_duration,ss_price,out_msg
    
    print("Done with try catch") 
    found = 0
    selected_option = {}
    print("ssdict")
    print(cust_responses["sub_service_dict"])

    
    for option in cust_responses["sub_service_dict"]:
        print("HHH")
        print(option)
        print(cust_sub_service_menu_int)
        if str(cust_sub_service_menu_int) == option:
            print("found")
            found = 1
            ss_id = cust_responses["sub_service_dict"][option]["id"]
            ss_name = cust_responses["sub_service_dict"][option]["item"]
            ss_duration = cust_responses["sub_service_dict"][option]["duration"]
            ss_price = cust_responses["sub_service_dict"][option]["price"]
            break
        else:
            print("not found")
            ss_id = 0
            ss_name = "" 
            ss_duration = 0 
            ss_price = ""

    if found == 0:
        print("I am not found")
        ss_status = 0
        out_msg = wrong_cust_sub_service_message

    elif found == 1:
        print("I am found")
        ss_status = 1
        out_msg = all_okay_message
    
    
    return ss_status,ss_id,ss_name,ss_duration,ss_price,out_msg




def check_avail_options(cust_avail_options_menu_int, avail_display_options):
    cust_avail_options_status = 0
    try:
        cust_avail_options_menu_int = int(cust_avail_options_menu_int)
    except:
        cust_avail_options_status = 0
        cust_avail_options_response = None
        out_msg = wrong_cust_avail_options_message
        return cust_avail_options_status, cust_avail_options_response, out_msg

    #avail_options_id = avail_options_menu_int_to_id(cust_avail_options_menu_int)
    found = 0
    selected_option = [0,0,0]
    print("HELLO")
    for option in avail_display_options:
        print(option)
        print(option[0])
        if cust_avail_options_menu_int == option[0]:
            found = 1
            selected_option = option
            break # This works without "break" only because I have not added ELSE part

    if found == 0:
        cust_avail_options_status = 0
        cust_avail_options_response = None
        out_msg = wrong_cust_avail_options_message

    elif found == 1:
        cust_avail_options_status = 1
        cust_avail_options_response = selected_option
        out_msg = all_okay_message

    return cust_avail_options_status, selected_option, out_msg



def check_phone(phone):
    phone_status = 0
    if not phone:
        phone_status = 0
        return phone_status, empty_phone_message
    else:
        phone_status = 1
        return phone_status, all_okay_message

def check_color(color_menu_int):
    print("ColorMenuInt: " + str(color_menu_int))
    print("Inside CheckColor")
    color_status = 0
    if not color_menu_int:
        print("Inside NotColorMenuInt")
        color_status = 0
        color_response = 0
        color_idea = 0
        return color_status, color_response, color_idea, wrong_color_message
    else:
        print("Inside Else")
        color_name = color_menu_int_to_name(color_menu_int)
        print("ColorName: " + str(color_name))
        if color_name == "nothing":
            print("Inside ColorNameNothing")
            color_status = 0
            color_response = 0
            color_idea = 0
            return color_status, color_response, color_idea, wrong_color_message
        else:
            print("Inside Inner Else")
            color_status = 1
            color_response = color_name
            color_idea = color_menu_int_to_idea(color_menu_int)
        print("All Okay")
    return color_status, color_response, color_idea, all_okay_message


def check_hobby(hobby_text):
    hobby_status = 0
    if not hobby_text:
        hobby_status = 0
        hobby_idea = 0
        return hobby_status, hobby_idea, wrong_hobby_message
    else:
        print("Inside Else")
        hobby_status = 1
        hobby_idea = hobby_to_idea(hobby_text)
    return hobby_status, hobby_idea, all_okay_message

def check_date(date_inp):
    date_status = 0
    date_obj = None

    try:
        date_obj = datetime.datetime.strptime(date_inp, '%Y-%m-%d')
    except:
        date_status = 0
        return date_obj, date_status, wrong_date_message

    if date_obj is None:
        date_status = 0
        return date_obj, date_status, wrong_date_message
    else:
        date_status = 1
        return date_obj, date_status, all_okay_message



def check_time(time_inp):
    time_status = 0
    dummy_time_inp = "01-01-2000 " + time_inp
    time_obj = None

    try:
        time_obj = datetime.datetime.strptime(dummy_time_inp, '%d-%m-%Y %H:%M')
        print("Time Obj: " + str(time_obj))
    except:
        time_status = 0
        return time_obj, time_status, wrong_time_message

    if time_obj is None:
        time_status = 0
        return time_obj, time_status, wrong_time_message
    else:
        time_status = 1
        return time_obj, time_status, all_okay_message 


def old_ask_date():
    date_str = input(get_date_message)
    date_obj = None

    while date_obj is None:

        try:
            date_obj = datetime.datetime.strptime(date_str, '%d-%m-%Y')
    #print ("DateObject:" + str(date_obj))
        except:
            #print(wrong_date_message)
            date_str = input(wrong_date_message)
        return date_obj



def ask_time():
    time_str = input(get_time_message)
    dummy_time_str = "01-01-2000 " + time_str

    time_obj = None

    while time_obj is None:

        try:
            time_obj = datetime.datetime.strptime(dummy_time_str, '%d-%m-%Y %H:%M')
    #print ("DateTimeObject:" + str(date_time_obj))
        except:
            #print(wrong_date_message)
            time_str = input(wrong_time_message)
            dummy_time_str = "01-01-2000 " + time_str
    return time_obj

def calc_date_time(date_obj,time_obj):
    inp_hour = time_obj.hour
    inp_minute = time_obj.minute
    date_time_obj = date_obj.replace(hour=inp_hour, minute=inp_minute)
    return date_time_obj

##########################################################################
###### CHAT BOT VARIABLES END HERE
##########################################################################





# Preparing the Classifier
#monthwise

cur_dir = os.path.dirname('__file__')

#total sales
#monthwise
regressor = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelmonths.pkl'), 'rb'))
model_colm = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsm.pkl'),'rb')) 

#daywise
clf = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modeldays.pkl'), 'rb'))
model_cold = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsd.pkl'),'rb')) 

#weekwise
clfweek = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelweeks.pkl'), 'rb'))
model_colw = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsw.pkl'),'rb')) 



#customer visits
#daywise
clfvd = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelvdays.pkl'), 'rb'))
model_colvd = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsvd.pkl'),'rb')) 


#monthwise
clfvm = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelvmonths.pkl'), 'rb'))
model_colvm = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsvm.pkl'),'rb')) 

#weekwise
clfvw = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelvweeks.pkl'), 'rb'))
model_colvw = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsvw.pkl'),'rb')) 


#expenses monthwise
regressor_exp = pickle.load(open(os.path.join(cur_dir,
                'pkl_objects/modelexm.pkl'), 'rb'))
model_colexp = pickle.load(open(os.path.join(cur_dir,
                'pkl_objects/model_columnsexm.pkl'),'rb'))


# Your API definition
app = Flask(__name__)
#app.secret_key = os.urandom(24)



#for localhost
cors = CORS(app, resources={r"/": {"origins": "http://localhost:5000"}})

#daywise
@app.route('/day', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

#for gcp cloud
#cors = CORS(app, resources={r"/": {"origins": "https://jts-board.appspot.com/"}})

#@app.route('/', methods=['POST'])
#@cross_origin(origin='*',headers=['Content- Type','Authorization'])

def predict():
#print(request)
    if clf:
        try:
            print("LLLLLLLLLLLLLLL")
            jsond = request.json
            queryd = pd.get_dummies(pd.DataFrame(jsond))
            queryd = queryd.reindex(columns=model_cold, fill_value=0)
            
            predictiond = list(clf.predict(queryd).astype("int64"))
            print(predictiond)
            


            print(queryd)
            copy_queryd = queryd.copy(deep=True)
            copy_queryd.columns = ['day','month','year']

            date_time = pd.to_datetime(copy_queryd[['day', 'month', 'year']])
            #date_time.columns = ['timestamp']

            date_time_df=pd.DataFrame(date_time, columns=["timestamp"])
            date_time_df['day'] = date_time_df['timestamp'].dt.dayofweek
            dnum=pd.DataFrame(date_time_df['day'])
            dname = dnum['day'].apply(lambda x: calendar.day_abbr[x])
            #df['weekday'] = df['Timestamp'].apply(lambda x: x.weekday())
            
            print("PPPPPPPPPPPPPP")
            #print(copy_queryd)
            #print(date_time_df)
            #print(dname)
            print("JJJJJJJJJJJJJJ")

            #print(queryd['m'])
            #mname = queryd['d'].apply(lambda x: calendar.day_abbr[x])
            #print(mname)
            #print(queryxid1)

            #mname=pd.DataFrame(queryd['d'])
            #mname=pd.DataFrame(mname)

            predictiond=pd.DataFrame(predictiond, columns=["sales"])
            predictiond['sales'] = predictiond['sales'].apply(lambda x: x/1000)

            print(predictiond)
            con=pd.concat([dname,predictiond], axis=1)##################
            print(con)
            df=pd.DataFrame(con)###############


            df.set_index('day')['sales'].to_dict()
            print(df)

            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            days = df['day'].tolist()
            sales = df['sales'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=days[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")



            a = "cheese"
            return json_dict
            #return jsonify({'prediction': str(predictiond)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#monthwise
@app.route('/month', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predmonth():
    #print(request)
    if regressor:
        try:
            json1= request.json
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colm, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'


            print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            #print(query1)
            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (regressor.predict(query1).astype('int64'))
            #print(prediction1)
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["sales"])
            
            prediction1['sales'] = prediction1['sales'].apply(lambda x: x/1000)

            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()

            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            months = df['month'].tolist()
            sales = df['sales'].tolist()

            print("PPPPPPPPPP")
            print(months)
            print(sales)
            print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=months[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])

            print("BBBBBBBBBBBBBB")
            print(list_of_dicts)
            print("LLLLLLLLLLLLLL")

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts,ensure_ascii=False)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")


            #dict(zip(df.m, df.s))
            
            #from collections import defaultdict
            #mydict = defaultdict(list)
            #for k, v in zip(df.m.values,df.s.values):
            #    mydict[k].append(v)
            #    mydict[k]="x"
            #    mydict[v]="v"

            
            #print("LLLLLLLLLLOOO")
            #print(mydict)
            #print(k)
            #print(v)
            #print("LLLLLLLLLL")
            
            #df.groupby('name')[['value1','value2']].apply(lambda g: g.values.tolist()).to_dict()

            
            
            #return jsonify({'prediction': str(prediction1)})
            #t = "cheese"
            #return(t)
            return(json_dict)

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#weekwise
@app.route('/week', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predweek():
    #print(request)
    if clfweek:
        try:
            print("WWWWWWWWWWWWWWWWWWWWWWWWW")
            jsonw= request.json
            queryw = pd.get_dummies(pd.DataFrame(jsonw))
            queryw = queryw.reindex(columns=model_colw, fill_value=0)


            print(queryw)
            print("OOOOOOOOOOOOOOOOO")
            #print(query1['m'])
            #mname = queryw['w'].apply(lambda x: calendar.day_abbr[x])########
            #print(mname)
            #print(query1)
            mname=pd.DataFrame(queryw['week'])#########
            print(mname)
            print("WWWWWWWWWWWWWWWWWWWWWw")

            
            predictionw = (clfweek.predict(queryw).astype("int64"))
            
            #print("PPPPPPPPPPPPPP")
            #print(predictionw)
            #print("JJJJJJJJJJJJJJ")

            #print(prediction1)
            #print(prediction)
            predictionw=pd.DataFrame(predictionw, columns=["sales"])##########
            print(predictionw)
            predictionw['sales'] = predictionw['sales'].apply(lambda x: x/1000)

            con=pd.concat([mname,predictionw], axis=1)##################
            print(con)
            df=pd.DataFrame(con)################


            df.set_index('week')['sales'].to_dict()
            #print(df)



            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            weeks = df['week'].tolist()
            sales = df['sales'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=weeks[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

            return json_dict
            #return jsonify({'prediction weekwise': str(predictionw).splitlines()})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')


#customer visits  
#daywise
@app.route('/vdays', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

#for gcp cloud
#cors = CORS(app, resources={r"/": {"origins": "https://jts-board.appspot.com/"}})

#@app.route('/', methods=['POST'])
#@cross_origin(origin='*',headers=['Content- Type','Authorization'])

def predictvdays():
    #print(request)
    if clfvd:
        try:
           # print("LLLLLLLLLLLLLLL")
            jsond = request.json
            queryd = pd.get_dummies(pd.DataFrame(jsond))
            queryd = queryd.reindex(columns=model_colvd, fill_value=0)
            
            predictiond = list(clfvd.predict(queryd))
            #print(predictiond)
            


            #print(queryd)
            copy_queryd = queryd.copy(deep=True)
            copy_queryd.columns = ['day','month','year']

            date_time = pd.to_datetime(copy_queryd[['day', 'month', 'year']])
            #date_time.columns = ['timestamp']

            date_time_df=pd.DataFrame(date_time, columns=["timestamp"])
            date_time_df['day'] = date_time_df['timestamp'].dt.dayofweek
            dnum=pd.DataFrame(date_time_df['day'])
            dname = dnum['day'].apply(lambda x: calendar.day_abbr[x])
            #df['weekday'] = df['Timestamp'].apply(lambda x: x.weekday())
            
            #print("PPPPPPPPPPPPPP")
            #print(copy_queryd)
            #print(date_time_df)
            #print(dname)
            #print("JJJJJJJJJJJJJJ")

            #print(queryd['m'])
            #mname = queryd['d'].apply(lambda x: calendar.day_abbr[x])
            #print(mname)
            #print(queryxid1)

            #mname=pd.DataFrame(queryd['d'])
            #mname=pd.DataFrame(mname)

            predictiond=pd.DataFrame(predictiond, columns=["visits"])
            #predictiond[''] = predictiond['s'].apply(lambda x: x/1000)

            #print(predictiond)
            con=pd.concat([dname,predictiond], axis=1)##################
            #print(con)
            df=pd.DataFrame(con)###############


            df.set_index('day')['visits'].to_dict()
            #print(df)

            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            days = df['day'].tolist()
            sales = df['visits'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=days[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            """
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")
            """











            a = "cheese"
            return json_dict
            #return jsonify({'prediction': str(predictiond)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')



#monthwise

#monthwise
@app.route('/vmonths', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predvmonths():
    #print(request)
    if clfvm:
        try:
            json1= request.json
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colvm, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            

            """print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            """
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            #print(query1)
            
            mname=pd.DataFrame(mname)
            #print(mname)
            
            prediction1 = (clfvm.predict(query1))
            #print(prediction1)
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["visits"])
            
            #prediction1['visits'] = prediction1['s'].apply(lambda x: x/1000)

            con=pd.concat([mname,prediction1], axis=1)
            """print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")"""
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['visits'].to_dict()

            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            months = df['month'].tolist()
            sales = df['visits'].tolist()

            """print("PPPPPPPPPP")
            print(months)
            print(sales)
            print("KKKKKKKKKKKKK")"""

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=months[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])

            """print("BBBBBBBBBBBBBB")
            print(list_of_dicts)
            print("LLLLLLLLLLLLLL")"""

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts,ensure_ascii=False)

            # the result is a JSON string:
            """print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")"""


            #dict(zip(df.m, df.s))
            
            #from collections import defaultdict
            #mydict = defaultdict(list)
            #for k, v in zip(df.m.values,df.s.values):
            #    mydict[k].append(v)
            #    mydict[k]="x"
            #    mydict[v]="v"

            
            #print("LLLLLLLLLLOOO")
            #print(mydict)
            #print(k)
            #print(v)
            #print("LLLLLLLLLL")
            
            #df.groupby('name')[['value1','value2']].apply(lambda g: g.values.tolist()).to_dict()

            
            
            #return jsonify({'prediction': str(prediction1)})
            #t = "cheese"
            #return(t)
            return(json_dict)
    
        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')



#weekwise
@app.route('/vweeks', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predvweeks():
    #print(request)
    if clfvw:
        try:
            print("WWWWWWWWWWWWWWWWWWWWWWWWW")
            jsonw= request.json
            queryw = pd.get_dummies(pd.DataFrame(jsonw))
            queryw = queryw.reindex(columns=model_colvw, fill_value=0)


            print(queryw)
            print("OOOOOOOOOOOOOOOOO")
            #print(query1['m'])
            #mname = queryw['w'].apply(lambda x: calendar.day_abbr[x])########
            #print(mname)
            #print(query1)
            mname=pd.DataFrame(queryw['week'])#########
            print(mname)
            print("WWWWWWWWWWWWWWWWWWWWWw")

            
            predictionw = (clfvw.predict(queryw).astype("int64"))
            
            #print("PPPPPPPPPPPPPP")
            #print(predictionw)
            #print("JJJJJJJJJJJJJJ")

            #print(prediction1)
            #print(prediction)
            predictionw=pd.DataFrame(predictionw, columns=["visits"])##########
            print(predictionw)
            predictionw['visits'] = predictionw['visits'].apply(lambda x: x/1000)

            con=pd.concat([mname,predictionw], axis=1)##################
            print(con)
            df=pd.DataFrame(con)################


            df.set_index('week')['visits'].to_dict()
            #print(df)



            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            weeks = df['week'].tolist()
            sales = df['visits'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=weeks[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

            return json_dict
            #return jsonify({'prediction weekwise': str(predictionw).splitlines()})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')


#monthwise expenses

@app.route('/monthexp', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predmonthexp():
    #print(request)
    if regressor_exp:
        try:
            print("HELLLO")
            json1= request.json
            length = len(json1)
            
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colexp, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            
            
            print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)

            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (regressor_exp.predict(query1).astype('int64'))

            print("JJJJJJJJJJ")
            print(prediction1)
            print("KkKKKKKK")
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["expenses"])
            
            #prediction1['expenses'] = prediction1['expenses'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['expenses'].to_dict()
            
            count = df.shape[0]
            #print(count)
            
            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")
            
            
            #months = df['month'].tolist()
            expenses = df['expenses'].tolist()
            
            
            ###################################################################
            
            
            
            query2 = pd.get_dummies(pd.DataFrame(json1))
            query2 = query2.reindex(columns=model_colm, fill_value=0)
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            

            copy_query2 = query2.copy(deep=True)
            copy_query2['month'] = copy_query2['month'].astype(str) + '月'
            
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query2['month']
            mname=pd.DataFrame(mname)
            
            
            prediction2 = (regressor.predict(query2).astype('int64'))
            prediction2=pd.DataFrame(prediction2, columns=["sales"])
            
            #prediction2['sales'] = prediction2['sales'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction2], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()
            
            count = df.shape[0]
            #print(count)
            months = df['month'].tolist() ########################
            sales = df['sales'].tolist() ##########################
            
            sales_npar = np.asarray(sales)
            expenses_npar = np.asarray(expenses)
            profit_npar = sales_npar - expenses_npar
            profit = profit_npar.tolist()
            
            #profit = sales - expenses
            print("NNNNNNNNNNNNN")
            print(sales)
            print(expenses)
            print(profit)
            print("KKKKKKKKKKKKK")
            
            
            
            
            ################################################################
            
            join = list(zip(months,sales,expenses,profit))  ###################
            join_json_string = json.dumps(join,ensure_ascii=False)
            

            
            '''
            print("PPPPPPPPPP")
            print(months)
            print(sales)
            print("KKKKKKKKKKKKK")
            
            list_of_dicts = []
            D={}
            
            #add a key and setup for a sub-dictionary
            
            for i in range(count):
                D[i] = {}
                D[i]['x']=months[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])

            print("BBBBBBBBBBBBBB")
            print(list_of_dicts)
            print("LLLLLLLLLLLLLL")
            
            # convert into JSON:
            json_dict = json.dumps(list_of_dicts,ensure_ascii=False)
            
            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

            '''
            #t = "cheese"
            #return(t)
            #return(json_dict)
            return(join_json_string)

        except:
        
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#monthwise donut
@app.route('/monthexpdonut', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

def predmonth_expdonut():
    #print(request)
    if regressor_exp:
        try:
            print("HELLLO")
            json1= request.json
            length = len(json1)
            
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colexp, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            
            
            print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            
            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (regressor_exp.predict(query1).astype('int64'))
            
            print("JJJJJJJJJJ")
            print(prediction1)
            print("KkKKKKKK")
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["expenses"])
            
            #prediction1['expenses'] = prediction1['expenses'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['expenses'].to_dict()
            
            count = df.shape[0]
            #print(count)
            
            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")
            
            
            #months = df['month'].tolist()
            expenses = df['expenses'].tolist()
            
            
            ###################################################################
            
            
            
            query2 = pd.get_dummies(pd.DataFrame(json1))
            query2 = query2.reindex(columns=model_colm, fill_value=0)
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            copy_query2 = query2.copy(deep=True)
            copy_query2['month'] = copy_query2['month'].astype(str) + '月'
            
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query2['month']
            mname=pd.DataFrame(mname)
            
            
            prediction2 = (regressor.predict(query2).astype('int64'))
            prediction2=pd.DataFrame(prediction2, columns=["sales"])
            
            #prediction2['sales'] = prediction2['sales'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction2], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()
            
            count = df.shape[0]
            #print(count)
            months = df['month'].tolist() ########################
            sales = df['sales'].tolist() ##########################
            
            sales_npar = np.asarray(sales)
            expenses_npar = np.asarray(expenses)
            profit_npar = sales_npar - expenses_npar
            profit = profit_npar.tolist()
            
            list_of_dicts = []
            D = {}
            D['x']="利益"
            D['value']=profit[0]
            list_of_dicts.append(D)
            
            E = {}
            E['x']="費用"
            E['value']=expenses[0]
            list_of_dicts.append(E)
            
            #list_of_dicts.append(D[i])
            
            #list_output = [['Expenses', expenses[0]],['Saving', profit[0]]]
            #profit = sales - expenses
            print("NNNNNNNNNNNNN")
            #print(sales[0])
            print(expenses[0])
            print(profit[0])
            print(list_of_dicts)
            print("KKKKKKKKKKKKK")
            
            
            ################################################################
            
            #out_json_string = json.dumps(list_output,ensure_ascii=False)
            out_json_string = json.dumps(list_of_dicts,ensure_ascii=False)
            
            
            #t = "cheese"
            #return(t)
            #return(json_dict)
            return(out_json_string)

        except:
    
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#monthwise column
@app.route('/monthexpcolumn', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

def predmonth_expcolumn():
    #print(request)
    if regressor_exp:
        try:
            print("HELLLO")
            json1= request.json
            length = len(json1)
            
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colexp, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            
            
            print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            
            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (regressor_exp.predict(query1).astype('int64'))
            
            print("JJJJJJJJJJ")
            print(prediction1)
            print("KkKKKKKK")
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["expenses"])
            
            #prediction1['expenses'] = prediction1['expenses'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['expenses'].to_dict()
            
            count = df.shape[0]
            #print(count)
            
            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")
            
            
            #months = df['month'].tolist()
            expenses = df['expenses'].tolist()
            
            
            ###################################################################
            
            
            
            query2 = pd.get_dummies(pd.DataFrame(json1))
            query2 = query2.reindex(columns=model_colm, fill_value=0)
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            copy_query2 = query2.copy(deep=True)
            copy_query2['month'] = copy_query2['month'].astype(str) + '月'
            
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query2['month']
            mname=pd.DataFrame(mname)
            
            
            prediction2 = (regressor.predict(query2).astype('int64'))
            prediction2=pd.DataFrame(prediction2, columns=["sales"])
            
            #prediction2['sales'] = prediction2['sales'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction2], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()
            
            count = df.shape[0]
            #print(count)
            months = df['month'].tolist() ########################
            sales = df['sales'].tolist() ##########################
            
            sales_npar = np.asarray(sales)
            expenses_npar = np.asarray(expenses)
            profit_npar = sales_npar - expenses_npar
            profit = profit_npar.tolist()
            
            #list_of_dicts = []
            #D = {}
            #D['x']="Saving"
            #D['value']=profit[0]
            #list_of_dicts.append(D)
            
            #E = {}
            #E['x']="Expenses"
            #E['value']=expenses[0]
            #list_of_dicts.append(E)
            
            list_output = [['売上', sales[0]],['費用', expenses[0]]]

            print("NNNNNNNNNNNNN")
            #print(sales[0])
            print(expenses[0])
            print(profit[0])
            print("KKKKKKKKKKKKK")
            
            
            ################################################################
            
            out_json_string = json.dumps(list_output,ensure_ascii=False)
            #out_json_string = json.dumps(list_of_dicts,ensure_ascii=Fa1lse)
            
            
            #t = "cheese"
            #return(t)
            #return(json_dict)
            return(out_json_string)

        except:
        
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')




#monthwise
@app.route('/monthv', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predmonv():
    #print(request)
    if clfvm:
        try:
            print("HELLLO")
            json1= request.json
            length = len(json1)
            
            
            
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colvm, fill_value=0)
            
            #mname = query1['month'].apply(lambda x: calendar.month_abbr[x])
            
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query1)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            #print(query1)
            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (clfvm.predict(query1).astype('int64'))

            print("JJJJJJJJJJ")
            print(prediction1)
            print("KkKKKKKK")
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["visits"])
            
            #prediction1['expenses'] = prediction1['expenses'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['visits'].to_dict()
            
            count = df.shape[0]
            #print(count)
            
            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")
            
            
            months = df['month'].tolist()
            visits = df['visits'].tolist()
            
            
            ###################################################################
            
            """
            
            query2 = pd.get_dummies(pd.DataFrame(json1))
            query2 = query2.reindex(columns=model_colm, fill_value=0)
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            mname = query2['month'].apply(lambda x: calendar.month_abbr[x])
            mname=pd.DataFrame(mname)
            
            
            prediction2 = (regressor.predict(query2).astype('int64'))
            prediction2=pd.DataFrame(prediction2, columns=["sales"])
            
            #prediction2['sales'] = prediction2['sales'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction2], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()
            
            count = df.shape[0]
            #print(count)
            months = df['month'].tolist() ########################
            sales = df['sales'].tolist() ##########################
            
            
            
            
            ################################################################
            """
            
            join = list(zip(months, visits))  ###################
            
            join_json_string = json.dumps(join,ensure_ascii=False)
            

            
            '''
            print("PPPPPPPPPP")
            print(months)
            print(sales)
            print("KKKKKKKKKKKKK")
            
            list_of_dicts = []
            D={}
            
            #add a key and setup for a sub-dictionary
            
            for i in range(count):
                D[i] = {}
                D[i]['x']=months[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])

            print("BBBBBBBBBBBBBB")
            print(list_of_dicts)
            print("LLLLLLLLLLLLLL")
            
            # convert into JSON:
            json_dict = json.dumps(list_of_dicts,ensure_ascii=False)
            
            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

            '''
            
            
            #t = "cheese"
            #return(t)
            #return(json_dict)
            return(join_json_string)

        except:
        
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#####################################################################
#####  CHAT BOT API
#####################################################################

# PROGRAM STARTS HERE


@app.route('/dropsession', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def dropsession():
    print("inside drop session")
    json_input = request.json
    ip = json_input['ip']
    print("IP:",ip)

    sql = "DELETE FROM sessions WHERE ip = %s"
    delete_tuple = (ip,)
    mycursor.execute(sql,delete_tuple)
    mydb.commit()
    #DELETE FROM table_name WHERE condition;
    return "dropped\n"



@app.route('/chat', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])



def chat():


    print("START")
    print("I am inside chat method")
    print("Inside CHAT")
    json_input = request.json

    ip = json_input['ip']
    inp_msg  = json_input['message']
    user_id = json_input['user']

    print("\n\n\n\n\n\n\n\n")
    print(ip)
    print("\n\n\n\n\n\n\n\n")
    
    sql = """select * from sessions where ip = %s """
    data = (ip,)
    mycursor.execute(sql,data)

    myresult_list = mycursor.fetchall()
    #emp_name_dict = dict()

    print("Myresult",type(myresult_list),"List")
    #print(myresult_list)
    #return "nothing"

    if len(myresult_list) != 0:
        print("matched")
        #myfirst_tuple = None
        myfirst_tuple = myresult_list[0]
        #if myfirst_tuple is not None:
        ip= myfirst_tuple[0]
        #cust_name= myfirst_tuple[1]
        #is_nickname= myfirst_tuple[2]
        #cust_nickname= myfirst_tuple[3]
        #cust_birthday= myfirst_tuple[4]
        #cust_phone= myfirst_tuple[5]
        #cust_is_time_for_more= myfirst_tuple[6]
        #cust_color= myfirst_tuple[7]
        #cust_type_of_salon= myfirst_tuple[8]
        #cust_is_reservation_now= myfirst_tuple[9]
        #cust_date= myfirst_tuple[10]
        #cust_service_id= myfirst_tuple[11]
        #cust_avail_msg=myfirst_tuple[12]
        #cust_avail_display_options= myfirst_tuple[13]
        #cust_avail_display_options = list(cust_avail_display_options)
        #cust_avail_option_list= myfirst_tuple[14]
        #cust_avail_option_list = list(cust_avail_option_list)



        print("\n\n\n I am here1 \n\n\n")
        return_list_of_dicts = []
        
        return_list_of_dicts_1= myfirst_tuple[15]
        #return_list_of_dicts_proc=list(return_list_of_dicts_proc)

        print("\n\n\nReturn List OF Dicts PROC\n\n\n")
        #print(return_list_of_dicts_1)
        #print(type(return_list_of_dicts_1))

        return_list_of_dicts_2 = return_list_of_dicts_1.replace("'", "\"")
        #print(return_list_of_dicts_2) 
        
        return_list_of_dicts = json.loads(return_list_of_dicts_2)
        #return_list_of_dicts = json.loads(return_list_of_dicts_1)
        #return "nothing"
         
        #print(return_list_of_dicts)
        #print(type(return_list_of_dicts))

        print("\n\n\n I am here2 \n\n\n")
        #count = 0


        #return "nothing"
        """
        for dict_str in return_list_of_dicts_3:
            #if count > 1:
            print("\n\n\n Inside For \n\n\n") 
            print(dict_str)
            print(type(dict_str))
             
            print("\n\n\n I am inside \n\n\n")
            accept_str = dict_str.replace("'", "\"")
            print("\n\n\n I am inside2 \n\n\n")
            print("accept",accept_str,"str")
            return_dict = json.loads(accept_str)
            print("\n\n\n I am inside3 \n\n\n")
            return_list_of_dicts.append(return_dict)
            #count += 1
        """
        #cust_duration= myfirst_tuple[16]
        STATE= myfirst_tuple[17]

        return_dict_str= myfirst_tuple[18]
        return_dict_accept_str = return_dict_str.replace("'", "\"")
        return_dict = json.loads(return_dict_accept_str)
        print("here2.5")
        cust_responses_str= myfirst_tuple[19]
        cust_responses_accept_str = cust_responses_str.replace("'", "\"")


        print("cust responses acc\n")
        #print(cust_responses_accept_str)
        print("\ncust responses acc\n")


        cust_responses = json.loads(cust_responses_accept_str)
        print("here3")
        #return_dict= dict(return_dict)
        #print(session)
        #return "hello"
    else:
        print("unmatched")
        STATE= "WELCOME_ASK_NAME"
        cust_name= ""
        is_nickname= ""
        cust_nickname= ""
        cust_birthday= ""
        is_time_for_more= ""
        cust_phone= ""
        cust_color= ""
        cust_type_of_salon= ""
        is_reservation_now= ""
        cust_date_obj= ""
        cust_service_id= ""
        cust_avail_msg= ""
        cust_avail_display_options= []
        cust_avail_option_list= []
        cust_responses= {}
        return_list_of_dicts= []
        return_dict= {}
        duration= 2



    print("Return Dicts")
    #print(type(return_dict))
    #return "okay"

    #print(type(cust_avail_display_options))
    #print(type(cust_avail_option_list))
    #print(type(return_list_of_dicts))

    #return("okay")
    #if 'user' not in session:
    #    return "yes are not logged in"
    print("Inside CHAT")
    #print("Session", session)
    print(STATE)
    print("LLLLLLLLLLLLLLLLLLLLLLLLLL")
    #return "nothing"

    """
    
    if inp_msg == "init" and STATE != "WELCOME_ASK_NAME":
        
        if STATE == "IS_RESERVATION_NOW":
            out_msg,option_list = is_reservation_now_fun()
            STATE = "IS_RESERVATION_NOW_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            return_dict["rid"] = ""
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none", "qid": "is_reservation_now"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
        else:
            print("ReturnDict")
            #print(return_dict)

            if return_dict["status"] == "failure":
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""   
                return_dict["rid"] = ""
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
    """ 
   
    
    if inp_msg == "init" and STATE != "WELCOME_ASK_NAME":
        
        if STATE == "NEW_WELCOME":
            out_msg,option_list = new_welcome_fun(cust_responses)
            STATE = "NEW_WELCOME_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "new_welcome"}
            return_list_of_dicts.append(out_dict)

            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json
        else:
            print("ReturnDict")
            #print(return_dict)

            if return_dict["status"] == "failure":
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""   
                return_dict["rid"] = ""
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
      

    """ 
    if inp_msg == "init" and STATE != "WELCOME_ASK_NAME":
        print("here1")
        if return_dict["status"] == "failure":
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""   
            return_dict["rid"] = ""
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
    """ 
    
    return_dict["rid"] = ""

    while True:
        print("loop")
        #if STATE == "NEW_WELCOME":
        #    return "nothing"


        if STATE == "WELCOME_ASK_NAME":
            out_msg = welcome_ask_name()

            #cust_responses["device_id"] = json_input['device_id']
            #cust_responses["device_token"] = json_input['device_token']

            #STATE = "NAME_ASKED"
            STATE = "WELCOME_MESSAGE_SHOWN"

            #out_dict = {"type" : "input", "question": out_msg, "message_type": "name", "place_holder": "苗字 ファーストネーム"}
            out_dict = {"type" : "text", "question": out_msg,"qid": "welcome"}
            return_list_of_dicts.append(out_dict)
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            insert_into_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
         
        if STATE == "WELCOME_MESSAGE_SHOWN":
            print("OOOOOOOOOOOOOOOOOOOO")
            #cust_name = inp_msg
            #name_st,out_msg = check_name(cust_name)
            if inp_msg == "init2":
                print("inside if")
                
                return_dict["status"] = "success"
                return_dict["status"] = ""
                return_dict["chat"] = return_list_of_dicts


                STATE = "ASK_NAME"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                print("SUCCESSFULLYT UPDATED DB")

            else:
                print("inside else")
                return_dict["status"] = "failure"
                return_dict["error_msg"] = "ウェルカムメッセージを表示した後にinit2を受信しなかった" 
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_NAME":
            out_msg = ask_name_fun()
            STATE = "NAME_ASKED"

            out_dict = {"type" : "input", "question": out_msg, "message_type": "name", "place_holder": "氏　名","qid": "ask_name"}
            return_list_of_dicts.append(out_dict)
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
        
        if STATE == "NAME_ASKED":
            cust_name = inp_msg
            name_st,out_msg = check_name(cust_name)
            if name_st == 1:
                cust_responses["name"] = cust_name

                return_dict["status"] = "success"
                return_dict["status"] = ""
                return_dict["chat"] = return_list_of_dicts

                out_dict = {"type": "text", "answer": cust_name, "message_type": "none","qid": "ask_name"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE = "IS_NICKNAME"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "IS_NICKNAME":
            out_msg,option_list = is_nickname_fun()
            STATE = "IS_NICKNAME_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "is_nickname"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json


        if STATE == "IS_NICKNAME_ASKED":
            print("I am here")
            is_nickname_menu_int = inp_msg
            
            is_nickname_status,is_nickname_response,out_msg = check_is_nickname(is_nickname_menu_int)
            
            if is_nickname_status == 1:
                cust_responses["is_nickname"] = is_nickname_response
            
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                if is_nickname_response == "yes":
                    is_nickname_response_jap = "はい"
                else:
                    is_nickname_response_jap = "いいえ"
               
                out_dict = {"type": "text", "answer": is_nickname_response_jap, "message_type": "none","qid": "is_nickname"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                if is_nickname_response == "yes":
                    STATE = "ASK_NICKNAME"
                elif is_nickname_response == "no":
                    STATE = "ASK_BIRTHDAY"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ASK_NICKNAME":
            print("JJJJJ")
            out_msg = ask_nickname()
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {"type" : "input", "question": out_msg, "message_type": "none","qid": "ask_nickname"}
            return_list_of_dicts.append(out_dict)
            STATE = "NICKNAME_ASKED"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)

            #time.sleep(2) 
            return out_json

        if STATE == "NICKNAME_ASKED":
            print("KKKKKK")
            cust_nickname = inp_msg
            nickname_status,out_msg = check_name(cust_nickname)
            if nickname_status == 1:
                cust_responses["nickname"] = cust_nickname
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": cust_nickname, "message_type": "none","qid": "ask_nickname"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "ASK_BIRTHDAY"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ASK_BIRTHDAY":
            out_msg = ask_birthday(cust_responses)
            STATE = "BIRTHDAY_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "input", "question": out_msg, "message_type": "date", "place_holder": "1993年06月09日","qid": "ask_birthday"}
            return_list_of_dicts.append(out_dict)
            out_json = json.dumps(return_dict,ensure_ascii= False)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            #time.sleep(2) 
            return out_json

        if STATE == "BIRTHDAY_ASKED":
            cust_birthday_inp = inp_msg
            jap = 0
            #cust_birthday_inp_plus_day_sym = cust_birthday_inp + "日"
            cust_birthday_inp_plus_day_sym = cust_birthday_inp 
            
            try:
                check_cust_birthday = datetime.datetime.strptime(cust_birthday_inp, '%Y-%m-%d')
            except:
                birthday_status,birthday_obj,out_msg = get_date_in_ddmmyyyy_format(cust_birthday_inp)
                birthday_str = str(birthday_obj)
                jap = 1

            if jap != 1:
                birthday_obj,birthday_status,out_msg = check_date(cust_birthday_inp)
                birthday_str = str(birthday_obj)

            
            if birthday_status == 1:
                cust_responses["birthday"] = birthday_str
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                #out_dict = {"type" : "text", "status": "success", "answer": birthday_str, "message_type": "none","qid": "ask_birthday"}
                out_dict = {"type" : "text", "status": "success", "answer": cust_birthday_inp_plus_day_sym, "message_type": "none","qid": "ask_birthday"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "ASK_PHONE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_PHONE":
            out_msg = ask_phone()
            STATE = "PHONE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "input", "question": out_msg, "message_type": "phone", "place_holder": "XXX-XXXX-XXXX","qid": "ask_phone"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "PHONE_ASKED":
            cust_phone = inp_msg
            phone_status,out_msg = check_phone(cust_phone)
            if phone_status == 1:
                cust_responses["phone"] = cust_phone
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": cust_phone, "message_type": "none","qid": "ask_phone"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "IS_TIME_FOR_MORE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "IS_TIME_FOR_MORE":
            out_msg,option_list = is_time_for_more_fun()
            STATE = "IS_TIME_FOR_MORE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "is_time_for_more"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "IS_TIME_FOR_MORE_ASKED":
            print("inside is time for more asked")
            is_time_for_more_menu_int = inp_msg
            is_time_for_more_status,is_time_for_more_response,out_msg = check_is_time_for_more(is_time_for_more_menu_int)
            if is_time_for_more_status == 1:
                cust_responses["is_time_for_more"] = is_time_for_more_response
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                

                if is_time_for_more_response == "yes":
                    is_time_for_more_response_jap = "はい"
                else:
                    is_time_for_more_response_jap = "いいえ"
                    
                out_dict = {"type" : "text", "status":"success", "answer": is_time_for_more_response_jap, "message_type": "none","qid": "is_time_for_more"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if is_time_for_more_response == "yes":
                    STATE = "ASK_TYPE_OF_SALON"
                
                elif is_time_for_more_response == "no":
                    STATE = "IS_RESERVATION_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "IS_TIME_FOR_MORE_2":
            print("HERE HERE HERE HERE HERE")
            out_msg,option_list = is_time_for_more_fun()
            STATE = "IS_TIME_FOR_MORE_ASKED_2"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "is_time_for_more_2"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)

            print("HERE HERE HERE HERE HERE")
            #time.sleep(2) 
            return out_json

        if STATE == "IS_TIME_FOR_MORE_ASKED_2":
            print("inside is time for more 2 asked")
            is_time_for_more_menu_int = inp_msg
            is_time_for_more_status,is_time_for_more_response,out_msg = check_is_time_for_more(is_time_for_more_menu_int)
            if is_time_for_more_status == 1:
                cust_responses["is_time_for_more"] = is_time_for_more_response
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                

                if is_time_for_more_response == "yes":
                    is_time_for_more_response_jap = "はい"
                else:
                    is_time_for_more_response_jap = "いいえ"
                    
                out_dict = {"type" : "text", "status":"success", "answer": is_time_for_more_response_jap, "message_type": "none","qid": "is_time_for_more_2"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if is_time_for_more_response == "yes":
                    STATE = "ASK_COLOR"
                elif is_time_for_more_response == "no":
                    STATE = "GOOD_BYE_FOR_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ASK_COLOR":
            out_msg, option_list = ask_color(cust_responses)
            STATE = "COLOR_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            out_dict = {"type" : "option", "question": out_msg,"option_list": option_list, "message_type": "none","qid": "ask_color"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "COLOR_ASKED":
            cust_color = inp_msg
            
            color_status,color_response,color_idea,out_msg = check_color(cust_color)
            if color_status == 1:
                print("Inside ColorStatus 1")
                color_idea = color_idea
                cust_responses["color"] = color_response
                cust_responses["color_idea"] = color_idea
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": color_response, "message_type": "none","qid": "ask_color"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                #STATE = "ASK_TYPE_OF_SALON"
                STATE = "ASK_HOBBIES"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                print("ColorStatusnot1")
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_HOBBIES":
            color_idea = cust_responses["color_idea"]
            #out_msg = ask_hobbies_fun(color_idea)
            out_msg_1,out_msg_2 = ask_hobbies_fun(color_idea)
            STATE = "HOBBIES_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            #out_dict = {"type" : "input", "question": out_msg,"message_type": "none","qid": "ask_hobbies"}
            out_dict = {"type" : "text", "question": out_msg_1,"message_type": "none","qid": "ask_hobbies_1"}
            return_list_of_dicts.append(out_dict)
            
            out_dict = {"type" : "input", "question": out_msg_2,"message_type": "none","qid": "ask_hobbies_2"}
            return_list_of_dicts.append(out_dict)
 
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "HOBBIES_ASKED":
            cust_hobbies = inp_msg
            
            hobby_status,hobby_idea,out_msg = check_hobby(cust_hobbies)
            
            if hobby_status == 1:
                cust_responses["hobby"] = cust_hobbies 
                #cust_responses["hobby_idea"] = hobby_idea

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": cust_hobbies, "message_type": "none","qid": "ask_hobbies"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                STATE = "GOOD_BYE_FOR_NOW"
                out_msg = hobby_idea +"\nすべての情報をありがとう。"
                cust_responses["good_bye_msg"] = out_msg
                
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            else:
                print("HobbyStatusnot1")
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json
        
        if STATE == "GOOD_BYE_FOR_NOW":
            if "good_bye_msg" in cust_responses:
                out_msg =  cust_responses["good_bye_msg"]
            else:
                out_msg = ""

            out_msg = out_msg + "\nまたお話しましょう。\nさようなら。"

            if "booked_just_now" in cust_responses:
                if cust_responses["booked_just_now"] == 1:
                    rsv_id = cust_responses["rsv_id"]
                    return_dict["rid"] = str(rsv_id)
                cust_responses["booked_just_now"] = 0  
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "text", "question": out_msg, "qid": "goodbye_bye_for_now"}
            return_list_of_dicts.append(out_dict)
            
            STATE = "NEW_WELCOME"

            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json



        if STATE == "NEW_WELCOME":
            out_msg,option_list = new_welcome_fun(cust_responses)
            STATE = "NEW_WELCOME_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "new_welcome"}
            return_list_of_dicts.append(out_dict)

            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "NEW_WELCOME_ASKED":
            new_welcome_menu_int = inp_msg
            new_welcome_status,new_welcome_response = check_new_welcome(new_welcome_menu_int)

            if new_welcome_response == "new_reservation":
                new_welcome_response_jap = "新しい予約"
                STATE = "ASK_DATE"

            if new_welcome_response == "cancel_reservation":
                new_welcome_response_jap = "予約をキャンセルする"
                STATE = "CANCEL_RESERVATION"
            
            if new_welcome_response == "change_reservation":
                new_welcome_response_jap = "予約変更"
                STATE = "CHANGE_RESERVATION"


            print("LKLKLKLKKLKKKLKLKLKLKLKLKL")
            
            
            if new_welcome_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": new_welcome_response_jap, "message_type": "none","qid": "new_welcome"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                print("New welcomeStatusnot1")
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "CANCEL_RESERVATION":
            out_msg = "予約番号を入力してください"
            STATE = "CANCEL_RESERVATION_ASKED"

            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "input", "question": out_msg, "message_type": "none","qid": "cancel_ask_id"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "CANCEL_RESERVATION_ASKED":
            cancel_rsv_id = inp_msg
            rsv_status = delete_from_reservations_table(cancel_rsv_id)
             
            if rsv_status == 1:
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text","answer": cancel_rsv_id, "message_type": "none","qid": "cancel_ask_id"}

                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                cust_responses["good_bye_msg"] = "あなたの予約はキャンセルされました。"

                
                STATE = "GOOD_BYE_FOR_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_msg = "そのような予約は見つかりませんでした。 有効な予約番号を入力してください。"
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "CHANGE_RESERVATION":
            out_msg = "予約番号を入力してください"
            STATE = "CHANGE_RESERVATION_ASKED"

            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "input", "question": out_msg, "message_type": "none","qid": "change_ask_id"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "CHANGE_RESERVATION_ASKED":
            change_rsv_id = inp_msg
            rsv_status = delete_from_reservations_table(change_rsv_id)
             
            if rsv_status == 1:
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text","answer": change_rsv_id, "message_type": "none","qid": "cancel_ask_id"}

                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE = "ASK_DATE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_msg = "そのような予約は見つかりませんでした。 有効な予約番号を入力してください。"
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_TYPE_OF_SALON":
            #color_idea = cust_responses["color_idea"]
            #out_msg,option_list = ask_type_of_salon(color_idea)
            out_msg,option_list = ask_type_of_salon()
            STATE = "TYPE_OF_SALON_ASKED"

            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "multiple_choice", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "ask_type_of_salon"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "TYPE_OF_SALON_ASKED":
            cust_type_of_salon_csl = inp_msg
            cust_type_of_salon_list = cust_type_of_salon_csl.split(",")
            
            cust_type_of_salon_status,type_of_salon_list,out_msg = check_cust_type_of_salon(cust_type_of_salon_list)
            #cust_type_of_salon = ",".join(type_of_salon_list)
            cust_type_of_salon = "\n".join(type_of_salon_list)
            
            ############################### NEED TO REWRITE THIS FUNCTION ###############################################
            #cust_type_of_salon_status = 1
            #cust_type_of_salon = "default"
            #out_msg = "all okay"
             
            if cust_type_of_salon_status == 1:
                cust_responses["type_of_salon"] = cust_type_of_salon
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text","answer": cust_type_of_salon, "message_type": "none","qid": "ask_type_of_salon"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE = "IS_RESERVATION_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "IS_RESERVATION_NOW":
            #out_msg,option_list = is_reservation_now_fun()
            out_msg_1,out_msg_2,option_list = is_reservation_now_fun()
            STATE = "IS_RESERVATION_NOW_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            #out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "is_reservation_now"}
            out_dict = {"type" : "text", "question": out_msg_1, "message_type": "none","qid": "is_res_now_1"}
            
            return_list_of_dicts.append(out_dict)
            
            out_dict = {"type" : "option", "question": out_msg_2, "option_list": option_list, "message_type": "none", "qid": "is_res_now_2"}
            
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json


        if STATE == "IS_RESERVATION_NOW_ASKED":
            is_reservation_now_menu_int = inp_msg
            is_reservation_now_status,is_reservation_now_response,out_msg = check_is_reservation_now(is_reservation_now_menu_int)
            if is_reservation_now_status == 1:
                cust_responses["is_reservation_now"] = is_reservation_now_response
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                if is_reservation_now_response == "yes":
                    is_reservation_now_response_jap = "はい"
                else:
                    is_reservation_now_response_jap = "いいえ"
              
                out_dict = {"type" : "text", "answer": is_reservation_now_response_jap, "message_type": "none","qid": "is_reservation_now"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if is_reservation_now_response == "yes":
                    STATE = "ASK_DATE"
                elif is_reservation_now_response == "no":
                    STATE = "GOOD_BYE_FOR_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_DATE":
            out_msg = ask_date()
            STATE = "DATE_ASKED"
            out_dict = {"type" : "input", "question": out_msg, "message_type": "rsv_date", "place_holder": "06月21日","qid": "ask_date"}
            return_list_of_dicts.append(out_dict)
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            time.sleep(2) 
            return out_json



        if STATE == "DATE_ASKED":
            print("Inside Date Asked")


            cust_date_inp = inp_msg
            cust_date_inp_plus_day_sym = cust_date_inp + "日"
            jap = 0
            
            try:
                check_cust_date = datetime.datetime.strptime(cust_date_inp, '%Y-%m-%d')
            except:
                cust_date_status,cust_date_obj,out_msg = get_date_in_ddmmyyyy_format(cust_date_inp)
                cust_date_str = str(cust_date_obj)
                jap = 1

            if jap != 1:
                cust_date_obj,cust_date_status,out_msg = check_date(cust_date_inp)
                cust_date_str = str(cust_date_obj)

            #cust_date_jap = inp_msg
            #cust_date_status,cust_date,out_msg = get_date_in_ddmmyyyy_format(cust_date_jap)
            ####################### NEED TO REWRITE THIS #####################
            #if cust_date_status ==1:
            #    cust_date_obj,cust_date_status,out_msg = check_date(cust_date)
            #    cust_date_str = str(cust_date_obj)
            ##################################################################
            
            if cust_date_status == 1:
                cust_responses["date"] = cust_date_str
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                #out_dict = {"type" : "text","answer": cust_date_str, "message_type": "none","qid": "ask_date"}
                out_dict = {"type" : "text","answer": cust_date_inp_plus_day_sym, "message_type": "none","qid": "ask_date"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "ASK_SERVICE"
                
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_SERVICE":
            out_msg,option_list,service_dict = ask_service_fun(user_id)
            STATE = "SERVICE_ASKED"
            cust_responses["service_dict"] = service_dict
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "ask_service"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json



        if STATE == "SERVICE_ASKED":
            cust_service_menu_int = inp_msg
            serv_status,serv_id,serv_name,out_msg = check_service(cust_service_menu_int,cust_responses)
            
            if serv_status == 1:
                cust_responses["service"] = serv_id
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                #if cust_service_id == 1:
                #    cust_service_name = "ネイル / Nail"
                #elif cust_service_id == 2:
                #    cust_service_name = "エステ / Aesthetic"

                out_dict = {"type" : "text", "answer": serv_name, "id": serv_id , "message_type": "none","qid": "ask_service"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                sub_service_dict = get_sub_services(serv_id,user_id)
                cust_responses["sub_service_dict"] = sub_service_dict
                
                #super_service_dict = get_super_services(serv_id,user_id)
                #cust_responses["super_service_dict"] = super_service_dict
                
                STATE = "ASK_SUB_SERVICE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_SUPER_SERVICE":
            
            out_msg,option_list = ask_sub_service_fun(cust_responses)

            STATE = "SUPER_SERVICE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "ask_sub_service"}
            
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "SUPER_SERVICE_ASKED":
            print("sub service asked") 
            #print(cust_responses)
            
            ss_menu_int = inp_msg
            ss_status,ss_id,ss_name,ss_dur,cust_price,out_msg = check_sub_service(ss_menu_int,cust_responses)
            #print("\n\n\n\n\n CHECK SUB SERVICE ENDS \n\n\n\n\n\n\n\n") 
            
            print("ss_dur")
            print(ss_dur)
            
            if ss_status == 1:
                
                cust_responses["sub_service"] = ss_id
                cust_responses["duration"] = ss_dur
                cust_responses["price"] = cust_price
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text", "answer": ss_name,"id":ss_id, "message_type": "none","qid": "ask_sub_service"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                print("cust_responses[service]")
                print(cust_responses["service"])
                
                relevant_employee_list = find_employees_for_service(cust_responses["service"],user_id)
                #return "nothing"
                duration_in_hours = int(int(ss_dur) / 60)
                #duration = 2
                print("ss_dur,duration_in_hours")
                print(ss_dur,duration_in_hours)
                #return "nothing"

                cust_date_str = cust_responses["date"]
                cust_date_obj = datetime.datetime.strptime(cust_date_str, '%Y-%m-%d %H:%M:%S')
                
                avail_emp_dict = check_new_availability(cust_date_obj,relevant_employee_list,duration_in_hours,user_id)
                #return "nothing" 
                emp_name_dict = find_employee_name(user_id)

                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")

                print("avail_emp_dict")
                print(avail_emp_dict)
                
                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")
                
                
                cust_avail_msg, cust_avail_display_options,cust_avail_option_list = convert_avail_dict_to_display_options(avail_emp_dict,emp_name_dict)
                #return "nothing" 
                cust_responses["cust_avail_msg"] = cust_avail_msg 
                cust_responses["cust_avail_display_options"] = cust_avail_display_options 
                
                STATE = "SHOW_AVAIL_OPTIONS"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ASK_SUB_SERVICE":
            
            out_msg,option_list = ask_sub_service_fun(cust_responses)

            STATE = "SUB_SERVICE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "ask_sub_service"}
            
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "SUB_SERVICE_ASKED":
            print("sub service asked") 
            #print(cust_responses)
            
            ss_menu_int = inp_msg
            ss_status,ss_id,ss_name,ss_dur,cust_price,out_msg = check_sub_service(ss_menu_int,cust_responses)
            #print("\n\n\n\n\n CHECK SUB SERVICE ENDS \n\n\n\n\n\n\n\n") 
            
            print("ss_dur")
            print(ss_dur)
            
            if ss_status == 1:
                
                cust_responses["sub_service"] = ss_id
                cust_responses["duration"] = ss_dur
                cust_responses["price"] = cust_price
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text", "answer": ss_name,"id":ss_id, "message_type": "none","qid": "ask_sub_service"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                print("cust_responses[service]")
                print(cust_responses["service"])
                
                relevant_employee_list = find_employees_for_service(cust_responses["service"],user_id)
                #return "nothing"
                duration_in_hours = int(int(ss_dur) / 60)
                #duration = 2
                print("ss_dur,duration_in_hours")
                print(ss_dur,duration_in_hours)
                #return "nothing"

                cust_date_str = cust_responses["date"]
                cust_date_obj = datetime.datetime.strptime(cust_date_str, '%Y-%m-%d %H:%M:%S')
                
                avail_emp_dict = check_new_availability(cust_date_obj,relevant_employee_list,duration_in_hours,user_id)
                #return "nothing" 
                emp_name_dict = find_employee_name(user_id)

                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")

                print("avail_emp_dict")
                print(avail_emp_dict)
                
                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")
                
                
                cust_avail_msg, cust_avail_display_options,cust_avail_option_list = convert_avail_dict_to_display_options(avail_emp_dict,emp_name_dict)
                #return "nothing" 
                cust_responses["cust_avail_msg"] = cust_avail_msg 
                cust_responses["cust_avail_display_options"] = cust_avail_display_options 
                
                STATE = "SHOW_AVAIL_OPTIONS"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "SHOW_AVAIL_OPTIONS":
            print("Inside Show Avail Options")

            cust_avail_msg = cust_responses["cust_avail_msg"]
            print("cust_responses")
            print(cust_responses)
            
            out_msg = cust_avail_msg
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": cust_avail_option_list, "message_type": "none","qid": "show_avail_options"}
            return_list_of_dicts.append(out_dict)
            
            STATE = "AVAIL_OPTIONS_SHOWN"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "AVAIL_OPTIONS_SHOWN":
            cust_avail_options_menu_int = inp_msg
            cust_avail_display_options = cust_responses["cust_avail_display_options"]
            print("cust_avail_display_options")
            print(cust_avail_display_options)
            cust_avail_options_status, cust_selected_option, out_msg = check_avail_options(cust_avail_options_menu_int,cust_avail_display_options)
            
            if cust_avail_options_status == 1:
                print("cust_selected_option")
                print(cust_selected_option)
                #return "nothing"
                cust_responses["avail_options"] = cust_selected_option
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                if cust_selected_option[1] != "none":
                    sel_emp = cust_selected_option[1]
                    slot = cust_selected_option[2]
                    select_sql = """select name from employees where id = %s"""
                    select_tuple = (sel_emp,)
                    mycursor.execute(select_sql,select_tuple)
                    myresult_list = mycursor.fetchall()
                    a1 = myresult_list[0]
                    a2 = a1[0]
                    sel_emp_name = a2.decode() ; sel_emp_name  
                    
                    sel_time = slot_list[slot]

                    long_option = sel_emp_name + " で " + str(sel_time) 
                else:
                    long_option = "上記の時間のどれも私には合いません。"


                out_dict = {"type" : "text","answer": long_option, "message_type": "none","qid": "show_avail_options"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if cust_selected_option[1] == "none":
                    STATE = "ASK_ALT_TIME"
                    #STATE = "ASK_DATE"
                else: 
                    STATE = "IS_CONFIRM"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ASK_ALT_TIME":
            out_msg = ask_alt_time_fun()
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "input", "question": out_msg, "place_holder": "19:00", "message_type": "time"}
            return_list_of_dicts.append(out_dict)
            
            STATE = "ALT_TIME_ASKED"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "ALT_TIME_ASKED":
            print("inside alt time asked")
            cust_alt_time = inp_msg
            time_obj, time_status,out_msg = check_time(cust_alt_time) 
            if time_status == 1:

                cust_selected_option = inp_msg
                cust_responses["cust_alt_time"] = cust_selected_option 
                today = datetime.datetime.now()

                next_seven_day_list = [today,]
                for i in range(1,7):
                    new= today + datetime.timedelta(days=i)
                    next_seven_day_list.append(new)
                relevant_employee_list = find_employees_for_service(cust_responses["service"],user_id)
                alt_avail_days = []

                for day in next_seven_day_list:
                    employee_schedule_dict = get_employee_schedule_for_date(day,relevant_employee_list)
                    start_time = cust_alt_time
                    time_duration_in_mins = int(cust_responses["duration"])
                    time_duration_in_hours = int(time_duration_in_mins/60)
                    emp_avail_dict = check_emp_avail_for_time(employee_schedule_dict,start_time,time_duration_in_hours)
                    
                    any_emp_avail_on_day = 0
                    
                    for emp in emp_avail_dict:
                        if len(emp_avail_dict[emp]) != 0:
                            any_emp_avail_on_day = 1

                    if any_emp_avail_on_day == 1:
                        day_format = day.strftime("%Y-%m-%d")
                        alt_avail_days.append(day_format)

                option_list = []
                serial = 1 
                for avail_day in alt_avail_days:
                    option = {"key": serial, "value": avail_day}
                    option_list.append(option)
                    serial += 1
                
                jap_option_list = []
                serial = 1 
                for avail_day in alt_avail_days:
                    x = avail_day[:4] + '年' + avail_day[5:]
                    y = x[:7] + '月' + x[8:]
                    z = y + "日"
                    option = {"key": serial, "value": z}
                    jap_option_list.append(option)
                    serial += 1


                cust_responses["alt_avail_days_list"] = alt_avail_days
                cust_responses["alt_avail_days"] = option_list 
                cust_responses["jap_option_list"] = jap_option_list 

                cust_responses["cust_alt_time"] = cust_selected_option
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                out_dict = {"type" : "text","answer": cust_alt_time, "message_type": "none"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                STATE = "ASK_ALT_DATE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json



        if STATE == "ASK_ALT_DATE":
            out_msg,option_list = ask_alt_date_fun(cust_responses)
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none"}
            return_list_of_dicts.append(out_dict)
            
            STATE = "ALT_DATE_ASKED"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            #print("lkj")
            #print(return_dict)
            #print("lkj")
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json
        
        if STATE == "ALT_DATE_ASKED":
            print("inside alt date asked")
            cust_alt_date = inp_msg
            #cust_selected_option = inp_msg
            days_list = cust_responses["alt_avail_days_list"]
            cust_alt_time = cust_responses["cust_alt_time"] 
            date_index = int(cust_alt_date) - 1
            selected_date = days_list[date_index]
            
            x = selected_date[:4] + '年' + selected_date[5:]
            y = x[:7] + '月' + x[8:]
            z = y + "日"
            selected_date_jap = z 

            print(selected_date) 
            date_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%d")

            relevant_employee_list = find_employees_for_service(cust_responses["service"],user_id)
            employee_schedule_dict = get_employee_schedule_for_date(date_obj,relevant_employee_list)
            start_time = cust_alt_time
            time_duration_in_mins = int(cust_responses["duration"])
            time_duration_in_hours = int(time_duration_in_mins/60)
            emp_avail_dict = check_emp_avail_for_time(employee_schedule_dict,start_time,time_duration_in_hours)

            print(emp_avail_dict)
            emp_name_dict = find_employee_name(user_id)
            cust_avail_msg, cust_avail_display_options,cust_avail_option_list = convert_avail_dict_to_display_options(emp_avail_dict,emp_name_dict)

            cust_responses["date"] = str(date_obj)
            cust_responses["cust_avail_msg"] = cust_avail_msg 
            cust_responses["cust_avail_display_options"] = cust_avail_display_options 
            print(cust_avail_msg)
            print(cust_avail_display_options)
            print(cust_avail_option_list)

            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            out_dict = {"type" : "text","answer": selected_date_jap, "message_type": "none"}
            return_list_of_dicts.append(out_dict)
            return_list_of_dicts[-2]["type"] = "text"

            STATE = "SHOW_AVAIL_OPTIONS"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))



        if STATE == "IS_CONFIRM":
            out_msg, option_list = is_confirm()
            STATE = "IS_CONFIRM_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "is_confirm"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "IS_CONFIRM_ASKED":
            print("inside is confirm asked")
            cust_is_confirm_menu_int = inp_msg
            cust_is_confirm_status, cust_is_confirm_response, out_msg = check_is_confirm(cust_is_confirm_menu_int)
            
            if cust_is_confirm_status == 1:
                cust_responses["is_confirm"] = cust_is_confirm_response
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                if cust_is_confirm_response == "yes":
                    cust_is_confirm_response_jap = "はい"
                else:
                    cust_is_confirm_response_jap = "いいえ"
              
                
                out_dict = {"type" : "text", "answer": cust_is_confirm_response_jap, "message_type": "none","qid": "is_confirm"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if cust_is_confirm_response == "yes":
                    STATE = "ENTER_DB"
                elif cust_is_confirm_response == "no":
                    STATE = "ASK_DATE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ENTER_DB":
            print ("inside enter db")

            if cust_responses["is_nickname"] == "no":
                cust_responses["nickname"] = ""

            if cust_responses["is_time_for_more"] == "no":
                #cust_responses["color"] = ""
                cust_responses["type_of_salon"] = ""

            if cust_responses["is_reservation_now"] == "no":
                cust_responses["date"] = ""
                cust_responses["avail_options"] = [0,0,0]
                cust_responses["service"] = 0

            cust_name = cust_responses["name"]
            cust_is_nickname = cust_responses["is_nickname"]
            cust_nickname = cust_responses["nickname"]
            cust_birthday = cust_responses["birthday"]
            cust_is_time_for_more = cust_responses["is_time_for_more"]
            cust_phone = cust_responses["phone"]
            #cust_color = cust_responses["color"]
            cust_type_of_salon = cust_responses["type_of_salon"]
            cust_is_reservation_now = cust_responses["is_reservation_now"]
            cust_res_date = cust_responses["date"]
            cust_slot = cust_responses["avail_options"][2]
            cust_res_time = slot_list[cust_slot]
            cust_service_id = cust_responses["service"]
            cust_sub_service_id = cust_responses["sub_service"]
            cust_emp_id = cust_responses["avail_options"][1]
            cust_is_confirm = cust_responses["is_confirm"]
            cust_duration_in_mins = cust_responses["duration"]
            cust_price = cust_responses["price"]
            cust_last_state = STATE
            #cust_device_id = cust_responses["device_id"]
            #cust_device_token = cust_responses["device_token"]

            #insert_into_chats_db(user_id,ip,cust_name,cust_is_nickname,cust_nickname,cust_birthday,cust_is_time_for_more,cust_phone,cust_color,cust_type_of_salon,cust_is_reservation_now,cust_res_date,cust_res_time,cust_service_id,cust_emp_id,cust_is_confirm,cust_last_state)

             
            c_id = insert_into_customers_table(cust_name,cust_nickname,cust_birthday,cust_phone,user_id)
            #c_id = insert_into_customers_table(cust_name,cust_nickname,cust_birthday,cust_phone,user_id,cust_device_id,cust_device_token)


            i_u_id=int(user_id)
            i_c_id=c_id
            i_s_id=int(cust_service_id)
            i_ss_id=int(cust_sub_service_id)
            i_e_id=str(cust_emp_id)
            #i_s_date=str(cust_res_date)
            start_date=str(cust_res_date)
            #i_e_date=str(cust_res_date)
            end_date=str(cust_res_date)
           
            start_slot = int(cust_slot)
            start_time = slot_list[start_slot] 
            
            slots_needed = int(int(cust_duration_in_mins) / 30)
            next_slot = start_slot + slots_needed
            end_time = slot_list[next_slot]
            i_s_time=str(start_time)
            i_e_time=str(end_time)

            print("--------------------------\n\n\n\n")
            print("--------------------------\n\n\n\n")

            start_date_wo_0s = start_date[:-9] 
            end_date_wo_0s = end_date[:-9] 
            
            i_s_date=str(start_date_wo_0s)
            i_e_date=str(end_date_wo_0s)

            print("--------------------------\n\n\n\n")
            print("--------------------------\n\n\n\n")
            #return "nothing"
            
            i_total= cust_price

            rsv_num,rsv_id = insert_into_reservations_table(i_u_id,i_c_id,i_s_id,i_ss_id,i_e_id,i_s_date,i_e_date,i_s_time,i_e_time,i_total)

            ##### CODE TO SEND PUSH NOTIFICATION ##############
            URL = "https://api.jtsboard.com/web_servicesv42/push_notification_mirai"
            r_id = rsv_id
            PARAMS = {'reservation_id':r_id}
            r = requests.get(url = URL, params = PARAMS)
            ####################################################
            cust_responses["rsv_id"] = rsv_id

            if "color" not in cust_responses:
                out_msg,option_list = confirmed_fun(rsv_num)
            
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                return_dict["rid"] = str(rsv_id)
                out_dict = {"type" : "option", "question": out_msg,"message_type": "none","option_list":option_list,"qid": "confirmed_ask_if_more"}
                return_list_of_dicts.append(out_dict)
                STATE = "IS_TIME_FOR_MORE_ASKED_2" 
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json
            else:
                out_msg = confirmed_without_more_fun(rsv_num)
                cust_responses["good_bye_msg"] = out_msg
                cust_responses["booked_just_now"] = 1
                STATE = "GOOD_BYE_FOR_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
    
    return "Cheese"

########################################################################################
########## CHAT BOT API ENDS HERE
########################################################################################


if __name__ == '__main__':
    app.run(debug=True)
    #context = ('fullchain1.pem','privkey1.pem')
    #app.run(debug=True,host='0.0.0.0',ssl_context=context)


