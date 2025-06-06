from django.shortcuts import render
from .models import Student
from .serialzers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Model object yaani ek ek row 

# def student_detail(request,pk):
#     stu=Student.objects.get(id=pk)
#     serializer=StudentSerializer(stu)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')
#     # return JsonResponse(serializer.data)

# # queryset All student data

# def student_list(request):
#     stu=Student.objects.all()
#     serializer=StudentSerializer(stu,many=True)
#     # json_data=JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data,content_type='application/json')
#     return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def student_create(request):
    if request.method=="POST":
        json_data=request.body
        print("json data",json_data)
        stream=io.BytesIO(json_data)
        print("stream",stream)
        pythondata=JSONParser().parse(stream)
        print("python data",pythondata)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Create'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')