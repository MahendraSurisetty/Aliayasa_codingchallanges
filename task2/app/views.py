from django.shortcuts import render

# Create your views here.
# views.py

from django.http import StreamingHttpResponse
import time
import random

def generate_sentence():
    # Function to generate a random sentence
    sentences = ["The quick brown fox jumps over the lazy dog.",
                 "A journey of a thousand miles begins with a single step.",
                 "To be or not to be, that is the question.",
                 "All that glitters is not gold.",
                 "The only way to do great work is to love what you do."]
    
    # Generate a random sentence
    random_sentence = random.choice(sentences)
    
    # Yield the sentence with some delay
    yield random_sentence.encode('utf-8')
    time.sleep(1)

def stream_sentence(request):
    # View to stream the generated sentence
    response = StreamingHttpResponse(generate_sentence(), content_type='text/html')
    return response
