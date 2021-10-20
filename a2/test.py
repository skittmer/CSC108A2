from typing import List

COLUMN_APPROVAL = 4

#SAMPLE_DATA_1 = [[0, 1, ['NDP', 'LIBERAL', 'GREEN', 'CPC'], [1, 4, 2, 3],
                  #[False, True, False, False]],
                 #[1, 2, ['LIBERAL', 'NDP', 'GREEN', 'CPC'], [2, 1, 4, 2],
                  #[False, False, True, True]],
                 #[1, 3, ['GREEN', 'NDP', 'CPC', 'LIBERAL'], [1, 5, 1, 2],
                  #[False, True, False, True]],
                 #[1, 4, ['CPC', 'LIBERAL', 'NDP', 'GREEN'], [5, 0, 3, 2], 
                  #[True, False, True, True]]]
##Edited =data set
SAMPLE_DATA_1 = [[0, 1, ['NDP', 'LIBERAL', 'GREEN', 'CPC'], [1, 4, 2, 3],
        [False, True, False, False]],
       [1, 2, ['LIBERAL', 'NDP', 'GREEN', 'CPC'], [2, 1, 4, 2],
        [False, False, True, True]],
       [1, 3, ['GREEN', 'NDP', 'CPC', 'LIBERAL'], [1, 5, 1, 2],
        [False, False, False, True]],
       [1, 4, ['CPC', 'LIBERAL', 'NDP', 'GREEN'], [5, 0, 3, 2], 
        [False, False, True, True]]]

gg = ['GREEN', 'GREEN', 'NDP', 'GREEN', 'CPC']
def extract_column(data: List[list], column: int) -> List:
    """Return a list containing only the elements at index column for each
    item in data.

    Precondition: each inner list has an item at position column. 

    >>> extract_column([[1, 2, 3], [4, 5, 6]], 0)
    [1, 4]
    >>> extract_column(SAMPLE_DATA_1, COLUMN_APPROVAL)
    [0] [False, True, False, False]
    """
    extract_list = []
    for item in data:
        extract_list.append(item[column])
    return extract_list    


def voting_approval(av_ballots: List[List[bool]]) -> List[int]:
    """Return the total number of approvals received for each party in 
    av_ballots. The list elements are ordered by PARTY_ORDER.

    >>> voting_approval(extract_column(SAMPLE_DATA_1, COLUMN_APPROVAL))
    [1, 2, 2, 3]
    """
    extract_list = [0, 0, 0, 0]
    total_cpc = 0
    total_green = 0
    total_liberal = 0
    total_ndp = 0    
    for vote in av_ballots:
        i = 0
        for section in vote:
            if section:
                extract_list.pop(i)
                extract_list.insert(i, extract_list[i] + 1) 
            i = i + 1
    return extract_list
   
def manipulate_list (temp_list: List[List[bool]], index_value, total_value) -> List[int]:
    """Return the updated total_value included at index index_value in the list
    temp_list
    
    >>>manipulate_list ([4, 0, 1, 0], 0, 4)
    [5, 0, 1, 0]
    """
    temp_list.pop(index_value) 
    temp_list.insert(index_value, total_value) 
    return temp_list

def voting_plurality(votes: List[str]) -> List[int]:
    """Based on the single-candidate ballots in votes, return a list with the
    totals for each party in the order specified in PARTY_ORDER.

    >>> voting_plurality(['GREEN', 'GREEN', 'NDP', 'GREEN', 'CPC'])
    [1, 3, 0, 1]
    """
    extract_list = [0, 0, 0, 0]
    total_cpc = 0
    total_green = 0
    total_liberal = 0
    total_ndp = 0
    for vote in votes:
        if vote == 'CPC':  #as to not create new lists, pop is uesed
            total_cpc = total_cpc + 1
            extract_list.insert(0, total_cpc)
        if vote == 'GREEN':
            total_green = total_green + 1
            manipulate_list(extract_list, 1, total_green)          
        if vote == 'LIBERAL':
            total_liberal = total_liberal + 1
            manipulate_list(extract_list, 2, total_liberal)      
        if vote == 'NDP':
            total_ndp = total_ndp + 1
            manipulate_list(extract_list, 3, total_ndp)  
    return extract_list