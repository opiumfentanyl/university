import re
import urllib.request
import csv

site = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()
pattern = (r'(?:org-widget-header__title-link">)(?P<names>[^<]+)(?:[^9]+)(?:location">\s+)(?P<adres>[^<]+\b)(?:[^0-9]+)(?:spec__value">)(?P<numbers>.[^<]+)(?:[^0-9,]+)(?:[^0-9,]spec__value">)(?P<time>[^<]+)')
matches = re.findall(pattern, site)
lst = []

for match in matches:
    lst.append(match)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')

    for i in lst:
        writer.writerow(i)

