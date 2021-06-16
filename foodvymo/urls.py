from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('', views.index, name='index'),
    path('addmerchant', views.addmerchant, name='addMerchant'),
    path('signup', views.sign_up, name="signup"),
    path('login', LoginView.as_view(template_name='login.html'), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    ]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)