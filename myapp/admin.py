from django.contrib import admin
from myapp.models import Language, Decidiability, Problem, IsClosed, SetOperation, DecidiabilityNote, ClosurePropertyNote
admin.site.register(Language)
admin.site.register(Decidiability)
admin.site.register(Problem)
admin.site.register(IsClosed,)
admin.site.register(SetOperation)
admin.site.register(DecidiabilityNote)
admin.site.register(ClosurePropertyNote)


