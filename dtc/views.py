from django.shortcuts import redirect, render
from sklearn.tree import DecisionTreeClassifier
import pickle

model = pickle.load(open('model.sav', 'rb'))

# Create your views here.
def home(request):
    if request.method == 'POST':
        prediction = "Sorry, unable to classify!"
        sepallength = float(request.POST['sepallength'])
        sepalwidth = float(request.POST['sepalwidth'])
        petallength = float(request.POST['petallength'])
        petalwidth = float(request.POST['petalwidth'])
        data = [[sepallength, sepalwidth, petallength, petalwidth]]
        prediction = model.predict(data)[0]
        df = {
            'prediction':prediction,
        }
        return render(request, 'dtc/home.html', df)
    return render(request, 'dtc/home.html')
