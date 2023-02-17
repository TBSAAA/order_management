from django.shortcuts import render, redirect, HttpResponse

def level_list(request):
    HttpResponse("level_list")

def level_add(request):
    HttpResponse("level_add")

def level_edit(request, nid):
    HttpResponse("level_edit")

def level_delete(request, nid):
    HttpResponse("level_delete")