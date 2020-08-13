from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == "GET":
        return render(request, 'contact.html')
    else:
            first_name = request.POST["first_name"]
            student_name = request.POST["student_name"]
            students = request.POST["students"]
            tel = request.POST["tel"]

            from_email = request.POST['from_email'] 
            try:
                send_mail("Student Registration","Registration Request: <br >This is a registration request by " + first_name +". Their email-id is " + from_email + ". The age group of the students is: " + students +  "Contact information: " + tel, from_email, ['hatechz14@gmail.com', 'hasrayrah970@gmail.com'] )
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect('success')
    return render(request, 'contact.html')

def success(request):
    return render(request, 'success_email_send.html')
