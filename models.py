from django.db import models

class Deposit(models.Model):
    name = models.CharField(max_length=30)
    depsum = models.CharField(max_length=30)
    depperiod = models.CharField(max_length=30)
    

    def restrict (self):
                 
        depperiod > 6

    
    def calc (self):
        self.calc = depsum*depperiod*0.01+depsum

    def __unicode__(self):
        return u'%s %s %s %s' % (self.name, self.depsum, self.depperiod, self.deptype)

class SimpleDeposit (Deposit):
                pass

class CompDeposit (Deposit):
      def calc (self):
        self.calc = depsum*(1.025**(depperiod*0.33))

class BonusDeposit (Deposit):

    def bonus (self):
        self.bonus = floor (depperiod/6) * depsum * 0.02

    def calc (self):
        self.calc = depsum*(1.025**(depperiod*0.33)) + self.bonus

