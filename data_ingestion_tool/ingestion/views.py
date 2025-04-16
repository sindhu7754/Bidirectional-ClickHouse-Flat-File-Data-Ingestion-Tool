from django.shortcuts import render
from .forms import DataSourceForm, ClickHouseConfigForm, FlatFileConfigForm
from .utils import fetch_data_from_clickhouse, write_to_flatfile, ingest_flatfile_to_clickhouse

def home(request):
    form = DataSourceForm()
    clickhouse_form = None
    flatfile_form = None
    result = None
    error = None

    if request.method == 'POST':
        form = DataSourceForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data['source']
            if source == 'clickhouse':
                clickhouse_form = ClickHouseConfigForm(request.POST)
                if clickhouse_form.is_valid():
                    try:
                        host = clickhouse_form.cleaned_data['host']
                        port = clickhouse_form.cleaned_data['port']
                        database = clickhouse_form.cleaned_data['database']
                        user = clickhouse_form.cleaned_data['user']
                        jwt_token = clickhouse_form.cleaned_data['jwt_token']
                        query = "SELECT * FROM your_table LIMIT 10"  # Example query
                        data = fetch_data_from_clickhouse(host, port, database, user, jwt_token, query)
                        write_to_flatfile('output.csv', data)
                        result = f"Data fetched from ClickHouse and written to output.csv with {len(data)} records."
                    except Exception as e:
                        error = f"Error: {e}"

            elif source == 'flatfile':
                flatfile_form = FlatFileConfigForm(request.POST)
                if flatfile_form.is_valid():
                    try:
                        file_name = flatfile_form.cleaned_data['file_name']
                        delimiter = flatfile_form.cleaned_data['delimiter']
                        host = 'clickhouse_host'
                        port = 9000
                        database = 'your_database'
                        user = 'your_user'
                        jwt_token = 'your_jwt_token'
                        record_count = ingest_flatfile_to_clickhouse(host, port, database, user, jwt_token, file_name, delimiter)
                        result = f"Data ingested from Flat File to ClickHouse with {record_count} records."
                    except Exception as e:
                        error = f"Error: {e}"

    return render(request, 'ingestion/home.html', {
        'form': form,
        'clickhouse_form': clickhouse_form,
        'flatfile_form': flatfile_form,
        'result': result,
        'error': error
    })
