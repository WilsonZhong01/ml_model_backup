#-*-coding:utf8-*- 
import json
def data_prepro(chat_user_info):

    region = []
    city = []
    signature = []
    count = 0
    for one in chat_user_info:
        one_info = json.loads(one)
#         print(one_info[0]['NickName'])  # if encounting list issues, just print the username above the empty one
        region.append(one_info[0]['Province'])
        city.append(one_info[0]['City'])
        signature.append(one_info[0]['Signature'])
        # check if the userinfo was saved in database
        count += 1
        if one_info[0]['Province']:
            continue
            print(count)
            print(one_info[0]['NickName'])
    return region, city, signature