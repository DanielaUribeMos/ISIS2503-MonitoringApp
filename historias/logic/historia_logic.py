from ..models import Historia

def get_historias():
    queryset = Historia.objects.all()
    return (queryset)

def create_historia(form):
    plantilla = form.save()
    plantilla.save()
    return ()