from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer

#API1 - Add a new student record
class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#API2 - Fetch student records
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#API3 - Average marks 
class AverageMarksView(APIView):

    def get(self, request):

        students = Student.objects.all()

        if not students.exists():
            return Response({
                "average_marks": 0,
                "average_percentage": 0
            })

        total_obtained = sum(
            student.marks_obtained
            for student in students
        )

        total_marks = sum(
            student.total_marks
            for student in students
        )

        average_marks = total_obtained / students.count()

        average_percentage = (
            total_obtained / total_marks
        ) * 100

        return Response({
            "average_marks": round(average_marks, 2),
            "average_percentage": round(
                average_percentage, 2
            )
        })
    
#API4 - Count Students
class PassedStudentsCountView(APIView):

    def get(self, request):

        students = Student.objects.all()

        count = 0

        for student in students:

            percentage = (
                student.marks_obtained /
                student.total_marks
            ) * 100

            if percentage >= 33:
                count += 1

        return Response({
            "students_above_33_percent": count
        })