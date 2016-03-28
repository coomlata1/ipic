# ipic #

Python script for searching and downloading images from the iTunes, App, and Mac App Stores.

# ipic_ios #

Modified version of ipic.py to run on iOS.

## Dependencies ##

* [requests][1] for handling communication with the [iTunes Search API][2].
* [docopt][3] for handling the command line switches.

## Usage ##

    ipic (-i | -m | -a | -f | -t | -b | -n | -h) SEARCHTERM

Generate and open a web page of thumbnail images and links to larger images
for items in the iTunes/App/Mac App Stores.

The switches are

* -i: iOS app
* -m: Mac app
* -a: album
* -f: movie (mnemonic: film)
* -t: TV show
* -b: book
* -n: audiobook (mnemonic: narration)
* -h: show this help message

Only one switch is allowed. The HTML file for the generated web page is
saved on your Desktop.

Because the API usually returns several hits, `ipic` creates and opens a web page of thumbnail images that let you choose the one you want visually. Here's an example:

<img class="ss" src="http://leancrew.com/all-this/images2016/20160302-Web%20page%20from%20ipic.png" alt="Web page from ipic" title="Web page from ipic" />

Each thumbnail is a link to a full-sized version of the image, 512×512 for apps and 600×600 otherwise. Hovering over a thumbnail will show the name of the item.


[1]: https://github.com/kennethreitz/requests
[2]: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
[3]: http://docopt.org/
