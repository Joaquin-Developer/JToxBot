from googletrans import Translator


def translate_text(original_text, lang_dest):
    try:
        translator = Translator(service_urls=["translate.googleapis.com"])
        text = translator.translate(original_text, dest=lang_dest).text
        return text
    except Exception as ex:
        return f"Error {str(ex)}"
