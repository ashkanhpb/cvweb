from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'website/index.html')
def contact_view(request):
    return render(request,'website/contact.html')
def about_view(request):
    context={"birthday":"25 July 1995" , "web":"www.example.com" , "phone":"+98 918 646 7306" , "city":"Baneh" , "age":"29","degree":"Bsc" , "email":"Ashaknhpb@gmail.com"}
    return render(request,'website/about.html' , context )
def portfolio_view(request):
    return render(request,'website/portfolio.html')
def portfolio_details_view(request):
    return render(request,'website/portfolio-details.html')
def resume_view(request):
    return render(request,'website/resume.html')
def services_view(request):
    return render(request,'website/services.html')