# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

# a command only for my yuxuan
# 爱你亲爱哒 我们一起一生一死！
# 雨萱我希望可以meet你

# importing files
from app.utils.messages import send_message

async def bot_person_yuxuan(app, msg):
    message: list[str] = app.cacher.cache["interactions"]["bot_person"]["bot_yuxuan"][app.cacher.cache["config"]["config"]["lang"]]
    await send_message(msg, message[0] + "\n" + message[1] , 1.3)
    await send_message(msg, message[2] , 0.3)