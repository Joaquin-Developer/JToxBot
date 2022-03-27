# -*- coding: utf-8 -*-

import wikipedia
from command_functions import translator
# import translator   # for tests with "if __name__ == __main__"

def get_page(name, number_page):
    try:
        page_name = wikipedia.search(translator.translate_text(name, 'en'))[number_page - 1]
        page = wikipedia.page(page_name)
        page_content = translator.translate_text(page.content[0:3000], 'es')
        page_link = "https://es.wikipedia.org/wiki/{}".format((page.title).replace(" ", "_"))
        text = "{}\n\n{} ...\n\n Mas info en {}\n\nTox.".format(page.title, page_content, page_link)
    except Exception as e:
        print("Error: " + str(e))
        return None
    else:
        return text
    
def search_pages(text):
    try:
        pages = wikipedia.search(text)
        list_pages = "Páginas obtenidas de la búsqueda en Wikipedia:\n\n"
        for i in range(0, len(pages) - 1):
            list_pages += "{} - {}\n\n".format((i + 1), translator.translate_text(pages[i], 'es'))

        list_pages += "Para ver una página en concreto, digita el siguiente comando:\n"
        list_pages += "/page [título]➡[número]\n"
        list_pages += "Ejemplo: /page Uruguay 1\n\n Tox."
    except Exception as e:
        print("Error: \n" + str(e))
        return None
    else:
        return list_pages        

if __name__ == "__main__":
    # Test:
    print(get_page("Uruguay", 1))
