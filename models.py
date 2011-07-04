from django.db import models

class Deposit(models.Model):
    name = models.CharField(max_length=30)
    depsum = models.CharField(max_length=30)
    depperiod = models.CharField(max_length=30)
    deptype = models.CharField(max_length=30)


    def __unicode__(self):
        return u'%s %s %s %s' % (self.name, self.depsum, self.depperiod, self.deptype)


