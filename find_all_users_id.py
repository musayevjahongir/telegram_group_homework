from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    a=[]
    for i in data["messages"]:
        if "actor_id" in i and i["actor_id"] not in a and "channel" not in i["actor_id"]:
            a.append(i["actor_id"])
        elif "from_id" in i and i["from_id"] not in a and "channel" not in i["from_id"]:
            a.append(i["from_id"])
    return a
s=read_data("data/result.json")
print(len(find_all_users_id(s)))