from django.shortcuts import render
from django.http.response import HttpResponse
import csv
from elastic_search import models
import fnmatch
import datetime
from django.conf import settings


def upload_sales(request):
    dataReader = csv.reader(open('/home/saurabh/Downloads/SalesFile.csv'),
                            delimiter=',', quotechar='"')
    date = datetime.datetime.now().date()
    details = None
    for row in dataReader:
        details = models.SalesDetails.objects.create(order_id=row[0], order_date=date,
                                                     customer_id=row[1], customer_name=row[2],
                                                     city=row[3],state=row[4],postal_code=row[5],
                                                     product_id=row[6],product_name=row[7],
                                                     value=row[8],quantity=row[9])
        details.save()
    return details

