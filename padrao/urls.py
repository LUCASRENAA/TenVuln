"""controle_estoque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', views.registro),


                  path('registro/submit', views.submit_registro),

                  path('inicio/',views.telainicial),
                  path('vuln3/submit', views.vuln3_submit),

                path('inicio/<pagina>/<ano>/', views.inicio),

path('desafios/htmls/templates/<titulo>/', views.funcaoRespostas),

path('inicio/<pagina>/<ano>/resposta', views.resposta),

                  path('inicio/<pagina>/', views.inicio),
                  path('inicio/<pagina>/resposta', views.resposta),
                  #path('inicio/<pagina>/submit', views.submit_teste),

                  path('parte1/administrador', views.adminsite),

                  path('login/', views.login_user),
    path('login/submit',views.submit_login),

                  path('',RedirectView.as_view(url='inicio/'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
