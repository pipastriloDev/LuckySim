class LuckySim_Logging(object):
    """description of class"""
    def write_log(message:str, lvl):
        import logging
        log = logging.getLogger("LuckySim_Logging")
        #TODO: remove log level debug
        #TODO: Why isn't info/debug printing?
        log.setLevel("DEBUG")
        lvl_dict = {"DEBUG": log.debug,
                    "INFO": log.info,
                    "WARN": log.warning,
                    "ERROR": log.error,
                    "CRITICAL":log.critical,
                    "EXCEPTION": log.exception
                    }
        lvl_dict[lvl](message)


