from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Deposit

def deposit_form(request):
    return render_to_response('deposit_form.html')

def deposit_result(request):
    name = request.POST['name']
    depperiod = request.POST['depperiod']
    depsum = request.POST['depsum']
    deptype = request.POST['deptype']
    deposit = (name, depsum, depperiod)
      

        if deptype = 'simple':
	   depfinal = deposit.simplecalc()
	elif deptype = 'compound':
	  depfinal = deposit.compcalc()
	else:
	  depfinal = deposit.bonuscalc()
    return render_to_response('deposit_result.html', 
{'name' : name, 'depperiod' : depperiod, 'deptype' : deptype, 'depfinal' : depfinal }
		) 
   


