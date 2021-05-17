
class AutomationError(Exception):
    
    def __init__(self, *args, **kwargs):
        super(Exception, self).__init__(*args)
        AutomationError.__init__(self, *args, **kwargs)

    def __str__(self):
        return "Automation error is occurred: {0}".format(self.args)

    def __repr__(self):
        return "Automation error is occurred: {0}".format(self.__str__())
