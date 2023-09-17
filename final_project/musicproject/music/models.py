from django.db import models
from django.utils.translation import gettext_lazy as _

class Artist(models.Model):
    artistName = models.CharField(_("Artist Name"), max_length=50)
    create = models.DateTimeField(_("Artist create date"),auto_now=True)
    last_update = models.DateTimeField(_("Lastest artist last_update"),auto_now=True)

    class Meta:
        verbose_name =_("Artist")
        verbose_name_plural = _("Artist")

    def _str_(self):
        return self.artistName

class Album(models.Model):
    Artist = models.ForeignKey("Artist", verbose_name=_("Artrist Album"), on_delete=models.CASCADE)
    albumName = models.CharField(_("Album Name"), max_length=50)
    created = models.DateTimeField(_("Album created date"), auto_now=True)
    last_update = models.DateTimeField(_("Latest album update"), auto_now=True)

class meta:
    verbose_name = _("Album")
    verbose_name_plural = _("Albums")

def _str_(self):
    return self.albumName

class Song(models.Model):
    album = models.ForeignKey("Album", verbose_name=_("Song Album"), on_delete=models.CASCADE)
    SongThumbnail = models.ImageField(_("Song Thumbnail"), upload_to='thumbnail/', help_text=".jpg, png, .jpeg, .svg supported")
    Song = models.FileField(_("Song"), upload_to='song/', help_text=" .mp3 supported only")
    songName = models.CharField(_("Song Name"), max_length=50)
    created = models.DateTimeField(_("Song created date"), auto_now=True)
    last_updated = models.DateTimeField(_("Latest song update"), auto_now=True)

    class meta:
     verbose_name = _("Song")
     verbose_name_plural = _("Songs")

     def __str__(self):
         return self.songname



