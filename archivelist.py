from archivecdx import Listing
import os, csv

SITE = os.environ["ARCHIVE_SITE"]
kwargs = {}
args = "matchType fl from to filter collapse".split()
for arg in args:
#	print(arg,"ARCHIVE_"+arg.upper())
	if "ARCHIVE_"+arg.upper() in os.environ:
		kwargs[arg] = os.environ["ARCHIVE_"+arg.upper()]
kwargs["showDupeCount"]="true"
#print(SITE,kwargs)
listing = Listing(SITE,**kwargs)
print(listing[0]._fields)
res = {}
listing.listing.sort(key=lambda x: x.timestamp)
for entry in listing.listing:
	res[entry.original]=entry
with open("out.csv","w") as f:
	w = csv.writer(f)
	w.writerow(listing.listing[0]._fields)
	w.writerows([res[x] for x in res])
	f.close()

