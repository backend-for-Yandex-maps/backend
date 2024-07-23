import json


class convert_data_to_json:
    @staticmethod
    def convert_data(data,points_id):
        # with open(file_path, 'r', encoding='utf-8') as file:
        # data = file.read()

        #reviews_data = json.loads(data)

        reviews = data['company_reviews']

        processed_reviews = []

        # Обрабатываем каждый отзыв
        for review in reviews:
            processed_review = {
                "Имя": review['name'],
                "Иконка": review['icon_href'],
                "Дата": review['date'],
                "Звезды": review['stars'],
                "Текст отзыва": review['text'],
                "Ответ": review['answer'],
                "Организация": str(points_id)
            }
            processed_reviews.append(processed_review)

        # Преобразуем список обработанных отзывов обратно в JSON-формат
        processed_reviews_json = json.dumps(processed_reviews, ensure_ascii=False, indent=4)

        # with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # output_file.write(processed_reviews_json)

        print(processed_reviews_json)
        print(f"Данные были успешно преобразованы")
        return processed_reviews_json
