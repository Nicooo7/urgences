# coding: utf-8

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, Http404
from django.template import loader
#from django.core.exceptions import ObjectDoesNotExist


from .models import *
from django.contrib.auth.models import* 
from django.contrib.auth import *
from bs4 import BeautifulSoup
from django.template.response import *
import bs4
import re
import pickle
import os
import json
from nltk import *
from bs4 import BeautifulSoup
from random import *
from unidecode import unidecode
from django.utils.safestring import mark_safe




app_name = 'gestion_patient'




#_____________________vue_______________________#

def rentrer_patient(request):
	return render(request, 'rentrer_patient.html', {})

def afficher_patient(request):
	donnee = request.GET
	donnee = dict(donnee._iterlists())
	print (donnee)
	return render(request, 'afficher_patient.html', {"donnee":donnee})























