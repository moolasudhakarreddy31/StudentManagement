from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Student
from rest_framework.response import Response

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    data = {'students': list(students.values())}
    return JsonResponse(data)

@api_view(['POST'])
def student_add(request):
    name = request.data.get('name')
    roll_no = request.data.get('roll_no')
    dob = request.data.get('dob')
    marks_percentage = request.data.get('marks_percentage')
    class_group = request.data.get('class_group')
    father_name = request.data.get('father_name')
    student = Student(name=name, roll_no=roll_no, dob=dob, marks_percentage=marks_percentage, class_group=class_group, father_name=father_name)
    student.save()
    data = {'status': 200, 'message': 'successfully added'}
    return JsonResponse(data)

@api_view(['GET'])
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    data = {'student': model_to_dict(student)}
    return JsonResponse(data)

@api_view(['POST'])
def student_add_mark(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.marks_percentage = request.data.get('marks_percentage')
    student.save()
    data = {'status': 200, 'message': 'successfully added'}
    return JsonResponse(data)

@api_view(['PUT'])
def student_update_mark(request):
    id = request.GET.get('id')
    student = get_object_or_404(Student, pk=id)
    student.marks_percentage = request.data.get('marks_percentage')
    student.save()
    data = {'status': 200, 'message': 'successfully updated'}
    return JsonResponse(data)

@api_view(['GET'])
def student_results(request):
    students = Student.objects.all()
    total_count = students.count()
    pass_count = students.filter(marks_percentage__gte=50).count()
    fail_count = total_count - pass_count
    pass_percentage = (pass_count / total_count) * 100
    data = {'pass_percentage': pass_percentage}
    return JsonResponse(data)

@api_view(['GET'])
def overall_pass_percentage(request):
    # calculate overall pass percentage
    total_students = Student.objects.count()
    passed_students = Student.objects.filter(marks_percentage__gte=40).count()
    pass_percentage = (passed_students / total_students) * 100
    
    # return response
    return Response({'pass_percentage': pass_percentage})
