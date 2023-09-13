def challenge(chaine: str):

    to_be_search = {
        "cat": 0,
        "garden": 0,
        "mice": 0,
    }

    chaine = chaine.lower()

    for key in to_be_search.keys():
        
        key.lower()

        if key in chaine:
            to_be_search[key] += 1
        

    chaine = chaine[::-1]

    for key in to_be_search.keys():

        key.lower()

        if key in chaine:
            to_be_search[key] += 1

    return sum(to_be_search.values())

print(f"Challenge : {challenge('thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN')}")