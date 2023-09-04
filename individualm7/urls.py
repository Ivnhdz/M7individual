"""
URL configuration for individualm7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from pagina import views as vistas_pagina
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vistas_pagina.landing, name='landing'),
    path('login/',auth_views.LoginView.as_view(template_name = 'pagina/login.html'), name='login' ),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'pagina/logout.html'), name='logout' ),
    path('tareas/', vistas_pagina.listar_tareas, name='listar_tareas'),
    path('tareas/<int:tarea_id>/', vistas_pagina.ver_tarea, name='ver_tarea'),
    path('tareas/crear/', vistas_pagina.crear_tarea, name='crear_tarea'),
    path('tareas/<int:tarea_id>/editar/', vistas_pagina.editar_tarea, name='editar_tarea'),
    path('tareas/<int:tarea_id>/eliminar/', vistas_pagina.eliminar_tarea, name='eliminar_tarea'),
]