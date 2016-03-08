#!/usr/bin/env python3.4
import ursgal
import os
import csv
import subprocess
import sys
import copy

class msamanda_1_0_0_5243( ursgal.UNode ):
    """
    MSAmanda 1_0_0_5243 UNode
    Parameter options at http://ms.imp.ac.at/inc/pd-nodes/msamanda/Manual%20MS%20Amanda%20Standalone.pdf

    Reference:
    Dorfer V, Pichler P, Stranzl T, Stadlmann J, Taus T, Winkler S, Mechtler K. (2014) MS Amanda, a universal identification algorithm optimized for high accuracy tandem mass spectra.

    """
    META_INFO = {
        'engine_type': {
            'search_engine': True,
        },
        'output_extension'          : '.csv',
        'input_types'               : ['.mgf'],
        'create_own_folder'         : True,
        'citation'                  : 'Dorfer V, Pichler P, Stranzl T, '\
            'Stadlmann J, Taus T, Winkler S, Mechtler K. (2014) MS Amanda, '\
            'a universal identification algorithm optimized for high accuracy '\
            'tandem mass spectra.',
        'include_in_git'            : None,
        'cannot_distribute'         : True,
        'in_development'            : False,
        'utranslation_style'        : 'msamanda_style_1',
        'engine': {
            'linux' : {
                '64bit' : {
                    'exe'            : 'MSAmanda.exe',
                    'url'            : '',
                    'zip_md5'        : None,
                    'additional_exe' : [],
                },
            },
            'darwin' : {
                '64bit' : {
                    'exe'            : 'MSAmanda.exe',
                    'url'            : '',
                    'zip_md5'        : None,
                    'additional_exe' : [],
                },
            },
        },
    }

    def __init__(self, *args, **kwargs):
        super(msamanda_1_0_0_5243, self).__init__(*args, **kwargs)
        if sys.platform in ['win32']:
            self.dependencies_ok = True
        else:
            try:
                proc = subprocess.Popen( ['mono', '-V'], stdout = subprocess.PIPE)
            except FileNotFoundError:
                print( '''
        ERROR: MS Amanda requires Mono 3.10.0 or newer.
        Installation: http://www.mono-project.com/download'''
                )

                self.dependencies_ok = False
        pass

    def preflight( self ):
        '''
        Formatting the command line via self.params

        Settings file is created in the output folder
        and added to self.created_tmp_files (can be deleted)

        Returns:
                self.params(dict)
        '''

        translations = self.params['_TRANSLATIONS_GROUPED_BY_TRANSLATED_KEY']
        # import pprint
        # pprint.pprint(translations)
        # pprint.pprint(self.params)
        # exit(1)

        self.params['mgf_input_file'] = os.path.join(
            self.params['input_dir_path'],
            self.params['input_file']
        )

        self.params['output_file_incl_path'] = os.path.join(
            self.params['output_dir_path'],
            self.params['output_file']
        )

        # if translations['unimod_file_incl_path']['unimod_file_incl_path'] == '' :
        self.params['unimod_file_incl_path'] = os.path.join(
            os.path.dirname(__file__),
            '..',
            'resources',
            'platform_independent',
            'arc_independent',
            'ext',
            'unimod.xml'
        )

        # building command_list !
        #
        if sys.platform in ['win32']:
            self.params['command_list'] = []
        else:
            self.params['command_list'] = ['mono']
        self.params['command_list'] += [
            self.exe,
            '{mgf_input_file}'.format(**self.params),
            '{database}'.format(**self.params),
            '{0}'.format( self.params['output_file_incl_path'] + '_settings.xml' ),
            '{output_file_incl_path}'.format(**self.params)
        ]
        self.created_tmp_files.append(self.params['output_file_incl_path'] + '_settings.xml')

        score_ions = []
        instruments_file_input = []
        for ion in [ "a", "b", "c", "x", "y", "z", "-H2O", "-NH3", "Imm", "z+1", "z+2", "INT" ]:
            if self.params[ 'score_{0}_ions'.format( ion.lower() ) ] == True:
                score_ions.append( ion )
                instruments_file_input.append('''<series>{0}</series>'''.format(ion))
        instruments_file_input.append('''</setting>''')
        instruments_file_input.append('''</instruments>''')
        self.params['score_ions'] = ', '.join( score_ions )
        self.params['instruments_file_input'] = ''.join( instruments_file_input )

        self.params['precursor_mass_tolerance'] = ( float(self.params['precursor_mass_tolerance_plus']) + \
                                                    float(self.params['precursor_mass_tolerance_minus']) ) \
                                                / 2.0

        considered_charges = []
        for charge in range( int(self.params[ 'precursor_min_charge' ]), int(self.params[ 'precursor_max_charge' ])+1 ):
            considered_charges.append( '+{0}'.format(charge) )
        self.params['considered_charges'] = ', '.join( considered_charges )

        # if self.params['semi_enzyme'] == True:
        #     self.params['semi_enzyme'] = 'Semi'
        # else:
        #     self.params['semi_enzyme'] = 'Full'

        # if self.params['precursor_mass_type'] == 'monoisotopic':
        #     self.params['monoisotopic_precursor'] = 'true'
        # else:
        #     self.params['monoisotopic_precursor'] = 'false'

        if self.params['label'] == '15N':
            for aminoacid, N15_Diff in ursgal.kb.ursgal.DICT_15N_DIFF.items():
                existing = False
                for mod in self.params[ 'mods' ][ 'fix' ]:
                    if aminoacid == mod[ 'aa' ]:
                        mod[ 'mass' ] += N15_Diff
                        mod[ 'name' ] += '_15N_{0}'.format(aminoacid)
                        existing = True
                if existing == True:
                    continue
                self.params[ 'mods' ][ 'fix' ].append( { 'pos' : 'any',
                                                         'aa'  : aminoacid,
                                                         'name': '15N_{0}'.format(aminoacid),
                                                         'mass': N15_Diff }
                                                      )
        self.params['enzyme_name'] = self.ORIGINAL_PARAMS['enzyme']
        self.params['enzyme_cleavage'], self.params['enzyme_position'], self.params['enzyme_inhibitors'] = self.params['enzyme']

        modifications = [ ]
        for t in [ 'fix', 'opt' ]:
            fix = 'false'
            if t == 'fix':
                fix = 'true'
            for mod in self.params[ 'mods' ][ t ]:
                protein = 'false'
                n_term = 'false'
                c_term = 'false'
                if '>' in mod['name']:
                    print(
                        '''
                        [ WARNING ] MS Amanda cannot deal with '>'
                        [ WARNING ] in the modification name
                        [ WARNING ] Continue without modification {0} '''.format(mod, **mod)
                        )
                    continue
                if 'Prot' in mod[ 'pos' ]:
                    protein = 'true'
                if 'N-term' in mod[ 'pos' ]:
                    n_term = 'true'
                if 'C-term' in mod[ 'pos' ]:
                    c_term = 'true'
                if '*' in mod[ 'aa' ]:
                    modifications.append( '<modification fix="{0}" protein="{1}" nterm="{2}" cterm="{3}" delta_mass="{4}">{5}</modification>'.format(
                                        fix, protein, n_term, c_term, mod[ 'mass' ], mod[ 'name' ] ))
                    continue
                modifications.append( '<modification fix="{0}" protein="{1}" nterm="{2}" cterm="{3}" delta_mass="{4}">{5}({6})</modification>'.format(
                                    fix, protein, n_term, c_term, mod[ 'mass' ], mod['name'], mod[ 'aa' ] )
                                )

        self.params['modifications'] = ''.join( modifications )

        templates = self.format_templates( )
        for file_name, content in templates.items():
            with open(
              self.params['output_file_incl_path'] + file_name,
              'w') as out:
                print(content, file=out)
                print('  wrote input file {0}'.format( file_name))
                self.created_tmp_files.append(
                    self.params['output_file_incl_path'] + file_name
                    )
        return self.params

    def postflight( self ):
        '''
        Convert .tsv result files to .csv
        '''
        self.meta_unodes['ucontroller'].verify_engine_produced_an_output_file(
            self.params['output_file_incl_path'], 'MSAmanda'
        )

        cached_msamanada_output = []
        with open(self.params['output_file_incl_path'], 'r') as result_file:
            csv_dict_reader_object = csv.DictReader(
                (row for row in result_file if not row.startswith('#')),
                delimiter = '\t'
            )
            headers = csv_dict_reader_object.fieldnames
            translated_headers = []
            for header in headers:
                translated_headers.append(
                    self.USEARCH_PARAM_VALUE_TRANSLATIONS.get(header, header)
                )
            translated_headers += [
                'Is decoy',
                'Start',
                'Stop',
                'Calc m/z'
            ]
            print('[ PARSING  ] Loading unformatted MS Amanda results ...')
            for line_dict in csv_dict_reader_object:
                cached_msamanada_output.append( line_dict )
        print('[ PARSING  ] Done')

        self.params['output_file'] = self.params['output_file'].replace(
            'tsv',
            'csv'
        )
        with open(
            os.path.join(
                self.params['output_dir_path'],
                self.params['output_file'],
            ),
            'w'
        ) as result_file:
            csv_dict_writer_object = csv.DictWriter(
                result_file,
                fieldnames = translated_headers
            )
            csv_dict_writer_object.writeheader()
            print('[ INFO  ] Writing MS Amanda results, this can take a while...')
            database = self.params['database']
            csv_write_list = []

            total_docs =len(cached_msamanada_output)

            for cache_pos, m in enumerate(cached_msamanada_output):
                tmp = {}
                for header in headers:
                    translated_header = self.USEARCH_PARAM_VALUE_TRANSLATIONS.get(header, header)
                    tmp[ translated_header ] = m[ header ]
                tmp['Sequence'] = tmp['Sequence'].upper()

                if cache_pos % 500 == 0:
                    print(
                        '[ INFO ] Processing line number:    {0}/{1}'.format(
                            cache_pos,
                            total_docs
                        ),
                        end='\r'
                    )

                dict_2_write = copy.deepcopy( tmp )
                translated_mods = []
                #N-Term(Acetyl|42.010565|fixed);M1(Oxidation|15.994915|fixed);M23(Oxidation|15.994915|fixed)
                if dict_2_write['Modifications'] != '':
                    splitted_Modifications = dict_2_write['Modifications'].split(';')
                    for mod in splitted_Modifications:

                        position_or_aa_and_pos_unimod_name, mod_mass, fixed_or_opt = mod.split('|')
                        position_or_aa_and_pos,unimod_name = position_or_aa_and_pos_unimod_name.split('(')
                        position_or_aa_and_pos = position_or_aa_and_pos.strip()
                        unimod_name = unimod_name.strip()

                        if position_or_aa_and_pos.upper() == 'N-TERM':
                            position = 0
                        else:
                            position = position_or_aa_and_pos[ 1: ]

                        translated_mods.append(
                            '{0}:{1}'.format(
                                unimod_name,
                                position
                            )
                        )

                dict_2_write['Modifications'] = ';'.join( translated_mods )

                protein_id = tmp['proteinacc_start_stop_pre_post_;']

                if ';' in protein_id:
                    protein_id_list = protein_id.split(';')
                else:
                    protein_id_list = [ protein_id ]
                for protein_id in protein_id_list:

                    returned_peptide_regex_list = self.peptide_regex(
                        self.params['database'],
                        protein_id,
                        tmp['Sequence']
                    )
                    for protein in returned_peptide_regex_list:
                        for pep_regex in protein:
                            start, stop, pre_aa, post_aa, returned_protein_id = pep_regex
                    # for start, stop, pre_aa, post_aa, returned_protein_id in returned_peptide_regex_list:
                            # dict_2_write['proteinacc_start_stop_pre_post_;'] = returned_protein_id
                            dict_2_write['Start'] = start
                            dict_2_write['Stop']  = stop

                            dict_2_write['proteinacc_start_stop_pre_post_;'] = '{0}_{1}_{2}_{3}_{4}'.format(
                                returned_protein_id,
                                start,
                                stop,
                                pre_aa,
                                post_aa
                            )

                            if self.params['decoy_tag'] in dict_2_write['proteinacc_start_stop_pre_post_;']:
                                dict_2_write['Is decoy'] = 'true'
                            else:
                                dict_2_write['Is decoy'] = 'false'
                            csv_write_list.append( dict_2_write )
            duplicity_buffer = set()
            for final_dict_2_write in csv_write_list:
                duplicity_key = (
                    final_dict_2_write['Sequence'],
                    final_dict_2_write['Modifications'],
                    final_dict_2_write['proteinacc_start_stop_pre_post_;'],
                    final_dict_2_write['Spectrum ID']
                )
                if duplicity_key not in duplicity_buffer:
                    csv_dict_writer_object.writerow( final_dict_2_write )
                    duplicity_buffer.add( duplicity_key )
        print('[ INFO  ] Writing MS Amanda results done!')
        pass


    def format_templates( self ):
        self.params['exe_dir_path'] = os.path.dirname(self.exe)

        templates = {
            '_settings.xml' : '''<?xml version="1.0" encoding="utf-8" ?>
<settings>
    <search_settings>
        <enzyme specificity="{semi_enzyme}">{enzyme}</enzyme>
        <missed_cleavages>{maximum_missed_cleavages}</missed_cleavages>
        <modifications>
            {modifications}
        </modifications>
        <instrument>{score_ions}</instrument>
        <ms1_tol unit="{precursor_mass_tolerance_unit}">{precursor_mass_tolerance}</ms1_tol>
        <ms2_tol unit="{frag_mass_tolerance_unit}">{frag_mass_tolerance}</ms2_tol>
        <max_rank>{num_match_spec}</max_rank>
        <generate_decoy>false</generate_decoy>
    </search_settings>

  <basic_settings>
    <instruments_file>{output_file_incl_path}_instrument.xml</instruments_file>
    <unimod_file>{unimod_file_incl_path}</unimod_file>
    <enzyme_file>{output_file_incl_path}_enzymes.xml</enzyme_file>
    <monoisotopic>{monoisotopic_precursor}</monoisotopic>
    <considered_charges>{considered_charges}</considered_charges>
  </basic_settings>
</settings>
'''.format(**self.params),

        '_instrument.xml' : '''<?xml version="1.0"?>
<!-- possible values are "a", "b", "c", "x", "y", "z", "H2O", "NH3", "IMM", "z+1", "z+2", "INT" (for internal fragments) -->
<instruments>
  <setting name="{score_ions}">
{instruments_file_input}
'''.format(**self.params),

        '_enzymes.xml' : '''<?xml version="1.0" encoding="utf-8" ?>
<enzymes>
  <enzyme>
    <name>{enzyme_name}</name>
    <cleavage_sites>{enzyme_cleavage}</cleavage_sites>
    <inhibitors>{enzyme_inhibitors}</inhibitors>
    <position>{enzyme_position}</position>
  </enzyme>
<enzyme>
    <name>Trypsin/P</name>
    <cleavage_sites>KR</cleavage_sites>
    <position>after</position>
  </enzyme>
  <enzyme>
    <name>LysC</name>
    <cleavage_sites>K</cleavage_sites>
    <position>after</position>
  </enzyme>
  <enzyme>
    <name>GluC</name>
    <cleavage_sites>DE</cleavage_sites>
    <position>after</position>
  </enzyme>
  <enzyme>
    <name>No-Enzyme</name>
    <cleavage_sites>X</cleavage_sites>
  </enzyme>
  <enzyme>
    <name>No-Cleavage</name>
    <cleavage_sites></cleavage_sites>
  </enzyme>
</enzymes>'''.format(**self.params),
            }
        return templates
