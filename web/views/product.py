from django.shortcuts import render, redirect, HttpResponse

def product_list(request):
    HttpResponse("product_list")

def product_add(request):
    HttpResponse

def product_edit(request, nid):
    HttpResponse("product_edit")

def product_delete(request, nid):
    HttpResponse("product_delete")