from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Contact(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=50, blank=True)
    office = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    url = models.URLField(max_length=200, blank=True)
    next_call = models.DateField(blank=True)
    note = models.TextField(blank=True)
    introduced_by = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _get_full_name(self):
        "returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)

    def get_absolute_url(self):
        return reverse("tocall:contact_detail", kwargs={"pk": self.pk})

    def __unicode__(self):
        return self.last_name


class History(models.Model):
    contact = models.ForeignKey('Contact')
    email_in = models.BooleanField(default=False)
    email_out = models.BooleanField(default=False)
    email_linkedin = models.BooleanField(default=False)
    call_in = models.BooleanField(default=False)
    call_out = models.BooleanField(default=False)
    voice_mail = models.BooleanField(default=False)
    message = models.BooleanField(default=False)
    no_message = models.BooleanField(default=False)
    no_answer = models.BooleanField(default=False)
    meeting = models.BooleanField(default=False)
    write_up = models.TextField(blank=True)
    contacted_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse(
            "tocall:contact_update_date",
            kwargs={"pk": self.contact.pk}
        )

    def __unicode__(self):
        return self.write_up
