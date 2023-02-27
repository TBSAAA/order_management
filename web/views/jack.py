from django.shortcuts import render, redirect, HttpResponse


def study_experience(request):
    return render(request, 'study_experience.html')
