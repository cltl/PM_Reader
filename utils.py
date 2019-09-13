import pandas
from collections import defaultdict, Counter
from datetime import datetime



def load_pm(path='resources/PredicateMatrix.v1.3/PredicateMatrix.v1.3.txt',
            verbose=0):
    df = pandas.read_csv(path,
                         sep='\t')
    if verbose:
        print(f'loaded predicate matrix from: {path}')
        print(f'found {len(df)} rows')
        print(f'columns: {df.columns}')
    return df


def clean_value(pm_string):
    prefix, value = pm_string.split(':')
    if value == 'NULL':
        value = None 
    return value

assert clean_value(pm_string='vn:NULL') is None
    
def load_mapping(df, from_column, to_column, verbose=0):
    """
    load mapping between columns 
    
    :param pandas.core.frame.DataFrame df: Predicate Matrix loaded as pandas dataframe
    :param str from_column: a column name
    :param str to_column: a column name
    
    :rtype: dict
    :return: value -> set of values
    """
    for column in [from_column, to_column]:
        assert column in df, f'not a valid column name: {column}'
        
    mapping = defaultdict(set)
    
    for index, row in df.iterrows():
        
        from_string = clean_value(row[from_column])
        to_string = clean_value(row[to_column])
        
        if all([from_string, to_string]):
            
            from_values = from_string.split(';')
            to_values = to_string.split(';')
            
            for from_value in from_values:
                for to_value in to_values:
                    mapping[from_value].add(to_value)
        
        if verbose:
            if index % 50000 == 0:
                print(datetime.now(), f'{index} of {len(df)}')
                
    
    if verbose:
        num_keys = len(mapping)
        num_values = Counter([len(value) for value in mapping.values()])
        print(f'found {num_keys} unique keys')
        print(f'distribution of length of mapped values')
        print(num_values)
    
    return mapping
    