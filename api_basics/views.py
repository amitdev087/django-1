from re import A
from django.shortcuts import render

from django.http.response import HttpResponse,JsonResponse 
from rest_framework.parsers import JSONParser
from .models import Article
from .serilizers import ArticleSerializer

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def article_list(request):
    if request.method=="GET":
        articles=Article.objects.all()
        serilizer=ArticleSerializer(articles,many=True)
        return JsonResponse(serilizer.data, safe=False)

    elif request.method=="POST":
        data=JSONParser().parse(request)
        serilizer=ArticleSerializer(data=data)

        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse(serilizer.data ,status=201)
        return JsonResponse(serilizer.errors,status=400)


@csrf_exempt
def article_details(request,pk):
    try:
        article=Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=="GET":
        serilizer=ArticleSerializer(article)
        return JsonResponse(serilizer.data ,status=201)

    elif request.method=="PUT":
        data=JSONParser().parse(request)
        serilizer=ArticleSerializer(article,data=data)
        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse(serilizer.data )
        return JsonResponse(serilizer.errors,status=400)

    elif request.method=="DELETE":
        article.delete()
        return HttpResponse(status=204)

