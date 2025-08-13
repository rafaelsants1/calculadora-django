from django.contrib import admin
from django.urls import path
from app_portal import views
from app_portal.views import login_view, calculadora_view
from django.contrib.auth.views import LogoutView

# Permitindo que o LogoutView aceite o método GET
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Rotas (admin, login (página principal), calculadora e logout que redireciona o usuário a tela de login)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'), # Página inicial com login
    path('calculadora/', calculadora_view, name='calculadora'),
    path('logout/', CustomLogoutView.as_view(), name='logout'), # Logout
]
