from django.shortcuts import render, redirect, HttpResponse

def user_list(request):
    HttpResponse("user_list")


def user_add(request):
    HttpResponse("user_add")


def user_edit(request, nid):
    HttpResponse("user_edit")


def user_delete(request, nid):
    HttpResponse("user_delete")
