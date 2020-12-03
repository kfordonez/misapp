from django.forms import ModelForm
from .models import Turno, HistorialMedico, Pedido
from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime, timedelta, timezone


class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'

class HistorialForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    estado = forms.CharField(widget=forms.HiddenInput(), initial= "PENDIENTE") 
    class Meta:
        model = Pedido
        fields = ('producto','vendedor', 'paciente', 'cantidad', 'tipoPago', 'estado')





        