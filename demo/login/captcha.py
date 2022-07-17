"""
验证码登录
"""


from pycloudmusic import LoginMusic163
import asyncio


async def main():
    login = LoginMusic163()
    phone = input("you login phone: ")
    # 发送验证码
    print(await login.send_captcha(phone))
    code, cookie, musicapi = await login.cellphone(
        phone,
        input("you captcha code: "),
        captcha=True
    )
    # 验证登录
    print("=" * 60)
    print(code, cookie, musicapi)
    print("=" * 60)
    print(await musicapi.my())


asyncio.run(main())