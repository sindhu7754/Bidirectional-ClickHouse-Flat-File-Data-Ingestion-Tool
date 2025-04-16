from django import forms


class DataSourceForm(forms.Form):
    SOURCES = [
        ('clickhouse', 'ClickHouse'),
        ('flatfile', 'Flat File'),
    ]
    source = forms.ChoiceField(choices=SOURCES, label='Select Data Source', widget=forms.Select(attrs={'class': 'form-control'}))


class ClickHouseConfigForm(forms.Form):
    host = forms.CharField(label='Host', widget=forms.TextInput(attrs={'class': 'form-control'}))
    port = forms.IntegerField(label='Port', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    database = forms.CharField(label='Database', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user = forms.CharField(label='User', widget=forms.TextInput(attrs={'class': 'form-control'}))
    jwt_token = forms.CharField(label='JWT Token', widget=forms.TextInput(attrs={'class': 'form-control'}))


class FlatFileConfigForm(forms.Form):
    file_name = forms.CharField(label='File Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    delimiter = forms.CharField(label='Delimiter', widget=forms.TextInput(attrs={'class': 'form-control'}))
