"""
URL configuration for manage_scuola project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studente.views import  *#student_list, home, add_studente
from corso.views import *
from docente.views import *
from iscrizione_corso.views import *


urlpatterns = [

    path('admin/', admin.site.urls), 
    path('',home, name='home'), # per la home page
    path('studenti/',student_list, name='studenti'), # lista studenti    
    #path('categorie/',lista_category, name='categorie'), #lista categorie
    path('corsi/',lista_corsi, name='corsi'), #lista corsi
    path('docenti/',lista_docenti, name='docenti'), #lista docenti
    path('risultati/',lista_risultati, name='risultati'), #risultati
    path('add_stud/',add_studente, name='add_stud'), #add uno studente
    #path('studenti/', views.lista_studenti, name='lista_studenti')
    path('cancella_studente/<int:id>/',del_student, name='cancella'),  #cancellare uno studente
    path('cancella_docente/<int:id>/',del_docente, name='cancella_doc'),# cancella docente
    path('cancella_corso/<int:id>/',del_corso, name='cancella_cor'), #cancella corso
    path('viz_corsi_studente/<int:id>/',viz_corsi_studente, name='corsi_stud'),#vederei corsi per uno sttudente
    path('add_corso/',add_corso, name='add_cors'), #add uno studente
    path('viz_corsi_docdente/<int:id>/',lista_corsi_docente, name='corsi_doc'),#vederei corsi per uno docente
]
   