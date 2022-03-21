from django.urls import path

from ciphers import views

urlpatterns = [
    # ceaser cipher
    path('ceaser/encrypt/', views.ceaser_encrypt, name='ceaser_encrypt'),
    path('ceaser/decrypt/', views.ceaser_decrypt, name='ceaser_decrypt'),
    path('ceaser/encrypt/response/', views.ceaser_encrypt_response, name='ceaser_encrypt_response'),
    path('ceaser/decrypt/response/', views.ceaser_decrypt_response, name='ceaser_decrypt_response'),
    # transpositional cipher
    path('transposition/encrypt/', views.transposition_encrypt, name='transposition_encrypt'),
    path('transposition/decrypt/', views.transposition_decrypt, name='transposition_decrypt'),
    path('transposition/encrypt/response/', views.transposition_encrypt_response, name='transposition_encrypt_response'),
    path('transposition/decrypt/response/', views.transposition_decrypt_response, name='transposition_decrypt_response'),
]