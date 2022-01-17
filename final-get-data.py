import json
import cdsapi
import requests
import pandas as pd
from datetime import datetime


year = ['2014','2015','2016','2017','2018','2019','2020']

for i in year:
    sat_client = cdsapi.Client() # Open a satellite client instance
    sat_request = sat_client.retrieve( # Make the satellite api call
    'reanalysis-era5-single-levels', # ERA5 data set
    {
            
            'variable':'surface_solar_radiation_downwards ',
            'product_type':'reanalysis',
            'year':i,
            'month':['01','02','03','04','05','06','07','08','09','10',
                    '11','12'],
            'day':['01','02','03','04','05','06','07','08','09','10',
                    '11','12','13','14','15','16','17','18','19','20',
                    '21','22','23','24','25','26','27','28','29','30',
                    '31'],
            'time':['00:00','01:00','02:00','03:00','04:00','05:00',
                    '06:00','07:00','08:00','09:00','10:00','11:00',
                    '12:00','13:00','14:00','15:00','16:00','17:00',
                    '18:00','19:00','20:00','21:00','22:00','23:00'],
            'area':'53.7/-6.5/53.2/-6',
            'format':'netcdf'
    })

    # Download request and store satellite data in netcdf file
    sat_request.download('Dublin' + '_surface_solar_radiation_downwards_' + str(i) + '.nc') 

