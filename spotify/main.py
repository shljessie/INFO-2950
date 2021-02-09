from bs4 import BeautifulSoup
import json

# Open up source code and pipe to Beautiful Soup
with open("sourcecode.html", "r" ) as f: 
  soup = BeautifulSoup(f, features = "html.parser")

# Find the h2 tag that has the Albums heading
albumTag= soup.find( "h2", string= "Albums")


# Find the parent section of the h2 tag
albumSection= albumTag.find_parent("section")

# Find all list items within the section tag
albums = albumSection.findAll("li")

# Iterate through list items and extract data.

# Initiallise list of albums before for loop
allAlbumDetails=[]

for album in albums:
    aTag= album.find("a")
    albumLink = aTag['href']
    albumName = aTag['alt']

    # album images have two divs, cherrypick one the correct classname
    albumImageDiv= aTag.find('div', {'class': 'grid-item-image'})
    albumImage = albumImageDiv["data-src"]

    # print(albumLink, albumName, albumImage, sep= "\n")

    albumDetails= {
      "name": albumName,
      "link": albumLink,
      "cover": albumImage
    }


    allAlbumDetails.append(albumDetails)

print(allAlbumDetails)

# Write the extracted data to a data file
with open('albums.json',"w") as a:
  json.dump(allAlbumDetails, a)