import os

olam = True
while olam:
    print(f'''
    \033[1;33m___________________________
    |
    |\033[1;32m  [ 1 ] \033[1;32mTekshirish.
    |\033[1;32m  [ 2  ] \033[1;32mNomer ulash.
    |\033[1;32m  [ 3  ] \033[1;32mKanal va grga a'zo.
    |\033[1;32m  [ 4  ] \033[1;32mPrem yutganini tekshirish.
    |\033[1;32m  [ 5  ] \033[1;32mBarcha kanalardan chiq.
    |\033[1;32m  [ 6  ] \033[1;32mBarcha gruhlarni ochirish.
    |\033[1;32m  [ 7  ] \033[1;32mTelegram kod olish.
    |\033[1;32m  [ 8  ] \033[1;32mBan akk filter.
    |\033[1;32m  [ 9  ] \033[1;32mKop kanalga a'zo.
    |\033[1;32m  [ 10 ] \033[1;32mAytgan kanaldan chiq.
    |\033[1;32m  [ 11 ] \033[1;32mLickaga yoz.
    |\033[1;32m  [ 12 ] \033[1;32mRasm ornat.
    |\033[1;32m  [ 13 ] \033[1;32mLike bos.
    |\033[1;32m  [ 14 ] \033[1;32mBot Start
    |\033[1;32m  [ 15 ] \033[1;32mSpam tekshir
    |\033[1;32m  [ x ] \033[1;32mChiqish
    |\033[1;33m________MuhYo_______\033''')
    
    bf = f'''\033[1;32m\nTanlang>>>:'''
    
    jm = input(bf)
    if jm == "1":
        os.system("python module/login.py")
    elif jm == "2":
        os.system("python module/reg.py")
    elif jm == "3":
        os.system("python module/join.py")
    elif jm == "4":
        os.system("python premtest.py")
    elif jm == "5":
        os.system("python kanallardanchiqish.py")
    elif jm == "6":
        os.system("python allleave2.py")
    elif jm == "7":
        os.system("python code1.py")
    elif jm == "8":
        os.system("python banfilter.py")
    elif jm == "9":
        os.system("python kk.py")
    elif jm == "10":
        os.system("python kanalliv.py")
    elif jm == "11":
        os.system("python Send_msg.pyc")
    elif jm == "12":
        os.system("python Rasm_pro_s.pyc")
    elif jm == "13":
        os.system("python like.py")
    elif jm == "14":
        os.system("python bot.py")
    elif jm == "15":
        os.system("python spam.py")
    elif jm == "16":
        os.system("python getdata.pyc")

    elif jm == "x":
        olam = False
