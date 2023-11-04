from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    a=[]
    for i in data["messages"]:
        if "actor_id" in i:
            a.append(i["actor_id"])
        if "from_id" in i:
            a.append(i["from_id"])
    d={}
    for i in users_id:
        d[i]=a.count(i)
    return d
data=read_data("data/result.json")
user_id=find_all_users_id(data)
print(find_user_message_count(data, user_id))