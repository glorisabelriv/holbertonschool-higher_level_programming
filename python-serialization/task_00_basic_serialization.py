import json
def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    Parameter:
    data (dict): The data to serialize
    filename (str): The name of the file to save the serialized data.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file to a Python dictionary.
    Parameters:
    filename (str): The name of the file to load the data from.
    
    Returns:
    dict: The deserialized data.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        return data
