class Subscribe(models.Model):
    subLevel = models.CharField(max_length=15)
    id = models.AutoField(primary_key=True)