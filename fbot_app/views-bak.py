# if event.message.type == 'text':
#                     mtext = event.message.text
#                     if "Please send your location" in mtext:

#                         # ButtonsTemplate,
#                         # MessageTemplateAction

#                         # ConfirmTemplate
#                         # PostbackTemplateAction

#                         message = TemplateSendMessage(
#                             alt_text='Send your location?',
#                             template=ConfirmTemplate(
#                                 text="Send your location?",
#                                 actions=[
#                                     URITemplateAction(
#                                         type='uri',
#                                         label='Yes',
#                                         uri='https://line.me/R/nv/location'
#                                     ),
#                                     PostbackTemplateAction(
#                                         label="No",
#                                         text="Thanks",
#                                         data="No Location"
#                                     )
#                                 ]
#                             )
#                         )

#                         line_bot_api.reply_message(
#                             event.reply_token, message)

                    # if mtext == 'Hello':
                    #     # alt_text='Buttons template',

                    #     message = TemplateSendMessage(
                    #         alt_text='Find MICHELIN',
                    #         template=ButtonsTemplate(
                    #             title='Menu',
                    #             text='Find your favorite MICHELIN:',
                    #             actions=[
                    #                 PostbackTemplateAction(
                    #                     label='by Location',
                    #                     text='Please send your location ...',
                    #                     data='AAAA&byloc'
                    #                 ),
                    #                 PostbackTemplateAction(
                    #                     label='by Style & Location',
                    #                     text='Please choose food style:',
                    #                     data='BBBB&bystyleloc',
                    #                 ),
                    #                 PostbackTemplateAction(
                    #                     label='List All',
                    #                     data='CCCC&bylist',
                    #                 )
                    #             ]
                    #         )
                    #     )

                    #     line_bot_api.reply_message(event.reply_token, message)

#                 elif event.message.type == 'location':
#                     # print('location message')
#                     # print(event.message.latitude)
#                     # print(event.message.longitude)
#                     mybkk = calDistance(
#                         event.message.latitude, event.message.longitude)
#                     # ltext = '位置訊息\n\n' + 'lat - ' + str(event.message.latitude) + '\n' + 'lng - ' + str(event.message.longitude)
#                     # ltext = ltext +'\n'+ mdata[0]['mbname']+'\n\n' + mybkk[0]['mbname'] + '\n\n' + mybkk[0]['mbcontact']
#                     # message.append(TextSendMessage(text='位置訊息'))
#                     ltext = "Nearby MICHELIN restaurants:"
#                     message1 = TextSendMessage(text=ltext)
#                     message2 = flex_example(mybkk)

#                     # message.append(message1)
#                     # message.append(message2)
#                     line_bot_api.reply_message(
#                         event.reply_token, [message1, message2])
#                     # line_bot_api.reply_message(event.reply_token, message1)


# ------------------------------------------------------------------------------------




            # if isinstance(event, MessageEvent):
            #     mtext=event.message.text
            #     # message=[]
            #     # message.append(TextSendMessage(text=mtext))
            #     # line_bot_api.reply_message(event.reply_token,message)

            #     myContent = ''  # 回覆使用者的內容
            #     # print(mtext)

            #     if (mtext.isdigit()):

            #         if (int(event.message.text)>=1) and (int(event.message.text)<=325):
            #                 mySequence = int(event.message.text)

            #                 #print(mySequence)

            #                 # 篩選 poem 資料表
            #                 selectedPoem = poempoem.objects.filter(poemid=mySequence).first()

            #                 #print('--------------------------')
            #                 #print(selectedPoem.poemen)
            #                 #print(selectedPoem.all)
            #                 #myContent = "Poem"

            #                 # print (selectedPoem.poemen.splitlines())
            #                 # print('--------------------------')

            #                 enStr = selectedPoem.poemen1

            #                 if len(selectedPoem.poemen2) >= 1:
            #                     enStr = enStr + '\n\n' + selectedPoem.poemen2
            #                 if len(selectedPoem.poemen3) >= 1:
            #                     enStr = enStr + '\n\n' + selectedPoem.poemen3
            #                 if len(selectedPoem.poemen4) >= 1:
            #                     enStr = enStr + '\n\n' + selectedPoem.poemen4

            #                 cnStr = selectedPoem.poemcn1

            #                 if len(selectedPoem.poemcn2) >= 1:
            #                     cnStr = cnStr + '\n\n' + selectedPoem.poemcn2
            #                 if len(selectedPoem.poemcn3) >= 1:
            #                     cnStr = cnStr + '\n\n' + selectedPoem.poemcn3
            #                 if len(selectedPoem.poemcn4) >= 1:
            #                     cnStr = cnStr + '\n\n' + selectedPoem.poemcn4

            #                 myContent += 'Stray Birds 飛鳥集' + '\n' +  mtext + '\n\n' + enStr + '\n\n' + cnStr

            #         else:
            #             myContent = "Poem from 1 to 325, please try again..."
            #     else:
            #         myContent = "Poem from 1 to 325, please try again..."

            #     # {
            #     #     "type": "image",
            #     #     "originalContentUrl": "https://example.com/original.jpg",
            #     #     "previewImageUrl": "https://example.com/preview.jpg"
            #     # }


            #     imgUrl = "https://straybirds.herokuapp.com/media/a.jpg"
            #     imgPreUrl = "https://straybirds.herokuapp.com/media/a.jpg"




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
