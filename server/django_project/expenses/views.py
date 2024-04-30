from django.shortcuts import render
from django.http import JsonResponse

def data_view(request):
    # Process the request and fetch data from the database or elsewhere
    data = [{'id': 1, 'name': 'Example'}, {'id': 2, 'name': 'Example 2'}]

    # Return the data as JSON response
    return JsonResponse(data, safe=False)

