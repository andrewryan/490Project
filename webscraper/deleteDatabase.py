from .models import *
from .views import *

######### loop to delete entire contents of House model #########
def deleteDatabase():
    # test = House.objects.all()

    # test = House.objects.all()[:5].delete()
    test = House.objects.get(pk=8).delete()

    # for x in House.objects.all().iterator():
    #     x.delete()
    return test
