from django.urls import path 
from . import views
app_name=  'myapp'

urlpatterns = [
    path('', views.tables, name='table-page'),
    path('quiz/', views.quiz, name='quiz'),
    path('tough-quiz/', views.tough_quiz, name='tough-quiz'),
    path('toggle-closeness/<int:pk>', views.toggle_closeness, name='toggle-closeness'),
    path('toggle-decidiability/<int:pk>', views.toggle_decidiability, name='toggle-decidiability'),
    path('new-decidablity-note/', views.add_note_dec, name='new-decidablity-note'),
    path('new-closureproperty-note/', views.add_note_cp, name='new-closureproperty-note'),
]

