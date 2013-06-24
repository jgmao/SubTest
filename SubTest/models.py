from django.db import models


# Create your models here.

class SubTestResult(models.Model):
    # DIST_TYPE = (('MS','Micro Shift'),('MR','Micro Rotate'),('BR','Blur'),('BL','Blocking'),('LC','Light Change'))
    orgName = models.CharField(max_length=50)
    candName = models.CharField(max_length=50)
	# path = models.CharField(max_length=100)
    # distortion = models.CharField(max_length=2,choices = DIST_TYPE)
    rank = models.FloatField()
	
    def __unicode__(self):
        return self.orgName + "_to_" + self.candName +"_with_"+ str(self.rank)


# class PlayerRecord(models.Model):
    # name    = models.CharField(max_length=60)
    # email   = models.EmailField(max_length=120)
    # created = models.DateTimeField(auto_now_add=True)
    # passed  = models.BooleanField(default=False)

    # def __unicode__(self):
        # return "%s - %s" % (self.name, self.email)

    # class Meta:
        # ordering        = ["created"]
        # unique_together = [["name", "email"]]

