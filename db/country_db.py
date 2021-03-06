from typing import Dict
from pydantic import BaseModel

class CountryInDB(BaseModel):
    id:int
    name:str

database_country_name = Dict[str, CountryInDB]
database_country = Dict[int, CountryInDB]

database_country = {
    1:CountryInDB(**{"id":1,"name":"Afghanistan"}),
    2:CountryInDB(**{"id":2,"name":"Albania"}),
    3:CountryInDB(**{"id":3,"name":"Algeria"}),
    4:CountryInDB(**{"id":4,"name":"American Samoa"}),
    5:CountryInDB(**{"id":5,"name":"Andorra"}),
    6:CountryInDB(**{"id":6,"name":"Angola"}),
    7:CountryInDB(**{"id":7,"name":"Anguilla"}),
    8:CountryInDB(**{"id":8,"name":"Antarctica"}),
    9:CountryInDB(**{"id":9,"name":"Antigua and Barbuda"}),
    10:CountryInDB(**{"id":10,"name":"Argentina"}),
    11:CountryInDB(**{"id":11,"name":"Armenia"}),
    12:CountryInDB(**{"id":12,"name":"Aruba"}),
    13:CountryInDB(**{"id":13,"name":"Australia"}),
    14:CountryInDB(**{"id":14,"name":"Austria"}),
    15:CountryInDB(**{"id":15,"name":"Azerbaijan"}),
    16:CountryInDB(**{"id":16,"name":"Bahamas"}),
    17:CountryInDB(**{"id":17,"name":"Bahrain"}),
    18:CountryInDB(**{"id":18,"name":"Bangladesh"}),
    19:CountryInDB(**{"id":19,"name":"Barbados"}),
    20:CountryInDB(**{"id":20,"name":"Belarus"}),
    21:CountryInDB(**{"id":21,"name":"Belgium"}),
    22:CountryInDB(**{"id":22,"name":"Belize"}),
    23:CountryInDB(**{"id":23,"name":"Benin"}),
    24:CountryInDB(**{"id":24,"name":"Bermuda"}),
    25:CountryInDB(**{"id":25,"name":"Bhutan"}),
    26:CountryInDB(**{"id":26,"name":"Bolivia"}),
    27:CountryInDB(**{"id":27,"name":"Bosnia and Herzegovina"}),
    28:CountryInDB(**{"id":28,"name":"Botswana"}),
    29:CountryInDB(**{"id":29,"name":"Bouvet Island"}),
    30:CountryInDB(**{"id":30,"name":"Brazil"}),
    31:CountryInDB(**{"id":31,"name":"British Indian Ocean Territory"}),
    32:CountryInDB(**{"id":32,"name":"Brunei"}),
    33:CountryInDB(**{"id":33,"name":"Bulgaria"}),
    34:CountryInDB(**{"id":34,"name":"Burkina Faso"}),
    35:CountryInDB(**{"id":35,"name":"Burundi"}),
    36:CountryInDB(**{"id":36,"name":"Cambodia"}),
    37:CountryInDB(**{"id":37,"name":"Cameroon"}),
    38:CountryInDB(**{"id":38,"name":"Canada"}),
    39:CountryInDB(**{"id":39,"name":"Cape Verde"}),
    40:CountryInDB(**{"id":40,"name":"Cayman Islands"}),
    41:CountryInDB(**{"id":41,"name":"Central African Republic"}),
    42:CountryInDB(**{"id":42,"name":"Chad"}),
    43:CountryInDB(**{"id":43,"name":"Chile"}),
    44:CountryInDB(**{"id":44,"name":"China"}),
    45:CountryInDB(**{"id":45,"name":"Christmas Island"}),
    46:CountryInDB(**{"id":46,"name":"Cocos Keeling) Islands"}),
    47:CountryInDB(**{"id":47,"name":"Colombia"}),
    48:CountryInDB(**{"id":48,"name":"Comoros"}),
    49:CountryInDB(**{"id":49,"name":"Congo"}),
    50:CountryInDB(**{"id":50,"name":"Congo"}),
    51:CountryInDB(**{"id":51,"name":"Cook Islands"}),
    52:CountryInDB(**{"id":52,"name":"Costa Rica"}),
    53:CountryInDB(**{"id":53,"name":"Côte dIvoire"}),
    54:CountryInDB(**{"id":54,"name":"Croatia"}),
    55:CountryInDB(**{"id":55,"name":"Cuba"}),
    56:CountryInDB(**{"id":56,"name":"Cyprus"}),
    57:CountryInDB(**{"id":57,"name":"Czech Republic"}),
    58:CountryInDB(**{"id":58,"name":"Denmark"}),
    59:CountryInDB(**{"id":59,"name":"Djibouti"}),
    60:CountryInDB(**{"id":60,"name":"Dominica"}),
    61:CountryInDB(**{"id":61,"name":"Dominican Republic"}),
    62:CountryInDB(**{"id":62,"name":"East Timor"}),
    63:CountryInDB(**{"id":63,"name":"Ecuador"}),
    64:CountryInDB(**{"id":64,"name":"Egypt"}),
    65:CountryInDB(**{"id":65,"name":"El Salvador"}),
    66:CountryInDB(**{"id":66,"name":"Equatorial Guinea"}),
    67:CountryInDB(**{"id":67,"name":"Eritrea"}),
    68:CountryInDB(**{"id":68,"name":"Estonia"}),
    69:CountryInDB(**{"id":69,"name":"Ethiopia"}),
    70:CountryInDB(**{"id":70,"name":"Falkland Islands"}),
    71:CountryInDB(**{"id":71,"name":"Faroe Islands"}),
    72:CountryInDB(**{"id":72,"name":"Fiji Islands"}),
    73:CountryInDB(**{"id":73,"name":"Finland"}),
    74:CountryInDB(**{"id":74,"name":"France"}),
    75:CountryInDB(**{"id":75,"name":"French Guiana"}),
    76:CountryInDB(**{"id":76,"name":"French Polynesia"}),
    77:CountryInDB(**{"id":77,"name":"French Southern territories"}),
    78:CountryInDB(**{"id":78,"name":"Gabon"}),
    79:CountryInDB(**{"id":79,"name":"Gambia"}),
    80:CountryInDB(**{"id":80,"name":"Georgia"}),
    81:CountryInDB(**{"id":81,"name":"Germany"}),
    82:CountryInDB(**{"id":82,"name":"Ghana"}),
    83:CountryInDB(**{"id":83,"name":"Gibraltar"}),
    84:CountryInDB(**{"id":84,"name":"Greece"}),
    85:CountryInDB(**{"id":85,"name":"Greenland"}),
    86:CountryInDB(**{"id":86,"name":"Grenada"}),
    87:CountryInDB(**{"id":87,"name":"Guadeloupe"}),
    88:CountryInDB(**{"id":88,"name":"Guam"}),
    89:CountryInDB(**{"id":89,"name":"Guatemala"}),
    90:CountryInDB(**{"id":90,"name":"Guinea"}),
    91:CountryInDB(**{"id":91,"name":"Guinea-Bissau"}),
    92:CountryInDB(**{"id":92,"name":"Guyana"}),
    93:CountryInDB(**{"id":93,"name":"Haiti"}),
    94:CountryInDB(**{"id":94,"name":"Heard Island and McDonald Islands"}),
    95:CountryInDB(**{"id":95,"name":"Holy See Vatican City State)"}),
    96:CountryInDB(**{"id":96,"name":"Honduras"}),
    97:CountryInDB(**{"id":97,"name":"Hong Kong"}),
    98:CountryInDB(**{"id":98,"name":"Hungary"}),
    99:CountryInDB(**{"id":99,"name":"Iceland"}),
    100:CountryInDB(**{"id":100,"name":"India"}),
    101:CountryInDB(**{"id":101,"name":"Indonesia"}),
    102:CountryInDB(**{"id":102,"name":"Iran"}),
    103:CountryInDB(**{"id":103,"name":"Iraq"}),
    104:CountryInDB(**{"id":104,"name":"Ireland"}),
    105:CountryInDB(**{"id":105,"name":"Israel"}),
    106:CountryInDB(**{"id":106,"name":"Italy"}),
    107:CountryInDB(**{"id":107,"name":"Jamaica"}),
    108:CountryInDB(**{"id":108,"name":"Japan"}),
    109:CountryInDB(**{"id":109,"name":"Jordan"}),
    110:CountryInDB(**{"id":110,"name":"Kazakstan"}),
    111:CountryInDB(**{"id":111,"name":"Kenya"}),
    112:CountryInDB(**{"id":112,"name":"Kiribati"}),
    113:CountryInDB(**{"id":113,"name":"Kuwait"}),
    114:CountryInDB(**{"id":114,"name":"Kyrgyzstan"}),
    115:CountryInDB(**{"id":115,"name":"Laos"}),
    116:CountryInDB(**{"id":116,"name":"Latvia"}),
    117:CountryInDB(**{"id":117,"name":"Lebanon"}),
    118:CountryInDB(**{"id":118,"name":"Lesotho"}),
    119:CountryInDB(**{"id":119,"name":"Liberia"}),
    120:CountryInDB(**{"id":120,"name":"Libyan Arab Jamahiriya"}),
    121:CountryInDB(**{"id":121,"name":"Liechtenstein"}),
    122:CountryInDB(**{"id":122,"name":"Lithuania"}),
    123:CountryInDB(**{"id":123,"name":"Luxembourg"}),
    124:CountryInDB(**{"id":124,"name":"Macao"}),
    125:CountryInDB(**{"id":125,"name":"Macedonia"}),
    126:CountryInDB(**{"id":126,"name":"Madagascar"}),
    127:CountryInDB(**{"id":127,"name":"Malawi"}),
    128:CountryInDB(**{"id":128,"name":"Malaysia"}),
    129:CountryInDB(**{"id":129,"name":"Maldives"}),
    130:CountryInDB(**{"id":130,"name":"Mali"}),
    131:CountryInDB(**{"id":131,"name":"Malta"}),
    132:CountryInDB(**{"id":132,"name":"Marshall Islands"}),
    133:CountryInDB(**{"id":133,"name":"Martinique"}),
    134:CountryInDB(**{"id":134,"name":"Mauritania"}),
    135:CountryInDB(**{"id":135,"name":"Mauritius"}),
    136:CountryInDB(**{"id":136,"name":"Mayotte"}),
    137:CountryInDB(**{"id":137,"name":"Mexico"}),
    138:CountryInDB(**{"id":138,"name":"Micronesia"}),
    139:CountryInDB(**{"id":139,"name":"Moldova"}),
    140:CountryInDB(**{"id":140,"name":"Monaco"}),
    141:CountryInDB(**{"id":141,"name":"Mongolia"}),
    142:CountryInDB(**{"id":142,"name":"Montserrat"}),
    143:CountryInDB(**{"id":143,"name":"Morocco"}),
    144:CountryInDB(**{"id":144,"name":"Mozambique"}),
    145:CountryInDB(**{"id":145,"name":"Myanmar"}),
    146:CountryInDB(**{"id":146,"name":"Namibia"}),
    147:CountryInDB(**{"id":147,"name":"Nauru"}),
    148:CountryInDB(**{"id":148,"name":"Nepal"}),
    149:CountryInDB(**{"id":149,"name":"Netherlands"}),
    150:CountryInDB(**{"id":150,"name":"Netherlands Antilles"}),
    151:CountryInDB(**{"id":151,"name":"New Caledonia"}),
    152:CountryInDB(**{"id":152,"name":"New Zealand"}),
    153:CountryInDB(**{"id":153,"name":"Nicaragua"}),
    154:CountryInDB(**{"id":154,"name":"Niger"}),
    155:CountryInDB(**{"id":155,"name":"Nigeria"}),
    156:CountryInDB(**{"id":156,"name":"Niue"}),
    157:CountryInDB(**{"id":157,"name":"Norfolk Island"}),
    158:CountryInDB(**{"id":158,"name":"North Korea"}),
    159:CountryInDB(**{"id":159,"name":"Northern Mariana Islands"}),
    160:CountryInDB(**{"id":160,"name":"Norway"}),
    161:CountryInDB(**{"id":161,"name":"Oman"}),
    162:CountryInDB(**{"id":162,"name":"Pakistan"}),
    163:CountryInDB(**{"id":163,"name":"Palau"}),
    164:CountryInDB(**{"id":164,"name":"Palestine"}),
    165:CountryInDB(**{"id":165,"name":"Panama"}),
    166:CountryInDB(**{"id":166,"name":"Papua New Guinea"}),
    167:CountryInDB(**{"id":167,"name":"Paraguay"}),
    168:CountryInDB(**{"id":168,"name":"Peru"}),
    169:CountryInDB(**{"id":169,"name":"Philippines"}),
    170:CountryInDB(**{"id":170,"name":"Pitcairn"}),
    171:CountryInDB(**{"id":171,"name":"Poland"}),
    172:CountryInDB(**{"id":172,"name":"Portugal"}),
    173:CountryInDB(**{"id":173,"name":"Puerto Rico"}),
    174:CountryInDB(**{"id":174,"name":"Qatar"}),
    175:CountryInDB(**{"id":175,"name":"Réunion"}),
    176:CountryInDB(**{"id":176,"name":"Romania"}),
    177:CountryInDB(**{"id":177,"name":"Russian Federation"}),
    178:CountryInDB(**{"id":178,"name":"Rwanda"}),
    179:CountryInDB(**{"id":179,"name":"Saint Helena"}),
    180:CountryInDB(**{"id":180,"name":"Saint Kitts and Nevis"}),
    181:CountryInDB(**{"id":181,"name":"Saint Lucia"}),
    182:CountryInDB(**{"id":182,"name":"Saint Pierre and Miquelon"}),
    183:CountryInDB(**{"id":183,"name":"Saint Vincent and the Grenadines"}),
    184:CountryInDB(**{"id":184,"name":"Samoa"}),
    185:CountryInDB(**{"id":185,"name":"San Marino"}),
    186:CountryInDB(**{"id":186,"name":"Sao Tome and Principe"}),
    187:CountryInDB(**{"id":187,"name":"Saudi Arabia"}),
    188:CountryInDB(**{"id":188,"name":"Senegal"}),
    189:CountryInDB(**{"id":189,"name":"Seychelles"}),
    190:CountryInDB(**{"id":190,"name":"Sierra Leone"}),
    191:CountryInDB(**{"id":191,"name":"Singapore"}),
    192:CountryInDB(**{"id":192,"name":"Slovakia"}),
    193:CountryInDB(**{"id":193,"name":"Slovenia"}),
    194:CountryInDB(**{"id":194,"name":"Solomon Islands"}),
    195:CountryInDB(**{"id":195,"name":"Somalia"}),
    196:CountryInDB(**{"id":196,"name":"South Africa"}),
    197:CountryInDB(**{"id":197,"name":"South Georgia and the South Sandwich Islands"}),
    198:CountryInDB(**{"id":198,"name":"South Korea"}),
    199:CountryInDB(**{"id":199,"name":"Spain"}),
    200:CountryInDB(**{"id":200,"name":"Sri Lanka"}),
    201:CountryInDB(**{"id":201,"name":"Sudan"}),
    202:CountryInDB(**{"id":202,"name":"Suriname"}),
    203:CountryInDB(**{"id":203,"name":"Svalbard and Jan Mayen"}),
    204:CountryInDB(**{"id":204,"name":"Swaziland"}),
    205:CountryInDB(**{"id":205,"name":"Sweden"}),
    206:CountryInDB(**{"id":206,"name":"Switzerland"}),
    207:CountryInDB(**{"id":207,"name":"Syria"}),
    208:CountryInDB(**{"id":208,"name":"Taiwan"}),
    209:CountryInDB(**{"id":209,"name":"Tajikistan"}),
    210:CountryInDB(**{"id":210,"name":"Tanzania"}),
    211:CountryInDB(**{"id":211,"name":"Thailand"}),
    212:CountryInDB(**{"id":212,"name":"Togo"}),
    213:CountryInDB(**{"id":213,"name":"Tokelau"}),
    214:CountryInDB(**{"id":214,"name":"Tonga"}),
    215:CountryInDB(**{"id":215,"name":"Trinidad and Tobago"}),
    216:CountryInDB(**{"id":216,"name":"Tunisia"}),
    217:CountryInDB(**{"id":217,"name":"Turkey"}),
    218:CountryInDB(**{"id":218,"name":"Turkmenistan"}),
    219:CountryInDB(**{"id":219,"name":"Turks and Caicos Islands"}),
    220:CountryInDB(**{"id":220,"name":"Tuvalu"}),
    221:CountryInDB(**{"id":221,"name":"Uganda"}),
    222:CountryInDB(**{"id":222,"name":"Ukraine"}),
    223:CountryInDB(**{"id":223,"name":"United Arab Emirates"}),
    224:CountryInDB(**{"id":224,"name":"United Kingdom"}),
    225:CountryInDB(**{"id":225,"name":"United States"}),
    226:CountryInDB(**{"id":226,"name":"United States Minor Outlying Islands"}),
    227:CountryInDB(**{"id":227,"name":"Uruguay"}),
    228:CountryInDB(**{"id":228,"name":"Uzbekistan"}),
    229:CountryInDB(**{"id":229,"name":"Vanuatu"}),
    230:CountryInDB(**{"id":230,"name":"Venezuela"}),
    231:CountryInDB(**{"id":231,"name":"Vietnam"}),
    232:CountryInDB(**{"id":232,"name":"Virgin Islands"}),
    233:CountryInDB(**{"id":233,"name":"Virgin Islands"}),
    234:CountryInDB(**{"id":234,"name":"Wallis and Futuna"}),
    235:CountryInDB(**{"id":235,"name":"Western Sahara"}),
    236:CountryInDB(**{"id":236,"name":"Yemen"}),
    237:CountryInDB(**{"id":237,"name":"Yugoslavia"}),
    238:CountryInDB(**{"id":238,"name":"Zambia"}),
    239:CountryInDB(**{"id":239,"name":"Zimbabwe"})
}

