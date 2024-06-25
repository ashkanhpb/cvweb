from django.urls import path , include
from website.views import *
app_name = 'cvweb'
urlpatterns = [
    path('', index_view , name='index'),
    path('about/', about_view , name='about'),
    path('contact/', contact_view , name='contact'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('portfolio_details/', portfolio_details_view, name='portfolio_details'),
    path('resume/', resume_view, name='resume'),
    path('services/', services_view, name='services'),
]
