from mailbox import _mboxMMDFMessage
from fbot_app.models import *
from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
# from linebot.models import MessageEvent, TextSendMessage,
from linebot.models import *

# 2022-01-23 Michelin Bkk - Data Array

from fbot_app.mdata import *
from fbot_app.mdatabkk import *
# from fbot_app.mdatalocation import *

from fbot_app.mflexbkk import *
from fbot_app.mflexlistall import *
from fbot_app.mflexcontact import *

# 2022-01-23 Michelin Bkk - Data Array


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):

    if request.method == 'POST':

        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            # 如果事件為訊息
            if isinstance(event, MessageEvent):
                if event.message.type == 'text':
                    mtext = event.message.text
                    mSource = event.source.user_id

                    if 'Bkk Schools' in mtext:
                        # alt_text='Buttons template',
                        message = TemplateSendMessage(
                            alt_text='Bkk Schools Info',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='Bkk Schools Info:',
                                actions=[
                                    PostbackTemplateAction(
                                        label='List (by Ranks)',
                                        data='LISTBYRANKS&'
                                    ),

                                    # PostbackTemplateAction(
                                    #     label='List (by Alphabet)',
                                    #     data='LISTBYALPHA&'
                                    # ),

                                    PostbackTemplateAction(
                                        label='by Location',
                                        text='Please send location ...',
                                        data='LISTBYLOCATION&' + mSource
                                    )

                                    # PostbackTemplateAction(
                                    #     label='by Style & Location',
                                    #     text='Please choose food style:',
                                    #     data='BBBB&' + mSource
                                    # ),
                                    # PostbackTemplateAction(
                                    #     label='List All',
                                    #     data='CCCC&'
                                    # )
                                ]
                            )
                        )

                        line_bot_api.reply_message(event.reply_token, message)

                    elif 'delete!@#$%^&*()' in mtext:
                        # alt_text='Buttons template',
                        mbkkstyle.objects.all().delete()

                elif event.message.type == 'location':

                    theUser = event.source.user_id

                    mybkk = calDistance(
                        event.message.latitude, event.message.longitude, theUser)

                    ltext = "Bangkok Schools:"
                    # message1 = TextSendMessage(text=ltext)
                    # message2 = flex_example(mybkk)
                    # message3 = flex_Ad()

                    message_all = flex_example(mybkk)

                    # message1= flex_Locs(mybkk, 12, 1)

                    line_bot_api.reply_message(
                        event.reply_token, message_all)
                    # , message2, message3

            elif isinstance(event, PostbackEvent):
                # print('PostbackEvent')
                # print(event.postback.data)
                # print('PostbackEvent ---------------------------')

                if (event.postback.data.isdigit()):

                    message1 = TextSendMessage(text='More info...')
                    # print('the location-------------------->',event.postback.data)
                    message2 = theLocation(event.postback.data)
                    message3 = theFlex(event.postback.data)
                    message4 = flex_Ad()

                    line_bot_api.reply_message(event.reply_token, [message1, message2, message3, message4])
                        # event.reply_token, [message1, message2, message3,message4])
                        
                elif "LISTBYRANKS&" in event.postback.data:

                    list_message = theFlexListByRanks()
                    ad_message = flex_Ad()
                    line_bot_api.reply_message(event.reply_token, [list_message,ad_message])
                
                elif "LISTBYLOCATION&" in event.postback.data:

                    # print("AAAA -----------------")
                    # print(event.postback.data)
                    # print("AAAA -----------------")

                    # thisUser = event.postback.data[5:]
                    # mbkkstyle.objects.create(
                    #     mbuserid=thisUser, mbfoodstyle='all')

                    message = TemplateSendMessage(
                        alt_text='Send your location?',
                        template=ConfirmTemplate(
                            text="Send your location?",
                            actions=[
                                URITemplateAction(
                                    type='uri',
                                    label='Yes',
                                    uri='https://line.me/R/nv/location'
                                ),
                                PostbackTemplateAction(
                                    label="No",
                                    text="Thanks",
                                    data="No Location"
                                )
                            ]
                        )
                    )

                    line_bot_api.reply_message(
                        event.reply_token, message)

                elif "BBBB&" in event.postback.data:

                    print("BBBB -----------------")
                    thisUser = event.postback.data[5:]
                    # mbkkstyle.objects.create(mbuserid=thisUser, mbfoodstyle='all')

                    message = TemplateSendMessage(
                        alt_text='Choose Style',
                        template=CarouselTemplate(
                            columns=[
                                CarouselColumn(
                                    # thumbnail_image_url='https://example.com/item1.jpg',
                                    title='Menu',
                                    text='Choose Food Style:',
                                    actions=[
                                        PostbackTemplateAction(
                                            label='Street Food',
                                            text='Street Food',
                                            data='SSSS&' + thisUser + '&streetfood'
                                        ),
                                        PostbackTemplateAction(
                                            label='Thai',
                                            text='Thai',
                                            data='SSSS&' + thisUser + '&thai'
                                        ),
                                        PostbackTemplateAction(
                                            label='Europen',
                                            text='Europen',
                                            data='SSSS&' + thisUser + '&europen'
                                        ),
                                    ]
                                ),

                                CarouselColumn(
                                    # thumbnail_image_url='https://example.com/item1.jpg',
                                    title='Menu',
                                    text='Choose Food Style:',
                                    actions=[
                                        PostbackTemplateAction(
                                            label='Chinese',
                                            text='Chinese',
                                            data='SSSS&' + thisUser + '&chinese'
                                        ),
                                        PostbackTemplateAction(
                                            label='Japanese & Asian',
                                            text='Japanese & Asian',
                                            data='SSSS&' + thisUser + '&japanese'
                                        ),
                                        PostbackTemplateAction(
                                            label='Others',
                                            text='Others',
                                            data='SSSS&' + thisUser + '&others'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )

                    line_bot_api.reply_message(event.reply_token, message)

                elif "SSSS&" in event.postback.data:

                    # print("SSSS -----------------")
                    # # print(event.postback.data)

                    # thisUser = event.postback.data.split("&")
                    # print(thisUser)

                    # print("SSSS -----------------")

                    thisData = event.postback.data.split("&")
                    thisUser = thisData[1]
                    thisStyle = thisData[2]
                    # print(thisUser)

                    mbkkstyle.objects.create(
                        mbuserid=thisUser, mbfoodstyle=thisStyle)

                    message = TemplateSendMessage(
                        alt_text='Send your location?',
                        template=ConfirmTemplate(
                            text="Send your location?",
                            actions=[
                                URITemplateAction(
                                    type='uri',
                                    label='Yes',
                                    uri='https://line.me/R/nv/location'
                                ),
                                PostbackTemplateAction(
                                    label="No",
                                    text="Thanks",
                                    data="No Location"
                                )
                            ]
                        )
                    )

                    line_bot_api.reply_message(
                        event.reply_token, message)

                elif "CCCC&" in event.postback.data:

                    # print("CCCC-----------------")
                    # print(event.postback.data)
                    # print("CCCC -----------------")
                    # theFlexList()
                    list_message = theFlexList()
                    line_bot_api.reply_message(event.reply_token, list_message)

                elif "mcontact" in event.postback.data:
                    print(event.postback.data)
                    print('mcontact -----------------')

                    list_message = flex_Contact()
                    line_bot_api.reply_message(event.reply_token, list_message)

                    # thisUser = event.postback.data[5:]
                    # mbkkstyle.objects.create(
                    #     mbuserid=thisUser, mbfoodstyle='all')

                    # message = TemplateSendMessage(
                    #     alt_text='Send your location?',
                    #     template=ConfirmTemplate(
                    #         text="Send your location?",
                    #         actions=[
                    #             URITemplateAction(
                    #                 type='uri',
                    #                 label='Yes',
                    #                 uri='https://line.me/R/nv/location'
                    #             ),
                    #             PostbackTemplateAction(
                    #                 label="No",
                    #                 text="Thanks",
                    #                 data="No Location"
                    #             )
                    #         ]
                    #     )
                    # )

                    # line_bot_api.reply_message(
                    #     event.reply_token, message)



        return HttpResponse()
    else:
        return HttpResponseBadRequest()
