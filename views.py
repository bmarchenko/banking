from django.shortcuts import render_to_response
from django.http import HttpResponse

def deposit_form(request):
    return render_to_response('deposit_form.html')

def deposit_result(request):
    if 'name' and 'depsum' and 'depperiod' in request.GET:
	return render_to_response('deposit_result.html', 
		{'name':name, 'depperiod':depperiod, 'finaldep':finaldep}) 

      
    else:
        return render_to_response('deposit_form.html', {'error': True})

