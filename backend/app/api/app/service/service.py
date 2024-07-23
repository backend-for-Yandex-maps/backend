from ..utils.yandex_parser import get_data
from ..utils.convert_to_json import convert_data_to_json
from ..repository.repository import repository


class service:
    @staticmethod
    def create_map_organizations(points_id, request_type):
        data = get_data.request_to_data(points_id, request_type)
        data_formatted_json_id = convert_data_to_json.convert_data(data,points_id)
        repository.bd_create(data_formatted_json_id)
        return data_formatted_json_id

    @staticmethod
    def read_map_organizations(points_id):
        repository.bd_read(points_id)

    @staticmethod
    def update_map_organizations(points_id, request_type):
        service.delete_map_organizations(points_id)  # можно попробовать удалить из бд потом добавить измененную
        service.create_map_organizations(points_id, request_type)

    @staticmethod
    def delete_map_organizations(points_id):
        repository.bd_delete(points_id)
