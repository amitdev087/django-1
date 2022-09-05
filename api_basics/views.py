import imp
from re import A
from django.shortcuts import render

from django.http.response import HttpResponse,JsonResponse 
from rest_framework.parsers import JSONParser
from .models import Article
from .serilizers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# @csrf_exempt
# def article_list(request):
#     if request.method=="GET":
#         articles=Article.objects.all()
#         serilizer=ArticleSerializer(articles,many=True)
#         return JsonResponse(serilizer.data, safe=False)

#     elif request.method=="POST":
#         data=JSONParser().parse(request)
#         serilizer=ArticleSerializer(data=data)

#         if serilizer.is_valid():
#             serilizer.save()
#             return JsonResponse(serilizer.data ,status=201)
#         return JsonResponse(serilizer.errors,status=400)


# @csrf_exempt
# def article_details(request,pk):
#     try:
#         article=Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method=="GET":
#         serilizer=ArticleSerializer(article)
#         return JsonResponse(serilizer.data ,status=201)

#     elif request.method=="PUT":
#         data=JSONParser().parse(request)
#         serilizer=ArticleSerializer(article,data=data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return JsonResponse(serilizer.data )
#         return JsonResponse(serilizer.errors,status=400)

#     elif request.method=="DELETE":
#         article.delete()
#         return HttpResponse(status=204)

@api_view(["GET","POST"])
def article_list(request):
    if request.method=="GET":
        articles=Article.objects.all()
        serilizer=ArticleSerializer(articles,many=True)
        return Response(serilizer.data)

    elif request.method=="POST":
        
        serilizer=ArticleSerializer(data=request.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data ,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def article_details(request,pk):
    try:
        article=Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serilizer=ArticleSerializer(article)
        return Response(serilizer.data ,status=201)

    elif request.method=="PUT":
       
        serilizer=ArticleSerializer(article,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data )
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
