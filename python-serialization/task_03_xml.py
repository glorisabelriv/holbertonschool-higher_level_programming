#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to the given filename.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the serialized XML.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and return a Python dictionary.

    Parameters:
    filename (str): The name of the file to read the XML data from.

    Returns:
    dict: The deserialized data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {child.tag: child.text for child in root}
        return dictionary
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"Error deserializing XML: {e}")
        return None
