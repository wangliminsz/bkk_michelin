import os
import time

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

from fbot_app.mdata import *
# mdata_ranks
# mdata_alpha
# from fbot_app.mflexlist_bubble import *

def theFlexListByRanks():

    contents = dict()
    contents['type'] = 'carousel'

    mybubbles = []

    for externalIdx in range(6):

        mybubble = dict()

        mybubble['type'] = 'bubble'
        mybubble['size'] = 'kilo'

        # ------------------

        mybubble_styles_footer = dict()
        mybubble_styles_footer['separator'] = False
        mybubble_styles = dict()
        mybubble_styles['footer'] = mybubble_styles_footer

        # ------------------

        mybubble_body = dict()
        mybubble_body['type'] = 'box'
        mybubble_body['layout'] = 'vertical'

        # ------------------

        mybubble_body_contents = []

        range_Num  = 9

        for internalIdx in range(range_Num):

            exitMark = (externalIdx * range_Num + internalIdx)
            if exitMark >= 51:
                break

            myKernal = dict()
            myKernal['type'] = 'button'
            myKernal_action = {
                "type": "postback",
                "label": mdata_ranks[(externalIdx * range_Num + internalIdx)]['school_name'][:30],
                "data": mdata_ranks[(externalIdx * range_Num + internalIdx)]['id'],
                "displayText": "More info..."
            }
            myKernal['action'] = myKernal_action
            myKernal['height'] = 'sm'
            mybubble_body_contents.append(myKernal)

        mybubble_body['contents'] = mybubble_body_contents
        mybubble['body'] = mybubble_body
        mybubble['styles'] = mybubble_styles

        mybubbles.append(mybubble)

    contents['contents'] = mybubbles

    lmessage = FlexSendMessage(alt_text='List by Ranks...', contents=contents)
    return lmessage

# ---------------------------------------------

def theFlexList():

    # mybkklist = mdata
    mybkklist = sorted(mdata, key=lambda x: x['mbname'], reverse=False)

    # -----------------------------------------------

    mybubble_sample = {
        "type": "bubble",
        "size": "micro",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello",
                        "displayText": "wanglimin"
                    }
                }
            ]
        },
        "styles": {
            "footer": {
                "separator": False
            }
        }
    }

    # ---------------------------------------------

    # for mybkk in mybkklist:
    # print(mybkk['mbname'])

    contents = dict()
    contents['type'] = 'carousel'

    mybubbles = []

    for externalIdx in range(12):

        mybubble = dict()

        mybubble['type'] = 'bubble'
        mybubble['size'] = 'kilo'

        # ------------------

        mybubble_styles_footer = dict()
        mybubble_styles_footer['separator'] = False
        mybubble_styles = dict()
        mybubble_styles['footer'] = mybubble_styles_footer

        # ------------------

        mybubble_body = dict()
        mybubble_body['type'] = 'box'
        mybubble_body['layout'] = 'vertical'

        # ------------------

        mybubble_body_contents = []

        range_Num  = 15

        for internalIdx in range(range_Num):

            exitMark = (externalIdx * range_Num + internalIdx)
            if exitMark >= 177:
                break

            myKernal = dict()
            myKernal['type'] = 'button'
            myKernal_action = {
                "type": "postback",
                "label": mybkklist[(externalIdx * range_Num + internalIdx)]['mbname'][:30],
                "data": mybkklist[(externalIdx * range_Num + internalIdx)]['mbid'],
                "displayText": "More info..."
            }
            myKernal['action'] = myKernal_action
            myKernal['height'] = 'sm'
            mybubble_body_contents.append(myKernal)

        mybubble_body['contents'] = mybubble_body_contents
        mybubble['body'] = mybubble_body
        mybubble['styles'] = mybubble_styles

        mybubbles.append(mybubble)

    contents['contents'] = mybubbles

    lmessage = FlexSendMessage(alt_text='List All...', contents=contents)
    return lmessage

# ---------------------------------------------
