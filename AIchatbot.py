# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:24:36 2019

@author: Manish
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
import mysql.connector
import datetime
import time
from dateutil import relativedelta
from flask import Flask, session, jsonify, request
import os
import traceback
import json




########################################################################
######### CHAT BOT VARIABLES
########################################################################


STATE = "WELCOME_ASK_NAME"
cust_name = ""
is_nickname = ""
cust_nickname = ""
cust_birthday = ""
is_time_for_more = ""
cust_phone = ""
cust_color = ""
cust_type_of_salon = ""
is_reservation_now = ""
cust_date_obj = ""
cust_service_id = ""
cust_avail_msg = ""
cust_avail_display_options = []
cust_avail_option_list = []
cust_responses = {}
return_list_of_dicts = []

cust_first_name = ""
cust_phone = ""
service_int = 0
date_obj = 0
time_obj = 0
date_time_obj = 0
duration = 2
emp_serial_id_dict = dict()


WELCOME = 0
BOOK_NAIL = 1
CHECK_NAIL_DATE = 2
BOOKED = 3
BOOKING = 4

now = datetime.datetime.now()
now1= now + datetime.timedelta(days=1)
now2= now + datetime.timedelta(days=2)
now3= now + datetime.timedelta(days=3)
now4= now + datetime.timedelta(days=4)
now5= now + datetime.timedelta(days=5)
now6= now + datetime.timedelta(days=6)



welcome_ask_name_message="""
Hey There! I am Healthcare AI Chatbot
I am your personal assistant.
I'm pleased to talk to you.
Firstly, I would  want to know a little bit about you.
Please tell me your name.
"""
    
good_name_message = """
That's a nice name, {}.
Please let me know your phone number as well.
"""
    
    

empty_name_message = """
I am pretty sure you have a wonderful name.
Please tell me. I won't tell anyone.
"""
all_okay_message = """
All Okay.
"""
    
is_nickname_message = """
Very lovely name, do you have a nickname?
"""

ask_nickname_message = """
What is your nickname?
"""

wrong_is_nickname_message = """
Please type a valid response which I can understand.
Press 1 for Yes or 2 for No.

"""
empty_nickname_message = """
Hmm.. I guess you forgot to type your nickname.

"""
ask_birthday_message = """
Great, thank you , we are going to be best friends.
May I know your birthday (nickname chan/san)?

"""

ask_phone_message = """
Oh, I’m so happy we can talk now
What is your phone number?
"""

empty_phone_message = """
I need your phone number to serve you better.
Don't worry I won't call you in odd hours.
"""



#FUNCTION DEFINED FOR EACH MESSAGE

def welcome_ask_name():
    return welcome_ask_name_message


def check_name(name):
    name_status = 0
    if not name:
        name_status = 0
        return name_status, empty_name_message
    else:
        name_status = 1
        return name_status, good_name_message


def is_nickname():
    is_nickname_options = ["1) Yes", "2) No"]
    return is_nickname_message,is_nickname_options

def ask_nickname():
    return ask_nickname_message


def check_nickname(nickname):
    nickname_status = 0
    if not nickname:
        nickname_status = 0
        return nickname_status, empty_nickname_message
    else:
        nickname_status = 1
        return nickname_status, all_okay_message


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




def ask_birthday():
    return ask_birthday_message


def ask_phone():
    return ask_phone_message



def check_phone(phone):
    phone_status = 0
    if not phone:
        phone_status = 0
        return phone_status, empty_phone_message
    else:
        phone_status = 1
        return phone_status, all_okay_message




##########################################################################
###### CHAT BOT VARIABLES END HERE
##########################################################################


# Your API definition
app = Flask(__name__)

#for localhost
cors = CORS(app, resources={r"/": {"origins": "http://localhost:5000"}})

#####################################################################
#####  CHAT BOT API
#####################################################################

# PROGRAM STARTS HERE

@app.route('/')
def index():
    session['user'] = 'Anthony'
    return "Index\n"

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return "Not logged in!"

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return "dropped"

@app.route('/logout')
def logout():
    STATE = "WELCOME_ASK_NAME"
    return_list_of_dicts = []
    session.clear()
    return "cleared" 




