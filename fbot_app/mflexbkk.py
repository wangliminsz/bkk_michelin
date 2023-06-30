import os
import time

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

from fbot_app.mdata import *

# Flex_Msg.py


def flex_example(mybkklist):
    # print(mybkklist[0]['mbname'])
    # print(mybkklist[0]['mbstyle'])
    # print('inside flex ----------------------------------------')

    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []

    for mybkkitem in mybkklist[:12]:
        imgUrl = mybkkitem['mbimgurl']
        theName = mybkkitem['mbname']
        theStyle = mybkkitem['mbstyle']
        theIndex = mybkkitem['mbid']
        theDistance = mybkkitem['mbdistance']
        # print(theDistance)
        theDistanceStr = str(round(139.276 * theDistance, 2)) + " km"

        bubble = {
            "type": "bubble",
            "size": "micro",
            # "hero": {
            #         "type": "image",
            #         # "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg",
            #         "url":  imgUrl,
            #         "size": "full",
            #         "aspectMode": "cover",
            #         "aspectRatio": "320:213"
            # },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                        {
                            "type": "text",
                            "text": theName,
                            "weight": "bold",
                            "size": "sm",
                            "wrap": True
                        },
                    {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": theStyle,
                                            "wrap": True,
                                            "color": "#8c8c8c",
                                            "size": "xs",
                                            "flex": 5
                                        },

                                        {
                                            "type": "text",
                                            "text": theDistanceStr,
                                            "wrap": True,
                                            "color": "#8c8c8c",
                                            "size": "xs",
                                            "flex": 5
                                        },
                                    ]
                                }
                            ]
                    }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "postback",
                                "label": "MORE ...",
                                "data": theIndex
                            }
                        }
                ],
                "flex": 0
            }
        }

        bubbles.append(bubble)

    contents['contents'] = bubbles

    fmessage = FlexSendMessage(
        alt_text='Nearby MICHELIN restaurants', contents=contents)
    return fmessage


