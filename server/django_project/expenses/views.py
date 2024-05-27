from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
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

class ExpenseListView(generics.ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter expenses based on the authenticated user
        return Expense.objects.filter(user=self.request.user)
