{"filter":false,"title":"urls.py","tooltip":"/auction/urls.py","undoManager":{"mark":55,"position":55,"stack":[[{"start":{"row":19,"column":37},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":47},"action":"insert","lines":["    url(r'^$', all_products, name='index'),"],"id":3}],[{"start":{"row":20,"column":18},"end":{"row":20,"column":31},"action":"remove","lines":[" all_products"],"id":4},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":[","]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"remove","lines":["    "],"id":5},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "],"id":6}],[{"start":{"row":16,"column":32},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":42},"action":"insert","lines":["from accounts import urls as urls_accounts"],"id":8}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":32},"action":"remove","lines":["from django.conf.urls import url"],"id":9},{"start":{"row":15,"column":0},"end":{"row":15,"column":41},"action":"insert","lines":["from django.conf.urls import url, include"]}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":29},"action":"remove","lines":["    url(r'^$', name='index'),"],"id":10},{"start":{"row":20,"column":37},"end":{"row":21,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":15,"column":0},"end":{"row":17,"column":42},"action":"remove","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts"],"id":11},{"start":{"row":15,"column":0},"end":{"row":17,"column":58},"action":"insert","lines":["from django.conf.urls import url, include","from . import urls_reset","from .views import index, register, profile, logout, login"]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":37},"action":"remove","lines":["url(r'^admin/', admin.site.urls),"],"id":12}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["#"],"id":13}],[{"start":{"row":16,"column":1},"end":{"row":16,"column":2},"action":"insert","lines":[" "],"id":14}],[{"start":{"row":20,"column":4},"end":{"row":21,"column":43},"action":"insert","lines":[" url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),"],"id":15}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"remove","lines":[" "],"id":16}],[{"start":{"row":15,"column":0},"end":{"row":17,"column":58},"action":"remove","lines":["from django.conf.urls import url, include","# from . import urls_reset","from .views import index, register, profile, logout, login"],"id":17},{"start":{"row":15,"column":0},"end":{"row":16,"column":32},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin"]}],[{"start":{"row":16,"column":32},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":18}],[{"start":{"row":16,"column":32},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":19}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":42},"action":"insert","lines":["from accounts import urls as urls_accounts"],"id":20}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":28},"action":"remove","lines":["all_products,"],"id":21},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"remove","lines":[" "]}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"remove","lines":[" "],"id":22}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":[" "],"id":23}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["/"],"id":24}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"remove","lines":["/"],"id":25}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["#"],"id":26}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":21},"action":"remove","lines":["name="],"id":27}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["'"],"id":28}],[{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"remove","lines":["'"],"id":29}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"remove","lines":["#"],"id":30}],[{"start":{"row":22,"column":22},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":47},"action":"insert","lines":["url(r'^accounts/', include(urls_accounts)),"],"id":32}],[{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"insert","lines":["#"],"id":33}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"remove","lines":[" "],"id":34},{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"remove","lines":["#"]}],[{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"insert","lines":[" "],"id":35}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":20},"action":"remove","lines":[", index"],"id":36}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"remove","lines":["$"],"id":37}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["i"],"id":38},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["n"]},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["d"]},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["e"]},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"remove","lines":["s"],"id":39}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["z"],"id":40},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["."]}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["."],"id":41},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"remove","lines":["z"]}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["x"],"id":42},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["/"]}],[{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":[")"],"id":43}],[{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"remove","lines":[")"],"id":44}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["#"],"id":45}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"remove","lines":["#"],"id":46}],[{"start":{"row":22,"column":3},"end":{"row":23,"column":47},"action":"remove","lines":[" url(r'^index/'),","    url(r'^accounts/', include(urls_accounts)),"],"id":48},{"start":{"row":22,"column":3},"end":{"row":24,"column":47},"action":"insert","lines":[" url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),"]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":37},"action":"remove","lines":["    url(r'^admin/', admin.site.urls),"],"id":49},{"start":{"row":21,"column":37},"end":{"row":22,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":43},"action":"remove","lines":["    url(r'^$', all_products, name='index'),"],"id":56},{"start":{"row":21,"column":37},"end":{"row":22,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":21,"column":37},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":59},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":42},"action":"insert","lines":["url(r'^index/$', index, name='index'),"],"id":60}],[{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"remove","lines":[","],"id":61},{"start":{"row":22,"column":25},"end":{"row":22,"column":26},"action":"remove","lines":["x"]},{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"remove","lines":["e"]},{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"remove","lines":["d"]},{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"remove","lines":["n"]},{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"remove","lines":["i"]},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"remove","lines":[" "]}],[{"start":{"row":16,"column":32},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":62}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["from .views import index",""],"id":63}],[{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["h"],"id":64},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["o"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["m"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":35},"action":"remove","lines":["url(r'^index/$', name='index'),"],"id":65},{"start":{"row":24,"column":4},"end":{"row":24,"column":37},"action":"insert","lines":[" url(r'^$', index, name=\"index\"),"]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"remove","lines":[" "],"id":66}]]},"ace":{"folds":[],"scrolltop":177,"scrollleft":0,"selection":{"start":{"row":24,"column":29},"end":{"row":24,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1568752049919,"hash":"3360630a7e1c65982edbb603120c8cbebd34ff4b"}