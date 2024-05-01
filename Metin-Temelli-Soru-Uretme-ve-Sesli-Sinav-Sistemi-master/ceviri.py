from deep_translator import GoogleTranslator


try:
    # Kullanıcıdan metni al
    input_text = input("Lütfen çevrilmek istenen metni girin: ")

    # Metni İngilizce'ye çevir
    translated_text = GoogleTranslator(source='auto', target='en').translate(input_text)

    print("Çevirilen metin:", translated_text)
except Exception as e:
    print("Bir hata oluştu:", e)
