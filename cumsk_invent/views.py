from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from cumsk_invent import models
from py_linq import Enumerable

# Create your views here.


def snmpc_devices_all(request):
    list_objects = models.Nodetable.objects.all().order_by('-node_id')
    context = {
        'list_objects': list_objects
    }
    return render(request, 'cumsk_invent/snmpc_devices.html', context)


def snmpc_device(request, node_id):
    snmpc_item = get_object_or_404(models.Nodetable, pk=node_id)
    return render(request, 'cumsk_invent/snmpc_device.html', {'snmpc_device': snmpc_item})


def esma_devices_all(request):
    return render(request, 'cumsk_invent/esma_devices.html', {'esma_devices': models.CiscoDs.objects.all()})
