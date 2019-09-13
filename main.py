import utils

df = utils.load_pm(verbose=1)

mapping = utils.load_mapping(df, 
                             from_column='19_MCR_DOMAIN', 
                             to_column='13_FN_FRAME',
                             verbose=1)

print(mapping['factotum'])