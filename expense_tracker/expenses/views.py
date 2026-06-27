from django.shortcuts import render,redirect
from . models import Expense
from datetime import date
# Create your views here.

def add_expense(request):
    today=date.today()
    if request.method == "POST":
        print(request.POST)
        amounts=request.POST.getlist('amount[]')
        categories=request.POST.getlist('category[]')
        descriptions=request.POST.getlist('description[]')
        expense_date=request.POST['expense_date']
        
        for i in range(len(categories)):

            Expense.objects.create(
                amount=amounts[i],
                category=categories[i],
                description=descriptions[i],
                expense_date=expense_date
            )
        
    return render(request, 
                  'add_expense.html',
                  {'today':today}
                  )

def view_expenses(request):
    expenses=Expense.objects.all().order_by('-expense_date')
    grouped_expenses={}
    total_spent=0
    for expense in expenses:
        date=expense.expense_date
        if  date not in grouped_expenses:
            grouped_expenses[date]={
                'expenses':[],
                'daily_total':0
            }
        grouped_expenses[date]['expenses'].append(expense)
        grouped_expenses[date]['daily_total']+=expense.amount
        total_spent+=expense.amount
        
    return render(
        request,
        'view_expenses.html',
        {'grouped_expenses':grouped_expenses,
         'total_spent':total_spent
         }
    )
def edit_expense(request,id):
    expense=Expense.objects.get(id=id)
    if request.method=="POST":
        expense.category=request.POST['category']
        expense.description=request.POST['description']
        expense.amount=request.POST['amount']
        expense.save()
        return redirect('view_expenses')
    return render(
        request,
        'edit_expense.html',
        {'expense':expense}
    )
def delete_expense(request,id):
    expense=Expense.objects.get(id=id)
    expense.delete()
    return redirect('view_expenses')