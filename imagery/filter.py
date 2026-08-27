import json

included_countries = [
  'Switzerland',
  'Netherlands',
  'Latvia',
  'Austria',
  'Belgium',
  'Cyprus',
  'Czech',
  'Denmark',
  'Estonia',
  'Spain',
  'Finland',
  'Bulgaria',
  'Sweden',
  'Norway',
  'Germany',
  'France',
  'Portugal',
]
print('len included', len(included_countries))

data = {}
with open('countries.geojson') as f:
    data = json.load(f)

out_features = []
for feature in data['features']:
    for included_country in included_countries:
        if included_country in feature['properties']['name']:
            out_features.append(feature)
            break
with open('out_features.geojson', 'w') as f:
    json.dump({'type': 'FeatureCollection', 'features': out_features}, f, indent=2)