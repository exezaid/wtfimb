from django.db import models

class Stage(models.Model):
	display_name = models.CharField(max_length=255)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	mtc_name = models.CharField(max_length=255)
	#routes = models.ManyToManyField('Route') #Since Route isn't yet defined

	def save(self, comment=""):
		sh = StageRevision(
							stage = self, 
							display_name = self.display_name,
							latitude = self.latitude,
							longitude = self.longitude,
							comment = comment
						  )
		sh.save()												
		super(Stage, self).save()

class Route(models.Model):
	display_name = models.CharField(max_length=64)
	mtc_name = models.CharField(max_length=64)
	types = models.CharField(max_length=64)
	start = models.ForeignKey(Stage, related_name='start')
	end = models.ForeignKey(Stage, related_name='end')
	stages = models.ManyToManyField(Stage, through="RouteStage")
	time = models.FloatField()
	fare = models.FloatField()

class RouteStage(models.Model):
	route = models.ForeignKey(Route)
	stage = models.ForeignKey(Stage)
	sequence = models.IntegerField()

class StageRevision(models.Model):
	stage = models.ForeignKey(Stage)
	edited_at = models.DateTimeField(auto_now_add=True)
	display_name = models.CharField(max_length=255)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	comment = models.CharField(max_length=1024, blank=True, null=True)
