from django.db import models

class Deposit(models.Model):
    name = models.CharField(max_length=30)
    depsum = models.CharField(max_length=30)
    depperiod = models.CharField(max_length=30)
    
    def simplecalc (self):
        self.simplecalc = depperiod*0.01*depsum+depsum

    def compcalc (self):
        self.compcalc = depsum*(1.025**(depperiod*0.33))

    def bonuscalc (self):
        self.calc = depsum*(1.025**(depperiod*0.33)) + floor (depperiod/6) * depsum * 0.02

    def __unicode__(self):
        return u'%s %s %s %s' % (self.name, self.depsum, self.depperiod, self.deptype)


