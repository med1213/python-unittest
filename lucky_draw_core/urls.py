from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Lucky Draw API",
        default_version='v1',
        description="Lucky Draw API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@luadgame.la"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[permissions.IsAuthenticated],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', (schema_view.with_ui('swagger',
         cache_timeout=0)), name='schema-swagger-ui'),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path('', include('apps.user.api.v1.urls'), name='user'),
    path('', include('apps.period.api.v1.urls'), name='period'),
    path('', include('apps.bill.api.v1.urls'), name='bill'),
    path('', include('apps.prize.api.v1.urls'), name='prize'),
    path('', include('apps.candidate.api.v1.urls'), name='candidate'),
    path('', include('apps.province.api.v1.urls'), name='province'),
    path('', include('apps.district.api.v1.urls'), name='district'),
    path('', include('apps.about.api.v1.urls'), name='about'),
    path('', include('apps.slide.api.v1.urls'), name='slide'),
    path('', include('apps.footer.api.v1.urls'), name='footer'),
    path('', include('apps.village.api.v1.urls'), name='village'),
    path('', include('apps.post.api.v1.urls'), name='post'),
    path('', include('apps.prize_type.api.v1.urls'), name='prize_type'),
    path('', include('apps.period_type.api.v1.urls'), name='period_type'),
    path('', include('apps.winner.api.v1.urls'), name='winner'),
    path('', include('apps.user_profile.api.v1.urls'), name='profile'),
    path('', include('apps.live_data.api.v1.urls'), name='live_data'),
    path('', include('apps.lucky_draw.api.v1.urls'), name='lucky_draw'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
