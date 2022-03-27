# pylint: disable=broad-except
# -*- coding: utf-8 -*-

import wikipedia
import translator

# import translator   # for tests with "if __name__ == __main__"


class Wikipedia:
    """Wrapper"""

    @staticmethod
    def get_page(name, number_page):
        """Busqueda a una pagina"""
        try:
            page_name = wikipedia.search(translator.translate_text(name, "en"))[number_page - 1]
            page = wikipedia.page(page_name)
            page_content = translator.translate_text(page.content[0:3000], "es")
            page_link = "https://es.wikipedia.org/wiki/{}".format((page.title).replace(" ", "_"))
            text = "{}\n\n{} ...\n\n Mas info en {}\n\nTox.".format(page.title, page_content, page_link)
            return text

        except Exception as ex:
            print("Error: " + str(ex))
            return None

    @staticmethod
    def search_pages(text):
        """Buscar pagina en wikipedia"""
        try:
            pages = wikipedia.search(text)
            list_pages = "Páginas obtenidas de la búsqueda en Wikipedia:\n\n"
            for i in range(0, len(pages) - 1):
                list_pages += "{} - {}\n\n".format((i + 1), translator.translate_text(pages[i], "es"))

            list_pages += "Para ver una página en concreto, digita el siguiente comando:\n"
            list_pages += "/page [título]➡[número]\n"
            list_pages += "Ejemplo: /page Uruguay 1\n\n Tox."
            return list_pages

        except Exception as ex:
            print("Error: \n" + str(ex))
            return None


if __name__ == "__main__":
    pass
