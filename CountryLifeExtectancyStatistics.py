import requests
import plotly.express as px
url = f"https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=SpatialDim%20eq%20%27USA%27%20and%20TimeDimensionValue%20eq%20%272021%27%20and%20Dim1%20eq%20%27SEX_BTSX%27"

country_code_list = ['AFG','ALB','DZA','ASM','AND','AGO','AIA','ATA','ATG','ARG','ARM','ABW','AUS','AUT','AZE',
'BHS','BHR','BGD','BRB','BLR','BEL','BLZ','BEN','BMU','BTN','BOL','BES','BIH','BWA','BVT','BRA',
'IOT','BRN','BGR','BFA','BDI','CPV','KHM','CMR','CAN','CYM','CAF','TCD','CHL','CHN','CXR','CCK',
'COL','COM','COG','COD','COK','CRI','CIV','HRV','CUB','CUW','CYP','CZE','DNK','DJI','DMA','DOM',
'ECU','EGY','SLV','GNQ','ERI','EST','SWZ','ETH','FLK','FRO','FJI','FIN','FRA','GUF','PYF','ATF',
'GAB','GMB','GEO','DEU','GHA','GIB','GRC','GRL','GRD','GLP','GUM','GTM','GGY','GIN','GNB','GUY',
'HTI','HMD','VAT','HND','HKG','HUN','ISL','IND','IDN','IRN','IRQ','IRL','IMN','ISR','ITA','JAM',
'JPN','JEY','JOR','KAZ','KEN','KIR','PRK','KOR','KWT','KGZ','LAO','LVA','LBN','LSO','LBR','LBY',
'LIE','LTU','LUX','MAC','MDG','MWI','MYS','MDV','MLI','MLT','MHL','MTQ','MRT','MUS','MYT','MEX',
'FSM','MDA','MCO','MNG','MNE','MSR','MAR','MOZ','MMR','NAM','NRU','NPL','NLD','NCL','NZL','NIC',
'NER','NGA','NIU','NFK','MKD','MNP','NOR','OMN','PAK','PLW','PSE','PAN','PNG','PRY','PER','PHL',
'PCN','POL','PRT','PRI','QAT','REU','ROU','RUS','RWA','BLM','SHN','KNA','LCA','MAF','SPM','VCT',
'WSM','SMR','STP','SAU','SEN','SRB','SYC','SLE','SGP','SXM','SVK','SVN','SLB','SOM','ZAF','SGS',
'SSD','ESP','LKA','SDN','SUR','SJM','SWE','CHE','SYR','TWN','TJK','TZA','THA','TLS','TGO','TKL',
'TON','TTO','TUN','TUR','TKM','TCA','TUV','UGA','UKR','ARE','GBR','USA','UMI','URY','UZB','VUT',
'VEN','VNM','VGB','VIR','WLF','ESH','YEM','ZMB','ZWE']

data = []
for i in range(len(country_code_list)):
    country_code = country_code_list[i]
    r = requests.get(f"https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=SpatialDim eq '{country_code_list[i]}' and TimeDimensionValue eq '2021' and Dim1 eq 'SEX_BTSX'")
    json = r.json()
    if(len(json["value"] ) != 0):
        life_expectancy = json["value"][0]["NumericValue"]
        data.append((country_code, life_expectancy))

fig = px.choropleth(data, locations=0, color=1)
fig.show()
