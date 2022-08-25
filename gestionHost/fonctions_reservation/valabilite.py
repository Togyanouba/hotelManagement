import datetime
from gestionHost.models import Chambre, Reservation

def EstValable(chambre, dateEntre, dateSorti):
    avail_list= []
    reservations= Reservation.objects.filter(chambre=chambre)
    for reservation in reservations:
        if reservation.dateEntre > dateSorti or reservation.dateSorti < dateEntre:
            avail_list.append(True)
        else:
            avail_list.append(False)
        return all(avail_list)