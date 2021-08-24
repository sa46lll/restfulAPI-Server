from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.parsers import JSONParser

from .models import Addresses
from .serializers import AddressesSerializer


@csrf_exempt
def address_list(request):
    if request.method == 'GET': # 데이터 조회
        query_set = Addresses.objects.all() # addresses 객체 모두 가져옴
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST': # 데이터 생성
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save() # 객체 생성
            return JsonResponse(serializer.data, status=201) # 성공
        return JsonResponse(serializer.errors, status=400) # 실패


@csrf_exempt
def address(request, pk):
    obj = Addresses.objects.get(pk=pk) # filter은 여러개

    if request.method == 'GET': # 데이터 조회
        serializer = AddressesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT': # 데이터 생성
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save() # 객체 생성
            return JsonResponse(serializer.data, status=201) # 성공
        return JsonResponse(serializer.errors, status=400) # 실패

    elif request.method =='DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_name = data['name']
        print(search_name)
        # search_name = request.POST.get('name', False) # False -> 없으면 아무것도 안하고 있으면 쓴다
        obj = Addresses.objects.get(name=search_name)
        print(obj.phone_number)
        
        if data['phone_number'] == obj.phone_number:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
