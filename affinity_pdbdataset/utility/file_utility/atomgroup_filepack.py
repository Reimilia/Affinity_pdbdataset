import prody as pd
import os
import re
import commands
import gzip

class atomgroup_filepack:

    instance_index = 0

    # This is critical for manage filesystems
    related_filelist={}

    # This is critical for setting the output file direction
    dump_filedir_prefix=''

    def __init__(self):
        pass

    @classmethod
    def get_num_of_instance(cls):
        cls.instance_index += 1
        return cls.instance_index

    @property
    def receptor(self):
        pass

    @receptor.setter
    def receptor(self,receptor):
        self.__receptor = receptor

    @receptor.getter
    def receptor(self):
        return self.__receptor

    @receptor.deleter
    def receptor(self):
        '''
        delete all unrelated files here
        depends on filelist or filedict
        :return:
        '''
        pass

    def prepare_autodock_receptor(self,repair_policy=None):
        '''

        :return: filename of the receptor with correct format suffix
        '''
        pass


    def prepare_autodock_ligand(self,repair_policy=None):
        '''

        :return:
        '''
        pass

    def prepare_output_file(self,format,repair_policy=None):
        '''
        Prepare a normal file
        :param format:
        :return:
        '''
        pass


    def import_atomgroup_from_file(self,filename,repair_policy=None):
        pass
