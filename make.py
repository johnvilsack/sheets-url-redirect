from sys import argv
import csv
import os

# Find all @@INSERTS and replace

os.chdir('@@PATH_TO_THIS_SCRIPT')
file = open('@@NAME_OF_CSV_FILE', 'rU')
urls = csv.reader(file)

Redirects = []
LinkList = []

# Skip Header
next(urls, None)

for line in urls:
# Purge white space from the column
	validator = line[5].strip()
# If validator threw an error, exit out.
	if validator:
		print "%s error thrown.  redirect.conf rewrite aborted."
		exit()
	elif (line[2] != ""):
# Write all to list, in case it bombs out
		Redirects.append("rewrite /%s %s permanent;" % (line[2], line[3]))
		LinkList.append("%s - %s : <a href=\"http://@@URL/%s\" target=\"_blank\">http://@@URL/%s</a><br>" % (line[0], line[1], line[2], line[2]))

# Open file
redirectfile = "redirect.conf"
redirectconf = open(redirectfile, 'w')
# Wipe old file
redirectconf.truncate()

for redirect in Redirects:
	redirectconf.write(redirect)
	redirectconf.write("\n")

# Close File
redirectconf.close()

linklistfile = "@@PATH_TO_HTML_FILE_INDEX"
linklisthtml = open(linklistfile, 'w')

linklisthtml.truncate()

for link in LinkList:
	linklisthtml.write(link)
	linklisthtml.write("\n")

linklisthtml.close()
