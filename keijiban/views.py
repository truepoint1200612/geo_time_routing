from django.shortcuts import render
from keijiban.forms import KakikomiForm
from django.http import HttpResponse
from . import forms
from . import loadOsm
from . import route as rt
from . import map_api
import folium

def kakikomi(request):
    f = KakikomiForm()
    return render(request, 'keijiban/kakikomiform.html', {'form1': f})

def geo_form(request):
    form = forms.GeoTimeForm()
    if form.is_valid():
        message = '検索を開始します'
    else:
        message = 'データを入力してください'
    posted_val = ''
    if request.method == 'POST':
        posted_val = request.POST
        start_latlng = map_api.getLatLng(posted_val['start'])
        end_latlng = map_api.getLatLng(posted_val['goal'])
        start = (start_latlng['lat'], start_latlng['lng'])
        end = (end_latlng['lat'], end_latlng['lng'])
        data = loadOsm.LoadOsm("cycle")
        # Set the longitude and latitude
        node1 = data.findNode(start[0],start[1])
        node2 = data.findNode(end[0], end[1])
        m = folium.Map(location=[start[0],start[1]])
        # Add marker of start and end point to map
        folium.Marker([start[0],start[1]]).add_to(m)
        folium.Marker([end[0], end[1]]).add_to(m)
        
        router = rt.Router(data)
        route_list = []
        result, route = router.doRoute(node1, node2)
        if result == 'success':
            for i in route:
                node = data.rnodes[i]
                position = (node[0], node[1])
                # Using a list to store the data of path, every elemen of the list is a tuple,
                # i.e. [(lon,lat), (lon,lat), ...]
                route_list.append(position)
            folium.PolyLine(route_list).add_to(m)
            # Store results
            m.save("./keijiban/templates/keijiban/map.html")
            return render(request, 'keijiban/map.html')
        else:
            print("Failed (%s)" % result)

    d = {
        'form': form,
        'message': message,
        'posted_val': posted_val,
    }
    return render(request, 'keijiban/kakikomiform.html', d)
