#!/usr/bin/env python3.4
import ursgal
import importlib
import os
import sys
import pickle

class xtandem2csv_1_0_0( ursgal.UNode ):
    """xtandem2csv_1_0_0 UNode"""
    def __init__(self, *args, **kwargs):
        super(xtandem2csv_1_0_0, self).__init__(*args, **kwargs)

    def _execute( self ):
        '''
        XML result files from X!Tandem are converted to CSV

        Input file has to be a .xml

        Creates a .csv file and returns its path

        '''
        print('[ -ENGINE- ] Executing conversion ..')
        self.time_point(tag = 'execution')
        xtandem2csv_main = self.import_engine_as_python_function()
        # if self.params['output_file'].lower().endswith('.xml') is False:
        #     raise ValueError('Trying to convert a non-xml file')

        output_file = os.path.join(
                self.params['output_dir_path'],
                self.params['output_file']
            )
        input_file  = os.path.join(
                self.params['input_dir_path'],
                self.params['input_file']
            )

        xtandem2csv_main(
            input_file     = input_file,
            output_file    = output_file,
            decoy_tag      = self.params['decoy_tag'],
        )

        self.print_execution_time(tag='execution')
        return output_file
