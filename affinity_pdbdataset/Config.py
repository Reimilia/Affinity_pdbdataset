'''
This file will set up python configuration from the file instead of setting it by static text
It has advantage when the configuration needs to change rapidly.
'''
import ConfigParser
cf = ConfigParser.ConfigParser()


cf.read('CONFIG.ini')

try:
    url_PREFIX =
    sdf_PREFIX =
    RCSB_pdb_PREFIX =
    temp_data_PREFIX =
    result_PREFIX =


except:
    raise AttributeError('Some configs cannot be found in config files!')


'''
This is where we put the inner configuration, which cannot changed by user but still be considered as global setting.
'''

#This is what we want to know, but not used in this program
Sdf_Cocrystal_Identifier = "PDB ID(s) for Ligand-Target Complex"

#Thought to be the name, but not, its just some ID
Sdf_Identifier = 'BindingDB MonomerID'


# The keys need to be recorded
_Sdf_key= [Sdf_Cocrystal_Identifier,'Link to Ligand in BindingDB','Ki (nM)','IC50 (nM)','Kd (nM)','EC50 (nM)','kon (M-1-s-1)','koff (s-1)']
csv_sdf_experiment_COLUMN =['NAME']+_Sdf_key
_electype= ['A','C','d','e','HD','N','NA','OA']

# Keys for pdb record in csv files
csv_pdb_COLUMN = ['Target PDB', 'PDBtype', 'PDB_ligand_name' , 'PDB_ligand_resIndex', 'Center of Vector',
            'Rotation Degree(pi)', 'Autodockvina_affinity (kcal/mol)','Autodockvina_gauss1','Autodockvina_gauss2',
            'Autodockvina_repulsion','Autodockvina_hydrophobic','Autodockvina_Hydrogen','Resolution(A)',
            'Ligand-Protein Contact Similarity','Ligand RMSF ','PDBSequence', 'Atom_Vector']
#Complete the column name
for i in range(8):
    csv_pdb_COLUMN.append('protein_gridmaps_'+_electype[i])
for i in range(8):
    csv_pdb_COLUMN.append('ligand_gridmaps_'+_electype[i])
for i in range(8):
    csv_pdb_COLUMN.append('complex_gridmaps_'+_electype[i])

# How many columns will the output csv files have
csv_total_COLUMN= len(csv_sdf_experiment_COLUMN)+ len(csv_pdb_COLUMN)
