from django.shortcuts import render

# Create your views here.
# views.py

from django.http import JsonResponse
from .tasks import count_words_in_file

def process_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)

        # Save the uploaded file
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Call the Celery task to count words
        word_count_task = count_words_in_file.delay(file_path)

        # You can optionally wait for the result and handle it here
        # word_count = word_count_task.get()

        return JsonResponse({'message': 'File processing started. Check back later for results.'})

    return JsonResponse({'error': 'File not found or invalid request.'}, status=400)

