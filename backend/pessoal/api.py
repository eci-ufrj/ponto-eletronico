'''
Created on 22/04/2014

@author: submarino
'''
from backend.pessoal.models import Person, Boss


def addPerson(name):
    person = Person()
    person.name = name
    person.save()
    return {'success': True, 'id': person.pk}


def getPeople():
    people = Person.objects.all()
    data = {'people': list(people.values())}
    return data


def setPersonAsBoss(id):
    person = Person.objects.filter(pk=id)
    boss = Boss(person)
    boss.save()