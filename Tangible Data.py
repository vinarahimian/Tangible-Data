import rhinoscriptsyntax as rs
import math 
#from sets import Set as set 
 
rs.DeleteObjects (rs.AllObjects())
rs.EnableRedraw(False)
 
filename=rs.OpenFileName("Open CSV file", ".csv|", None, None, None)
 
file = open(filename, 'r')
rows = file.readlines()
file.close()
 
del rows[0]
neighborhoods=[]
 
for row in rows:
    row=row.strip() 
    ptInfo = row.split(',') 
    neighborhood = ptInfo[0] 
    neighborhoods.append(neighborhood) 
#print (neighborhoods)
 
 
neis_ = set()
for name in neighborhoods:
    neis_.add(name)
neis = list(neis_)
 
 
listOfFourAttributes=[]
for row in rows:
    for i in neis:
        row=row.strip()
        attributes=row.split(',')
        if attributes[0] == i:
            listOfFourAttributes.append(attributes)
#print listOfFourAttributes #[[neighborhood, type, price, review],[...]] 
 
filteredByNeighborhood=[]
for j in neis:
    currentNeighborhood=[]
    for i in listOfFourAttributes:
        nei=i[0]
        if nei == j:
            currentNeighborhood.append(i)
    filteredByNeighborhood.append(currentNeighborhood) 
#print filteredByNeighborhood #[[[neighorhood1, type, price, review],[...]],[[neighborhood2, type, price, review],[...]]] 
 
#############################################################################################################################
 
# find the maximum price of the entire neighborhoods in the city
def maxPrice (listOfFourAttributes):
    priceList = []
    for i in listOfFourAttributes:
        price = float(i[2])
        priceList.append(price)
        maxPrice = max(priceList) 
    return maxPrice
 
# find the minimum price of the entire neighborhoods in the city
def minPrice (listOfFourAttributes):
    priceList = []
    for i in listOfFourAttributes:
        price = float(i[2])
        priceList.append(price)
        minPrice = min(priceList) 
    return minPrice
 
currMaxPrice= maxPrice(listOfFourAttributes)
currMinPrice = minPrice(listOfFourAttributes) 
 
#remap the prices to the sphere degree values 
def reMap(value, currMaxPrice, currMinPrice):
    value = currMaxPrice if value > currMaxPrice else value
    value = currMinPrice if value < currMinPrice else value
    inputSpan = currMaxPrice - currMinPrice
    outputSpan = 180 - 0
    scaledThrust = float(value - currMinPrice) / float(inputSpan)
    return 0 + (scaledThrust * outputSpan)
 
 
r0 = 500
noOfNeighborhoods = float(len(neis)) 
 
# spherical coordinates
def houseToSphere(house):
    theta= math.radians(reMap(float(house[2]), currMaxPrice, currMinPrice))
    r = float(r0 + float(house[3]))
    return (r, theta)
 
#a list of [r, theta] for each neighborhood
listOfPointsPerNeighborhood=[]
for neighborhood in filteredByNeighborhood:
    pointsPerNeighborhood=[] 
    for house in neighborhood:
        pointsPerNeighborhood.append(houseToSphere(house))
    srt = sorted(pointsPerNeighborhood, key=lambda point: point[1])
    listOfPointsPerNeighborhood.append(srt)
 
 
#go to each neighborhood, get the info for each house and create a line with the points
lines=[]
i = 0
for neighborhood in listOfPointsPerNeighborhood:
    listOfPointCoords=[]
    deltaPhi = math.radians(360/noOfNeighborhoods)
    for house in neighborhood:
        radius = house[0]
        theta = house[1]
        phi= i*deltaPhi
        x=radius*math.sin(theta)*math.cos(phi)
        y=radius*math.sin(theta)*math.sin(phi)
        z=radius*math.cos(theta)
        pointInfo = rs.AddPoint(x,y,z)
        pointInfoCoord = rs.PointCoordinates(pointInfo)
        listOfPointCoords.append(pointInfoCoord)
        rs.DeleteObjects(pointInfo)
    line=rs.AddInterpCurve(listOfPointCoords,1)
    i = i+1
    lines.append(line)
 
rs.EnableRedraw(True)
