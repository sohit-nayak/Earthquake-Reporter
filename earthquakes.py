
import urllib2
import json, os.path


def printResults(data):
	theJSON = json.loads(data)
	if 'title' in theJSON['metadata']:
		print theJSON['metadata']['title']
	count = theJSON['metadata']['count']
	print str(count) + " events recorded."

	# for i in theJSON['features']:
	# 	if i['properties']['mag'] > 4:
	# 		print "%2.2f" % i['properties']['mag'], i['properties']['place']
	# print "Events that were felt:"
	for i in theJSON['features']:
		f = open('<The path to which you want the reports to be saved.>' + i['id'] + '.txt', 'wb') #assign the path to which the reports are to be saved.
		feltReports = i['properties']['felt']
		string = "Magnitude: " + str(i['properties']['mag']) +'\nPlace: ' + i['properties']['place'] + ' reported ' + str(feltReports) + ' times.\n'
		string = string + 'url: ' + i['properties']['url'] + '\nIt caused ' + str(i['properties']['tsunami']) + ' tsunamis.'
		f.write(string)
		f.close()
		# if ((feltReports != None) & (feltReports > 0)):
		# 	print "%2.2f" % i['properties']['mag'] , i['properties']['place'], 'reported ' + str(feltReports) + ' times.'
def main():
	url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
	webUrl = urllib2.urlopen(url)
	print webUrl.getcode()
	if(webUrl.getcode() == 200):
		data = webUrl.read()
		with open('data.json', 'wb') as file:
			file.write(json.dumps(data, file))
		printResults(data)

if __name__ == '__main__':
	main()