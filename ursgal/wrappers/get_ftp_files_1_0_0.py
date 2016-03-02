#!/usr/bin/env python3.4
import ursgal
import os

class get_ftp_files_1_0_0( ursgal.UNode ):
    """
    get_ftp_files_1_0_0 UNode

    Downloads files from FTP servers

    Args:
    def main(
        ftp_url             = None,
        folder              = None,
        login               = None,
        password            = None,
        include_ext         = None,
        output_folder       = None,
        max_number_of_files = None,
        blocksize           = None
    )
    """
    META_INFO = {
        'engine_type' : {
            'fetcher' : True,
        },
        'engine': {
            'platform_independent' : {
                'arc_independent' : {
                    'exe'     : 'get_ftp_files_1_0_0.py',
                },
            },
        },

        'input_types': '',
        'output_suffix' :  None,
        'in_development' : True,
        'include_in_git' : True,
    }

    def __init__(self, *args, **kwargs):
        super(get_ftp_files_1_0_0, self).__init__(*args, **kwargs)

    def _execute( self ):
        '''
        Downloads files from FTP server

        '''
        print('[ -ENGINE- ] Executing FTP Download ..')
        self.time_point(tag = 'execution')
        main = self.import_engine_as_python_function()
        downloaded_files = main(
            ftp_url             = self.params.get('ftp_url', None),
            folder              = self.params.get('ftp_folder', None),
            login               = self.params.get('ftp_login', None),
            password            = self.params.get('ftp_password', None),
            include_ext         = self.params.get('ftp_include_ext', None),
            output_folder       = self.params.get('ftp_output_folder', None),
            max_number_of_files = self.params.get('ftp_max_number_of_files', None),
            blocksize           = self.params.get('ftp_blocksize', None)
        )
        self.print_execution_time(tag='execution')
        self.io['output']['finfo']['dir'] =  os.path.dirname( downloaded_files[-1] )
        self.io['output']['finfo']['file'] = os.path.basename( downloaded_files[-1] )
        return
