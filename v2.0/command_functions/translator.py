from googletrans import Translator

def translate_text(original_text):
    try:
        translator = Translator(service_urls=['translate.googleapis.com'])
        text = translator.translate(original_text, dest='es').text
    except Exception as e:
        print("Error: " + str(e))
        return None
    else:
        return text
