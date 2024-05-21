from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Expense, ExpenseCategory
from .serializers import ExpenseSerializer
from django.shortcuts import render

class ExpenseSubmissionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            category_name = data.get('category')
            date = data.get('date')
            amount = data.get('amount')
            description = data.get('description')

            category, created = ExpenseCategory.objects.get_or_create(name=category_name)
            expense = Expense.objects.create(
                category=category,
                date=date,
                amount=amount,
                description=description,
                user=request.user
            )
            
            serializer = ExpenseSerializer(expense)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ExpenseListView(APIView):
    def get(self, request):
        expenses = Expense.objects.all()  # Retrieve all expenses
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