def theFlex(theIdx):
    # print(mybkklist[0]['mbname'])
    # print(mybkklist[0]['mbstyle'])
    # print('inside flex ----------------------------------------')

    mLoc = mdata[int(theIdx)-1]
    # print(mLoc)
    # print('=========================================')

    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []

    # imgUrl = mLoc['mbimgurl']
    imgUrl  = "https://i.imgur.com/LTB6Tvr.jpg"

    imgUrl1 = "https://i.imgur.com/2PdQYSO.png"
    imgUrl2 = "https://i.imgur.com/jC0v7WS.jpg"
    imgUrl3 = "https://i.imgur.com/jC0v7WS.jpg"

    theName = mLoc['mbname']
    theStyle = mLoc['mbstyle']
    theIndex = mLoc['mbid']
    theContact = mLoc['mbcontact']
    thePrice = mLoc['mbprice']
    theTakeaway = mLoc['mbtakeaway']
    theService = mLoc['mbservice']
    theAward = mLoc['mbaward']
    theView = mLoc['mbview']
    theUrl = mLoc['mburl']

    theTel = theContact[4:]
    # theTelLink = ("https://line.me/R/call/66/" + theTel.replace(' ','')).strip()

    theTelCall = ("tel:0" + theTel.replace(' ','')).strip()

    # -----------------------------------------------

    bubbles = [

        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url":  imgUrl,
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": theName,
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    # {
                                    #     "type": "text",
                                    #     "text": "Tel: ",
                                    #     "color": "#aaaaaa",
                                    #     "size": "sm",
                                    #     "flex": 2
                                    # },

                                    # {
                                    #     "type": "text",
                                    #     "text": theContact,
                                    #     "wrap": True,
                                    #     "color": "#666666",
                                    #     "size": "sm",
                                    #     "flex": 4
                                    # }

                                    {
                                        "type": "button",
                                        "style": "link",
                                        "height": "sm",
                                        "action": {
                                            "type": "uri",
                                            "label": theContact,
                                            # "uri": theTelLink
                                            # "uri": "tel:09001234567"
                                            "uri": theTelCall

                                        }
                                    },

                                ]
                            },

                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Price: ",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 2
                                    },
                                    {
                                        "type": "text",
                                        "text": thePrice,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },


        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url":  imgUrl1,
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": theName,
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Style: ",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 2
                                    },
                                    {
                                        "type": "text",
                                        "text": theStyle,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Delivery: ",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 2
                                    },
                                    {
                                        "type": "text",
                                        "text": theTakeaway,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },


        {
            "type": "bubble",
            # "hero": {
            #     "type": "image",
            #     "url":  imgUrl1,
            #     "size": "full",
            #         "aspectRatio": "20:13",
            #         "aspectMode": "cover",
            # },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Service",
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            # {
                            #     "type": "box",
                            #     "layout": "baseline",
                            #     "spacing": "sm",
                            #     "contents": [
                            #         {
                            #             "type": "text",
                            #             "text": "Style: ",
                            #             "color": "#aaaaaa",
                            #             "size": "sm",
                            #             "flex": 2
                            #         },
                            #         {
                            #             "type": "text",
                            #             "text": theStyle,
                            #             "wrap": True,
                            #             "color": "#666666",
                            #             "size": "sm",
                            #             "flex": 4
                            #         }
                            #     ]
                            # },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    # {
                                    #     "type": "text",
                                    #     "text": "Delivery: ",
                                    #     "color": "#aaaaaa",
                                    #     "size": "sm",
                                    #     "flex": 2
                                    # },
                                    {
                                        "type": "text",
                                        "text": theService,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "md",
                                        "flex": 4
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },


        {
            "type": "bubble",
            # "hero": {
            #     "type": "image",
            #     "url":  imgUrl1,
            #     "size": "full",
            #         "aspectRatio": "20:13",
            #         "aspectMode": "cover",
            # },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "MICHELIN Point of View",
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            # {
                            #     "type": "box",
                            #     "layout": "baseline",
                            #     "spacing": "sm",
                            #     "contents": [
                            #         {
                            #             "type": "text",
                            #             "text": "Style: ",
                            #             "color": "#aaaaaa",
                            #             "size": "sm",
                            #             "flex": 2
                            #         },
                            #         {
                            #             "type": "text",
                            #             "text": theStyle,
                            #             "wrap": True,
                            #             "color": "#666666",
                            #             "size": "sm",
                            #             "flex": 4
                            #         }
                            #     ]
                            # },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    # {
                                    #     "type": "text",
                                    #     "text": "Delivery: ",
                                    #     "color": "#aaaaaa",
                                    #     "size": "sm",
                                    #     "flex": 2
                                    # },
                                    {
                                        "type": "text",
                                        "text": theView,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            ###
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "More...",
                            "uri": theUrl
                        }
                    }
                ],
                "flex": 0
            },
            ###
        },


        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url":  imgUrl2,
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Special Award",
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            # {
                            #     "type": "box",
                            #     "layout": "baseline",
                            #     "spacing": "sm",
                            #     "contents": [
                            #         {
                            #             "type": "text",
                            #             "text": "Style: ",
                            #             "color": "#aaaaaa",
                            #             "size": "sm",
                            #             "flex": 2
                            #         },
                            #         {
                            #             "type": "text",
                            #             "text": theStyle,
                            #             "wrap": True,
                            #             "color": "#666666",
                            #             "size": "sm",
                            #             "flex": 4
                            #         }
                            #     ]
                            # },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    # {
                                    #     "type": "text",
                                    #     "text": "Delivery: ",
                                    #     "color": "#aaaaaa",
                                    #     "size": "sm",
                                    #     "flex": 2
                                    # },
                                    {
                                        "type": "text",
                                        "text": theAward,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "md",
                                        "flex": 4
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
        },

    ]
    # -----------------------------------------------

    # bubbles.append(bubble)

    contents['contents'] = bubbles

    dmessage = FlexSendMessage(alt_text='More info...', contents=contents)
    return dmessage
