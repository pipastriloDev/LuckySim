class WoW_Requests(object):
    """
    self.region ## eu, kr, us, tw 
    self.auth_url
    self.request_url
    self.__client_id
    
    self.__access_token
    """
    import requests
    import json
    from LuckySim_Custom_Exceptions import Invalid_Response as Invalid_Response
    from LuckySim_Custom_Exceptions import Authentication_Failed as Authentication_Failed
    def __init__(self, region:str, client_id, client_secret):
        self.region = region
        #TODO: Confirm url is correct
        if region == "cn":
            self.auth_url = "gateway.battlenet.com.cn"
            self.request_url = "gateway.battlenet.com.cn"
        else:
            self.auth_url = f"https://{region}.battle.net/oauth/token"
            self.request_url = f"https://{region}.api.blizzard.com"
        try:
            self.__authenticate(client_id, client_secret)
        except self.Invalid_Response:
            #TODO create windows security event log 
            pass

    def __authenticate(self, client_id, client_secret):
        """
        Takes client_id and client_secret and uses OAuth2 to get and set self.__access_token.
        If it fails will raise an Invalid_Response error
        Private to prevent protect access token
        """
        from LuckySim_Logging import LuckySim_Logging as LS_Logging

        curl_data = {
          'grant_type': 'client_credentials'
        } 
        auth_data = (client_id,client_secret)
        response = self.requests.post(self.auth_url, data=curl_data, auth=auth_data)
        message:str = "{client_id}: "
        if response.status_code == 200:
            message = f" Authenticated Successfully with status code {response.status_code}, saving __access_token"
            LS_Logging.write_log(message, "INFO")
            self.__access_token = self.json.loads(response.text)['access_token']
            self.__token_type = self.json.loads(response.text)['token_type']
            self.__expires_in = self.json.loads(response.text)['expires_in']
            return
        elif 499<response.status_code<600: # Server Errors 
            message = f" Authentication ran into a server error with status code {response.status_code}"
        elif 399<response.status_code<500: # Client Errors
            message = f" Authentication ran into a client error with status code {response.status_code}"
        elif 299<response.status_code<400: # Client Errors
            message = f" Authentication ran into a redirection error with status code {response.status_code}"
        elif 200<response.status_code<300: # Success Outside of norm
            ##TODO: Change message, this could leak access token currently. Potentially deal with as windows informational error, security catalog should be access protected
            message = f" Authenticated Successfully with status code {response.status_code}; /nAttempting to return token ________________________ /n{response.text} /n ________________________"
            LS_Logging.write_auth_log(message, "WARN")
            self.__access_token = self.json.loads(response.text)['access_token']
            self.__token_type = self.json.loads(response.text)['token_type']
            self.__expires_in = self.json.loads(response.text)['expires_in']
            return
        elif 99<response.status_code<200: # Informational Errors
            message = f" Authentication returned Information instead of Success with status code {response.status_code} /n{response.text}"
        
        LS_Logging.write_log(message, "ERROR")
        raise self.Invalid_Response(text=f"Please check the security Event Log, {message}", status_code = response.status_code, expected_status_code = 200, expected_response = "access token was expected as a response")
        return

    def request_data(self, url_suffix):
        #TODO: Sanitize data before return using status_codes 
        url = f"{self.request_url}{url_suffix}&access_token={self.__access_token}"
        response = self.requests.get(url)
        return response
    #https://eu.api.blizzard.com/profile/wow/character/twisting-nether/pipasstd/statistics?namespace=profile-eu&locale=en_US&access_token=US3RPuYtT3Fm5muNVF8QYGDiUzJKlLSCRl









