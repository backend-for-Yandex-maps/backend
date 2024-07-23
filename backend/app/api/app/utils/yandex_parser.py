from yandex_reviews_parser.utils import YandexParser


class get_data:
    @staticmethod
    def request_to_data(id_ya, request_type):
        id_ya = int(id_ya)
        request_type = str(request_type)
        parser = YandexParser(id_ya)
        company = parser.parse(type_parse='reviews')  # список отзывов
        print(company)
        return company
