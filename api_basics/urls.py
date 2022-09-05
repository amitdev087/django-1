
from django.urls import path 
from .views import article_list,article_details,ArticleApiView,ArticleDetails

urlpatterns = [
    # path('article/', article_list ),
    path('article/', ArticleApiView.as_view() ),
    # path('detail/<int:pk>', article_details ),
    path('detail/<int:id>', ArticleDetails.as_view() )
 
]
