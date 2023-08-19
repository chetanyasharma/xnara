import logging
import requests
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from xnara_app.drf_utils import Response
from xnara_app.exception_handler import exception_handler

from .constants import URL_TO_API_1, URL_TO_API_2


class Webhook(APIView):
    """
    A view for retreving data from two apis
    and appending them in given format.
    """
    permission_classes = (AllowAny,)

    # added custom exception handler for all various exceptions
    @exception_handler(api_level=True)
    def get(self, request):
        new_list = []
        response_from_api1 = (requests.get(URL_TO_API_1)).json()
        response_from_api2 = (requests.get(URL_TO_API_2)).json()
        map_dict = {}
        for i, item in enumerate(response_from_api1):
            response_data = {}
            response_data['customer_id'] = item['customer_idiii']
            response_data['id'] = item['id']
            response_data['pack1'] = []
            map_dict[item['customer_id']] = i
            for pac_data in item['pack_data']:
                response_data['pack1'].append(
                    "{ingredients} {quantity}{unit}".format(ingredients=pac_data['ingredient'],
                                                            quantity=pac_data['quantity'],
                                                            unit=pac_data['unit']))
            new_list.append(response_data)
        for items in response_from_api2:
            if items['customer_id'] in map_dict.keys():
                postion = map_dict[items['customer_id']]
                new_list[postion]['pack2'] = []
                for pac_data in items['pack_data']:
                    new_list[postion]['pack2'].append(
                        "{ingredients} {quantity}{unit}".format(ingredients=pac_data['ingredient'],
                                                                quantity=pac_data['quantity'],
                                                                unit=pac_data['unit']))
        return Response(new_list)
