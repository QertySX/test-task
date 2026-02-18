from django.db import models


class Comment(models.Model):
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE
    )

    username = models.CharField(max_length=100)
    email = models.EmailField()
    homepage = models.URLField(blank=True)

    text = models.TextField()

    image = models.ImageField(
        upload_to="comments/images/",
        blank=True,
        null=True
    )

    file = models.FileField(
        upload_to="comments/files/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", 'username', 'email']

    def __str__(self):
        return f"{self.username} - {self.created_at}"
