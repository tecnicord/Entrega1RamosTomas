from django.urls import path
from django.contrib.auth.views import LogoutView
from UserTecnicord.views import *

urlpatterns = [
        path('login/', login_request, name='UserTecnicordLogin'),
        path('registro/', register, name='UserTecnicordRegister'),
        path('logout/', LogoutView.as_view(template_name='UserTecnicord/logout.html'), name='UserTecnicordLogout'),
        path('editar/', editar_usuario, name='UserTecnicordEditar'),
        path('avatar/', upload_avatar, name='UserTecnicordAvatar'),
        ]