import cv2
from cv2 import CascadeClassifier
import datetime
import telebot
import sys
import config

# важные переменные

token = ""  # token telegram bot || токен вашего телеграм бота
bot = telebot.TeleBot(token)  # переменная бота
num = 0  # счёт
faceCascade = CascadeClassifier('haarcascade_frontalface_default.xml')  # переменная скрипт
video_capture = cv2.VideoCapture(0)  # переменная камеры


# важные переменные

@bot.message_handler(content_types=['photo'])  # функция отправки фото
def photos(num):
    day1 = datetime.datetime.now().strftime("%H:%M:%S") # время
    bot.send_photo(chat_id='540220315', photo=open('photos_or_videos/photo' + str(num) + '.jpg', 'rb'),
                   caption='ВРЕМЯ: ' + str(day1)) #отправка сообещния

@bot.message_handler(content_types=['video'])
def video(num):
    day1 = datetime.datetime.now().strftime("%H:%M:%S")  # время
    bot.send_video(chat_id='540220315', photo=open('photos_or_videos/vide' + str(num) + '.mp4', 'rb'),
                   caption='ВРЕМЯ: ' + str(day1))  # отправка сообещния

# цикл анализа
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()  # береём кадр
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # серая картинка
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                         flags=cv2.CASCADE_SCALE_IMAGE)  # анализ картинки

    hel_day = datetime.datetime.now().strftime("%H:%M:%S")  # время и дата
    video_writer = cv2.VideoWriter('photos_or_videos/vidos' + str(hel_day) + '.avi', cv2.VideoWriter_fourcc(*"DIVX"),
                                   20,
                                   (640, 480))  # запись видео

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        day1 = datetime.datetime.now().strftime("%H:%M:%S")  # время и дата
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # рисование треугольника
        cv2.imwrite('photos_or_videos/photo' + str(num) + '.jpg', frame)  # запись фото
        # lol()
        photos(num)  # вызов функции
        video_writer.write(frame)  # запись видео
        num += 1

    # Display the resulting frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # остановка программы
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
bot.polling(none_stop=True)
