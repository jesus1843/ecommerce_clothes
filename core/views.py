from django.shortcuts import render


def home(request):
    return render(
        request=request,
        template_name="index.html",
        context={ }
    )

def contact(request):
    return render(
        request=request,
        template_name="contact.html",
        context={ }
    )
