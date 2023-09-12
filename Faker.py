import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

from faker import Faker
import random
from first_app.models import Topico,Pagina,Acessos

fakergen = Faker()

topicos = ['Pesquisa','Social','Loja','Jogos']

for i in range(3):
    t = Topico.objects.get_or_create(topico=random.choice(topicos))[0]

    p = Pagina.objects.get_or_create(topico = t,
                                    name = fakergen.name(),
                                    url = fakergen.url())[0]

    a = Acessos.objects.get_or_create(pagina = p,
                                    date = fakergen.date())[0]