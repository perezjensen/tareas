from django import forms

class FormularioTareaActualizar(forms.Form):
    productos=forms.CheckboxSelectMultiple()
    abono = forms.NumberInput()
    prioridad= forms.Select()
    colaboradores=forms.CheckboxSelectMultiple()
    precio = forms.NumberInput()
    
    
    