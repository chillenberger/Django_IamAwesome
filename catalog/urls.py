from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.generic import TemplateView

#dynamic page urls
urlpatterns =[
    path('', views.instructionsView.as_view(template_name='instructions.html'), name='home'),
    path('storyList', views.storyListView.as_view(), name='storyList'),
    path('story/<slug:pk>', views.storyDetailView.as_view(), name='story-detail'),
    path('profile/', views.profile.as_view(), name='user-profile'),
    path('productList', views.productListView.as_view(), name='productList'),
    path('product/<slug:pk>', views.productDetailView.as_view(), name='product-detail'),
]

#static page urls
urlpatterns +=[
    path('contact/', TemplateView.as_view(template_name='contact_us.html'), name='contact'),
    path('FAQ/', TemplateView.as_view(template_name='FAQ.html'), name='FAQ'),
    path('about/', TemplateView.as_view(template_name='about_us.html'), name='about'),
]

#form urls
urlpatterns +=[
    path('story/create/', views.NewStory, name='create-story'),
    path('story/<slug:pk>/update/', views.storyUpdate.as_view(), name='story_update'),
    path('story/<slug:pk>/delete/', views.storyDelete.as_view(), name='delete-story-conferm'),
]
