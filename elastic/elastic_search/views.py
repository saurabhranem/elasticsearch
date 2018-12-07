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


def prepare_template(self, obj):
    """
    Flattens an object for indexing.

    This loads a template
    (``search/indexes/{app_label}/{model_name}_{field_name}.txt``) and
    returns the result of rendering that template. ``object`` will be in
    its context.
    """
    if self.instance_name is None and self.template_name is None:
        raise SearchFieldError("This field requires either its instance_name variable to be populated or an explicit template_name in order to load the correct template.")

    if self.template_name is not None:
        template_names = self.template_name

        if not isinstance(template_names, (list, tuple)):
            template_names = [template_names]
    else:
        template_names = ['search/indexes/%s/%s_%s.txt' % (obj._meta.app_label, obj._meta.module_name, self.instance_name)]

    t = loader.select_template(template_names)
    return t.render(Context({'object': obj}))