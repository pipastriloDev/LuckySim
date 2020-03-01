import logging

class Invalid_Response(Exception):
    """g
    Holds text, status code and what was expected for use when handling the error
    """
    def __init__(self, text:str, status_code:int, expected_status_code, expected_response):
        """
        """
        self.__text = text
        self.__status_code = status_code
        self.__expected_status_code = expected_status_code
        self.__expected_response= expected_response
        
        log = logging.getLogger("Invalid_Reponse")
        message = f"Invalid Response given, we expected status code {expected_status_code} but got {status_code} "
        log.error(message)
        log.debug(text)

class Authentication_Failed(Exception):
    def __init__(self, text:str, status_code:int, expected_status_code, expected_response):
        self.__text = text
        self.__status_code = status_code
        self.__expected_status_code = expected_status_code
        self.__expected_response= expected
        log = logging.getLogger("Authentication_Failed")
        message = f"Failed to authenticate, expected status code {expected_status_code} and received {status_code}"
        message += f"/n Response text: {text} /n Expected: {expected_response}"
        if 199<status_code<299:
            log.info(message)
        else:
            log.error(message)
            #TODO: This should stop the thread/exit()
