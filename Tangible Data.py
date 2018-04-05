{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf200
{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red10\green82\blue135;\red255\green255\blue255;\red38\green38\blue38;
\red0\green0\blue0;\red15\green114\blue1;\red109\green109\blue109;\red0\green0\blue255;\red251\green0\blue129;
\red18\green139\blue2;}
{\*\expandedcolortbl;;\cssrgb\c0\c40000\c60000;\cssrgb\c100000\c100000\c100000;\cssrgb\c20000\c20000\c20000;
\cssrgb\c0\c0\c0;\cssrgb\c0\c50980\c0;\cssrgb\c50196\c50196\c50196;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c7843\c57647;
\cssrgb\c0\c60000\c0;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl352\partightenfactor0

\f0\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 rhinoscriptsyntax as rs\cf4 \strokec4 \
\cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 math \cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf6 \strokec6 #from sets import Set as set \cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 rs.DeleteObjects (rs.AllObjects())\cf4 \strokec4 \
\cf5 \strokec5 rs.EnableRedraw(\cf7 \strokec7 False\cf5 \strokec5 )\cf4 \strokec4 \
\'a0\
\cf5 \strokec5 filename\cf2 \strokec2 =\cf5 \strokec5 rs.OpenFileName(\cf8 \strokec8 "Open CSV file"\cf5 \strokec5 , \cf8 \strokec8 ".csv|"\cf5 \strokec5 , \cf7 \strokec7 None\cf5 \strokec5 , \cf7 \strokec7 None\cf5 \strokec5 , \cf7 \strokec7 None\cf5 \strokec5 )\cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf9 \strokec9 file\cf4 \strokec4  \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 open\cf5 \strokec5 (filename, \cf8 \strokec8 'r'\cf5 \strokec5 )\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 rows \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 file\cf5 \strokec5 .readlines()\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf9 \strokec9 file\cf5 \strokec5 .close()\cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 del\cf4 \strokec4  \cf5 \strokec5 rows[\cf10 \strokec10 0\cf5 \strokec5 ]\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 neighborhoods\cf2 \strokec2 =\cf5 \strokec5 []\cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 row \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 rows:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 row\cf2 \strokec2 =\cf5 \strokec5 row.strip() \cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 ptInfo \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 row.split(\cf8 \strokec8 ','\cf5 \strokec5 ) \cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 neighborhood \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 ptInfo[\cf10 \strokec10 0\cf5 \strokec5 ] \cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 neighborhoods.append(neighborhood) \cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf6 \strokec6 #print (neighborhoods)\cf4 \strokec4 \
\'a0\
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 neis_ \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 set\cf5 \strokec5 ()\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 name \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 neighborhoods:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 neis_.add(name)\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 neis \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 list\cf5 \strokec5 (neis_)\cf4 \strokec4 \
\'a0\
\'a0\
\cf5 \strokec5 listOfFourAttributes\cf2 \strokec2 =\cf5 \strokec5 []\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 row \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 rows:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 i \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 neis:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 row\cf2 \strokec2 =\cf5 \strokec5 row.strip()\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 attributes\cf2 \strokec2 =\cf5 \strokec5 row.split(\cf8 \strokec8 ','\cf5 \strokec5 )\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 attributes[\cf10 \strokec10 0\cf5 \strokec5 ] \cf2 \strokec2 ==\cf4 \strokec4  \cf5 \strokec5 i:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 listOfFourAttributes.append(attributes)\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf6 \strokec6 #print listOfFourAttributes #[[neighborhood, type, price, review],[...]] \cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 filteredByNeighborhood\cf2 \strokec2 =\cf5 \strokec5 []\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 j \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 neis:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 currentNeighborhood\cf2 \strokec2 =\cf5 \strokec5 []\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 i \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 listOfFourAttributes:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 nei\cf2 \strokec2 =\cf5 \strokec5 i[\cf10 \strokec10 0\cf5 \strokec5 ]\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 nei \cf2 \strokec2 ==\cf4 \strokec4  \cf5 \strokec5 j:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 currentNeighborhood.append(i)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 filteredByNeighborhood.append(currentNeighborhood) \cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf6 \strokec6 #print filteredByNeighborhood #[[[neighorhood1, type, price, review],[...]],[[neighborhood2, type, price, review],[...]]] \cf4 \strokec4 \
\'a0\
\cf6 \strokec6 #############################################################################################################################\cf4 \strokec4 \
\'a0\
\cf6 \strokec6 # find the maximum price of the entire neighborhoods in the city\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 def\cf4 \strokec4  \cf5 \strokec5 maxPrice (listOfFourAttributes):\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 priceList \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 []\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 i \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 listOfFourAttributes:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 price \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 float\cf5 \strokec5 (i[\cf10 \strokec10 2\cf5 \strokec5 ])\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 priceList.append(price)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 maxPrice \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 max\cf5 \strokec5 (priceList) \cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 return\cf4 \strokec4  \cf5 \strokec5 maxPrice\cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf6 \strokec6 # find the minimum price of the entire neighborhoods in the city\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 def\cf4 \strokec4  \cf5 \strokec5 minPrice (listOfFourAttributes):\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 priceList \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 []\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 i \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 listOfFourAttributes:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 price \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 float\cf5 \strokec5 (i[\cf10 \strokec10 2\cf5 \strokec5 ])\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 priceList.append(price)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 minPrice \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 min\cf5 \strokec5 (priceList) \cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 return\cf4 \strokec4  \cf5 \strokec5 minPrice\cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 currMaxPrice\cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 maxPrice(listOfFourAttributes)\cf4 \strokec4 \
\cf5 \strokec5 currMinPrice \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 minPrice(listOfFourAttributes) \cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf6 \strokec6 #remap the prices to the sphere degree values \cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 def\cf4 \strokec4  \cf5 \strokec5 reMap(value, currMaxPrice, currMinPrice):\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 value \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 currMaxPrice \cf2 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 value > currMaxPrice \cf2 \strokec2 else\cf4 \strokec4  \cf5 \strokec5 value\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 value \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 currMinPrice \cf2 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 value < currMinPrice \cf2 \strokec2 else\cf4 \strokec4  \cf5 \strokec5 value\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 inputSpan \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 currMaxPrice \cf2 \strokec2 -\cf4 \strokec4  \cf5 \strokec5 currMinPrice\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 outputSpan \cf2 \strokec2 =\cf4 \strokec4  \cf10 \strokec10 180\cf4 \strokec4  \cf2 \strokec2 -\cf4 \strokec4  \cf10 \strokec10 0\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 scaledThrust \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 float\cf5 \strokec5 (value \cf2 \strokec2 -\cf4 \strokec4  \cf5 \strokec5 currMinPrice) \cf2 \strokec2 /\cf4 \strokec4  \cf9 \strokec9 float\cf5 \strokec5 (inputSpan)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 return\cf4 \strokec4  \cf10 \strokec10 0\cf4 \strokec4  \cf2 \strokec2 +\cf4 \strokec4  \cf5 \strokec5 (scaledThrust \cf2 \strokec2 *\cf4 \strokec4  \cf5 \strokec5 outputSpan)\cf4 \strokec4 \
\'a0\
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 r0 \cf2 \strokec2 =\cf4 \strokec4  \cf10 \strokec10 500\cf4 \strokec4 \
\cf5 \strokec5 noOfNeighborhoods \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 float\cf5 \strokec5 (\cf9 \strokec9 len\cf5 \strokec5 (neis)) \cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf6 \strokec6 # spherical coordinates\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 def\cf4 \strokec4  \cf5 \strokec5 houseToSphere(house):\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 theta\cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 math.radians(reMap(\cf9 \strokec9 float\cf5 \strokec5 (house[\cf10 \strokec10 2\cf5 \strokec5 ]), currMaxPrice, currMinPrice))\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 r \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 float\cf5 \strokec5 (r0 \cf2 \strokec2 +\cf4 \strokec4  \cf9 \strokec9 float\cf5 \strokec5 (house[\cf10 \strokec10 3\cf5 \strokec5 ]))\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 return\cf4 \strokec4  \cf5 \strokec5 (r, theta)\cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf6 \strokec6 #a list of [r, theta] for each neighborhood\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 listOfPointsPerNeighborhood\cf2 \strokec2 =\cf5 \strokec5 []\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 neighborhood \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 filteredByNeighborhood:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 pointsPerNeighborhood\cf2 \strokec2 =\cf5 \strokec5 [] \cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 house \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 neighborhood:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 pointsPerNeighborhood.append(houseToSphere(house))\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 srt \cf2 \strokec2 =\cf4 \strokec4  \cf9 \strokec9 sorted\cf5 \strokec5 (pointsPerNeighborhood, key\cf2 \strokec2 =lambda\cf4 \strokec4  \cf5 \strokec5 point: point[\cf10 \strokec10 1\cf5 \strokec5 ])\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 listOfPointsPerNeighborhood.append(srt)\cf4 \strokec4 \
\'a0\
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf6 \strokec6 #go to each neighborhood, get the info for each house and create a line with the points\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 lines\cf2 \strokec2 =\cf5 \strokec5 []\cf4 \strokec4 \
\cf5 \strokec5 i \cf2 \strokec2 =\cf4 \strokec4  \cf10 \strokec10 0\cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0
\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 neighborhood \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 listOfPointsPerNeighborhood:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 listOfPointCoords\cf2 \strokec2 =\cf5 \strokec5 []\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 deltaPhi \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 math.radians(\cf10 \strokec10 360\cf2 \strokec2 /\cf5 \strokec5 noOfNeighborhoods)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf2 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 house \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 neighborhood:\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 radius \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 house[\cf10 \strokec10 0\cf5 \strokec5 ]\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 theta \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 house[\cf10 \strokec10 1\cf5 \strokec5 ]\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 phi\cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 i\cf2 \strokec2 *\cf5 \strokec5 deltaPhi\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 x\cf2 \strokec2 =\cf5 \strokec5 radius\cf2 \strokec2 *\cf5 \strokec5 math.sin(theta)\cf2 \strokec2 *\cf5 \strokec5 math.cos(phi)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 y\cf2 \strokec2 =\cf5 \strokec5 radius\cf2 \strokec2 *\cf5 \strokec5 math.sin(theta)\cf2 \strokec2 *\cf5 \strokec5 math.sin(phi)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 z\cf2 \strokec2 =\cf5 \strokec5 radius\cf2 \strokec2 *\cf5 \strokec5 math.cos(theta)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 pointInfo \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 rs.AddPoint(x,y,z)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 pointInfoCoord \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 rs.PointCoordinates(pointInfo)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 listOfPointCoords.append(pointInfoCoord)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 rs.DeleteObjects(pointInfo)\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 line\cf2 \strokec2 =\cf5 \strokec5 rs.AddInterpCurve(listOfPointCoords,\cf10 \strokec10 1\cf5 \strokec5 )\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 i \cf2 \strokec2 =\cf4 \strokec4  \cf5 \strokec5 i\cf2 \strokec2 +\cf10 \strokec10 1\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf5 \strokec5 lines.append(line)\cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl352\partightenfactor0
\cf5 \strokec5 rs.EnableRedraw(\cf7 \strokec7 True\cf5 \strokec5 )\cf4 \strokec4 \
}