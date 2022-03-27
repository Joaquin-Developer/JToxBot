from googletrans import Translator

def translate_text(original_text, lang_dest):
    try:
        translator = Translator(service_urls=['translate.googleapis.com'])
        text = translator.translate(original_text, dest=lang_dest).text
    except Exception as e:
        print("Error: " + str(e))
        return None
    else:
        return text
