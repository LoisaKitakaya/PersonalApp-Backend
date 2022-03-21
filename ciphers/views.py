from django.shortcuts import render, redirect

from ciphers.crypt_ciphers import CeaserCipher, TranspositionalCipher

# Create your views here.

def ceaser_encrypt(request):

    context = {}

    return render(request, 'ciphers/ceaser_encrypt.html', context)

def ceaser_decrypt(request):

    context = {}

    return render(request, 'ciphers/ceaser_decrypt.html', context)

def ceaser_encrypt_response(request):

    if request.method == 'GET':

        message = request.GET.get('message')
        key = request.GET.get('key')

        cipher = CeaserCipher(message)

        ciphertext = cipher.encrypt_message(key)

    context = {
        'response' : ciphertext,
    }

    return render(request, 'ciphers/ceaser_response.html', context)

def ceaser_decrypt_response(request):

    if request.method == 'GET':

        message = request.GET.get('message')
        key = request.GET.get('key')

        cipher = CeaserCipher(message)

        plaintext = cipher.decrypt_message(key)

    context = {
        'response' : plaintext,
    }

    return render(request, 'ciphers/ceaser_response.html', context)

def transposition_encrypt(request):

    context = {}

    return render(request, 'ciphers/transposition_encryption.html', context)

def transposition_decrypt(request):

    context = {}

    return render(request, 'ciphers/transposition_decryption.html', context)

def transposition_encrypt_response(request):

    if request.method == 'GET':

        message = request.GET.get('message')
        key = request.GET.get('key')

        cipher = TranspositionalCipher(message)

        ciphertext = cipher.encrypt_message(int(key))

    context = {
        'response' : ciphertext,
    }

    return render(request, 'ciphers/transposition_response.html', context)

def transposition_decrypt_response(request):

    if request.method == 'GET':

        message = request.GET.get('message')
        key = request.GET.get('key')

        cipher = TranspositionalCipher(message)

        plaintext = cipher.decrypt_message(key)

    context = {
        'response' : plaintext,
    }

    return render(request, 'ciphers/transposition_response.html', context)

