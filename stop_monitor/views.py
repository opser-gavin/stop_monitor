from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

def getCursor():
    return connection.cursor()
def getStatus(service,tname):
    cursor = getCursor()
    result = cursor.execute("select * from %s where is_monitor = 1  and monitor_name = '%s'" % (tname,service))
    if result == 0:
        return False
    else:
        return True

def stop_url(request):
    cursor = getCursor()
    service = request.GET.get('service')
    context = {
        'service':service
    }
    if getStatus(service,"monitor_url") == True:
        try:
            cursor.execute("update monitor_url set is_monitor = 0 where monitor_name = '%s'" % service)
            #return HttpResponse("close service:%s success" % service)
            return render(request,'success.html',context=context)
        except:
            #return HttpResponse("close service:%s failed" % service)
            return render(request,'failed.html',context=context)
        cursor.close()
    else:
        #return HttpResponse("%s already closed !" % service)
        return render(request,'already-closed.html',context=context)
def stop_port(request):
    cursor = getCursor()
    service = request.GET.get('service')
    context = {
        'service':service
    }
    if getStatus(service,"monitor_port") == True:
        try:
            cursor.execute("update monitor_port set is_monitor = 0 where monitor_name = '%s'" % service)
            #return HttpResponse("close service:%s success" % service)
            return render(request,'success.html',context=context)
        except:
            #return HttpResponse("close service:%s failied" % service)
            return render(request,'failed.html',context=context)
        cursor.close()
    else:
        #return HttpResponse("%s already closed !" % service)
        return render(request,'already-closed.html',context=context)