import filecmp
from flask import Flask, render_template, request, send_file
import xxx
import aqgFunction
from random import sample
import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext 
from tkinter import INSERT
import speech_recognition as sr
from gtts import gTTS
import time
import playsound
from deep_translator import GoogleTranslator
import pyttsx3
from gtts import gTTS
import os
import win32com.client as wincl
from pydub import AudioSegment
from pydub.playback import play
import io
from ffmpeg import input, output


globalSorular = []

app = Flask(__name__)

@app.route('/')
def home():
    dolar = xxx.x
    return render_template('index.html', dolar=dolar)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sorular.html')
def sorular():
    return render_template('sorular.html')

@app.route('/okumaSinavi.html')
def okuma_sinavi():
    return render_template('okumaSinavi.html')

@app.route('/kaydet-secilen-sorular', methods=['POST'])
def kaydet_secilen_sorular():
    secilen_sorular = request.form['secilenSorular']
    # secilenSorular.txt dosyasına kaydetme işlemi burada yapılmalı
    with open('secilenSorular.txt', 'w', encoding='utf-8') as file:
        file.write(secilen_sorular)
    return 'Başarılı', 200

@app.route('/save-text', methods=['POST'])
def save_text():
    metin = request.form['metin']
    with open('metin.txt', 'w') as file:
        file.write(metin)
    soruUret()  # Metin kaydedildikten sonra soruları üret
    return 'Metin başarıyla kaydedildi ve sorular üretildi!'

@app.route('/get-tum-sorular', methods=['GET'])
def get_tum_sorular():
    try:
        with open('sorular.txt', 'r', encoding='utf-8') as file:
            sorular = file.read()
        return sorular
    except Exception as e:
        return str(e), 500  # 500 hatası: Sunucu hatası


def soruUret():
    global globalSorular
    aqg = aqgFunction.AutomaticQuestionGenerator()
    with open("sorular.txt", "w", encoding="utf-8") as soruDosyasi, open("cevaplar.txt", "w", encoding="utf-8") as cevapDosyasi:
        textAl = open("metin.txt").read()
        translated_text = GoogleTranslator(source='auto', target='en').translate(textAl)
        sorular = aqg.aqgParse(translated_text)

        translated_sorular = translate_text_2d_array(sorular)
        soruFormatindaSorular = aqg.display(translated_sorular)
        for soru_cevap in translated_sorular:
            if len(soru_cevap) >= 2:  # Eğer hem soru hem de cevap mevcutsa
                soru = soru_cevap[0]  # Soru
                cevap = soru_cevap[1]  # Cevap
                soruDosyasi.write(soru + '\n')
                cevapDosyasi.write(cevap + '\n')
                print(translated_sorular)
                print("234")



def translate_text_2d_array(text_2d_array, target_language='tr'):
    translated_texts = []
    for row in text_2d_array:
        translated_row = []
        for text in row:
            translated = GoogleTranslator(source='auto', target=target_language).translate(text)
            translated_row.append(translated)
        translated_texts.append(translated_row)
    return translated_texts

@app.route('/get-sorular')
def get_sorular():
    try:
        with open("sorular.txt", "r", encoding="utf-8") as file:
            sorular = file.read()
        return sorular
    except Exception as e:
        return str(e), 500  # 500 hatası: Sunucu hatası
    

if __name__ == '__main__':
    app.run(debug=True)
