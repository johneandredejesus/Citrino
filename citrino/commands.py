from collections import OrderedDict
from xmltodict import parse
from lxml.etree import fromstring
from threading import Lock


class Commad():

    def __init__(self, manager):
        
        self.__manager = manager
        self.__lock = Lock()

    def __data(self, response):

        reply = parse(response)

        for data in reply:

            if type(reply[data]) is OrderedDict:

                for value in reply[data]:

                    if type(reply[data][value]) is OrderedDict:

                        return reply[data][value]

        return OrderedDict()

    def get_config(self, filter_, source=None):

        with self.__lock:

            if self.__manager:

                if source and filter_:

                    xml = self.__manager.get_config(source=source, filter=filter_).data_xml

                    return self.__data(xml)

                elif source:

                    xml = self.__manager.get_config(source=source).data_xml

                    return self.__data(xml)

        return OrderedDict()

    def get(self, filter_):

        with self.__lock:

            if self.__manager:

                if filter_:

                    xml = self.__manager.get(filter_).data_xml

                    return self.__data(xml)

        return OrderedDict()

    def edit_config(self, config, target):

        with self.__lock:

            if self.__manager:

                self.__manager.edit_config(config=config, target=target)

                self.__manager.commit()

    def delete_config(self, target):

        with self.__lock:

            if self.__manager:

                self.__manager.delete_config(target=target)

                self.__manager.commit()

    def dispatch(self, filter_):

        with self.__lock:

            if self.__manager:

                xml = self.__manager.dispatch(fromstring(filter_)).xml

                return self.__data(xml)

    def discard_changes(self):

        with self.__lock:

            if self.__manager:

                self.__manager.discard_changes()

    def __del__(self):

        del self.__lock
        self.__manager = None
        del self
