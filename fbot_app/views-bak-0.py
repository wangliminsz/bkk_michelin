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

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


# @csrf_exempt
# def callback(request):
#     if request.method == 'POST':
#         signature = request.META['HTTP_X_LINE_SIGNATURE']
#         body = request.body.decode('utf-8')

#         try:
#             events = parser.parse(body, signature)
#         except InvalidSignatureError:
#             return HttpResponseForbidden()
#         except LineBotApiError:
#             return HttpResponseBadRequest()

#         for event in events:
#             # line_bot_api.reply_message(event.reply_token, [ImageSendMessage(original_content_url=imgUrl, preview_image_url=imgPreUrl), TextSendMessage(text=myContent)])
#             print('hello world')

#         return HttpResponse()
#     else:
#         return HttpResponseBadRequest()

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        # 先設定一個要回傳的message空集合
        message = []
        my_str = ''
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        #在這裡將body寫入機器人回傳的訊息中，可以更容易看出你收到的webhook長怎樣#
        # message.append(TextSendMessage(text=str(body)))

        # print('---------------------------')
        # print(message)
        # print('---------------------------')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            # 如果事件為訊息
            if isinstance(event, MessageEvent):
                # print(event.message.type)
                if event.message.type == 'text':
                    mtext = event.message.text
                    if "Please send your location" in mtext:
                        # message.append(TextSendMessage(text='文字訊息'))
                        # my_str = '文字訊息'
                        # line_bot_api.reply_message(event.reply_token,TextSendMessage(text='文字訊息'))

                        # my_str = TextSendMessage(
                        #     text="---文字訊息---",
                        #     quick_reply=QuickReply(
                        #         items=[
                        #             # QuickReplyButton(
                        #             #     action=PostbackAction(
                        #             #         label="Postback", data="回傳資料")
                        #             # ),
                        #             QuickReplyButton(
                        #                 action=MessageAction(
                        #                     label="文字訊息", text="回傳文字")
                        #             ),
                        #             QuickReplyButton(
                        #                 action=DatetimePickerAction(
                        #                     label="時間選擇", data="時間選擇", mode='datetime')
                        #             ),
                        #             QuickReplyButton(
                        #                 action=CameraAction(label="拍照")
                        #             ),
                        #             QuickReplyButton(
                        #                 action=CameraRollAction(label="相簿")
                        #             ),
                        #             QuickReplyButton(
                        #                 action=LocationAction(label="傳送位置")
                        #             )
                        #         ]
                        #     )
                        # )

                        # ButtonsTemplate,
                        # MessageTemplateAction

                        # ConfirmTemplate
                        # PostbackTemplateAction

                        message = TemplateSendMessage(
                            alt_text='Location',
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

                    # message = TemplateSendMessage(
                    #     alt_text='訂單預約資料',
                    #     template=ConfirmTemplate(
                    #         text="預約資料是否正確?",
                    #         actions=[
                    #             PostbackTemplateAction(
                    #                 label="是",
                    #                 text="Yes",
                    #                 data="預約資料正確"
                    #             ),
                    #             PostbackTemplateAction(
                    #                 label="否",
                    #                 text="No",
                    #                 data="預約資料錯誤"
                    #             )
                    #         ]
                    #     )
                    # )

                    # message = TemplateSendMessage(
                    #     alt_text='Buttons template',
                    #     template=ButtonsTemplate(
                    #         title='Menu',
                    #         text='請選擇地區',
                    #         actions=[
                    #             MessageTemplateAction(
                    #                 label='台北市',
                    #                 text='台北市'
                    #             ),
                    #             MessageTemplateAction(
                    #                 label='台中市',
                    #                 text='台中市'
                    #             ),
                    #             MessageTemplateAction(
                    #                 label='高雄市',
                    #                 text='高雄市'
                    #             )
                    #         ]
                    #     )
                    # )

                    # message = TemplateSendMessage(
                    #     alt_text='Buttons template',
                    #     template=ButtonsTemplate(
                    #         title='Menu',
                    #         text='請選擇地區',
                    #         actions=[
                    #             PostbackTemplateAction(
                    #                 label='台北市',
                    #                 text='台北市',
                    #                 data='A&台北市'
                    #             ),
                    #             PostbackTemplateAction(
                    #                 label='台中市',
                    #                 text='台中市',
                    #                 data='A&台中市'
                    #             ),
                    #             PostbackTemplateAction(
                    #                 label='高雄市',
                    #                 text='高雄市',
                    #                 data='A&高雄市'
                    #             )
                    #         ]
                    #     )
                    # )

                    # message = TemplateSendMessage(
                    #     alt_text='Buttons template',
                    #     template=ButtonsTemplate(
                    #         title='Menu',
                    #         text='請選擇美食類別',
                    #         actions=[
                    #             PostbackTemplateAction(  # 將第一步驟選擇的地區，包含在第二步驟的資料中
                    #                 label='火鍋',
                    #                 text='火鍋',
                    #                 data='B&' + area + '&火鍋'
                    #             ),
                    #             PostbackTemplateAction(
                    #                 label='早午餐',
                    #                 text='早午餐',
                    #                 data='B&' + area + '&早午餐'
                    #             ),
                    #             PostbackTemplateAction(
                    #                 label='約會餐廳',
                    #                 text='約會餐廳',
                    #                 data='B&' + area + '&約會餐廳'
                    #             )
                    #         ]
                    #     )
                    # )

                        line_bot_api.reply_message(
                            event.reply_token, message)

            #     elif event.message.type == 'image':
            #         message.append(TextSendMessage(text='圖片訊息'))
            #         line_bot_api.reply_message(event.reply_token, message)

            #     elif event.message.type == 'location':
            #         message.append(TextSendMessage(text='位置訊息'))
            #         line_bot_api.reply_message(event.reply_token, message)

            #     elif event.message.type == 'video':
            #         message.append(TextSendMessage(text='影片訊息'))
            #         line_bot_api.reply_message(event.reply_token, message)

            #     elif event.message.type == 'sticker':
            #         message.append(TextSendMessage(text='貼圖訊息'))
            #         line_bot_api.reply_message(event.reply_token, message)

            #     elif event.message.type == 'audio':
            #         message.append(TextSendMessage(text='聲音訊息'))
            #         line_bot_api.reply_message(event.reply_token, message)

            #     elif event.message.type == 'file':
            #         message.append(TextSendMessage(text='檔案訊息'))
            #         line_bot_api.reply_message(event.reply_token, message)

            # elif isinstance(event, FollowEvent):
            #     print('加入好友')
            #     # line_bot_api.reply_message(event.reply_token,message)

            # elif isinstance(event, UnfollowEvent):
            #     print('取消好友')

            # elif isinstance(event, JoinEvent):
            #     print('進入群組')
            #     # line_bot_api.reply_message(event.reply_token,message)

            # elif isinstance(event, LeaveEvent):
            #     print('離開群組')
            #     # line_bot_api.reply_message(event.reply_token,message)

            # elif isinstance(event, MemberJoinedEvent):
            #     print('有人入群')
            #     # line_bot_api.reply_message(event.reply_token,message)

            # elif isinstance(event, MemberLeftEvent):
            #     print('有人退群')
            #     # line_bot_api.reply_message(event.reply_token,message)

            elif isinstance(event, PostbackEvent):
                print('PostbackEvent')

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
