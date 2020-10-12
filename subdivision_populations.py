"""
As of October 12th, 2020 (1AM), Aruba, Afghanistan, Andorra are complete.
Angola, Anguilla need statistics web pages. 
Albania and Åland Islands require further verification and data cleaning. 
"""
from subdivision_names import names

population = dict.fromkeys(names, None)

# Aruba 
# https://cbs.aw/wp/index.php/2020/06/15/quarterly-demographic-bulletin-2019-2/
population['AW-X01'] = 112269 

# Afghanistan
# https://www.nsia.gov.af:8080/wp-content/uploads/2020/05/Afghanistan-Statistical-Yearbook-2019-1st-Version.pdf
population['AF-BDG'] = 540009
population['AF-HER'] = 2095117
population['AF-BAM'] = 486928
population['AF-BAL'] = 1475649
population['AF-FYB'] = 1089228
population['AF-JOW'] = 590866
population['AF-GHO'] = 751254
population['AF-SAR'] = 609986
population['AF-FRA'] = 553058
population['AF-HEL'] = 1420682
population['AF-NIM'] = 180200
population['AF-URU'] = 428466
population['AF-KAN'] = 1368036
population['AF-ZAB'] = 377648
population['AF-GHA'] = 1338597
population['AF-KHO'] = 625473
population['AF-PIA'] = 601230
population['AF-BDS'] = 1035658
population['AF-NUR'] = 160993
population['AF-KNR'] = 490690
population['AF-KDZ'] = 1113676
population['AF-NAN'] = 1668481
population['AF-TAK'] = 1073319
population['AF-BGL'] = 995814
population['AF-KAB'] = 5029850
population['AF-KAP'] = 479875
population['AF-PAR'] = 724561
population['AF-LAG'] = 484952
population['AF-LOG'] = 426821
population['AF-SAM'] = 422859
population['AF-WAR'] = 648866
population['AF-PKA'] = 762108
population['AF-PAN'] = 167000
population['AF-DAY'] = 507610

# Angola
# official bureau of statistics page cannot be accessed with secure connection (Oct 12th, 2020) 
# population['AO-CUS'] = None

# Anguilla
# 'AI-X00', 'AI-X01~', 'AI-X02~', 'AI-X03~', 'AI-X04~', 'AI-X05~', 'AI-X06~', 'AI-X07~', 'AI-X08~', 'AI-X09~', 'AI-X10~', 'AI-X11~', 'AI-X12~', 'AI-X13~', 'AI-X14~'

# Albania (Jan 1st, 2020) 
# http://www.instat.gov.al/media/6850/population-on-1-january-2020___.pdf
population['AL-02'] = 290,697
population['AL-04'] = 289,889
population['AL-10'] = 200,007
population['AL-07'] = 75,428
population['AL-VL'] = 188,922
population['AL-06'] = 204,831
population['AL-BR'] = 122,003
population['AL-EL'] = 270,074
population['AL-GJ'] = 59,381
population['AL-DI'] = 115,857
population['AL-LE'] = 122,700
population['AL-DR'] = 906,166
# MUST EDIT: THE KEY 'AL-DR' FOR THE FINAL LINE IS WRONG. THIS MUST CORRESPOND TO Tiranë, OR 'AL-11'. 
# MUST EDIT: THE ORIGINAL DATA FILE MAINTAINS A MIX OF LETTER CODES AND NUMERIC CODES. THIS MUST BE FIXED. 

# Åland Islands (2019)
# https://www.asub.ax/en/statistics/population/size-and-structure-population
population['AX-X02~'] = 5233
population['AX-X04~'] = 952
population['AX-X06~'] = 531
population['AX-X09~'] = 11679
population['AX-X10~'] = 2053
population['AX-X11~'] = 366
population['AX-X12~'] = 447
population['AX-X13~'] = 88
population['AX-X14~'] = 314
population['AX-X15~'] = 445
population['AX-X16~'] = 232
# MUST EDIT: 

# Andorra (2019)
# https://www.estadistica.ad/serveiestudis/web/banc_dades4.asp?lang=4&codi_tema=2&codi_divisio=2162&codi_subtemes=8
population['AD-07'] = 22440
population['AD-02'] = 4325
population['AD-03'] = 11688
population['AD-08'] = 14599
population['AD-04'] = 10174
population['AD-05'] = 4942
population['AD-06'] = 9375

# UAE
# https://u.ae/en/about-the-uae/the-seven-emirates/
# MUST EDIT: 'AE-X01~', 'AE-X02~'
population['AE-AZ'] = 2908173
population['AE-AJ'] = 262186
population['AE-FU'] = 256256
population['AE-SH'] = 1171097
population['AE-DU'] = 3403906
population['AE-RK'] = 345000
population['AE-UQ'] = 49159

# Argentina (2010)
# https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-135
population['AR-Z'] = 273964
population['AR-V'] = 127205 
population['AR-J'] = 681055
population['AR-U'] = 509108
population['AR-M'] = 1738929
population['AR-Q'] = 551266
population['AR-B'] = 15625084
population['AR-L'] = 318951
population['AR-R'] = 638645
population['AR-D'] = 432310
population['AR-X'] = 3308876
population['AR-K'] = 367828
population['AR-Y'] = 673307
population['AR-F'] = 333642
population['AR-A'] = 1214441
population['AR-G'] = 874006
population['AR-T'] = 1448188
population['AR-H'] = 1055259
population['AR-P'] = 530162
population['AR-W'] = 992595
population['AR-E'] = 1235994
population['AR-S'] = 3194537
population['AR-N'] = 1101593
population['AR-C'] = 2890151

# Armenia (2019)
# https://www.armstat.am/file/article/nasel_01.10.2019.pdf
population['AM-AG'] = 124400
population['AM-AV'] = 263400
population['AM-SH'] = 230800
population['AM-TV'] = 121100
population['AM-AR'] = 256200
population['AM-GR'] = 227200
population['AM-KT'] = 251200
population['AM-LO'] = 213500
population['AM-ER'] = 1083600
population['AM-SU'] = 137400
population['AM-VD'] = 48700

# American Samoa
# 'AS-X01~',
#  'AS-X02~',
#  'AS-X03~',
#  'AS-X04~',
#  'AS-X05~',

# Antarctica
# 'AQ-X01~',
 'AQ-X02~',
  
# Australia
  'AU-X04~',
   'AU-X03~',
 'AU-X02~',
 'AU-NT',
 'AU-WA',
 'AU-ACT',
 'AU-NSW',
 'AU-SA',
 'AU-VIC',
 'AU-QLD',
 'AU-NSW',
 'AU-TAS']

# French Southern Territories 
 'TF-X01~',
 'TF-X02~',
 'TF-X1~',
 'TF-X03~',

# Antigua and Barbuda
  'AG-10',
 'AG-11',
 'AG-03',
 'AG-07',
 'AG-08',
 'AG-06',
 'AG-05',
 'AG-04',

# Austria (2019)
# http://www.statistik.at/web_en/statistics/PeopleSociety/population/population_censuses_register_based_census_register_based_labour_market_statistics/totaL_population/index.html
population['AT-8'] = 396782
population['AT-1'] = 294389
population['AT-6'] = 1246034
population['AT-2'] = 561406
population['AT-4'] = 1489365
population['AT-5'] = 557780
population['AT-7'] = 756720
population['AT-3'] = 1683800
population['AT-9'] = 1908104

# Azerbaijan
