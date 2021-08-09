from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from pokemons.models import Card, Rarity, Type, Expansion

from .serializers import CardSerializer

@csrf_exempt
def cards_list(request):
    if request.method == 'GET':
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

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