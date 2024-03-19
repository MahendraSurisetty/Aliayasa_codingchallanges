# tasks.py

import os
from celery import shared_task
from django.conf import settings

@shared_task
def count_words_in_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        return f"File {file_path} not found"

    # Open the file and read its content
    with open(file_path, 'r') as file:
        content = file.read()

    # Count the number of words
    word_count = len(content.split())

    # Return the word count
    return word_count
