import yices_api as yapi


class Config(object):


    def __init__(self):
        self.config = yapi.yices_new_config()

    def default_config_for_logic(self, logicstr):
        assert self.config is not None
        yapi.yices_default_config_for_logic(self.config, logicstr)

    def set_config(self, key, value):
        assert self.config is not None
        yapi.yices_set_config(self.config, key, value)

    def dispose(self):
        yapi.yices_free_config(self.config)
        self.config = None