database_country_name = {
    "Afghanistan":CountryInDB(**{"id":1,"name":"Afghanistan"}),
    "Albania":CountryInDB(**{"id":2,"name":"Albania"}),
    "Algeria":CountryInDB(**{"id":3,"name":"Algeria"}),
    "American Samoa":CountryInDB(**{"id":4,"name":"American Samoa"}),
    "Andorra":CountryInDB(**{"id":5,"name":"Andorra"}),
    "Angola":CountryInDB(**{"id":6,"name":"Angola"}),
    "Anguilla":CountryInDB(**{"id":7,"name":"Anguilla"}),
    "Antarctica":CountryInDB(**{"id":8,"name":"Antarctica"}),
    "Antigua and Barbuda":CountryInDB(**{"id":9,"name":"Antigua and Barbuda"}),
    "Argentina":CountryInDB(**{"id":10,"name":"Argentina"}),
    "Armenia":CountryInDB(**{"id":11,"name":"Armenia"}),
    "Aruba":CountryInDB(**{"id":12,"name":"Aruba"}),
    "Australia":CountryInDB(**{"id":13,"name":"Australia"}),
    "Austria":CountryInDB(**{"id":14,"name":"Austria"}),
    "Azerbaijan":CountryInDB(**{"id":15,"name":"Azerbaijan"}),
    "Bahamas":CountryInDB(**{"id":16,"name":"Bahamas"}),
    "Bahrain":CountryInDB(**{"id":17,"name":"Bahrain"}),
    "Bangladesh":CountryInDB(**{"id":18,"name":"Bangladesh"}),
    "Barbados":CountryInDB(**{"id":19,"name":"Barbados"}),
    "Belarus":CountryInDB(**{"id":20,"name":"Belarus"}),
    "Belgium":CountryInDB(**{"id":21,"name":"Belgium"}),
    "Belize":CountryInDB(**{"id":22,"name":"Belize"}),
    "Benin":CountryInDB(**{"id":23,"name":"Benin"}),
    "Bermuda":CountryInDB(**{"id":24,"name":"Bermuda"}),
    "Bhutan":CountryInDB(**{"id":25,"name":"Bhutan"}),
    "Bolivia":CountryInDB(**{"id":26,"name":"Bolivia"}),
    "Bosnia and Herzegovina":CountryInDB(**{"id":27,"name":"Bosnia and Herzegovina"}),
    "Botswana":CountryInDB(**{"id":28,"name":"Botswana"}),
    "Bouvet Island":CountryInDB(**{"id":29,"name":"Bouvet Island"}),
    "Brazil":CountryInDB(**{"id":30,"name":"Brazil"}),
    "British Indian Ocean Territory":CountryInDB(**{"id":31,"name":"British Indian Ocean Territory"}),
    "Brunei":CountryInDB(**{"id":32,"name":"Brunei"}),
    "Bulgaria":CountryInDB(**{"id":33,"name":"Bulgaria"}),
    "Burkina Faso":CountryInDB(**{"id":34,"name":"Burkina Faso"}),
    "Burundi":CountryInDB(**{"id":35,"name":"Burundi"}),
    "Cambodia":CountryInDB(**{"id":36,"name":"Cambodia"}),
    "Cameroon":CountryInDB(**{"id":37,"name":"Cameroon"}),
    "Canada":CountryInDB(**{"id":38,"name":"Canada"}),
    "Cape Verde":CountryInDB(**{"id":39,"name":"Cape Verde"}),
    "Cayman Islands":CountryInDB(**{"id":40,"name":"Cayman Islands"}),
    "Central African Republic":CountryInDB(**{"id":41,"name":"Central African Republic"}),
    "Chad":CountryInDB(**{"id":42,"name":"Chad"}),
    "Chile":CountryInDB(**{"id":43,"name":"Chile"}),
    "China":CountryInDB(**{"id":44,"name":"China"}),
    "Christmas Island":CountryInDB(**{"id":45,"name":"Christmas Island"}),
    "Cocos Keeling) Islands":CountryInDB(**{"id":46,"name":"Cocos Keeling) Islands"}),
    "Colombia":CountryInDB(**{"id":47,"name":"Colombia"}),
    "Comoros":CountryInDB(**{"id":48,"name":"Comoros"}),
    "Congo":CountryInDB(**{"id":49,"name":"Congo"}),
    "Congo":CountryInDB(**{"id":50,"name":"Congo"}),
    "Cook Islands":CountryInDB(**{"id":51,"name":"Cook Islands"}),
    "Costa Rica":CountryInDB(**{"id":52,"name":"Costa Rica"}),
    "Côte dIvoire":CountryInDB(**{"id":53,"name":"Côte dIvoire"}),
    "Croatia":CountryInDB(**{"id":54,"name":"Croatia"}),
    "Cuba":CountryInDB(**{"id":55,"name":"Cuba"}),
    "Cyprus":CountryInDB(**{"id":56,"name":"Cyprus"}),
    "Czech Republic":CountryInDB(**{"id":57,"name":"Czech Republic"}),
    "Denmark":CountryInDB(**{"id":58,"name":"Denmark"}),
    "Djibouti":CountryInDB(**{"id":59,"name":"Djibouti"}),
    "Dominica":CountryInDB(**{"id":60,"name":"Dominica"}),
    "Dominican Republic":CountryInDB(**{"id":61,"name":"Dominican Republic"}),
    "East Timor":CountryInDB(**{"id":62,"name":"East Timor"}),
    "Ecuador":CountryInDB(**{"id":63,"name":"Ecuador"}),
    "Egypt":CountryInDB(**{"id":64,"name":"Egypt"}),
    "El Salvador":CountryInDB(**{"id":65,"name":"El Salvador"}),
    "Equatorial Guinea":CountryInDB(**{"id":66,"name":"Equatorial Guinea"}),
    "Eritrea":CountryInDB(**{"id":67,"name":"Eritrea"}),
    "Estonia":CountryInDB(**{"id":68,"name":"Estonia"}),
    "Ethiopia":CountryInDB(**{"id":69,"name":"Ethiopia"}),
    "Falkland Islands":CountryInDB(**{"id":70,"name":"Falkland Islands"}),
    "Faroe Islands":CountryInDB(**{"id":71,"name":"Faroe Islands"}),
    "Fiji Islands":CountryInDB(**{"id":72,"name":"Fiji Islands"}),
    "Finland":CountryInDB(**{"id":73,"name":"Finland"}),
    "France":CountryInDB(**{"id":74,"name":"France"}),
    "French Guiana":CountryInDB(**{"id":75,"name":"French Guiana"}),
    "French Polynesia":CountryInDB(**{"id":76,"name":"French Polynesia"}),
    "French Southern territories":CountryInDB(**{"id":77,"name":"French Southern territories"}),
    "Gabon":CountryInDB(**{"id":78,"name":"Gabon"}),
    "Gambia":CountryInDB(**{"id":79,"name":"Gambia"}),
    "Georgia":CountryInDB(**{"id":80,"name":"Georgia"}),
    "Germany":CountryInDB(**{"id":81,"name":"Germany"}),
    "Ghana":CountryInDB(**{"id":82,"name":"Ghana"}),
    "Gibraltar":CountryInDB(**{"id":83,"name":"Gibraltar"}),
    "Greece":CountryInDB(**{"id":84,"name":"Greece"}),
    "Greenland":CountryInDB(**{"id":85,"name":"Greenland"}),
    "Grenada":CountryInDB(**{"id":86,"name":"Grenada"}),
    "Guadeloupe":CountryInDB(**{"id":87,"name":"Guadeloupe"}),
    "Guam":CountryInDB(**{"id":88,"name":"Guam"}),
    "Guatemala":CountryInDB(**{"id":89,"name":"Guatemala"}),
    "Guinea":CountryInDB(**{"id":90,"name":"Guinea"}),
    "Guinea-Bissau":CountryInDB(**{"id":91,"name":"Guinea-Bissau"}),
    "Guyana":CountryInDB(**{"id":92,"name":"Guyana"}),
    "Haiti":CountryInDB(**{"id":93,"name":"Haiti"}),
    "Heard Island and McDonald Islands":CountryInDB(**{"id":94,"name":"Heard Island and McDonald Islands"}),
    "Holy See Vatican City State)":CountryInDB(**{"id":95,"name":"Holy See Vatican City State)"}),
    "Honduras":CountryInDB(**{"id":96,"name":"Honduras"}),
    "Hong Kong":CountryInDB(**{"id":97,"name":"Hong Kong"}),
    "Hungary":CountryInDB(**{"id":98,"name":"Hungary"}),
    "Iceland":CountryInDB(**{"id":99,"name":"Iceland"}),
    "India":CountryInDB(**{"id":100,"name":"India"}),
    "Indonesia":CountryInDB(**{"id":101,"name":"Indonesia"}),
    "Iran":CountryInDB(**{"id":102,"name":"Iran"}),
    "Iraq":CountryInDB(**{"id":103,"name":"Iraq"}),
    "Ireland":CountryInDB(**{"id":104,"name":"Ireland"}),
    "Israel":CountryInDB(**{"id":105,"name":"Israel"}),
    "Italy":CountryInDB(**{"id":106,"name":"Italy"}),
    "Jamaica":CountryInDB(**{"id":107,"name":"Jamaica"}),
    "Japan":CountryInDB(**{"id":108,"name":"Japan"}),
    "Jordan":CountryInDB(**{"id":109,"name":"Jordan"}),
    "Kazakstan":CountryInDB(**{"id":110,"name":"Kazakstan"}),
    "Kenya":CountryInDB(**{"id":111,"name":"Kenya"}),
    "Kiribati":CountryInDB(**{"id":112,"name":"Kiribati"}),
    "Kuwait":CountryInDB(**{"id":113,"name":"Kuwait"}),
    "Kyrgyzstan":CountryInDB(**{"id":114,"name":"Kyrgyzstan"}),
    "Laos":CountryInDB(**{"id":115,"name":"Laos"}),
    "Latvia":CountryInDB(**{"id":116,"name":"Latvia"}),
    "Lebanon":CountryInDB(**{"id":117,"name":"Lebanon"}),
    "Lesotho":CountryInDB(**{"id":118,"name":"Lesotho"}),
    "Liberia":CountryInDB(**{"id":119,"name":"Liberia"}),
    "Libyan Arab Jamahiriya":CountryInDB(**{"id":120,"name":"Libyan Arab Jamahiriya"}),
    "Liechtenstein":CountryInDB(**{"id":121,"name":"Liechtenstein"}),
    "Lithuania":CountryInDB(**{"id":122,"name":"Lithuania"}),
    "Luxembourg":CountryInDB(**{"id":123,"name":"Luxembourg"}),
    "Macao":CountryInDB(**{"id":124,"name":"Macao"}),
    "Macedonia":CountryInDB(**{"id":125,"name":"Macedonia"}),
    "Madagascar":CountryInDB(**{"id":126,"name":"Madagascar"}),
    "Malawi":CountryInDB(**{"id":127,"name":"Malawi"}),
    "Malaysia":CountryInDB(**{"id":128,"name":"Malaysia"}),
    "Maldives":CountryInDB(**{"id":129,"name":"Maldives"}),
    "Mali":CountryInDB(**{"id":130,"name":"Mali"}),
    "Malta":CountryInDB(**{"id":131,"name":"Malta"}),
    "Marshall Islands":CountryInDB(**{"id":132,"name":"Marshall Islands"}),
    "Martinique":CountryInDB(**{"id":133,"name":"Martinique"}),
    "Mauritania":CountryInDB(**{"id":134,"name":"Mauritania"}),
    "Mauritius":CountryInDB(**{"id":135,"name":"Mauritius"}),
    "Mayotte":CountryInDB(**{"id":136,"name":"Mayotte"}),
    "Mexico":CountryInDB(**{"id":137,"name":"Mexico"}),
    "Micronesia":CountryInDB(**{"id":138,"name":"Micronesia"}),
    "Moldova":CountryInDB(**{"id":139,"name":"Moldova"}),
    "Monaco":CountryInDB(**{"id":140,"name":"Monaco"}),
    "Mongolia":CountryInDB(**{"id":141,"name":"Mongolia"}),
    "Montserrat":CountryInDB(**{"id":142,"name":"Montserrat"}),
    "Morocco":CountryInDB(**{"id":143,"name":"Morocco"}),
    "Mozambique":CountryInDB(**{"id":144,"name":"Mozambique"}),
    "Myanmar":CountryInDB(**{"id":145,"name":"Myanmar"}),
    "Namibia":CountryInDB(**{"id":146,"name":"Namibia"}),
    "Nauru":CountryInDB(**{"id":147,"name":"Nauru"}),
    "Nepal":CountryInDB(**{"id":148,"name":"Nepal"}),
    "Netherlands":CountryInDB(**{"id":149,"name":"Netherlands"}),
    "Netherlands Antilles":CountryInDB(**{"id":150,"name":"Netherlands Antilles"}),
    "New Caledonia":CountryInDB(**{"id":151,"name":"New Caledonia"}),
    "New Zealand":CountryInDB(**{"id":152,"name":"New Zealand"}),
    "Nicaragua":CountryInDB(**{"id":153,"name":"Nicaragua"}),
    "Niger":CountryInDB(**{"id":154,"name":"Niger"}),
    "Nigeria":CountryInDB(**{"id":155,"name":"Nigeria"}),
    "Niue":CountryInDB(**{"id":156,"name":"Niue"}),
    "Norfolk Island":CountryInDB(**{"id":157,"name":"Norfolk Island"}),
    "North Korea":CountryInDB(**{"id":158,"name":"North Korea"}),
    "Northern Mariana Islands":CountryInDB(**{"id":159,"name":"Northern Mariana Islands"}),
    "Norway":CountryInDB(**{"id":160,"name":"Norway"}),
    "Oman":CountryInDB(**{"id":161,"name":"Oman"}),
    "Pakistan":CountryInDB(**{"id":162,"name":"Pakistan"}),
    "Palau":CountryInDB(**{"id":163,"name":"Palau"}),
    "Palestine":CountryInDB(**{"id":164,"name":"Palestine"}),
    "Panama":CountryInDB(**{"id":165,"name":"Panama"}),
    "Papua New Guinea":CountryInDB(**{"id":166,"name":"Papua New Guinea"}),
    "Paraguay":CountryInDB(**{"id":167,"name":"Paraguay"}),
    "Peru":CountryInDB(**{"id":168,"name":"Peru"}),
    "Philippines":CountryInDB(**{"id":169,"name":"Philippines"}),
    "Pitcairn":CountryInDB(**{"id":170,"name":"Pitcairn"}),
    "Poland":CountryInDB(**{"id":171,"name":"Poland"}),
    "Portugal":CountryInDB(**{"id":172,"name":"Portugal"}),
    "Puerto Rico":CountryInDB(**{"id":173,"name":"Puerto Rico"}),
    "Qatar":CountryInDB(**{"id":174,"name":"Qatar"}),
    "Réunion":CountryInDB(**{"id":175,"name":"Réunion"}),
    "Romania":CountryInDB(**{"id":176,"name":"Romania"}),
    "Russian Federation":CountryInDB(**{"id":177,"name":"Russian Federation"}),
    "Rwanda":CountryInDB(**{"id":178,"name":"Rwanda"}),
    "Saint Helena":CountryInDB(**{"id":179,"name":"Saint Helena"}),
    "Saint Kitts and Nevis":CountryInDB(**{"id":180,"name":"Saint Kitts and Nevis"}),
    "Saint Lucia":CountryInDB(**{"id":181,"name":"Saint Lucia"}),
    "Saint Pierre and Miquelon":CountryInDB(**{"id":182,"name":"Saint Pierre and Miquelon"}),
    "Saint Vincent and the Grenadines":CountryInDB(**{"id":183,"name":"Saint Vincent and the Grenadines"}),
    "Samoa":CountryInDB(**{"id":184,"name":"Samoa"}),
    "San Marino":CountryInDB(**{"id":185,"name":"San Marino"}),
    "Sao Tome and Principe":CountryInDB(**{"id":186,"name":"Sao Tome and Principe"}),
    "Saudi Arabia":CountryInDB(**{"id":187,"name":"Saudi Arabia"}),
    "Senegal":CountryInDB(**{"id":188,"name":"Senegal"}),
    "Seychelles":CountryInDB(**{"id":189,"name":"Seychelles"}),
    "Sierra Leone":CountryInDB(**{"id":190,"name":"Sierra Leone"}),
    "Singapore":CountryInDB(**{"id":191,"name":"Singapore"}),
    "Slovakia":CountryInDB(**{"id":192,"name":"Slovakia"}),
    "Slovenia":CountryInDB(**{"id":193,"name":"Slovenia"}),
    "Solomon Islands":CountryInDB(**{"id":194,"name":"Solomon Islands"}),
    "Somalia":CountryInDB(**{"id":195,"name":"Somalia"}),
    "South Africa":CountryInDB(**{"id":196,"name":"South Africa"}),
    "South Georgia and the South Sandwich Islands":CountryInDB(**{"id":197,"name":"South Georgia and the South Sandwich Islands"}),
    "South Korea":CountryInDB(**{"id":198,"name":"South Korea"}),
    "Spain":CountryInDB(**{"id":199,"name":"Spain"}),
    "Sri Lanka":CountryInDB(**{"id":200,"name":"Sri Lanka"}),
    "Sudan":CountryInDB(**{"id":201,"name":"Sudan"}),
    "Suriname":CountryInDB(**{"id":202,"name":"Suriname"}),
    "Svalbard and Jan Mayen":CountryInDB(**{"id":203,"name":"Svalbard and Jan Mayen"}),
    "Swaziland":CountryInDB(**{"id":204,"name":"Swaziland"}),
    "Sweden":CountryInDB(**{"id":205,"name":"Sweden"}),
    "Switzerland":CountryInDB(**{"id":206,"name":"Switzerland"}),
    "Syria":CountryInDB(**{"id":207,"name":"Syria"}),
    "Taiwan":CountryInDB(**{"id":208,"name":"Taiwan"}),
    "Tajikistan":CountryInDB(**{"id":209,"name":"Tajikistan"}),
    "Tanzania":CountryInDB(**{"id":210,"name":"Tanzania"}),
    "Thailand":CountryInDB(**{"id":211,"name":"Thailand"}),
    "Togo":CountryInDB(**{"id":212,"name":"Togo"}),
    "Tokelau":CountryInDB(**{"id":213,"name":"Tokelau"}),
    "Tonga":CountryInDB(**{"id":214,"name":"Tonga"}),
    "Trinidad and Tobago":CountryInDB(**{"id":215,"name":"Trinidad and Tobago"}),
    "Tunisia":CountryInDB(**{"id":216,"name":"Tunisia"}),
    "Turkey":CountryInDB(**{"id":217,"name":"Turkey"}),
    "Turkmenistan":CountryInDB(**{"id":218,"name":"Turkmenistan"}),
    "Turks and Caicos Islands":CountryInDB(**{"id":219,"name":"Turks and Caicos Islands"}),
    "Tuvalu":CountryInDB(**{"id":220,"name":"Tuvalu"}),
    "Uganda":CountryInDB(**{"id":221,"name":"Uganda"}),
    "Ukraine":CountryInDB(**{"id":222,"name":"Ukraine"}),
    "United Arab Emirates":CountryInDB(**{"id":223,"name":"United Arab Emirates"}),
    "United Kingdom":CountryInDB(**{"id":224,"name":"United Kingdom"}),
    "United States":CountryInDB(**{"id":225,"name":"United States"}),
    "United States Minor Outlying Islands":CountryInDB(**{"id":226,"name":"United States Minor Outlying Islands"}),
    "Uruguay":CountryInDB(**{"id":227,"name":"Uruguay"}),
    "Uzbekistan":CountryInDB(**{"id":228,"name":"Uzbekistan"}),
    "Vanuatu":CountryInDB(**{"id":229,"name":"Vanuatu"}),
    "Venezuela":CountryInDB(**{"id":230,"name":"Venezuela"}),
    "Vietnam":CountryInDB(**{"id":231,"name":"Vietnam"}),
    "Virgin Islands":CountryInDB(**{"id":232,"name":"Virgin Islands"}),
    "Virgin Islands":CountryInDB(**{"id":233,"name":"Virgin Islands"}),
    "Wallis and Futuna":CountryInDB(**{"id":234,"name":"Wallis and Futuna"}),
    "Western Sahara":CountryInDB(**{"id":235,"name":"Western Sahara"}),
    "Yemen":CountryInDB(**{"id":236,"name":"Yemen"}),
    "Yugoslavia":CountryInDB(**{"id":237,"name":"Yugoslavia"}),
    "Zambia":CountryInDB(**{"id":238,"name":"Zambia"}),
    "Zimbabwe":CountryInDB(**{"id":239,"name":"Zimbabwe"})
}

def get_id(name:str):
    if name in database_country_name.keys():
        return database_country_name[name]
    else:
        return None

def get_name(id:int):
    if id in database_country.keys():
        return database_country[id]
    else:
        return None

def get_list(por_id:bool):
    if por_id:
        return database_country
    else:
        return database_country_name