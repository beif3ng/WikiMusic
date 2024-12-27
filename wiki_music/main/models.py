from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField()
    image = models.ImageField(upload_to='groups/', blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/', blank=True, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True, related_name='songs')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='songs')
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class GroupMember(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    role = models.CharField(max_length=100)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='members/', blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.name
