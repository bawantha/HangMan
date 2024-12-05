from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Hangman Game API",
        default_version='v1',
        description="API documentation for the Hangman Game",
        contact=openapi.Contact(email="bawantha.inbox@gmail.com"),
    ),
    public=True,
)

urlpatterns = [
    path('game/', include('game.urls')),  # Include the game app's URLs

    # Swagger and Redoc documentation endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
