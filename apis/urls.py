from django.conf.urls import url
from apis import views

urlpatterns = [
    url( r'^api/merchant$', views.merchant_list ),
    url( r'^api/merchant/(?P<pk>[0-9]+)$', views.merchant_detail ),
    url( r'^api/merchant', views.merchant_detail ),
]