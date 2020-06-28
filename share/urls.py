from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sns.urls')),
    # ACCOUNTSアプリへのルーティングになっている
    path('accounts/', include('accounts.urls')),
    # Djangoの認証用のVIEWを呼び出す
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/sns/')),
]
