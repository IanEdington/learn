#!/usr/bin/python

# from https://github.com/udacity/ud120-projects
import os
os.chdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"data"))

print ( "start download" )
import urllib
url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
urllib.urlretrieve(url, filename="enron_mail_20150507.tar.gz")
print ( "download complete!" )

print ( "unzipping Enron dataset (this may take a while)" )
import tarfile
tfile = tarfile.open("enron_mail_20150507.tar.gz", "r:gz")
tfile.extractall(".")

print("done")

