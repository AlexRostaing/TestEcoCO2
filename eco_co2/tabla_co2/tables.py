import django_tables2 as tables
from .models import CO2Data
"""
class CO2Table(tables.Table):
    class Meta:
        model = CO2Data
"""
class CO2Table(tables.Table):
    datetime = tables.DateTimeColumn()
    co2_rate = tables.Column()
