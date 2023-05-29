from django.urls import path
from app_newsletter import views

urlpatterns = [
    path('',views.telaDeLogin,name="telaDeLogin"),
    path('cadastro/',views.cadastro,name="cadastro"),
    path('home/<int:id>/',views.home,name="home"),
    path('email/add_email/<int:id>/',views.add_email,name="add_email")
]
