from chembl_webresource_client.new_client import new_client

from chembl_webresource_client.new_client import new_client

molecule = new_client.molecule
mols = molecule.filter(molecule_synonyms__molecule_synonym__iexact='ASCORBIC ACID').only('molecule_structures')
print(mols[0]['molecule_structures']['standard_inchi_key'])
