from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv
from pathlib import Path


def read_csv(station_file):
    with open(station_file, encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        list_station = [dict(row) for row in reader]
    return list_station


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    station_list = read_csv(settings.BUS_STATION_CSV)
    paginator = Paginator(station_list, 10)  # Show 25 contacts per page.

    page_number = int(request.GET.get('page', default=1))
    bus_station = paginator.get_page(page_number)
    #print(bus_station.object_list)
    return render(request, 'stations/index.html', {'bus_station': bus_station})

