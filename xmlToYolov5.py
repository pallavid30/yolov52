import xml.etree.ElementTree as ET


tree = ET.parse("data/annotations_class2/img_01_425382400_00001.xml")
root = tree.getroot()
currentName = root[6][0].text

print(currentName)
for child in root:
    if child.tag == "size":
        width = int(child[0].text)
        height = int(child[1].text)
    if child.tag == "object":
        name = child[0].text
        for child1 in child:
            if child1.tag == "bndbox":
                xmin = int(child1[0].text)
                ymin = int(child1[1].text)
                xmax = int(child1[2].text)
                ymax = int(child1[3].text)
                print(xmin," ", xmax, " ", ymin, " ", ymax)
                print (width, " ", height, " ")
                x = float(xmin + xmax)/float(2.0*width)
                y = float(ymin + ymax)/float(2.0*height)
                w = float(xmax - xmin)/float(width)
                h = float(ymax - ymin)/float(height)
                print(x, " ", y , " ", w, " ", h)
