from django.db import models


class DemoModel(models.Model):

    input_file = models.FileField(upload_to="input/")
    processed_file = models.FileField(upload_to="output/")
