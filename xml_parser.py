from xml.dom import minidom

class xmlParser( url):
        def __init__(url=None):
                url = url
                print "parsing stream list..."
                xmldoc = minidom.parse('~/home/pi/ipcam/stream_list.xml ')
                print "parsed ok"
        def get_url_list():
                listNode = xmldoc.firstChild
                index = 0
                print listNode.toxml()
                for cam in listNode.childNodes:

