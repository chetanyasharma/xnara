from rest_framework.response import Response as drf_response

class Response(drf_response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None,
                 msg=''):
        super().__init__(data=data, status=status, template_name=template_name, headers=headers, exception=exception,
                         content_type=content_type)
        self.data = {'data': data, 'msg': msg}