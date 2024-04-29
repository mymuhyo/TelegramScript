import os

while True:
    print('''
    \033[1;33m___________________________
    |
    |\033[1;32m  [ 1 ] \033[1;32mAkkount ulash.
    |\033[1;32m  [ 2 ] \033[1;32mKanal yoki grga qo'shilish.
    |\033[1;32m  [ 3 ] \033[1;32mBarcha Guruh(kanal)dan chiqish.
    |\033[1;32m  [ 4 ] \033[1;32mBarcha kanalardan chiq.
    |\033[1;32m  [ 5 ] \033[1;32mBarcha gruhlarni ochirish.
    |\033[1;32m  [ 6 ] \033[1;32mTelegram kod olish.
    |\033[1;32m  [ 7 ] \033[1;32mBan akk filter.
    |\033[1;32m  [ 8 ] \033[1;32mKop kanalga a'zo.
    |\033[1;32m  [ 9 ] \033[1;32mAytgan kanaldan chiq.
    |\033[1;32m  [ 10 ] \033[1;32mLickaga yoz.
    |\033[1;32m  [ 11 ] \033[1;32mRasm ornat.
    |\033[1;32m  [ 12 ] \033[1;32mLike bos.
    |\033[1;32m  [ 13 ] \033[1;32mBot Start
    |\033[1;32m  [ 14 ] \033[1;32mSpam tekshir
    |\033[1;32m  [ x ] \033[1;32mChiqish
    |\033[1;33m________MuhYo_______\033''')

    option = input("\033[1;32m\nTanlang>>>: ").strip()

    if option == "x":
        break

    script_map = {
        "1": "module/reg.py",
        "2": "module/join.py",
        "3": "module/all_leave.py",
        "4": "kanallardanchiqish.py",
        "5": "allleave2.py",
        "6": "code1.py",
        "7": "banfilter.py",
        "8": "kk.py",
        "9": "kanalliv.py",
        "10": "Send_msg.pyc",
        "11": "Rasm_pro_s.pyc",
        "12": "like.py",
        "13": "bot.py",
        "14": "spam.py",
        "15": "getdata.pyc"  # Assuming 15 is for another script, add it accordingly
    }

    if option in script_map:
        os.system(f"python {script_map[option]}")
    else:
        print("Invalid option. Please select a valid option.")
