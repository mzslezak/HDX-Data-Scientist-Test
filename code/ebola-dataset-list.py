# Script to query HDX for a list of datasets 
# and return CSV table.

import sys
import csv
import yajl as json
import requests as r
from termcolor import colored as color

# Fetch arguments from command line.
if __name__ == '__main__':
	if len(sys.argv) <= 1:
	    usage = '''
	    Please provide a CSV path.

	    python code/ebola-dataset-list.py {path/to/file.csv} 

	    e.g.

	    python code/ebola-dataset-list.py data/data.csv
	    '''
	    print(usage)
	    sys.exit(1)

	csv_path = sys.argv[1]

# Get list of datasets form HDX.
def getDatasetListforTag(tag = None, l = None, verbose = False):

	if tag is None:
		print "Please provide tag."
		return

	if l is None:
		print "I need a CSV path, e.g. data/data.csv"
		return

	print "----------------------------------"

	u = "https://data.hdx.rwlabs.org/api/action/tag_show?id=" + tag
	d = r.get(u).json()

	if d["success"] is False:
		m = color("ERROR", "red", attrs=['bold'])
		print "%s : %s" % (m, d["error"]["message"])
		return

	if d["success"] is True:
		m = color("SUCCESS", "green", attrs=['bold'])
		n = color(len(d["result"]["packages"]), "blue", attrs=['dark'])
		print "%s : processing %s records." % (m, n)

        f = csv.writer(open(l, "wb+"))
        
        # Write headers.
        f.writerow(["title", "name", "owner_org", "maintainer", "revision_timestamp", "id", "num_resources", "num_tags", "num_extras"])
        
        # Write records.
        record_counter = 0
        for dataset in d["result"]["packages"]:
			record_counter += 1
			try:
			    f.writerow([
			    	dataset["title"],
			    	dataset["name"],
			    	dataset["owner_org"],
			    	dataset["maintainer"],
			    	dataset["maintainer_email"],
			    	dataset["revision_timestamp"],
			    	dataset["id"],
			    	dataset["num_resources"],
			    	dataset["num_tags"],
			    	len(dataset["extras"])
			    	])

			except Exception as e:
				err = color("ERROR", "red", attrs=['bold'])
				rec = color(record_counter, "yellow", attrs=['bold'])
				print "%s : record %s failed to write." % (err, rec)
				f.writerow([
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA",
			    	"NA"
			    	])

				# Printing more detailed error messages.
				if verbose is True:
					print e

	print "----------------------------------"
	print "************* %s ***************" % (color("DONE", "blue", attrs=['blink','bold']))
	print "----------------------------------"
	

# Running the function.
getDatasetListforTsg("ebola", csv_path, verbose = False)