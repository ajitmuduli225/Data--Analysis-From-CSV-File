from django.shortcuts import render

# Create your views here.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render, redirect
from django.conf import settings
from app.models import *

def home(request):
    if request.method == 'POST':
        file = request.FILES['file']
        uploaded_file = UploadedFile.objects.create(file=file)
        return redirect('data_analysis', pk=uploaded_file.pk)
    return render(request, 'home.html')

def data_analysis(request, pk):
    uploaded_file = UploadedFile.objects.get(pk=pk)
    df = pd.read_csv(uploaded_file.file.path)

    
    head = df.head().to_html()
    stats = df.describe().to_html()
    

    
    fig, ax = plt.subplots()
    df.hist(ax=ax)
    plt.savefig('app/static/img/histogram.png')
    histogram_plot = 'img/histogram.png'

    context = {
        'head': head,
        'stats': stats,
        
        'histogram_plot': histogram_plot
    }
    return render(request, 'data_analysis.html', context)
