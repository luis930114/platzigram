""" platzigram views. """

"""django"""
from django.http import HttpResponse, JsonResponse

""" utilities """
from datetime import datetime
import json


def hello_world(request):
    return HttpResponse('oh, hi! current server time is {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M HRS')
    ))

def sorted(request):
    """return a json ."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers) 
    data = {
        'status': 'ok',
        'numbers' : sorted_ints,
        'message' : 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
        ) 

def say_hi(request, name, age):
    ''' return a greeting. '''
    if age < 12:
        message = 'sorry {}, you are not allowed here.'.format(name)  
    else:
        message = 'hello, {} Welcome to platzigram.'.format(name)
    return HttpResponse(message)