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

# UAE (2018)
# 
population['AE-AZ'] = 
population['AE-AJ'] = 
population['AE-FU'] = 
population['AE-SH'] = 
population['AE-DU'] = 
population['AE-RK'] = 
population['AE-UQ'] = 
