from django.db import models

class Language(models.Model):
    title = models.CharField(max_length=50)
    full_name = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.title


class SetOperation(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Problem(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class IsClosed(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    set_operation = models.ForeignKey(SetOperation, on_delete=models.CASCADE)

    is_closed = models.BooleanField(default=False)

    def __str__(self):
        if self.is_closed:
            return f"{self.language.title} is CLOSED under {self.set_operation.title}"
        return f"{self.language.title} is NOT CLOSED under {self.set_operation.title}"



class Decidiability(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    is_decidiable = models.BooleanField(default=False)

    def __str__(self):
        if self.is_decidiable:
            return f"{self.language.title} is DECIDIABLE under {self.problem.title}"
        return f"{self.language.title} is UNDECIDIABLE under {self.problem.title}"

class DecidiabilityNote(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.text[:30]}..."

class ClosurePropertyNote(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.text[:30]}..."
        