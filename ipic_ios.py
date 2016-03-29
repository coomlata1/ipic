# coding: utf8
'''
#---Script: ipic_ios.py
#---Author: drdrang
#---Created: 03/03/2016
#---Modified: @coomlata1
#---Last Modified: 03/28/2016

A Pythonista script for downloading images from the iTunes, App,
and Mac stores. The script was originally written by drdrang for
OSX and is avaiable as ipic.py here: 'https://github/drdrang/ipic'.
His blog here: 'https://leancrew.com/all-this/2016/03/
images-from-the-itunes-app-mac-app-stores/', also furnishes a
wealth of information about the script. 

I have modified the script for use on iOS. Rather than writing
the search results to a file, this script sends them to the iOS
clipboard and then to 1Writer for pasting. I chose 1Writer
because it has an excellent browser that displays the thumbnails
as drdrang intended, and with only one click of the 'Preview'
button. They can then be enlarged for viewing and copying to the
clipboard or photo gallery. Of course the search results could
also be pasted into any other text editor that will handle and
display html.

The search arguments can be entered by holding down the run
button in Pythonista. For another option, I wrote a javascript
front end action in 1Writer that allows for a dialog based entry
of search criteria and then starts this script. It is available
here: 'https://1writerapp.com/action/b8d98'.

Dependencies: The Docopt module to conveniently handle the search
criteria  parsing is available here: 'https://github.com/docopt/docopt'. 
  
Installation involves simply copying one file, docopt.py, to the
'site-packages' folder in Pythonista. The script could also be
modified to do the parsing with Pythonista and avoid the
dependency.
'''
import requests
import docopt
import os
#import subprocess
import webbrowser
import clipboard
import sys

# You may want to change these.
#myDir = os.environ['HOME'] + '/Desktop/'  # directory for HTML file
#browser = 'com.apple.Safari'  # browser bundle identifier

#myDir = '../Documents/'  # directory for HTML file

usage = '''Usage: ipic (-i | -m | -a | -f | -t | -b | -h) SEARCHTERM
  
Generate and open a web page of thumbnail images and links to larger images for items in the iTunes/App/Mac App Stores.

Options:
  -i      iOS app
  -m      Mac app
  -a      album
  -f      film
  -t      TV show
  -b      book
  -h      show this help message

Only one option is allowed. The HTML file for the generated web page is saved on your Documents dir.'''

# Handle the command line.
args = docopt.docopt(usage)
searchterm = args['SEARCHTERM']
if args['-i']:
  size = 512
  media = 'software'
  entity = 'software'
  name = 'trackName'
elif args['-m']:
  size = 512
  media = 'software'
  entity = 'macSoftware'
  name = 'trackName'
elif args['-a']:
  size = 600
  media = 'music'
  entity = 'album'
  name = 'collectionName'
elif args['-f']:
  size = 600
  media = 'movie'
  entity = 'movie'
  name = 'trackName'
elif args['-t']:
  size = 600
  media = 'tvShow'
  entity = 'tvSeason'
  name = 'collectionName'
elif args['-b']:
  size = 600
  media = 'ebook'
  entity = 'ebook'
  name = 'trackName'
else:
  size = 600
  media = ''
  entity = ''
  name = ''

# Make the iTunes search call and collect the thumbnail and large image URLs.
iURL = 'https://itunes.apple.com/search'
parameters = {'term': searchterm, 'media': media, 'entity': entity}
console.hud_alert('Searching iTunes...')
r = requests.get(iURL, params=parameters)
results = r.json()['results']
turls = [ x['artworkUrl100'] for x in results ]
burls = [ x.replace('100x100', '{0}x{0}'.format(size)) for x in turls ]
names = [ x[name] for x in results ]

# Construct the HTML.
linkFmt = '<a href="{1}"><img src="{0}" alt="{2}", title="{2}" /></a>'
links = [linkFmt.format(x, y, z.encode('utf8'))
          for x, y, z in zip(turls, burls, names) ]
html = '''<html>                                                        <head><title>{0} pictures</title></head>
<body>
<h1>“{0}” pictures</h1>
{1}
</body>
</html>'''.format(searchterm, '\n'.join(links))

# Create an HTML file and open it.
#htmlFile = myDir + searchterm + '.html'
#with open(htmlFile, 'w') as f:
  #f.write(html)

#subprocess.check_call(['open', '-b', browser, htmlFile])

# Send html output to clipboard and shoot it to 1Writer for display in it's browser. 
clipboard.set(html)
cmd = 'onewriter://'
webbrowser.open(cmd)
sys.exit('Search results were sent to the clipboard for display in 1Writer.')
