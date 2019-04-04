# -*- coding: cp1252 -*-

import sqlite3
import io

conn = sqlite3.connect('agenda.db')

with io.open('agenda_bkp.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%f' % linha)

print('Backup realizado com sucesso.')
print('Salvo como agenda_bkp.sql')

conn.close()