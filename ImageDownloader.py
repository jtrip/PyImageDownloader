__author__ = 'jtrip'

import os
import sys
import time
import urllib
import urllib2
import BeautifulSoup


def get_user_url():
    url_input = raw_input("What URL would you like to download files from?")
    return url_input


def get_jpgs(source,url):
    """
    Grab any available jpg files
    """
    for a_tag in source.findAll('a'):
        if 'jpg' in a_tag['href']:
            print u'found a jpeg at {0}'.format(a_tag['href'])
            urllib.urlretrieve(str(url+a_tag['href']))


def get_pngs(source,url):
    """
    Grab any available png files
    """
    for a_tag in source.findAll('a'):
        if 'png' in a_tag['href']:
            print u'found a png at {0}'.format(a_tag['href'])
            file = open(a_tag['href'],'wb')
            urllib.urlretrieve(str(url+a_tag['href']))
            file.write(image)


def main(argv):

    arg_num = len(argv)
    if arg_num > 0:
        user_url = argv[0]
    else:
        user_url = get_user_url()

    try:
        root_page_requested = urllib2.Request(user_url)
        response_to_root_request = urllib2.urlopen(root_page_requested)
    except:
        ## I should make this exception more specific... maybe more than one
        print 'OMG! URL no good'

    try:
        os.makedirs(time.strftime('%d-%m-%Y %H:%M:%S'), mode=0777)
    except os.error:
        print 'cannot create folder, it already exists'

    source_of_root_page = BeautifulSoup.BeautifulSoup(response_to_root_request)

    get_jpgs(source_of_root_page,user_url)
    get_pngs(source_of_root_page,user_url)


if __name__ == "__main__":
   main(sys.argv[1:])
