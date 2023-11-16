from django.shortcuts import render
from .forms import FeedbackForm

from django.http import JsonResponse

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Feedback submitted successfully!'})
        else:
            return JsonResponse({'error': 'Form is not valid.'}, status=400)
    elif request.GET.get('validate') == 'true':
        form = FeedbackForm(request.GET)
        if form.is_valid():
            return JsonResponse({'message': 'Form is valid.'})
        else:
            errors = {field: form[field].errors[0] for field in form.errors}
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})
