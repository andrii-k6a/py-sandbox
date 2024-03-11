import xml.etree.ElementTree as ET


def person():
    person_xml = '''
        <person>
            <name>John</name>
            <age hide="true"></age>
            <phone type="intl">+1 734 111 2233</phone>
        </person>
    '''

    person_xml_tree = ET.fromstring(person_xml)
    print('Name:', person_xml_tree.find('name').text)
    print('Hidden age:', person_xml_tree.find('age').get('hide'))


def users():
    users_service_xml = '''
        <service>
            <name>users-info</name>
            <users>
                <user internal_id="1">
                    <id>1a</id>
                    <name>Anna</name>
                </user>
                <user internal_id="2">
                    <id>2b</id>
                    <name>Alex</name>
                </user>
                <user internal_id="3">
                    <id>3c</id>
                    <name>Mary</name>
                </user>
            </users>
        </service>
    '''

    service_xml_tree = ET.fromstring(users_service_xml)
    all_user_xml_elements = service_xml_tree.findall('users/user')
    print('Users count:', len(all_user_xml_elements))

    for user_element in all_user_xml_elements:
        print('Name:', user_element.find('name').text)
        print('ID:', user_element.find('id').text)
