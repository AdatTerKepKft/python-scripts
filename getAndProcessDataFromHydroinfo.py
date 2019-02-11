import urllib
import re
urlbase = 'http://www.hydroinfo.hu/vituki/archivum/bp'
path = 'u:/adatterkep/projektek/dunaiSzigetek/insegesNapok/raw/'
datafile = open(path + 'database.csv','w')
datafile.write('year;month;day;str_value;num_value;flag\n')
for y in range(1876, 2006):
    matrix = []
    year = str(y)
    url = urlbase + year + '.htm'
    page = urllib.urlopen(url).read()
    raw = page[page.find('Nap'):page.find('Minimum')]
    rows = raw.splitlines()
    for row in rows:
        r = re.sub(' {7}', ' - ', row) # "Nincs adat" helyőrzők 
        r = re.sub('\s+', ' ', r).strip() # Sok egymást követő szóköz cseréje, majd sor eleji és végi szóközök eltüntetése
        if len(r) != 0: # Üres sorok kihagyása
            matrix.append(r.split(' ')) # Adatokkal teli sorok hozzárendelése a mátrixhoz
    for m in range(1, 13):
        for d in range(1, 32):
            if matrix[d][m] != '-':
                datafile.write(year + ';' + str(m) + ';' + str(d) + ';' + matrix[d][m] + ';' + re.sub('[a-zA-Z]','', matrix[d][m]) + ';' + re.sub('[0-9]','', matrix[d][m]) + '\n')
datafile.close()
