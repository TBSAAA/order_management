from django.shortcuts import render, redirect, HttpResponse

def order_list(request):
    HttpResponse("order_list")


def order_add(request):
    HttpResponse("order_add")


def order_edit(request, nid):
    HttpResponse("order_edit")


def order_delete(request, nid):
    HttpResponse("order_delete")
