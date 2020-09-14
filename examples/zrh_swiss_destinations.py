#!/usr/bin/env python

import staticmaps

zurich = (47.465318, 8.551364)
destinations = [
    (28.945461, -13.605225),
    (36.6741, -4.499106),
    (41.9235991, 8.8029203),
    (52.308611, 4.763889),
    (59.651941, 17.918611),
    (37.936351, 23.944467),
    (36.898731, 30.800461),
    (41.297071, 2.078464),
    (44.818441, 20.309139),
    (52.453851, -1.748028),
    (37.2505981, 27.6643009),
    (13.681101, 100.747283),
    (19.088681, 72.867919),
    (42.364341, -71.005181),
    (50.901381, 4.484444),
    (47.436931, 19.255592),
    (39.251461, 9.054283),
    (30.121941, 31.405556),
    (49.012771, 2.55),
    (39.6018981, 19.9116993),
    (50.865911, 7.142744),
    (55.617911, 12.655972),
    (-33.964801, 18.601667),
    (37.466781, 15.0664),
    (-6.878111, 39.202625),
    (28.5661, 77.103088),
    (36.7131001, 28.7924995),
    (55.408611, 37.906111),
    (53.421331, -6.270075),
    (51.289451, 6.766775),
    (25.252771, 55.364444),
    (55.91, -3.3725),
    (40.6921, -74.168667),
    (37.014421, -7.965911),
    (41.804471, 12.250797),
    (43.809951, 11.2051),
    (32.697881, -16.774453),
    (50.026421, 8.543125),
    (28.452711, -13.863761),
    (57.6627991, 12.2798004),
    (-23.432071, -46.469511),
    (46.238061, 6.10895),
    (52.461051, 9.685078),
    (53.630381, 9.988228),
    (22.989151, -82.409086),
    (35.339711, 25.180297),
    (22.308911, 113.914603),
    (8.1131, 98.316872),
    (27.178311, 33.799436),
    (38.944531, -77.455811),
    (38.872851, 1.373117),
    (40.639751, -73.778925),
    (37.435121, 25.348103),
    (-26.139161, 28.246),
    (36.399161, 25.479333),
    (36.793331, 27.091667),
    (36.080051, -115.15225),
    (33.942531, -118.408075),
    (34.875111, 33.62485),
    (51.505271, 0.055278),
    (59.800291, 30.262503),
    (51.1481011, -0.190278),
    (51.4771, -0.461389),
    (38.781311, -9.135919),
    (46.223681, 14.457611),
    (27.931881, -15.386586),
    (46.004271, 8.910578),
    (49.626571, 6.211517),
    (40.493551, -3.566764),
    (53.353741, -2.27495),
    (23.593271, 58.284444),
    (25.79321, -80.290556),
    (35.857491, 14.4775),
    (4.191831, 73.529128),
    (48.353781, 11.786086),
    (45.630601, 8.728111),
    (-1.319161, 36.9275),
    (43.658411, 7.215872),
    (35.764721, 140.386389),
    (49.4981, 11.066897),
    (40.898661, 9.517628),
    (41.248051, -8.681389),
    (41.978601, -87.904842),
    (60.193911, 11.100361),
    (44.572161, 26.102178),
    (40.080111, 116.584556),
    (39.55361, 2.727778),
    (38.1759981, 13.0909996),
    (50.100831, 14.26),
    (42.572771, 21.035833),
    (18.567361, -68.363431),
    (31.143371, 121.805214),
    (31.606881, -8.0363),
    (36.405411, 28.086192),
    (37.618971, -122.374889),
    (1.350181, 103.994433),
    (40.5196991, 22.9708996),
    (41.961621, 21.621381),
    (43.538941, 16.297964),
    (48.689871, 9.221964),
    (38.9053991, 16.2423),
    (28.044471, -16.572489),
    (32.011381, 34.886667),
    (27.975471, -82.53325),
    (52.559681, 13.287711),
    (43.232071, 27.825106),
    (45.505271, 12.351944),
    (48.110271, 16.569722),
    (39.489311, -0.481625),
    (52.16571, 20.967122),
    (45.470551, -73.740833),
    (49.193881, -123.184444),
    (43.677221, -79.630556),
    (45.742931, 16.068778),
    (51.1246501, 13.765948),
    (40.657991, 17.939053),
    (43.305531, -2.905808),
    (41.1375071, 16.7652015),
    (46.994121, 15.444928),
    (50.0734231, 19.8052311),
    (51.4197411, 12.2201375),
    (40.8836541, 14.281466),
    (42.897311, -8.420327),
    (43.826681, 18.336065),
    (42.6912261, 23.4072643),
    (-22.8081241, -43.2497327),
    (51.131471, -114.010556),
    (44.891661, 13.923611),
    (-20.431991, 57.67663),
    (37.423471, -5.900136),
    (21.0374991, -86.8835981),
    (32.7311, -117.197312),
    (9.998231, -84.20408),
    (41.498631, 9.098223),
    (51.846641, -8.48914),
    (54.91521, 8.343056),
    (43.337221, 21.853611),
    (60.2933861, 5.2181417),
    (38.287091, -0.557381),
    (51.10481, 16.899403),
    (39.849511, -104.673856),
    (28.4313821, -81.3084374),
    (23.0344441, -81.4352778),
    (33.871111, 10.775556),
    (34.71151, 32.489105),
    (35.5401, 24.140373),
    (42.5598981, 18.2629376),
    (37.689311, 26.909909),
    (57.539341, -4.063738),
    (36.750611, -6.064535),
    (44.83101, -0.70217),
    (43.441031, 5.221569),
    (50.336011, 30.894331),
]

context = staticmaps.Context()

colors = [staticmaps.random_color() for _ in destinations]

for index, d in enumerate(destinations):
    line = staticmaps.Line([staticmaps.latlng(*zurich), staticmaps.latlng(*d)], color=colors[index])
    context.add_object(line)

for index, d in enumerate(destinations):
    marker = staticmaps.Marker(staticmaps.latlng(*d), color=colors[index], size=6)
    context.add_object(marker)

for name, provider in staticmaps.default_tile_providers.items():
    context.set_tile_provider(provider)

    svg_image = context.render_svg(800, 500)
    with open(f"{name}_zrh_swiss_destinations.svg", "w", encoding="utf-8") as f:
        svg_image.write(f, pretty=True)

    image = context.render_image(800, 500)
    image.write_to_png(f"{name}_zrh_swiss_destinations.png")
