from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from pokemons.models import Card, Rarity, Type, Expansion
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters
from .serializers import CardSerializer





class CardFilter(django_filters.FilterSet):
    card_name = django_filters.CharFilter(lookup_expr='iexact')
    card_expansion = django_filters.CharFilter(lookup_expr='iexact')
    card_type = django_filters.CharFilter(lookup_expr='iexact')
    card_rarity = django_filters.CharFilter(lookup_expr='iexact')
    card_hp = django_filters.NumberFilter()
    card_hp__gt = django_filters.NumberFilter(field_name='card_hp', lookup_expr='gt')
    card_hp__lt = django_filters.NumberFilter(field_name='card_hp', lookup_expr='lt')
    card_hp__gte = django_filters.NumberFilter(field_name='card_hp', lookup_expr='gte')
    card_hp__lte = django_filters.NumberFilter(field_name='card_hp', lookup_expr='lte')
    card_price__gt = django_filters.NumberFilter(field_name='card_price', lookup_expr='gt')
    card_price__lt = django_filters.NumberFilter(field_name='card_price', lookup_expr='lt')
    card_price__gte = django_filters.NumberFilter(field_name='card_price', lookup_expr='gte')
    card_price__lte = django_filters.NumberFilter(field_name='card_price', lookup_expr='lte')
    card_creation_date__gt = django_filters.DateTimeFilter(field_name='card_creation_date', lookup_expr='gt')
    card_creation_date__lt = django_filters.DateTimeFilter(field_name='card_creation_date', lookup_expr='lt')
    card_creation_date__gte = django_filters.DateTimeFilter(field_name='card_creation_date', lookup_expr='gte')
    card_creation_date__lte = django_filters.DateTimeFilter(field_name='card_creation_date', lookup_expr='lte')
    card_is_first_edition__eq = django_filters.BooleanFilter(field_name='card_is_first_edition')
    
    class Meta:
        model = Card
        fields = ['card_name','card_expansion','card_type','card_rarity','card_hp','card_price','card_creation_date','card_is_first_edition']
            
        



class CardList(generics.ListAPIView):
    queryset=Card.objects.all()
    serializer_class=CardSerializer
    filterset_class = CardFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['card_name', 'card_expansion','card_type','card_rarity']
    ordering_fields = ['card_name', 'card_price', 'id','card_creation_date','card_hp']
    ordering = ['id']

    

@csrf_exempt
def cards_list(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = CardSerializer(data=data)
        error = False
 
        rarity = data["card_rarity"]
        type = data["card_type"]
        expansion = data["card_expansion"]
        hp = data["card_hp"]
        image = data["card_image"]
        
        if image[-3:] not in ('png','jpg'):
            error = True
            error_msg = 'Wrong value for Image. Image must be an url with a PNG or JPG image. Read the Documentation for more information.'
        
        if hp % 10 != 0:
            error = True
            error_msg = 'Wrong value for HP. HP must be a multiple of 10. Read the Documentation for more information.'
            
        if not Expansion.objects.filter(expansion_desc=expansion):
            error = True
            error_msg = 'Wrong value for Expansion. Read the Documentation for more information.'
        
        if not Rarity.objects.filter(rarity_desc=rarity):
            error = True
            error_msg = 'Wrong value for Rarity. Read the Documentation for more information.'
            
        if not Type.objects.filter(type_desc=type):
            error = True
            error_msg = 'Wrong value for Type. Read the Documentation for more information.'
        
        if error:
            return JsonResponse({"error": error_msg}, status=400)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def card_detail(request, pk):
    try:
        cards = Card.objects.get(pk=pk)
    except Card.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CardSerializer(cards)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CardSerializer(cards, data=data)
        
        error = False
        
        rarity = data["card_rarity"]
        type = data["card_type"]
        expansion = data["card_expansion"]
        hp = data["card_hp"]
        image = data["card_image"]
        
        if image[-3:] not in ('png','jpg'):
            error = True
            error_msg = 'Wrong value for Image. Image must be an url with a PNG or JPG image. Read the Documentation for more information.'
        
        if hp % 10 != 0:
            error = True
            error_msg = 'Wrong value for HP. HP must be a multiple of 10. Read the Documentation for more information.'
                
        if not Expansion.objects.filter(expansion_desc=expansion):
            error = True
            error_msg = 'Wrong value for Expansion. Read the Documentation for more information.'
        
        if not Rarity.objects.filter(rarity_desc=rarity):
            error = True
            error_msg = 'Wrong value for Rarity. Read the Documentation for more information.'
            
        if not Type.objects.filter(type_desc=type):
            error = True
            error_msg = 'Wrong value for Type. Read the Documentation for more information.'
        
        if error:
            return JsonResponse({"error": error_msg}, status=400)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cards.delete()
        return HttpResponse(status=204)