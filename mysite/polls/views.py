from django.http import HttpResponse
from django.template import loader
import dbUtils

def index(request):
    template = loader.get_template('polls/index.html')

    context = {}
    rows = dbUtils.get_data()
    if len(rows) > 0:
        pass
    else:
        context = {
            "title0": "jangcoding",
            "desc0": "",
            "title1": "jangcoding1",
            "desc1": "",
            "title2": "jangcoding2",
            "desc2": ""
        }

    return HttpResponse(template.render(context, request))
