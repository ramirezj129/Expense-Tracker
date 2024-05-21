import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Income
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Income


@csrf_exempt
def add_income(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = data.get('amount')
            description = data.get('description')
            
            # Validate data
            if amount is None or description is None:
                return JsonResponse({'error': 'Amount and description are required'}, status=400)
            
            # Delete all existing income entries
            Income.objects.all().delete()

            # Create a new income entry
            Income.objects.create(amount=amount, description=description)
            
            return JsonResponse({'message': 'Income submitted successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def income_list(request):
    incomes = list(Income.objects.values())
    return JsonResponse(incomes, safe=False)
