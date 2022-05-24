from django.shortcuts import render

testdata = [
    {
        'name': 'oli',
        'number': '8667475'
    },
    {
        'name': 'sindri',
        'number': 'dno'
    },
    {
        'name': 'Frikki',
        'number': 'dno'
    },
    {
        'name': 'Davíð',
        'number': 'dno'
    }
    ]
# Create your views here.
def index(request):
    return render(request, 'event/index.html', context={ 'testdata':testdata })