@app.route('/chat', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

def chat():
    global STATE
    global cust_name
    global is_nickname
    global cust_nickname
    global cust_first_name
    global cust_birthday
    global is_time_for_more
    global cust_phone
    global cust_color
    global cust_type_of_salon
    global is_reservation_now
    global cust_date_obj
    global cust_service_id
    global cust_avail_msg
    global cust_avail_display_options
    global cust_avail_option_list
    global cust_responses
    global return_list_of_dicts
    
    global service_int
    global date_obj
    global time_obj
    global date_time_obj
    global duration
    global emp_serial_id_dict
    
    json_input = request.json
    inp_msg  = json_input['message']
    print(inp_msg)
    
    if STATE == "WELCOME_ASK_NAME":
        out_msg = welcome_ask_name()
        STATE = "NAME_ASKED"
        out_dict = {"type" : "input", "question": out_msg, "answer": 0}
        return_list_of_dicts.append(out_dict)
        #out_json = json.dumps(out_dict,ensure_ascii= False)
        out_json = json.dumps(return_list_of_dicts,ensure_ascii= False)
        return out_json
    
    
    if STATE == "NAME_ASKED":
        cust_name = inp_msg
        name_st,out_msg = check_name(cust_name)
        if name_st == 1:
            cust_responses["name"] = cust_name
            return_list_of_dicts[-1]["answer"] = cust_name
            return_list_of_dicts[-1]["type"] = "text"
            STATE = "IS_NICKNAME"
        else:
            return out_msg


    if STATE == "IS_NICKNAME":
        out_msg,option_list = is_nickname()
        STATE = "IS_NICKNAME_ASKED"
        out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "answer": 0}
        return_list_of_dicts.append(out_dict)
        out_json = json.dumps(return_list_of_dicts,ensure_ascii= False)
        return out_json


    if STATE == "IS_NICKNAME_ASKED":
        is_nickname_menu_int = inp_msg
        
        is_nickname_status,is_nickname_response,out_msg = check_is_nickname(is_nickname_menu_int)
        
        if is_nickname_status == 1:
            cust_responses["is_nickname"] = is_nickname_response
            return_list_of_dicts[-1]["answer"] = is_nickname_response
            return_list_of_dicts[-1]["type"] = "text"
            if is_nickname_response == "yes":
                STATE = "ASK_NICKNAME"
            elif is_nickname_response == "no":
                STATE = "ASK_BIRTHDAY"
        else:
            return out_msg


    if STATE == "ASK_NICKNAME":
        out_msg = ask_nickname()
        STATE = "NICKNAME_ASKED"
        out_dict = {"type" : "input", "question": out_msg, "answer": 0}
        return_list_of_dicts.append(out_dict)
        out_json = json.dumps(return_list_of_dicts,ensure_ascii= False)
        return out_json

    if STATE == "NICKNAME_ASKED":
        cust_nickname = inp_msg
        nickname_status,out_msg = check_name(cust_nickname)
        if nickname_status == 1:
            cust_responses["nickname"] = cust_nickname
            return_list_of_dicts[-1]["answer"] = cust_nickname
            return_list_of_dicts[-1]["type"] = "text"
            STATE = "ASK_BIRTHDAY"
        else:
            return out_msg



    if STATE == "ASK_BIRTHDAY":
        out_msg = ask_birthday()
        STATE = "BIRTHDAY_ASKED"
        out_dict = {"type" : "input", "question": out_msg, "answer": 0}
        return_list_of_dicts.append(out_dict)
        out_json = json.dumps(return_list_of_dicts,ensure_ascii= False)
        return out_json

    if STATE == "BIRTHDAY_ASKED":
        cust_birthday = inp_msg
        birthday_obj,birthday_status,out_msg = check_date(cust_birthday)
        birthday_str = str(birthday_obj)
        if birthday_status == 1:
            cust_responses["birthday"] = birthday_str
            return_list_of_dicts[-1]["answer"] = birthday_str
            return_list_of_dicts[-1]["type"] = "text"
            STATE = "IS_TIME_FOR_MORE"
        else:
            return out_msg



    if STATE == "IS_TIME_FOR_MORE":
        out_msg,option_list = is_time_for_more()
        STATE = "IS_TIME_FOR_MORE_ASKED"
        out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "answer": 0}
        return_list_of_dicts.append(out_dict)
        out_json = json.dumps(return_list_of_dicts,ensure_ascii= False)
        return out_json

    
    if STATE == "IS_TIME_FOR_MORE_ASKED":
        is_time_for_more_menu_int = inp_msg
        
        is_time_for_more_status,is_time_for_more_response,out_msg = check_is_time_for_more(is_time_for_more_menu_int)
        
        if is_time_for_more_status == 1:
            cust_responses["is_time_for_more"] = is_time_for_more_response
            return_list_of_dicts[-1]["answer"] = is_time_for_more_response
            return_list_of_dicts[-1]["type"] = "text"
            if is_time_for_more_response == "yes":
                STATE = "ASK_PHONE"
            elif is_time_for_more_response == "no":
                STATE = "IS_RESERVATION_NOW"
        else:
            return out_msg


    if STATE == "ASK_PHONE":
        out_msg = ask_phone()
        STATE = "PHONE_ASKED"
        out_dict = {"type" : "input", "question": out_msg, "answer": 0}
        return_list_of_dicts.append(out_dict)
        out_json = json.dumps(return_list_of_dicts,ensure_ascii= False)
        return out_json

    if STATE == "PHONE_ASKED":
        cust_phone = inp_msg
        phone_status,out_msg = check_phone(cust_phone)
        if phone_status == 1:
            cust_responses["phone"] = cust_phone
            return_list_of_dicts[-1]["answer"] = cust_phone
            return_list_of_dicts[-1]["type"] = "text"
            STATE = "ASK_COLOR"
        else:
            return out_msg


    
    return "END........."

########################################################################################
########## CHAT BOT API ENDS HERE 
########################################################################################





if __name__ == '__main__':
    app.run()


