from bs4 import BeautifulSoup
import urllib
import re
import urllib2

######### get URL for searching worms database

BASEURLp1 = 'http://www.marinespecies.org/aphia.php?p=taxlist&tid=-1&tName='
BASEURLp2 = '&searchpar=0&tComp=begins&action=search&rSkips=0&marine=1&fossil=4'

######## check url

def checkurl(mysearch):

	return urllib.urlopen(BASEURLp1 + mysearch + BASEURLp2).geturl()
###################### add search term 


def make_soup(mysearch):

	myspeciesurl = urllib.urlopen(BASEURLp1 + mysearch + BASEURLp2).read()


	return BeautifulSoup(myspeciesurl, 'html.parser')


######### find all the hits

def findhits(thesoup):

	return thesoup.findAll("li", {"class" : "list-group-item aphia_core_list_group_hover" } )

####### visit species-specific page

def make_species_soup(myID):

	speciesurl = urllib.urlopen('http://www.marinespecies.org/aphia.php?p=taxdetails&id=' + myID)
        return BeautifulSoup(speciesurl, 'html.parser')


############## search species info


def get_hitlist(searchterm):

	hitlist = []

	if 'taxdetails' in checkurl(searchterm):
		hitlist.append(checkurl(searchterm).split('=')[-1])
		return hitlist

	else:
		myhits = findhits(make_soup(searchterm)) ### each item in this list is a separate search result
    
		if len(myhits) > 0:
			hitsdict = dict()
			#get all unique hits

			for hit in myhits:

				for item in hit.findAll('a'):


					### find the nested tag holding the link
					thename = item.contents[-2].contents[0]
							
					mylink = item.get('href')

					taxID = mylink.split('=')[-1]

					if taxID in hitlist:
						continue
					else:
						hitlist.append(taxID)
						hitsdict[taxID] = thename
			return hitlist
		else:
			hitlist = []
			return hitlist

def parse_hitlist(hitlist):

	ID = hitlist[0]
	newsoup = make_species_soup(ID)

	mystatus = newsoup.findAll(text=re.compile("Status"))[0].parent.parent.findAll('span')[-1].contents[0] ####### whether or not the name is accepted


	pagespeciesID = newsoup.findAll("h3", {"class", "aphia_core_header-inline"})[0].findAll('b')[0].contents[-2].contents[0] ##### the species name of the page


	if pagespeciesID.split(' ')[-1] == samplename.split('_')[1]:

		if mystatus == 'unaccepted':
			return ['extinct', pagespeciesID]
		else:
			return ['extant', pagespeciesID]
	else:
		return ['extinct', pagespeciesID]

#mytable = open('test', 'r')
mytable = open('pyrate.input.v3', 'r')


livingordeaddict = dict()

for line in mytable:
	info = line.strip().split('\t')


	searchterm = info[0] + ' ' + info[1]

	samplename = info[0] + '_' + info[1]

	if samplename in livingordeaddict:
		continue
	else:

		hitlist = []

		if len(get_hitlist(searchterm)) > 0:
			livingordead = parse_hitlist(get_hitlist(searchterm))
		else:
			livingordead = ['extinct', 'NA']

		livingordeaddict[samplename] = livingordead


mytable.close()
#mytable = open('test', 'r')
mytable = open('pyrate.input.v3', 'r')

out = open('pyrate.input.v4', 'w')



for line in mytable:

	info = line.strip().split('\t')
	samplename = info[0] + '_' + info[1]

	info[2] = livingordeaddict[samplename][0]

	info.append(livingordeaddict[samplename][1])

	out.write('\t'.join(info) + '\n')





















