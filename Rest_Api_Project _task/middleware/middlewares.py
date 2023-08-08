import socket
import time
import json
from api.models import Request_Log


class RequestLogMiddleware():
    def __init__(self, get_response):
        print("Middle ware tak pahaucha")
        self.get_response = get_response
        self.start_time = time.time()


    def process_request(self, request):
        if request.method in ['GET','POST', 'PUT', 'PATCH']:
            request.req_body = request.body
        return request


    def __call__(self, request):
        request = self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)
        return response


    def process_response(self, request, response):
        request_path = request.get_full_path()

        if not request_path.startswith(''):
            return response
        request_data = None
        content_type = request.META.get('CONTENT_TYPE',  'application/json')
        request_type = request.META.get('HTTP_ACCEPT', content_type)
        if request.method in ['GET','POST', 'PUT', 'PATCH']:
            if content_type == 'application/json':
                request_data = json.loads(request.req_body)
        data = {
            "user_id": request.user.pk,
            "request_method": request.method,
            "request_path": request_path,
            "response_status": response.status_code,
            "remote_address": request.META['REMOTE_ADDR'],
            "server_hostname": socket.gethostname(),
            "request_body": request_data,
            "run_time": time.time() - self.start_time
        }
        print(data)
        request_instance=Request_Log(
            user_id=data['user_id'],
            request_method=data['request_method'],
            request_path=data['request_path'],
            response_status=data['response_status'],
            remote_address=data['remote_address'],
            server_hostname=data['server_hostname'],
            request_body=data['request_body'],
            run_time=data['run_time']
        )
        request_instance.save()
        return response