import requests

from helper.WebSocketHeader import get_header

from settings import settings

class GdsReader:
    """
    """
    def __init__(self):
        self.headers = get_header(settings.DEV)

    def get_person_from_an_guid(self, analysis_guid):

        analysis_id = self._execute_request(settings.analysis_id_endpoint.format(analysis_guid=analysis_guid))
        person_id = self._execute_request(settings.person_id_from_analysis_id_endpoint.format(analysis_id=analysis_id))

        return person_id

    def collect_parents(self, index_id):

        mother_id = None
        father_id = None

        family_id = self._execute_request(settings.family_id_endpoint.format(person_id=index_id))
        if family_id:

            family_members = self._execute_request(settings.family_members_endpoint.format(family_id=family_id))

            if family_members:
                for family_member in family_members:

                    person_status = self._execute_request(settings.person_status_endpoint.format(person_id=family_member))

                    if person_status:
                        if person_status == "Mutter":
                            mother_id = family_member
                        if person_status == "Vater":
                            father_id = family_member

        return mother_id, father_id
    
    def _execute_request(self, endpoint):

        response = requests.get(settings.gds_api_base_url + endpoint, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        return None