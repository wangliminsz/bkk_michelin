import os
import time
import math

from mailbox import _mboxMMDFMessage
from fbot_app.models import *
from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

# Flex_Msg.py

from fbot_app.mdata import *

def calDistance(latX, lngY, userInfo):

    # userCal = mbkkstyle.objects.filter(mbuserid=userInfo).last()
    # # print(userCal.mbfoodstyle)
    # # print('from DB --- inside the function location message ---------------------')

    # # mbkkstyle.objects.create(mbuserid=thisUser, mbfoodstyle=thisStyle)
    # if userCal.mbfoodstyle == 'all':
    #     mbkk = mdata
    # elif userCal.mbfoodstyle == 'streetfood':
    #     mbkk = mdata_streetfood
    # elif userCal.mbfoodstyle == 'thai':
    #     mbkk = mdata_thai
    # elif userCal.mbfoodstyle == 'europen':
    #     mbkk = mdata_europen
    # elif userCal.mbfoodstyle == 'chinese':
    #     mbkk = mdata_chinese
    # elif userCal.mbfoodstyle == 'japanese':
    #     mbkk = mdata_japanese
    # elif userCal.mbfoodstyle == 'others':
    #     mbkk = mdata_others

    # # print("latX ---------------", latX)
    # # print("lngY ---------------", lngY)
    # # print("--------------------------")

    mbkk = mdata_ranks
    
    for mbkk_location in mbkk:
        # print(mbkk_location['mblat'],mbkk_location['mblng'])
        latDiff = abs(latX - mbkk_location['lat'])
        lngDiff = abs(lngY - mbkk_location['lng'])
        totalDiff = pow(latDiff, 2) + pow(lngDiff, 2)

        myDistance = pow(totalDiff, 0.5)

        mbkk_location['distance'] = myDistance

    # mbkk.sort(key=lambda x: x['mbdistance'], reverse=False)
    # OK

    # mbkk1 = sorted(mbkk, key=lambda x: x['mbdistance'], reverse=False)
    # print('new mbkk---------------------------->', mbkk)

    return(mbkk)

# -----------------------------------------------------------------

def theLocation(theIdx):

    mLoc = mdata_ranks[int(theIdx)-1]

    # lmessage = LocationSendMessage(title= mLoc['mbname'], address = mLoc['mbaddress'], latitude = mLoc['mblat'], longitude = mLoc['mblng'])
    lmessage = LocationSendMessage(title= mLoc['school_name'], address = 'Address', latitude = mLoc['lat'], longitude = mLoc['lng'])

    return lmessage