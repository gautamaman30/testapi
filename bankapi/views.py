from .models import Banks
from rest_framework.decorators import APIView
from django.http import JsonResponse, HttpResponse


class ApiRoot(APIView):

    def get(self, request):
        return JsonResponse({"message": "go to endpoints api/branches/autocomplete or api/branches"})


class SearchByBranch(APIView):

    def get(self, request):
        q = self.request.query_params.get('q')
        limit = self.request.query_params.get('limit')
        offset = self.request.query_params.get('offset')
        if q is None:
            return JsonResponse({"message": "Enter Valid Data"})
        data = Banks.objects.all()
        temp_list = []
        response_data = {"branches": []}
        for i in data:
            if q.lower() in i.branch.lower():
                temp_dict = {"ifsc": i.ifsc_code, "bank_id": i.bank_id, "branch": i.branch, "address": i.address, "city": i.city, "district": i.district, "state": i.state, "bank_name": i.bank_name}
                temp_list.append(temp_dict.copy())
        if len(temp_list) == 0:
            return JsonResponse(response_data)
        if offset is not None and limit is not None:
            offset = int(offset)
            limit = int(limit)
            if offset < len(temp_list):
                if limit == 0:
                    response_data = {"branches": []}
                elif (offset+limit) < len(temp_list):
                    response_data = {"branches": temp_list[offset:offset+limit]}
                else:
                    response_data = {"branches": temp_list[offset:]}
            return JsonResponse(response_data)
        elif offset is not None and limit is None:
            offset = int(offset)
            if offset < len(temp_list):
                response_data = {"branches": temp_list[offset:]}
            return JsonResponse(response_data)
        elif offset is None and limit is not None:
            limit = int(limit)
            if limit == 0:
                response_data = {"branches": []}
            elif limit < len(temp_list):
                response_data = {"branches": temp_list[0:limit]}
            else:
                response_data = {"branches": temp_list}
            return JsonResponse(response_data)
        response_data = {"branches": temp_list}
        return JsonResponse(response_data)


class SearchByAll(APIView):

    def get(self, request):
        q = self.request.query_params.get('q')
        limit = self.request.query_params.get('limit')
        offset = self.request.query_params.get('offset')
        if q is None:
            return JsonResponse({"message": "Enter Valid Data"})
        data = Banks.objects.all()
        temp_list = []
        response_data = {"branches": []}
        for i in data:
            if q == i.ifsc_code or q == i.bank_id or q.lower() in i.branch.lower() or q.lower() in i.address.lower() or q.lower() in i.city.lower() or q.lower() in i.district.lower() or q.lower() in i.state.lower() or q.lower() in i.bank_name.lower():
                temp_dict = {"ifsc": i.ifsc_code, "bank_id": i.bank_id, "branch": i.branch, "address": i.address, "city": i.city, "district": i.district, "state": i.state, "bank_name": i.bank_name}
                temp_list.append(temp_dict.copy())
        if len(temp_list) == 0:
            return JsonResponse(response_data)
        if offset is not None and limit is not None:
            offset = int(offset)
            limit = int(limit)
            if offset < len(temp_list):
                if limit == 0:
                    response_data = {"branches": []}
                elif (offset + limit) < len(temp_list):
                    response_data = {"branches": temp_list[offset:offset + limit]}
                else:
                    response_data = {"branches": temp_list[offset:]}
            return JsonResponse(response_data)
        elif offset is not None and limit is None:
            offset = int(offset)
            if offset < len(temp_list):
                response_data = {"branches": temp_list[offset:]}
            return JsonResponse(response_data)
        elif offset is None and limit is not None:
            limit = int(limit)
            if limit == 0:
                response_data = {"branches": []}
            elif limit < len(temp_list):
                response_data = {"branches": temp_list[0:limit]}
            else:
                response_data = {"branches": temp_list}
            return JsonResponse(response_data)
        response_data = {"branches": temp_list}
        return JsonResponse(response_data)

