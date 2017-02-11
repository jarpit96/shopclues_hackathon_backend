from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from base.models import Shop, Counter
# Create your views here.


@csrf_exempt
def getBasic(request):
    print "Basic request is: ", request.POST
    data = json.loads(request.body)
    name = data['name']
    shop = Shop.objects.filter(name=name)
    if not shop:
        counter = Counter.objects.filter(name=name)
        if not counter:
            print "Response: Not Found"
            return HttpResponse(json.dumps({'status': 405, 'message': 'Not Found'}), content_type="application/json")
        else:
            counter = Counter.objects.get(name = name)
            print "Response: ", json.dumps({'status': 200, 'message': 'Success', 'name': name, 'intro': counter.intro, 'type': 'counter'})
            return HttpResponse(json.dumps({'status': 200, 'message': 'Success', 'name': name, 'intro': counter.intro, 'type': 'counter'}), content_type="application/json")
    else:
        shop = Shop.objects.get(name=name)
        print "Response: ", json.dumps(
            {'status': 200, 'message': 'Success', 'name': name, 'intro': shop.intro, 'type': 'counter'})
        return HttpResponse(json.dumps({'status': 200, 'message': 'Success', 'name': name, 'intro': shop.intro, 'type': 'shop'}),
                            content_type="application/json")

@csrf_exempt
def getDetail(request):
    # print "Detail request is: ", request.POST
    data = json.loads(request.body)
    name = data['name']
    shop = Shop.objects.filter(name=name)
    if not shop:
        counter = Counter.objects.filter(name=name)
        if not counter:
            return HttpResponse(json.dumps({'status': 405, 'message': 'Not Found'}), content_type="application/json")
        else:
            counter = Counter.objects.get(name = name)
            return HttpResponse(json.dumps({'status': 200, 'message': 'Success', 'name': name, 'intro': counter.intro, 'type': 'counter', 'usage': counter.usage, 'contact_details': counter.contact_details}), content_type="application/json")
    else:
        shop = Shop.objects.get(name=name)
        return HttpResponse(json.dumps({'status': 200, 'message': 'Success', 'name': name, 'intro': shop.intro, 'type': 'shop', 'pdis': shop.pdis, 'rating': shop.rating}),
                            content_type="application/json")
