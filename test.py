import matplotlib.pyplot as plt
import tinys3

plt.plot([1,2,3,4,5,6,7,8,9], [1,4,9,16,0,7.3,2,12,6])
plt.axis([0, 9, 0, 20])
plt.ylabel('Precipitation Level (mm)')
plt.xlabel('Day starting today')
plt.title("Precipitation Level for the City")
plt.savefig('/tmp/image.png')

conn = tinys3.Connection('AKIAJW7BQZSIBCI6JOXQ','SjF57ya3EweNzlAXvgbqAZx5ZT8+5tl4o/Dm9zZz')

f = open('/tmp/image.png','rb')
conn.upload('image.png',f,'alexaweather')

#Now we connect to our s3 bucket and upload from memory
#conn = S3Connection('AKIAJW7BQZSIBCI6JOXQ', 'SjF57ya3EweNzlAXvgbqAZx5ZT8+5tl4o/Dm9zZz')

#Connect to bucket and create key
#b = conn.get_bucket('alexaweather')
#k = b.new_key('alexa.png')

#fileImage = open('/tmp/image.png','r')
#k.set_contents_from_filename(fileImage)
#k.set_acl('public-read')
