import telebot
import mysql.connector
import mytoken
from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M:%S")
currently = now.strftime("%m/%d/%Y")

TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='broken_guli')
sql=myDb.cursor()
from telebot import apihelper


class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        photo = open('img/cowok-2-hai.png', 'rb')
        myBot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA + "\n           " \
                              "Aku Manager BG Production\n\n" \
                              "💬 Aku bisa bantu kamu dengan perintah :\n" \
                              "🚩 /start untuk memulai\n" \
                              "👱🏻‍♂ /crew melihat biodata crew\n" \
                              "🎥 /channel biodata channel kami\n\n\n" \
                              "👨‍🏫 admin & developer @rizkyfirmansyah 👨‍🏫 "

        # teks = mytoken.SAPA + "\n-- admin & developer @rizkyfirmansyah - BROKEN GULI -- "+"\n" \
        #                 "hari ini tanggal :  "+str(currently)+"\nJam : "+str(time)
        # myBot.reply_to(message, teks)

        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['hadir'])
    def start(message):
        teks = "✅ Kamu Sudah hadir di HOME SATE : \n" \
               "📆 tanggal : "+str(currently)+"\n📣 Pada Pukul :  "+str(time)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['channel'])
    def start(message):
        teks = "🙌🏻 Kunjungi channel kami di youtube\n" \
               "https://www.youtube.com/channel/UCYnMhtSWqATXFOmfxv_Nz-Q\n\n" \
               "📣 Jangan lupa subscribe & nyalain lonceng nya 🔔"
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['crew'])
    def menu_data_siswa(message):
        query = "SELECT nama_crew,job FROM `crew`"
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if (jmldata > 0):
            no = 0
        for x in data:
            no += 1
            kumpuldata = kumpuldata + str(x)
            print(kumpuldata)
            kumpuldata = kumpuldata.replace('(', '')
            kumpuldata = kumpuldata.replace(')', '\n')
            kumpuldata = kumpuldata.replace("'", '')
            kumpuldata = kumpuldata.replace(",", '')

        else:
            print('data kosong')
        myBot.reply_to(message, str(kumpuldata))

print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)