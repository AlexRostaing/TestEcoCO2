# -*- coding: utf-8 -*-

from django.shortcuts import render
from .tables import CO2Table
from .functions import *

data = convertToDateTime(getCO2Data())

def co2_list(request):
    table = CO2Table(data)

    return render(request, "co2_list.html",{
        "table": table
    })

def co2_list_hourly(request):
    table = CO2Table(getHourlyData(data))

    return render(request, "co2_list.html",{
        "table": table
    })
