import wikipedia
import translator

def get_page(name, number_page):
    try:
        page_name = wikipedia.search(name)[number_page - 1]
        page = wikipedia.page(page_name)
        text = "{}\n\n{}\n\nTox.".format(page.title, page.content)
    except Exception as e:
        print("Error: \n" + str(e))
        return None
    else:
        return text
    
def search_pages(text):
    try:
        pages = wikipedia.search(text)
        list_pages = "Páginas obtenidas de la búsqueda en Wikipedia:\n\n"
        for i in range(0, len(pages) - 1):
            list_pages += "{} - {}\n\n".format((i + 1), translator.translate_text(pages[i]))

        list_pages += "Para ver una página en concreto, digita el siguiente comando:\n"
        list_pages += "/wikipage [Búsqueda] [número de página]\n"
        list_pages += "Ejemplo: /wikipage Uruguay 1\n\n Tox."
    except Exception as e:
        print("Error: \n" + str(e))
        return None
    else:
        return list_pages        


