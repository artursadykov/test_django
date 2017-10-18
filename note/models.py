from django.db import models

class NoteType (models.Model):
    notetype = models.IntegerField()
    name =  models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NoteType'
        verbose_name_plural = 'A lot of NoteTypes'


class Note(models.Model):
    notetype = models.ForeignKey(NoteType, blank=True, null=True)
    contents = models.CharField(max_length=1024, blank=True, null=True)
    count = models.IntegerField (blank=True, null=True)
    price = models.IntegerField (blank=True, null=True)
    summ = models.IntegerField (blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'A lot of Notes'

    # def save(self, *args, **kwargs):
    #     price_per_item = self.price
    #     self.price_per_item = price_per_item
    #     self.summ = self.count * price_per_item
    #     super(Note, self).save(*args, **kwargs)