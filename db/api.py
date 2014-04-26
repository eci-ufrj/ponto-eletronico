'''
Created on 25/04/2014

@author: submarino
'''
from db.models import User, Place, TimeCard, TimeCardEntry
import datetime

def addUser(name, username):
    user = User()
    user.name = name
    user.username = username
    user.save()
    return {'user_id': user.pk, 'success':True}


def addPlace(name, owner_id, address=None, position=None):
    place = Place()
    place.address = address
    place.name = name
    place.position = position
    place.owner_id = owner_id
    place.save()
    return {'place_id': place.pk}

def addWorker(worker_id, place_id):
    place = Place.objects.get(pk=place_id)
    place.workers.add(worker_id)
    place.save()
    return {'success': True}


def addTimeCard(place_id):
    tc = TimeCard()
    tc.place_id = place_id
    tc.save()
    return {'timecard_id': tc.pk}


def addTimeCardEntry(worker_id, timecard_id, start_time=datetime.datetime.now(), end_time=None):
    tc = TimeCard.objects.get(pk=timecard_id)
    try:
        wk = User.objects.get(pk=worker_id, workplaces_id=tc.place_id)
    except:
        pass
    tce = TimeCardEntry()
    tce.timecard_id = tc.pk
    tce.worker_id = wk.pk
    tce.start_time = start_time
    tce.end_time = end_time
    tce.save()
    return {'time_card_entry_id': tce.pk}

def addEndTimeToTimeCardEntry(tce_id, end_time=datetime.datetime.now()):
    tce = TimeCardEntry.objects.get(pk=tce_id)
    tce.end_time = end_time
    tce.save()
    return {'success':True}
    
    
    