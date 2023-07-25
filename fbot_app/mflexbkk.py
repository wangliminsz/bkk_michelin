import os
import time

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

from fbot_app.mdata import *

# Flex_Msg.py

# -------------------------------------------------------

    # id
    # school_name
    # type
    # lat
    # lng
    # website
    # Img_url
    # 学费
    # 年级设置
    # memo
    # 学术成绩(10)
    # 师资情况(10)
    # 课程优势(10)
    # 体育艺术特长(10)
    # 生源质量(10)
    # 环境设施(10)
    # 国际化(10)
    # 背景资源(10)
    # 地理位置(10)
    # 坚守原则(10)
    # 教育总分(50)
    # 综合总分(100)
    # 综合排名
    # 教育排名

    # -------------------------------------------------------
    # if mLoc['Img_url']:
    #     imgUrl = mLoc['Img_url']
    # else:    
    #     imgUrl = "https://i.imgur.com/jC0v7WS.jpg"
    # -------------------------------------------------------    

###################################################################################

def flex_example(mybkklist):

    theLength = len(mybkklist)
    print('Length ---------------------------->', theLength)

    i = 0
    fmessage = []

    for i in range(5):

        contents = dict()
        contents['type'] = 'carousel'
        bubbles = []

        for mybkkitem in mybkklist[i*11:(i+1)*11]:
            if mybkkitem['Img_url']:
                imgUrl = mybkkitem['Img_url']
            else:    
                imgUrl = "https://i.imgur.com/jC0v7WS.jpg"    
            theName = mybkkitem['school_name']
            theStyle = mybkkitem['type']
            theIndex = mybkkitem['id']
            theDistance = mybkkitem['distance']
            # print(theDistance)
            theDistanceStr = str(round(139.276 * theDistance, 2)) + " km"

            bubble = {
                "type": "bubble",
                "size": "micro",
                "hero": {
                        "type": "image",
                        "url":  imgUrl,
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "320:213"
                },
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

        fmessage.append(FlexSendMessage(alt_text='Bangkok Schools', contents=contents))
    
    return fmessage

###################################################################################

def theFlex(theIdx):
    # print(mybkklist[0]['mbname'])
    # print(mybkklist[0]['mbstyle'])
    # print('inside flex ----------------------------------------')

    mLoc = mdata_ranks[int(theIdx)-1]
    # print(mLoc)
    # print('=========================================')

    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []

    # -------------------------------------------------------

    # id
    # school_name
    # type
    # lat
    # lng
    # website
    # Img_url
    # 学费
    # 年级设置
    # memo
    # 学术成绩(10)
    # 师资情况(10)
    # 课程优势(10)
    # 体育艺术特长(10)
    # 生源质量(10)
    # 环境设施(10)
    # 国际化(10)
    # 背景资源(10)
    # 地理位置(10)
    # 坚守原则(10)
    # 教育总分(50)
    # 综合总分(100)
    # 综合排名
    # 教育排名

    # -------------------------------------------------------

    if mLoc['Img_url']:
        imgUrl = mLoc['Img_url']
    else:    
        imgUrl = "https://i.imgur.com/jC0v7WS.jpg"

    # print(imgUrl, '<<<---------------------------------------------')    
    # imgUrl  = "https://i.imgur.com/LTB6Tvr.jpg"
    imgUrl1 = "https://i.imgur.com/ff5zuoz.jpg"
    imgUrl2 = "https://i.imgur.com/jC0v7WS.jpg"
    # imgUrl3 = "https://i.imgur.com/jC0v7WS.jpg"

    theName = mLoc['school_name']
    theIndex = mLoc['id']

    # theContact = 'mbcontact'
    theAcademicRank = mLoc['教育排名']
    theTotalRank = mLoc['综合排名']
    theType = mLoc['type']

    if mLoc['学术成绩(10)']:
        theAcademic = str(mLoc['学术成绩(10)'])
    else:
        theAcademic = "  "
    
    if mLoc['师资情况(10)']:
        theTeacher = str(mLoc['师资情况(10)'])
    else:
        theTeacher = "  "    
    if mLoc['课程优势(10)']:
        theClass = str(mLoc['课程优势(10)'])
    else:
        theClass = "  "    
    if mLoc['体育艺术特长(10)']:
        thePeArt = str(mLoc['体育艺术特长(10)'])
    else:
        thePeArt = "  "
    if mLoc['生源质量(10)']:
        theStudent = str(mLoc['生源质量(10)'])
    else:
        theStudent = "  "

    if mLoc['教育总分(50)']:
        theAcademicTotal = str(mLoc['教育总分(50)'])
    else:
        theAcademicTotal = "  "

    if mLoc['memo']:
        theMemo = mLoc['memo']
    else:
        theMemo = "   "

    if mLoc['环境设施(10)']:
        theEnvironment = str(mLoc['环境设施(10)'])
    else:
        theEnvironment = "  "
    
    if mLoc['国际化(10)']:
        theInternational = str(mLoc['国际化(10)'])
    else:
        theInternational = "  "    
    if mLoc['背景资源(10)']:
        theBackground = str(mLoc['背景资源(10)'])
    else:
        theBackground = "  "    
    if mLoc['地理位置(10)']:
        theSchoolLoc = str(mLoc['地理位置(10)'])
    else:
        theSchoolLoc = "  "
    if mLoc['坚守原则(10)']:
        thePrinciple = str(mLoc['坚守原则(10)'])
    else:
        thePrinciple = "  "

    if mLoc['综合总分(100)']:
        theTotal = str(mLoc['综合总分(100)'])
    else:
        theTotal = "  "    

    theUrl = mLoc['website']    

    theTakeaway = 'mbtakeaway'
    theService = 'mbservice'
    theAward = 'mbaward'
    theView = 'mbview'
    theTelCall = 'mbtelephone'

    # theTel = theContact[4:]
    # theTelLink = ("https://line.me/R/call/66/" + theTel.replace(' ','')).strip()

    # theTelCall = ("tel:0" + theTel.replace(' ','')).strip()

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
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Academic 学术: ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theAcademicRank,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "Total 综合: ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theTotalRank,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "System 体系: ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theType,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "   ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 6
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
                                        "text": "(数据来自徐公子，仅供参考)",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 6
                                    },
                                ]
                            }
                        ]
                    }
                ]
            }
        },

        #-- 1 -----------##############################################

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
                                        "text": "Memo 备注: ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theMemo,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "    ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
                                    },
                                ]
                            },
                            # {
                            #     "type": "box",
                            #     "layout": "baseline",
                            #     "spacing": "sm",
                            #     "contents": [
                            #         # {
                            #         #     "type": "text",
                            #         #     "text": "    ",
                            #         #     "color": "#666666",
                            #         #     "size": "sm",
                            #         #     "flex": 2
                            #         # },
                            #         {
                            #             "type": "button",
                            #             "style": "link",
                            #             "height": "sm",
                            #             "action": {
                            #                 "type": "uri",
                            #                 "label": "Website",
                            #                 "uri": theUrl
                            #             }
                            #         }
                            #     ]
                            # }
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
                            "label": "Website",
                            "uri": theUrl
                        }
                    }
                ],
                "flex": 0
            },
            ###
        },

        #-- 2 -----------##############################################

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
                        "text": "Academic 学术",
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
                            #     "layout": "vertical",
                            #     "spacing": "sm",
                            #     "contents": [
                            #         {
                            #             "type": "text",
                            #             "text": theAcademic,
                            #             "wrap": True,
                            #             "color": "#666666",
                            #             "size": "md",
                            #             "flex": 4
                            #         },
                            #     ]
                            # }
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "学术成绩(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theAcademic,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "师资情况(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theTeacher,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "课程优势(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theClass,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "体育艺术特长(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": thePeArt,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "生源质量(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theStudent,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "     ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": "  ",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "教育总分(50):",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theAcademicTotal,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
                                    }
                                ]
                            },
                        ]
                    }
                ]
            }
        },

        #-- 3 -----------##############################################

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
                        "text": "Comprehensive 综合",
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
                            #     "layout": "vertical",
                            #     "spacing": "sm",
                            #     "contents": [
                            #         {
                            #             "type": "text",
                            #             "text": theAcademic,
                            #             "wrap": True,
                            #             "color": "#666666",
                            #             "size": "md",
                            #             "flex": 4
                            #         },
                            #     ]
                            # }
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "环境设施(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theEnvironment,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "国际化(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theInternational,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "背景资源(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theBackground,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "地理位置(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theSchoolLoc,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "坚守原则(10): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": thePrinciple,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "     ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": "  ",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
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
                                        "text": "综合总分(100): ",
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 4
                                    },
                                    {
                                        "type": "text",
                                        "text": theTotal,
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 2
                                    }
                                ]
                            },
                        ]
                    }
                ]
            }
        },

        #-- 4 -----------##############################################

    ]
    # -----------------------------------------------

    # bubbles.append(bubble)

    contents['contents'] = bubbles

    dmessage = FlexSendMessage(alt_text='More info...', contents=contents)
    return dmessage

###################################################################################