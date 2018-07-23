from django.shortcuts import render
from .forms import PersonalInfoForm
from .models import PersonalData
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')

def add(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = PersonalInfoForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #book_inst.due_back = form.cleaned_data['renewal_date']
            #fullname = form.cleaned_data.get('fullname')
            #email = form.cleaned_data.get('email')
            info = form.save(commit=False)
            info.save()
            form = PersonalInfoForm()
            messages.success(request, 'Form Submitted Successful')


            # redirect to a new URL:
            return render(request, 'addinfo.html', {'form': form})

    # If this is a GET (or any other method) create the default form.
    else:
        form = PersonalInfoForm()

    return render(request, 'addinfo.html', {'form': form})



def list(request):
    data = PersonalData.objects.all()
    count = PersonalData.objects.count()

    return render(request, 'listinfo.html', {'data': data, 'count':count} )
