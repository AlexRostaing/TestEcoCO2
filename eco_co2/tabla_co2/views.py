# -*- coding: utf-8 -*-

from django.shortcuts import render
from .tables import CO2Table
from .functions import *

def co2_list(request):
    data = convertToDateTime(getCO2Data())

    table = CO2Table(data)

    return render(request, "co2_list.html",{
        "table": table
    })
