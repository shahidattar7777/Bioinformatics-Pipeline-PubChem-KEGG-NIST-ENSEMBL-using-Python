# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 19:52:38 2023

@author: shahi
"""

"""
We are going to start with Dr Duke's Database from Phytochem from where we have
already downloaded the database which was in the CSV format for the plants and 
the compounds that they have to offer
"""
import pandas as pd
import numpy as np
import requests


herbs = ['borage', 'basil', 'cardamom', 'fennel', 'dill', 'cumin', 'thyme', 'chervil',
         'chives', 'cinnamon', 'coriander', 'cloves', 'tarragon', 'garlic',
         'lemonbalm', 'ginseng', 'lovage', 'majoram', 'mint', 'oregano', 'parsley',
         'rosemary', 'sage', 'ginger']
herbs = pd.Series(data=herbs)

herbs = herbs.str.upper()

herb_names = pd.read_csv("C:\\Users\\shahi\\Downloads\\Duke-Source-CSV\\COMMON_NAMES.csv")

herb_names = herb_names[herb_names['CNID'].isin(herbs)]
herb_comp = pd.read_csv("C:\\Users\\shahi\\Downloads\\Duke-Source-CSV\\FARMACY_NEW.csv")

herb_summary = pd.merge(herb_names, herb_comp[['FNFNUM', 'CHEM']], left_on= 'FNFNUM',
                        right_on='FNFNUM', how = 'inner')

# ec , rn, path, cpd
url_comp = "https://rest.kegg.jp/list/compound"
page = requests.get(url_comp, stream=True)

cpd_code = []
cpd_name = []
for line in page.iter_lines():
    if line:
        line = line.decode("utf-8")
        line = str(line)
#       print(line.split("\t")[1])
        a = line.split("\t")[0]
        d =a.split(":")[1]
        d = d.strip()
        b = line.split("\t")[1]
        c = b.split(";")
        c= [x.upper() for x in c]
        for name in c:
            name=name.strip()
            cpd_name.append(name)
            cpd_code.append(d)

code=['NA' for i in range(len(herb_summary["CHEM"]))]

# for h in range(len(herb_summary["CHEM"])):
#     for i in range(len(cpd_name)):
#         if list(herb_summary["CHEM"])[h] in cpd_name[i]:
#             print("1")
#             code[h] = cpd_code[i]
#             break
    

    
    
herb_summary["CPDCODE"] = code
kegg_cpd = pd.DataFrame()

kegg_cpd["cpd_code"] = cpd_code

kegg_cpd["cpd_name"] = cpd_name




# for i in herb_summary['CHEM']:
#     i= i.upper()
#     for j in kegg_cpd["cpd_name"]:
#         j = [x.upper() for x in j]
# #        c = kegg_cpd.index[kegg_cpd["cpd_name"] == j]
#         if i in j:
#             compound_code.append(kegg_cpd["cpd_code"].iloc[kegg_cpd["cpd_name"].index(j)])

# #herb_summary["cpd_code"] = compound_code
        
chem_list = list(herb_summary["CHEM"])
name_list = list(kegg_cpd["cpd_name"])
code_list = list(kegg_cpd["cpd_code"])

for i in range(len(chem_list)):
    chem_list[i]= chem_list[i].upper()
    for j in name_list:
        j=j.upper()
        if chem_list[i] ==j:
            code[i] = code_list[name_list.index(j)]

herb_summary["code"] = code

herb_empty_cpd = herb_summary[(herb_summary.code == 'NA')]

left_out_cpd=[*set(list(herb_empty_cpd["CHEM"]))]

herb_cpd_kegg= herb_summary[(herb_summary.code != 'NA')]



# #creating a new data frame with compound codes, reactions, enzymes and pathways
# cpd_code_from_kegg = [*set(list(herb_cpd_kegg["code"]))]
# reactions = []
# enzymes = []
# reactions_for_cpd = []
# enzymes_for_reactions = []

# cpd_pathway = []
# cpd_for_pathway =[]

# for i in cpd_code_from_kegg:
#     url_reactions = "https://rest.kegg.jp/link/rn/" + i
#     page = requests.get(url_reactions, stream = True)
    
#     for line in page.iter_lines():
#         if line:
#             line=line.decode("utf-8")
#             line=str(line)
#             a = line.split("\t")[1]
#             b = a.split(":")[1]
#             reactions.append(b)
#             reactions_for_cpd.append(i)
#     url2 =  "https://rest.kegg.jp/link/path/" + i
#     page2 = requests.get(url2,  stream=True)
    
#     for line in page2.iter_lines:
#         if line:
#             line = line.decode("utf-8")
#             line = str(line)
#             a = line.split("\t")[1]
#             b = a.split(":")[1]
#             cpd_pathway.append(b)
#             cpd_for_pathway.append(i)
            
            

# distinct_reactions = [*set(list(reactions))]

# for i in distinct_reactions:
#     url_enzymes = "https://rest.kegg.jp/link/ec/" + i
#     page2 = requests.get(url_enzymes, stream = True)
#     for line in page2.iter_lines():
#         if line:
#             line=line.decode("utf-8")
#             line=str(line)
#             a = line.split("\t")[1]
#             b = a.split(":")[1]
#             enzymes.append(b)
#             enzymes_for_reactions.append(i)

# distinct_enzymes= [*set(list(enzymes))]

# enzyme_pathway=[]
# enzyme_for_pathway=[]
# for i in distinct_enzymes:
#     url_pathway = "https://rest.kegg.jp/link/path/" + i
#     page3 = requests.get(url_pathway, stream=True)
#     for line in page3.iter_lines():
#         if line:
#             line = line.decode("utf-8")
#             line=str(line)
#             a = line.split("\t")[1]
#             b = a.split(":")[1]
#             enzyme_pathway.append(b)
#             enzyme_for_pathway.append(i)





    
    
    

            
            



