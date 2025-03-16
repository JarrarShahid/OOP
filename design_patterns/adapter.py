import json
import xml.etree.ElementTree as ET

# Step 1: Define the Incompatible Class (XML Data Provider)
class XMLDataProvider:
    """Class that provides data in XML format."""

    def get_xml_data(self):
        """Returns a sample XML data string."""
        return """
        <data>
            <user>
                <id>1</id>
                <name>Alice</name>
                <email>alice@example.com</email>
            </user>
            <user>
                <id>2</id>
                <name>Bob</name>
                <email>bob@example.com</email>
            </user>
        </data>
        """

# Step 2: Create the Adapter
class XMLToJSONAdapter:
    """Adapter that converts XML data into JSON format."""

    def __init__(self, xml_provider: XMLDataProvider):
        self.xml_provider = xml_provider

    def get_json_data(self):
        """Converts XML data to JSON format."""
        xml_data = self.xml_provider.get_xml_data()
        root = ET.fromstring(xml_data)

        json_data = []
        for user in root.findall("user"):
            user_data = {
                "id": int(user.find("id").text),
                "name": user.find("name").text,
                "email": user.find("email").text
            }
            json_data.append(user_data)

        return json.dumps(json_data, indent=4)

# Step 3: Demonstration
if __name__ == "__main__":
    xml_provider = XMLDataProvider()
    adapter = XMLToJSONAdapter(xml_provider)

    print("Converted JSON Data:")
    print(adapter.get_json_data())
