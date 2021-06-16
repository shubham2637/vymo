from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from foodvymo.models import Merchant
from apis.serializer import MerchantSerializer
from rest_framework.decorators import api_view


@api_view( ['GET'] )
def merchant_list(request):
    merchant_lists = Merchant.objects.all()
    return Response( merchant_lists.values() )


@api_view( ['POST'] )
def add_merchant(request):
    merchant_data = JSONParser().parse( request )
    merchant_serializer = MerchantSerializer( data=merchant_data )
    if merchant_serializer.is_valid():
        merchant_serializer.save()
        return JsonResponse( merchant_serializer.data, status=status.HTTP_201_CREATED )
    return JsonResponse( merchant_serializer.errors, status=status.HTTP_400_BAD_REQUEST )



@api_view( ['GET', 'PUT', 'DELETE'] )
def merchant_detail(request, pk):
    try:
        merchant = Merchant.objects.get( pk=pk )
        if request.method == 'GET':
            merchant_serializer = MerchantSerializer(merchant)
            return JsonResponse(merchant_serializer.data)
        elif request.method == 'PUT':
            merchant_data = JSONParser().parse( request )
            merchant_serializer = MerchantSerializer( merchant, data=merchant_data )
            if merchant_serializer.is_valid():
                merchant_serializer.save()
                return JsonResponse( merchant_serializer.data )
            return JsonResponse( merchant_serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        elif request.method=='DELETE':
            merchant.delete()

    except Merchant.DoesNotExist:
        return JsonResponse( {'message': 'The Merchant does not exist'}, status=status.HTTP_404_NOT_FOUND )



