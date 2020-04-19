from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.core.paginator import EmptyPage,Paginator
from .models import *
from .forms import *
def List(request):
    items=Report.objects.all()
    print(items)
    paginator=Paginator(items,10)
    page=request.GET.get('page')
    pagged_items=paginator.get_page(page)

    context={
       'items':pagged_items
    }
    return render(request,'reports.html',context)

def Submit(request):
    if request.method=='POST':
        
        
        form=ReportForm(request.POST,request.FILES)
        print (str(form.is_valid()))
        if form.is_valid():
            
            Name=form.cleaned_data.get('Name')
            date=form.cleaned_data.get('date')
            reports=form.cleaned_data.get('reports')
            TL=form.cleaned_data.get('TL')
            No_hours=form.cleaned_data.get('No_hours')
            progress=form.cleaned_data.get('progress')
            Dtoday=form.cleaned_data.get('Dtoday')
            concern=form.cleaned_data.get('concern')
            Nextplan=form.cleaned_data.get('Nextplan')
            Dnextp=form.cleaned_data.get('Dnextp')


            form.save()
            messages.success(request,'Entry Submitted')
            return redirect('List')
        else:
            messages.error(request,'Error! Retry')
            form=ReportForm()
            return render(request,"submit.html",{'form':form})
    else:
        form=ReportForm()
        return render(request,"submit.html",{'form':form})