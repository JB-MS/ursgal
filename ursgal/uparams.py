ursgal_params = {
    '-xmx' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'mzidentml_lib_1_6_10',
            'mzidentml_lib_1_6_11',
        ],
        'default_value' : "13312m",
        'description' :  ''' Set maximum Java heap size (used RAM) ''',
        'trigger_rerun' : False,
        'ukey_translation' : {
            'msgfplus_style_1' : '-Xmx',
            'mzidentml_style_1' : '-Xmx',
        },
        'utag' : [
            'hardware_resources',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'aa_exception_dict' : {
        'available_in_unode' : [
            'unify_csv_1_0_0',
        ],
        'default_value' : {
            'J' : {
                'original_aa' : 'L',
            },
            'U' : {
                'original_aa' : 'C',
                'unimod_name' : 'Delta:S(-1)Se(1)',
                'unimod_name_with_cam' : 'SecCarbamidomethyl',
            },
        },
        'description' :  ''' Unusual aminoacids that are not accepted (e.g. by unify_csv_1_0_0), but reported by some engines. Given as a dictionary mapping on he original_aa as well as it's unimod modification name ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'unify_csv_style_1' : 'aa_exception_dict',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "dict",
    },
    'batch_size' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_140',
            'myrimatch_2_1_138',
        ],
        'default_value' : 100000,
        'description' :  ''' sets the number of sequences loaded in as a batch from the database file ''',
        'trigger_rerun' : False,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, sequence batch size',
            'myrimatch_style_1' : 'NumBatches'
        },
        'utag' : [
            'hardware_resources',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'bigger_scores_better' : {
        'available_in_unode' : [
            'percolator_2_08',
            'qvality_2_02',
        ],
        'default_value' : None,
        'description' :  ''' Defines if bigger scores are better (or the other way round), for scores that should be validated (see validation_score_field) e.g. by percolator, qvality ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'percolator_style_1' : 'bigger_scores_better',
            'qvality_style_1' : '-r',
        },
        'utag' : [
            'scoring',
            'validation',
        ],
        'uvalue_translation' : {
            'percolator_style_1' : {
                'msamanda_1_0_0_5242' : True,
                'msamanda_1_0_0_5243' : True,
                'msgfplus_v9979' : False,
                'xtandem_cyclone_2010' : True,
                'xtandem_jackhammer' : True,
                'xtandem_piledriver' : True,
                'xtandem_sledgehammer' : True,
                'xtandem_vengeance' : True,
            },
            'qvality_style_1' : {
                'msamanda_1_0_0_5242' : True,
                'msamanda_1_0_0_5243' : True,
                'msgfplus_v9979' : False,
                'xtandem_cyclone_2010' : True,
                'xtandem_jackhammer' : True,
                'xtandem_piledriver' : True,
                'xtandem_sledgehammer' : True,
                'xtandem_vengeance' : True,
            },
        },
        'uvalue_type' : "",
    },
    'cleavage_cterm_mass_change' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 17.00305,
        'description' :  ''' The mass added to the peptide C-terminus by protein cleavage ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, cleavage C-terminal mass change',
        },
        'utag' : [
            'protein',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "float",
    },
    'cleavage_nterm_mass_change' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 1.00794,
        'description' :  ''' The mass added to the peptide N-terminus bz protein cleavage ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, cleavage N-terminal mass change',
        },
        'utag' : [
            'protein',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "float",
    },
    'compensate_small_fasta' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : False,
        'description' :  ''' Compensate for very small database files. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'scoring, cyclic permutation',
        },
        'utag' : [
            'database',
        ],
        'uvalue_translation' : {
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'compress_after_post_flight' : {
        'available_in_unode' : [
        ],
        'default_value' : "False",
        'description' :  ''' Compress after post flight: True or False to .GZ  NOTE: This is old stuff, init ? ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'compress_ext_exculsion' : {
        'available_in_unode' : [
        ],
        'default_value' : [
            '.csv',
        ],
        'description' :  ''' file type excluded from compression ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'compress_output' : {
        'available_in_unode' : [
        ],
        'default_value' : "False",
        'description' :  ''' Compress output: True or False to .GZ ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'compress_raw_search_results_if_possible' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : True,
        'description' :  ''' Compress raw search result to .gz: True or False ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'compress_raw_search_results_if_possible',
        },
        'utag' : [
            'file_handling',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'cpus' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 4,
        'description' :  ''' Number of used cpus/threads ''',
        'trigger_rerun' : False,
        'ukey_translation' : {
            'msgfplus_style_1' : '-thread',
            'myrimatch_style_1' : '-cpus <integer>',
            'omssa_style_1' : '-nt',
            'xtandem_style_1' : 'spectrum, threads',
        },
        'utag' : [
            'hardware_resources',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'csv_filter_rules' : {
        'available_in_unode' : [
            'filter_csv_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' Rules are defined as list of tuples with the first tuple element as the column name/csv fieldname, the second tuple element the rule and the third tuple element the value which should be compared ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'filter_csv_style_1' : 'filter_rules',
        },
        'utag' : [
            'conversion',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "list",
    },
    'database' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : None,
        'description' :  ''' Path to database file containing protein sequences in fasta format ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'database',
            'msgfplus_style_1' : '-d',
            'myrimatch_style_1' : 'ProteinDatabase',
            'omssa_style_1' : '-d',
            'xtandem_style_1' : 'file URL',
        },
        'utag' : [
            'database',
            'input',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'database_taxonomy' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "all",
        'description' :  ''' If a taxonomy ID is specified, only the corresponding protein sequences from the fasta database are included in the search. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'taxon label',
        },
        'utag' : [
            'database',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'decoy_generation_mode' : {
        'available_in_unode' : [
            'generate_target_decoy_1_0_0',
        ],
        'default_value' : "shuffle_peptide",
        'description' :  ''' Decoy database: Creates a target decoy database based on shuffling of peptides or complete reversing the protein sequence (reverse_protein). ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'generate_target_decoy_style_1' : 'mode',
        },
        'utag' : [
            'database',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : [
            'reverse_protein',
            'shuffle_peptide',
        ],
    },
    'decoy_tag' : {
        'available_in_unode' : [
            'generate_target_decoy_1_0_0',
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'mzidentml_lib_1_6_10',
            'mzidentml_lib_1_6_11',
            'qvality_2_02',
            'xtandem2csv_1_0_0',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : "decoy_",
        'description' :  ''' decoy-specific tag to differentiate between targets and decoys ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'generate_target_decoy_style_1' : 'decoy_tag',
            'msamanda_style_1' : 'decoy_tag',
            'mzidentml_style_1' : '-decoyRegex',
            'qvality_style_1' : 'decoy_tag',
            'xtandem2csv_style_1' : 'decoy_tag',
            'myrimatch_style_1' : 'DecoyPrefix',
        },
        'utag' : [
            'database',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'del_from_params_before_json_dump' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : [
            'grouped_psms',
        ],
        'description' :  ''' List of parameters that are deleted before .json is dumped (to not overload the .json with unimportant informations) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'del_from_params_before_json_dump',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "list",
    },
    'engine_internal_decoy_generation' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : False,
        'description' :  ''' Engine creates an own decoy database. Not recommended, because a target decoy database should be generated independently from the search engine, e.g. by using the uNode generate_target_decoy_1_0_0 ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'generate_decoy',
            'msgfplus_style_1' : '-tda',
            'xtandem_style_1' : 'scoring, include reverse',
        },
        'utag' : [
            'input',
        ],
        'uvalue_translation' : {
            'msamanda_style_1' : {
                False : 'false',
                True : 'true',
            },
            'msgfplus_style_1' : {
                False : '0',
                True : '1',
            },
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'enzyme' : {
        'available_in_unode' : [
            'generate_target_decoy_1_0_0',
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "trypsin",
        'description' :  ''' Enzyme: Rule of protein cleavage
            Possible cleavages are :
                'argc'           -> '[R]|{P}'
                'aspn'           -> '[X]|[D]'
                'aspn_gluc'
                'chymotrypsin'   -> '[FMWY]|{P}'
                'chymotrypsin_p' -> '[FMWY]|[X]'
                'cnbr'           -> '[M]|{P}'
                'elastase'       -> '[AGILV]|{P}'
                'formic_acid'    -> '[D]|{P}'
                'gluc'
                'lysc'
                'lysc_p'
                'lysn'
                'no_cleavage'
                'nonspecific'
                'pepsina'
                'semi_chymotrypsin'
                'semi_gluc'
                'semi_tryptic'
                'thermolysin_p'
                'top_down'
                'trypsin'
                'trypsin_chymotrypsin
                'trypsin_cnbr'
                'trypsin_p'
                # Note not all search engines support all enzymes ! :) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'generate_target_decoy_style_1' : 'enzyme',
            'msamanda_style_1' : 'enzyme specificity',
            'msgfplus_style_1' : '-e',
            'myrimatch_style_1' : 'CleavageRules',
            'omssa_style_1' : '-e',
            'xtandem_style_1' : 'protein, cleavage site',
        },
        'utag' : [
            'database',
            'protein',
        ],
        'uvalue_translation' : {
            'generate_target_decoy_style_1' : {
                'argc' : 'R;C;P',
                'aspn' : 'D;N;',
                'chymotrypsin' : 'FMWY;C;P',
                'chymotrypsin_p' : 'FMWY;C;',
                'clostripain' : 'R;C;',
                'cnbr' : 'M;C;P',
                'elastase' : 'AGILV;C;P',
                'formic_acid' : 'D;C;P',
                'gluc' : 'DE;C;P',
                'gluc_bicarb' : 'E;C;P',
                'iodosobenzoate' : 'W;C;',
                'lysc' : 'K;C;P',
                'lysc_p' : 'K;C;',
                'lysn' : 'K;N;',
                'lysn_promisc' : 'AKRS;N;',
                'pepsina' : 'FL;C;',
                'protein_endopeptidase' : 'P;C;',
                'staph_protease' : 'E;C;',
                'trypsin' : 'KR;C;P',
                'trypsin_cnbr' : 'KRM;C;P',
                'trypsin_gluc' : 'DEKR;C;P',
                'trypsin_p' : 'KR;C;',
            },
            'msamanda_style_1' : {
                'argc' : 'R;after;P',
                'aspn' : 'D;before;',
                'chymotrypsin' : 'FMWY;after;P',
                'chymotrypsin_p' : 'FMWY;after;',
                'clostripain' : 'R;after;',
                'cnbr' : 'M;after;P',
                'elastase' : 'AGILV;after;P',
                'formic_acid' : 'D;after;P',
                'gluc' : 'DE;after;P',
                'gluc_bicarb' : 'E;after;P',
                'iodosobenzoate' : 'W;after;',
                'lysc' : 'K;after;P',
                'lysc_p' : 'K;after;',
                'lysn' : 'K;before;',
                'lysn_promisc' : 'AKRS;before;',
                'nonspecific' : ';;',
                'pepsina' : 'FL;after;',
                'protein_endopeptidase' : 'P;after;',
                'staph_protease' : 'E;after;',
                'trypsin' : 'KR;after;P',
                'trypsin_cnbr' : 'KRM;after;P',
                'trypsin_gluc' : 'DEKR;after;P',
                'trypsin_p' : 'KR;after;',
            },
            'msgfplus_style_1' : {
                'alpha_lp' : '8',
                'argc' : '6',
                'aspn' : '7',
                'chymotrypsin' : '2',
                'glutamyl_endopeptidase' : '5',
                'lysc' : '3',
                'lysn' : '4',
                'no_cleavage' : '9',
                'nonspecific' : '0',
                'trypsin' : '1',
            },
            'omssa_style_1' : {
                'argc' : '1',
                'aspn' : '12',
                'aspn_gluc' : '14',
                'chymotrypsin' : '3',
                'chymotrypsin_p' : '18',
                'cnbr' : '2',
                'formic_acid' : '4',
                'gluc' : '13',
                'lysc' : '5',
                'lysc_p' : '6',
                'lysn' : '21',
                'no_cleavage' : '11',
                'nonspecific' : '17',
                'pepsina' : '7',
                'thermolysin_p' : '22',
                'top_down' : '15',
                'trypsin' : '0',
                'trypsin_chymotrypsin' : '9',
                'trypsin_cnbr' : '8',
                'trypsin_p' : '10',
            },
            'xtandem_style_1' : {
                'argc' : '[R]|{P}',
                'aspn' : '[X]|[D]',
                'chymotrypsin' : '[FMWY]|{P}',
                'chymotrypsin_p' : '[FMWY]|[X]',
                'clostripain' : '[R]|[X]',
                'cnbr' : '[M]|{P}',
                'elastase' : '[AGILV]|{P}',
                'formic_acid' : '[D]|{P}',
                'gluc' : '[DE]|{P}',
                'gluc_bicarb' : '[E]|{P}',
                'iodosobenzoate' : '[W]|[X]',
                'lysc' : '[K]|{P}',
                'lysc_p' : '[K]|[X]',
                'lysn' : '[X]|[K]',
                'lysn_promisc' : '[X]|[AKRS]',
                'nonspecific' : '[X]|[X]',
                'pepsina' : '[FL]|[X]',
                'protein_endopeptidase' : '[P]|[X]',
                'staph_protease' : '[E]|[X]',
                'tca' : '[FMWY]|{P},[KR]|{P},[X]|[D]',
                'trypsin' : '[KR]|{P}',
                'trypsin_cnbr' : '[KR]|{P},[M]|{P}',
                'trypsin_gluc' : '[DEKR]|{P}',
                'trypsin_p' : '[RK]|[X]',
            },
            'myrimatch_style_1': {
                'trypsin' :'Trypsin/P',
                'trypsin_p'             :'Trypsin',
                'chymotrypsin'          :'Chymotrypsin',
                'lysc'                  :'Lys-C',
                'trypsin_chymotrypsin' : 'TrypChymo',
                'lysc'                 : 'Lys-C/P',
                'lysc_p'                : 'Lys-C',
                'aspn'                  : 'Asp-N',
                'pepsina'               : 'PepsinA',
                'cnbr'                  : 'CNBr',
                'formic_acid'          : 'Formic_acid',
            },
        },
        'uvalue_type' : [
            'argc',
            'aspn',
            'aspn_gluc',
            'chymotrypsin',
            'chymotrypsin_p',
            'clostripain',
            'cnbr',
            'elastase',
            'formic_acid',
            'gluc',
            'gluc_bicarb',
            'iodosobenzoate',
            'lysc',
            'lysc_p',
            'lysn',
            'lysn_promisc',
            'no_cleavage',
            'nonspecific',
            'pepsina',
            'protein_endopeptidase',
            'staph_protease',
            'tca',
            'thermolysin_p',
            'top_down',
            'trypsin',
            'trypsin_chymotrypsin',
            'trypsin_cnbr',
            'trypsin_gluc',
            'trypsin_p',
        ],
    },
    'filter_csv_converter_version' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "filter_csv_1_0_0",
        'description' :  ''' filter csv converter version: version name ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'filter_csv_converter_version',
        },
        'utag' : [
            'converter_version',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'forbidden_cterm_mods' : {
        'available_in_unode' : [
            'xtandem_vengeance',
        ],
        'default_value' : [
        ],
        'description' :  ''' List of modifications (unimod name) that are not allowed to occur at the C-terminus of a peptide, e.g. ['GG'] ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'residue, potential modification mass',
        },
        'utag' : [
            'Modifications',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "list",
    },
    'force' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "False",
        'description' :  ''' If set 'True', engines are forced to re-run although no node-related parameters have changed ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'force',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'frag_mass_tolerance' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 5,
        'description' :  ''' Mass tolerance of measured and calculated fragment ions ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'ms2_tol',
            'omssa_style_1' : '-to',
            'xtandem_style_1' : 'spectrum, fragment monoisotopic mass error',
            'myrimatch_style_1' : 'FragmentMzTolerance'
        },
        'utag' : [
            'fragment',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'frag_mass_tolerance_unit' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "ppm",
        'description' :  ''' Fragment mass tolerance unit: available in ppm (parts-per-millon), da (Dalton) or mmu (Milli mass unit) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'ms2_tol unit',
            'xtandem_style_1' : 'spectrum, fragment monoisotopic mass error units',
        },
        'utag' : [
            'fragment',
        ],
        'uvalue_translation' : {
            'msamanda_style_1' : {
                'da' : 'Da',
            },
            'xtandem_style_1' : {
                'da' : 'Daltons',
            },
        },
        'uvalue_type' : [
            'da',
            'mmu',
            'ppm',
        ],
    },
    'frag_mass_type' : {
        'available_in_unode' : [
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "monoisotopic",
        'description' :  ''' Fragment mass type: monoisotopic or average ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-tom',
            'xtandem_style_1' : 'spectrum, fragment mass type',
        },
        'utag' : [
            'fragment',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : [
            'average',
            'monoisotopic',
        ],
    },
    'frag_method' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch',
        ],
        'default_value' : "hcd",
        'description' :  ''' Used fragmentation method, e.g. collision-induced dissociation (CID), electron-capture dissociation (ECD), electron-transfer dissociation (ETD), Higher-energy C-trap dissociation (HCD) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-m',
            'myrimatch_style_1' : '-FragmentationRule<str>',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
            'msgfplus_style_1' : {
                'cid' : '1',
                'etd' : '2',
                'hcd' : '3',
            },
        },
        'uvalue_type' : [
            'cid',
            'ecd',
            'etd',
            'hcd',
        ],
    },
    'frag_min_mz' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 150,
        'description' :  ''' Minimal considered fragment ion m/z ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, minimum fragment mz',
        },
        'utag' : [
            'MS2',
            'fragment',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'ftp_blocksize' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : 1024,
        'description' :  ''' Blocksize for ftp download ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_blocksize',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_folder' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' ftp folder that should be downloaded ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_folder',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_include_ext' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' Only files with the defined file extension are downloaded with ftp download ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_include_ext',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_max_number_of_files' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' Maximum number of files that will be downloaded ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_max_number_of_files',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_output_folder' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' Default ftp download path ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_output_folder',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_password' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' ftp download password ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_password',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'ftp_url' : {
        'available_in_unode' : [
            'get_ftp_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' ftp download URL, will fail if it is not set by the user ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'ftp_url',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'header_translations' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
        ],
        'default_value' : "",
        'description' :  ''' Translate output headers into Ursgal unify_csv style headers ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'header_translations',
        },
        'utag' : [
            'conversion',
        ],
        'uvalue_translation' : {
            'msamanda_style_1' : {
                'Amanda Score' : 'Amanda:Score',
                'Charge' : 'Charge',
                'Filename' : 'Filename',
                'Modifications' : 'Modifications',
                'Protein Accessions' : 'proteinacc_start_stop_pre_post_;',
                'RT' : 'Retention Time (s)',
                'Rank' : 'Rank',
                'Scan Number' : 'Spectrum ID',
                'Sequence' : 'Sequence',
                'Title' : 'Spectrum Title',
                'Weighted Probability' : 'Amanda:Weighted Probability',
                'm/z' : 'Exp m/z',
            },
        },
        'uvalue_type' : "",
    },
    'helper_extension' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : ".u.json",
        'description' :  ''' Exension for helper files ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'helper_extension',
        },
        'utag' : [
            'file_extension',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'http_output_folder' : {
        'available_in_unode' : [
            'get_http_files_1_0_0',
        ],
        'default_value' : "None",
        'description' :  ''' Default http download path ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'http_output_folder',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'http_url' : {
        'available_in_unode' : [
            'get_http_files_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' http download URL, will fail if it is not set by the user ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'get_http_style_1' : 'http_url',
        },
        'utag' : [
            'download',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'input_file_type' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "None",
        'description' :  ''' Input file type ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, path type',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'instrument' : {
        'available_in_unode' : [
            'msgfplus_v9979',
        ],
        'default_value' : "q_exactive",
        'description' :  ''' Type of mass spectrometer (used to determine the scoring model) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-inst',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
            'msgfplus_style_1' : {
                'high_res_ltq' : '1',
                'low_res_ltq' : '0',
                'q_exactive' : '3',
                'tof' : '2',
            },
        },
        'uvalue_type' : [
            'high_res_ltq',
            'low_res_ltq',
            'q_exactive',
            'tof',
        ],
    },
    'json_extension' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : ".u.json",
        'description' :  ''' Exension for .json files ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'json_extension',
        },
        'utag' : [
            'file_extension',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'label' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "14N",
        'description' :  ''' 15N if the corresponding amino acid labeling was applied ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'label',
            'msgfplus_style_1' : 'label',
            'omssa_style_1' : '-tem / -tom',
            'xtandem_style_1' : 'protein, modified residue mass file',
        },
        'utag' : [
            'Modifications',
            'label',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : [
            '14N',
            '15N',
        ],
    },
    'log_enabled' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "False",
        'description' :  ''' Will redirect sys.stdout to the logfile, default name: ursgal.log ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'log_enabled',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'log_file_name' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "None",
        'description' :  ''' This can be used to specify a different log file path ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'log_file_name',
        },
        'utag' : [
            'file_handling',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'machine_offset_in_ppm' : {
        'available_in_unode' : [
            'mzml2mgf_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' Machine offset ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzml2mgf_style_1' : 'machine_offset_in_ppm',
        },
        'utag' : [
            'converter',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'max_mod_alternatives' : {
        'available_in_unode' : [
            'xtandem_vengeance',
        ],
        'default_value' : 6,
        'description' :  ''' Maximal number of variable modification alternatives, given as C in 2^C ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, ptm complexity',
        },
        'utag' : [
            'Modifications',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'max_num_mods' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 3,
        'description' :  ''' Maximal number of modifications per peptide ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : 'NumMods',
            'myrimatch_style_1' : 'MaxDynamicMods'
        },
        'utag' : [
            'Modifications',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'max_num_of_ions_per_series_to_search' : {
        'available_in_unode' : [
            'omssa_2_1_9',
        ],
        'default_value' : 0,
        'description' :  ''' max number of ions in each series being searched (0=all) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-sp',
        },
        'utag' : [
            'search',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'max_num_per_mod' : {
        'available_in_unode' : [
            'xtandem_vengeance',
        ],
        'default_value' : {
        },
        'description' :  ''' Maximal number of modification sites per peptide for a specific modification, given as a dictionary: {unimod_name : number} ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'residue, potential modification mass',
        },
        'utag' : [
            'Modifications',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "dict",
    },
    'max_output_e_value' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 1.0,
        'description' :  ''' Highest e-value for reported peptides ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'output, maximum valid expectation value',
        },
        'utag' : [
            'output',
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "float",
    },
     'min_output_score' : {
        'available_in_unode' : [
            'myrimatch_2_1_140',
            'myrimatch_2_1_138',
        ],
        'default_value' : 10e-08,
        'description' :  ''' Lowest score for reported peptides ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'MinResultScore',
        },
        'utag' : [
            'output',
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "float",
    },
    'max_pep_length' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch_2_1_140',
            'myrimatch_2_1_138',
            'omssa_2_1_9',
        ],
        'default_value' : 40,
        'description' :  ''' Maximal length of a peptide ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-maxLength',
            'myrimatch_style_1' : 'MaxPeptideLength',
            'omssa_style_1' : '-nox',
        },
        'utag' : [
            'peptide',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'max_pep_var' : {
        'available_in_unode' : [
            'myrimatch_2_1_140',
            'myrimatch_2_1_138',
        ],
        'default_value' : 1000000,
        'description' :  ''' Maximal peptide variants ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-maxLength',
            'myrimatch_style_1' : 'MaxPeptideVariants',
            'omssa_style_1' : '-nox',
        },
        'utag' : [
            'peptide',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'maximal_accounted_observed_peaks' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 100,
        'description' :  ''' Maximum number of peaks from a spectrum used. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : '-MaxPeakCount',
            'xtandem_style_1' : 'spectrum, total peaks',
            'myrimatch_style_1' : 'MaxPeakCount',
        },
        'utag' : [
            'MS2',
            'fragment',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'maximum_missed_cleavages' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'myrimatch_2_1_140',
            'myrimatch_2_1_138',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 2,
        'description' :  ''' Maximum number of missed cleavages per peptide ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'missed_cleavages',
            'myrimatch_style_1' : '-MaxMissedCleavages<int>',
            'omssa_style_1' : '-v',
            'xtandem_style_1' : 'scoring, maximum missed cleavage sites',
            'myrimatch_style_1' : 'MaxMissedCleavages'
        },
        'utag' : [
            'protein',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'maximum_pep_for_ident_csv' : {
        'available_in_unode' : [
        ],
        'default_value' : "0.1",
        'description' :  ''' Maximum value for PEP (posterior error probability): Threshold for identifications put in CSV-files. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'mgf_input_file' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : None,
        'description' :  ''' Path to input .mgf file ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'mgf_input_file',
            'msgfplus_style_1' : '-s',
            'xtandem_style_1' : 'spectrum, path',
        },
        'utag' : [
            'input',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'min_pep_length' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'myrimatch_2_1_140',
            'myrimatch_2_1_138',
            'omssa_2_1_9',
        ],
        'default_value' : 6,
        'description' :  ''' Minimal length of a peptide ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-minLength',
            'myrimatch_style_1' : 'MinPeptideLength',
            'omssa_style_1' : '-no',
        },
        'utag' : [
            'peptide',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'mininimal_required_matched_peaks' : {
        'available_in_unode' : [
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_140',
            'myrimatch_2_1_138',
        ],
        'default_value' : 4,
        'description' :  ''' Mimimum number of matched ions required for a peptide to be scored ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-hm',
            'xtandem_style_1' : 'scoring, minimum ion count',
            'myrimatch_style_1' : 'MinMatchedFragments'
        },
        'utag' : [
            'fragment',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'mininimal_required_observed_peaks' : {
        'available_in_unode' : [
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 5,
        'description' :  ''' Mimimum number of peaks in the spectrum to be considered. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-hs',
            'xtandem_style_1' : 'spectrum, minimum peaks',
        },
        'utag' : [
            'MS2',
            'fragment',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'modifications' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : [
            '*,opt,Prot-N-term,Acetyl',
            'M,opt,any,Oxidation',
        ],
        'description' :  ''' Modifications are given as a list of strings, each representing the modification of one amino acid. The string consists of four informations seperated by comma:

'amino acid,type,position,unimod name’

 amino acid : specify the modified amino acid as a single letter, use '*' if the amino acid is variable

 type   : specify if it is a fixed (fix) or potential (opt) modification

 position  : specify the position within the protein/peptide (Prot-N-term, Prot-C-term), use 'any' if the positon is variable

 unimod name : specify the unimod PSI-MS Name (see unimod.org)

Examples:

 [ 'M,opt,any,Oxidation' ]   - potential oxidation of Met at any position within a peptide

 [ '*,opt,Prot-N-term,Acetyl' ]  - potential acetylation of any amino acid at the N-terminus of a protein

 [ 'S,opt,any,Phospho' ]   - potential phosphorylation of Serine at any position within a peptide

 ['C,fix,any,Carbamidomethyl’, 'N,opt,any,Deamidated’, 'Q,opt,any,Deamidated’] - fixed carbamidomethylation of Cys and potential deamidation of Asn and/or Gln at any position within a peptide

Additionally, userdefined modifications can be given and are written to a userdefined_unimod.xml in ursgal/kb/ext. Userdefined modifications need to have a unique name instead of the unimod name the chemical composition needs to be given as a Hill notation on the fifth position in the string

Example:

 [ 'S,opt,any,New_mod,C2H5N1O3' ] ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'modifications',
            'msgfplus_style_1' : '-mod',
            'myrimatch_style_1' : ('DynamicMods','StaticMods')
            'omssa_style_1' : '-mv',
            'xtandem_style_1' : ('residue, modification mass', 'residue, potential modification mass', 'protein, N-terminal residue modification mass', 'protein, C-terminal residue modification mass', 'protein, C-terminal residue modification mass', 'protein, quick acetyl', 'protein, quick pyrolidone'),
        },
        'utag' : [
            'Modifications',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "list",
    },
    'msgfplus_protocol_id' : {
        'available_in_unode' : [
            'msgfplus_v9979',
        ],
        'default_value' : 0,
        'description' :  ''' MS-GF+ specific protocol identifier. Protocols are used to enable scoring parameters for enriched and/or labeled samples. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-protocol',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : [
            '0',
            '1',
            '2',
            '3',
        ],
    },
    'mzidentml_compress' : {
        'available_in_unode' : [
            'mzidentml_lib_1_6_10',
            'mzidentml_lib_1_6_11',
        ],
        'default_value' : False,
        'description' :  ''' Compress mzidentml_lib output files ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzidentml_style_1' : '-compress',
        },
        'utag' : [
            'output',
        ],
        'uvalue_translation' : {
            'mzidentml_style_1' : {
                False : 'false',
                True : 'true',
            },
        },
        'uvalue_type' : "bool",
    },
    'mzidentml_converter_version' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "mzidentml_lib_1_6_10",
        'description' :  ''' mzidentml converter version: version name ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'mzidentml_converter_version',
        },
        'utag' : [
            'converter_version',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'mzidentml_export_type' : {
        'available_in_unode' : [
            'mzidentml_lib_1_6_10',
            'mzidentml_lib_1_6_11',
        ],
        'default_value' : "exportPSMs",
        'description' :  ''' Defines which paramters shoul be exporte by mzidentml_lib ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzidentml_style_1' : '-exportType',
        },
        'utag' : [
            'output',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : [
            'exportPSMs',
            'exportProteinGroups',
            'exportProteinsOnly',
            'exportProteoAnnotator',
            'exportRepProteinPerPAGOnly',
        ],
    },
    'mzidentml_function' : {
        'available_in_unode' : [
            'mzidentml_lib_1_6_10',
            'mzidentml_lib_1_6_11',
        ],
        'default_value' : "Mzid2Csv",
        'description' :  ''' Defines the mzidentml_lib function to be used. Note: only 'Mzid2Csv' is suppoted so far ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzidentml_style_1' : 'mzidentml_function',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : [
            'AddEmpaiToMzid',
            'CreateRestrictedFASTADatabase',
            'Csv2mzid',
            'FalseDiscoveryRate',
            'InsertMetaDataFromFasta',
            'Mzid2Csv',
            'Omssa2mzid',
            'ProteoGrouper',
            'Tandem2mzid',
            'Threshold',
        ],
    },
    'mzidentml_output_fragmentation' : {
        'available_in_unode' : [
            'mzidentml_lib_1_6_10',
            'mzidentml_lib_1_6_11',
        ],
        'default_value' : False,
        'description' :  ''' Include fragmentation in mzidentml_lib output ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzidentml_style_1' : '-outputFragmentation',
        },
        'utag' : [
            'output',
        ],
        'uvalue_translation' : {
            'mzidentml_style_1' : {
                False : 'false',
                True : 'true',
            },
        },
        'uvalue_type' : "bool",
    },
    'mzidentml_verbose_output' : {
        'available_in_unode' : [
            'mzidentml_lib_1_6_10',
            'mzidentml_lib_1_6_11',
        ],
        'default_value' : False,
        'description' :  ''' Verbose mzidentml_lib output ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzidentml_style_1' : '-verboseOutput',
        },
        'utag' : [
            'output',
        ],
        'uvalue_translation' : {
            'mzidentml_style_1' : {
                False : 'false',
                True : 'true',
            },
        },
        'uvalue_type' : "bool",
    },
    'mzml2mgf_converter_version' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "mzml2mgf_1_0_0",
        'description' :  ''' mzml to mgf converter version: version name ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'mzml2mgf_converter_version',
        },
        'utag' : [
            'converter_version',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'neutral_loss_enabled' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : False,
        'description' :  ''' Neutral losses enabled for spectrum algorithm: set  True or False ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, use neutral loss window',
        },
        'utag' : [
            'MS2',
            'fragment',
        ],
        'uvalue_translation' : {
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'neutral_loss_mass' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 0,
        'description' :  ''' Sets the centre of the window for ignoring neutral molecule losses. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, neutral loss mass',
        },
        'utag' : [
            'MS2',
            'fragment',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'neutral_loss_window' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 0,
        'description' :  ''' Neutral loss window: sets the width of the window for ignoring neutral molecule losses. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, neutral loss window',
        },
        'utag' : [
            'MS2',
            'fragment',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'noise_suppression_enabled' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "False",
        'description' :  ''' used for noise suppresssion ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, use noise suppression',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'num_hits_retain_spec' : {
        'available_in_unode' : [
            'omssa_2_1_9',
        ],
        'default_value' : 30,
        'description' :  ''' Maximum number of hits retained per precursor charge state per spectrum during the search ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-hl',
        },
        'utag' : [
            'output',
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'num_match_spec' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
            'omssa_2_1_9',
        ],
        'default_value' : 10,
        'description' :  ''' Maximum number of peptide spectrum matches to report for each spectrum ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'max_rank',
            'msgfplus_style_1' : '-n',
            'myrimatch_style_1' : 'MaxResultRank',
            'omssa_style_1' : '-hc',
        },
        'utag' : [
            'output',
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'number_of_i_decimals' : {
        'available_in_unode' : [
            'mzml2mgf_1_0_0',
        ],
        'default_value' : 5,
        'description' :  ''' Number of decimals for intensity (peak) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzml2mgf_style_1' : 'number_of_i_decimals',
        },
        'utag' : [
            'converter',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'number_of_mz_decimals' : {
        'available_in_unode' : [
            'mzml2mgf_1_0_0',
        ],
        'default_value' : 5,
        'description' :  ''' Number of decimals for m/z mass ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzml2mgf_style_1' : 'number_of_mz_decimals',
        },
        'utag' : [
            'converter',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'output_add_features' : {
        'available_in_unode' : [
            'msgfplus_v9979',
        ],
        'default_value' : True,
        'description' :  ''' Number of decimals for intensity (peak) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-addFeatures',
        },
        'utag' : [
            'output',
        ],
        'uvalue_translation' : {
            'msgfplus_style_1' : {
                False : '0',
                True : '1',
            },
        },
        'uvalue_type' : "bool",
    },
    'output_file_incl_path' : {
        'available_in_unode' : [
            'generate_target_decoy_1_0_0',
            'merge_csv_1_0_0',
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'mzidentml_lib_1_6_10',
            'mzidentml_lib_1_6_11',
            'percolator_2_08',
            'qvality_2_02',
            'venndiagram_1_0_0',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : None,
        'description' :  ''' Path to output file ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'generate_target_decoy_style_1' : 'output_file',
            'merge_csv_style_1' : 'output',
            'msamanda_style_1' : 'output_file_incl_path',
            'msgfplus_style_1' : '-o',
            'mzidentml_style_1' : 'output_file_incl_path',
            'percolator_style_1' : 'output_file_incl_path',
            'qvality_style_1' : '-o',
            'venndiagram_style_1' : 'output_file',
            'xtandem_style_1' : 'output, path',
        },
        'utag' : [
            'output',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'output_file_type' : {
        'available_in_unode' : [
        ],
        'default_value' : "None",
        'description' :  ''' Output file type ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'output_mzid' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : False,
        'description' :  ''' Repot results in mzid format ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'refine',
        },
        'utag' : [
            'Output',
        ],
        'uvalue_translation' : {
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'output_suffix' : {
        'available_in_unode' : [
        ],
        'default_value' : "",
        'description' :  ''' Output suffix: string ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'precursor_isotope_range' : {
        'available_in_unode' : [
            'msgfplus_v9979',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : "0,1",
        'description' :  ''' Error range for incorrect carbon isotope parent ion assignment ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msgfplus_style_1' : '-ti',
            'xtandem_style_1' : 'spectrum, parent monoisotopic mass isotope error',
            'myrimatch_style_1' : 'MonoisotopeAdjustmentSet',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
            'xtandem_style_1' : {
                '0' : 'no',
                '0,1' : 'yes',
                '0,2' : 'yes',
            },
            'myrimatch_style_1'   : {
                '0'     : '[0,]',
                '0,1'   : '[0,1]',
                '0,1,2' : '[0,1,2]'
            },
        },
        'uvalue_type' : [
            '0',
            '0,1',
            '0,2',
        ],
    },
    'precursor_mass_tolerance_minus' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 5,
        'description' :  ''' Precursor mass tolerance: lower mass tolerance of measured and calculated parent ion M+H ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'ms1_tol',
            'msgfplus_style_1' : '-t',
            'myrimatch_style_1' : 'MonoPrecursorMzTolerance',
            'omssa_style_1' : '-te',
            'xtandem_style_1' : 'spectrum, parent monoisotopic mass error minus',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'precursor_mass_tolerance_plus' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 5,
        'description' :  ''' Precursor mass tolerance: higher mass tolerance of measured and calculated parent ion M+H ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'ms1_tol',
            'msgfplus_style_1' : '-t',
            'omssa_style_1' : '-te',
            'xtandem_style_1' : 'spectrum, parent monoisotopic mass error plus',
            'myrimatch_style_1' : 'MonoPrecursorMzTolerance'
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'precursor_mass_tolerance_unit' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : "ppm",
        'description' :  ''' Precursor mass tolerance unit: available in ppm (parts-per-millon), da (Dalton) or mmu (Milli mass unit) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'ms1_tol unit',
            'msgfplus_style_1' : '-t',
            'omssa_style_1' : '-teppm',
            'xtandem_style_1' : 'spectrum, parent monoisotopic mass error units',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
            'msamanda_style_1' : {
                'da' : 'Da',
            },
            'msgfplus_style_1' : {
                'da' : 'Da',
            },
            'xtandem_style_1' : {
                'da' : 'Daltons',
            },
            'myrimatch_style_1' : {
                'da' : 'Da'
            },
        },
        'uvalue_type' : [
            'da',
            'mmu',
            'ppm',
        ],
    },
    'precursor_mass_type' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'myrimatch_2_1_140',
            'myrimatch_2_1_138',
            'omssa_2_1_9',
        ],
        'default_value' : "monoisotopic",
        'description' :  ''' Precursor mass type: monoisotopic or average ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'monoisotopic',
            'myrimatch_style_1' : 'PrecursorMzToleranceRule',
            'omssa_style_1' : '-tem',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
            'msamanda_style_1' : {
                'average' : 'false',
                'monoisotopic' : 'true',
            },
            'omssa_style_1' : {
                'average' : '1',
                'monoisotopic' : '0',
            },
            'myrimatch_style_1' : {
                'average' : 'average',
                'monoisotopic' : 'mono',
            },
        },
        'uvalue_type' : [
            'average',
            'monoisotopic',
        ],
    },
    'precursor_max_charge' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'myrimatch',
            'omssa_2_1_9',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 5,
        'description' :  ''' Maximal accepted parent ion charge ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'considered_charges',
            'msgfplus_style_1' : '-maxCharge',
            'myrimatch_style_1' : 'NumChargeStates',
            'omssa_style_1' : '-zh',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'precursor_min_charge' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'omssa_2_1_9',
        ],
        'default_value' : 1,
        'description' :  ''' Minimal accepted parent ion charge ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'considered_charges',
            'msgfplus_style_1' : '-minCharge',
            'omssa_style_1' : '-zl',
        },
        'utag' : [
            'precursor',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'precursor_min_mass' : {
        'available_in_unode' : [
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 400,
        'description' :  ''' Minimal parent ion mass ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'MinPeptideMass',
            'xtandem_style_1' : 'spectrum, minimum parent m+h',
        },
        'utag' : [
            'Precursor',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'precursor_max_mass' : {
        'available_in_unode' : [
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 10000,
        'description' :  ''' Maximal parent ion mass ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'MaxPeptideMass',
            'xtandem_style_1' : 'spectrum, minimum parent m+h',
        },
        'utag' : [
            'Precursor',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'precursor_ppm_offset' : {
        'available_in_unode' : [
            'mzml2mgf_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' Precursor offset in ppm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzml2mgf_style_1' : 'precursor_ppm_offset',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'prefix' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : None,
        'description' :  '''  ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'prefix',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'qvality_cross_validation' : {
        'available_in_unode' : [
            'qvality_2_02',
        ],
        'default_value' : 0,
        'description' :  ''' The relative crossvalidation step size used as treshhold before ending the iterations, qvality determines step size automatically when set to 0 ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'qvality_style_1' : '-c',
        },
        'utag' : [
            'validation',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'qvality_epsilon_step' : {
        'available_in_unode' : [
            'qvality_2_02',
        ],
        'default_value' : 0,
        'description' :  ''' The relative step size used as treshhold before cross validation error is calculated, qvality determines step size automatically when set to 0 ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'qvality_style_1' : '-s',
        },
        'utag' : [
            'validation',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'qvality_number_of_bins' : {
        'available_in_unode' : [
            'qvality_2_02',
        ],
        'default_value' : 500,
        'description' :  ''' Number of bins used in qvality ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'qvality_style_1' : '-n',
        },
        'utag' : [
            'validation',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'qvality_verbose' : {
        'available_in_unode' : [
            'qvality_2_02',
        ],
        'default_value' : 2,
        'description' :  ''' Verbose qvality output (range from 0 = no processing info to 5 = all) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'qvality_style_1' : '-v',
        },
        'utag' : [
            'validation',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : [
            '1',
            '2',
            '3',
            '4',
            '5',
        ],
    },
    'raw_ident_csv_suffix' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : ".csv",
        'description' :  ''' CSV suffix of raw indentification: this is the conversion result after CSV conversion but before adding retention time ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'raw_ident_csv_suffix',
        },
        'utag' : [
            'file_extension',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'remove_temporary_files' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "False",
        'description' :  ''' Remove temporary files: True or False ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'remove_temporary_files',
        },
        'utag' : [
            'file_handling',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'rt_pickle_name' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "_ursgal_lookup.pkl",
        'description' :  ''' name of the pickle that is used to map the retention time ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'rt_pickle_name',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'scan_exclusion_list' : {
        'available_in_unode' : [
            'mzml2mgf_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' spectra rejected during mzml2mgf conversion ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzml2mgf_style_1' : 'scan_exclusion_list',
        },
        'utag' : [
            'converter',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'scan_skip_modulo_step' : {
        'available_in_unode' : [
            'mzml2mgf_1_0_0',
        ],
        'default_value' : None,
        'description' :  ''' include only the n'th spectrum during mzml2mgf conversion ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'mzml2mgf_style_1' : 'scan_skip_modulo_step',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "",
    },
    'score_-h2o_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true, ions loss of H2O are respected in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'score_-nh3_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true, ions loss of NH3 are respected in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'score_a_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true, a ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, a ions',
            'myrimatch_style_1' : 'FragmentationRule'
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
            'omssa_style_1' : {
                False : '',
                True : '0',
            },
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'score_b_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : True,
        'description' :  ''' Spectrum: if true, b ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, b ions',
            'myrimatch_style_1' : 'FragmentationRule'
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
            'omssa_style_1' : {
                False : '',
                True : '1',
            },
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'score_c_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true, c ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, c ions',
            'myrimatch_style_1' : 'FragmentationRule',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
            'omssa_style_1' : {
                False : '',
                True : '2',
            },
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'score_imm_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true, immonium ions are respected in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'score_int_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true, internal fragment ions are respect in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'score_x_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true, x ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, x ions',
            'myrimatch_style_1' : 'FragmentationRule'
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
            'omssa_style_1' : {
                False : '',
                True : '3',
            },
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'score_y_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : True,
        'description' :  ''' Spectrum: if true, y ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, y ions',
            'myrimatch_style_1' : 'FragmentationRule',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
            'omssa_style_1' : {
                False : '',
                True : '4',
            },
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'score_z+1_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true, z ion plus 1 Da mass are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'score_z+2_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true z ion plus 2 Da mass are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'score_z_ions' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : False,
        'description' :  ''' Spectrum: if true, z ions are used in algorithm ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'series',
            'omssa_style_1' : '-i',
            'xtandem_style_1' : 'scoring, z ions',
            'myrimatch_style_1' : 'FragmentationRule'
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
            'omssa_style_1' : {
                False : '',
                True : '5',
            },
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'myrimatch_class_size_multiplier' : {
        'available_in_unode' : [
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 2,
        'description' :  ''' Myrimatch ClassSizeMultiplier ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'ClassSizeMultiplier'
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'myrimatch_num_int_classes' : {
        'available_in_unode' : [
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 3,
        'description' :  ''' Myrimatch NumIntensityClasses ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'NumIntensityClasses'
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'myrimatch_prot_sampl_time' : {
        'available_in_unode' : [
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 15,
        'description' :  ''' Myrimatch ProteinSamplingTime ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'ProteinSamplingTime'
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'myrimatch_tic_cutoff' : {
        'available_in_unode' : [
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 0.98,
        'description' :  ''' Myrimatch TicCutoffPercentage ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'TicCutoffPercentage'
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "float",
    },
    'myrimatch_smart_plus_three' : {
        'available_in_unode' : [
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : True,
        'description' :  ''' Use Myrimatch UseSmartPlusThreeModel ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'UseSmartPlusThreeModel'
        },
        'utag' : [
        ],
        'uvalue_translation' : {
            'myrimatch_style_1' : {
                False : 0,
                True : 1,
            },
        },
        'uvalue_type' : "float",
    },
    'myrimatch_num_mz_fidelity_classes' : {
        'available_in_unode' : [
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : 3,
        'description' :  ''' Myrimatch NumMzFidelityClasses ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'NumMzFidelityClasses'
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'compute_xcorr' : {
        'available_in_unode' : [
            'myrimatch_2_1_138',
            'myrimatch_2_1_140',
        ],
        'default_value' : False,
        'description' :  ''' Compute xcorr ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'myrimatch_style_1' : 'ComputeXCorr'
        },
        'utag' : [
            'scoring'
        ],
        'uvalue_translation' : {
            'myrimatch_style_1' : {
                True : 1,
                False: 0,
            }
        },
        'uvalue_type' : "bool",
    },
    'search_c_terminal_ions' : {
        'available_in_unode' : [
            'omssa_2_1_9',
        ],
        'default_value' : True,
        'description' :  ''' search c terminal ions? ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-sct',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
            'omssa_style_1' : {
                False : '1',
                True : '0',
            },
        },
        'uvalue_type' : "bool",
    },
    'search_engines_create_folders' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "True",
        'description' :  ''' Create folders for search engines. True or False ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'search_engines_create_folders',
        },
        'utag' : [
            'file_handling',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'search_for_b1_ions' : {
        'available_in_unode' : [
            'omssa_2_1_9',
        ],
        'default_value' : False,
        'description' :  ''' should first forward (b1) product ions be in search (1=no) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'omssa_style_1' : '-sb1',
        },
        'utag' : [
            'scoring',
        ],
        'uvalue_translation' : {
            'omssa_style_1' : {
                False : '1',
                True : '0',
            },
        },
        'uvalue_type' : "bool",
    },
    'search_for_saps' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : False,
        'description' :  ''' Search for potential single amino acid polymorphisms. 'True' might cause problems in the downstream processing of th result files (unify_csv, ...) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, saps',
        },
        'utag' : [
            'protein',
        ],
        'uvalue_translation' : {
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'semi_enzyme' : {
        'available_in_unode' : [
            'msamanda_1_0_0_5242',
            'msamanda_1_0_0_5243',
            'msgfplus_v9979',
            'myrimatch_2_1_140',
            'myrimatch_2_1_138',
            'omssa_2_1_9',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : False,
        'description' :  ''' Allows semi-enzymatic peptide ends ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'msamanda_style_1' : 'enzyme specificity',
            'msgfplus_style_1' : '-ntt',
            'myrimatch_style_1' : 'MinTerminiCleavages',
            'omssa_style_1' : 'semi_enzyme',
            'xtandem_style_1' : 'protein, cleavage semi',
        },
        'utag' : [
            'protein',
        ],
        'uvalue_translation' : {
            'msamanda_style_1' : {
                False : 'Full',
                True : 'Semi',
            },
            'msgfplus_style_1' : {
                False : 2,
                True : 1,
            },
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
            'myrimatch_style_1' : {
                False : 2,
                True : 1,
            }
        },
        'uvalue_type' : "bool",
    },
    'show_unodes_in_development' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "False",
        'description' :  ''' Show ursgal nodes that are in development: False or True ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'show_unodes_in_development',
        },
        'utag' : [
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'spec_dynamic_range' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : 100,
        'description' :  ''' Internal normalization for MS/MS spectrum: The highest peak (intensity) within a spectrum is set to given value and all other peaks are normalized to this peak. If the normalized value is less than 1 the peak is rejected. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'spectrum, dynamic range',
        },
        'utag' : [
            'MS2',
            'fragment',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "int",
    },
    'unify_csv_converter_version' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "unify_csv_1_0_0",
        'description' :  ''' unify csv converter version: version name ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'unify_csv_converter_version',
        },
        'utag' : [
            'converter_version',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'use_refinement' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : False,
        'description' :  ''' X! TANDEM can use 'refinement' to improve the speed and accuracy of peptide modelling. This is not included in Ursgal, yet. See further: http://www.thegpm.org/TANDEM/api/refine.html ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'refine',
        },
        'utag' : [
            'refinement',
        ],
        'uvalue_translation' : {
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "bool",
    },
    'validated_ident_csv_suffix' : {
        'available_in_unode' : [
            'ucontroller',
        ],
        'default_value' : "validated.csv",
        'description' :  ''' CSV suffix of validated identification files: string, CSV-file which contains PSMs validated with validation tools ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'ucontroller_style_1' : 'validated_ident_csv_suffix',
        },
        'utag' : [
            'file_extension',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'validation_generalized' : {
        'available_in_unode' : [
            'qvality_2_02',
        ],
        'default_value' : False,
        'description' :  ''' Generalized target decoy competition, situations where PSMs known to more frequently be incorrect are mixed in with the correct PSMs ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'qvality_style_1' : '-g',
        },
        'utag' : [
            'validation',
        ],
        'uvalue_translation' : {
            'qvality_style_1' : {
                False : None,
                True : '',
            },
        },
        'uvalue_type' : "bool",
    },
    'validation_minimum_score' : {
        'available_in_unode' : [
            'qvality_2_02',
        ],
        'default_value' : "",
        'description' :  ''' Defines the minimum score used fo validation. If scores lower than this are produced, they are set to the minimum score. This is used to avoid huge gaps/jumps in the score distribution ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'qvality_style_1' : 'validation_minimum_score',
        },
        'utag' : [
            'scoring',
            'validation',
        ],
        'uvalue_translation' : {
            'qvality_style_1' : {
                'msamanda_1_0_0_5242' : 0,
                'msamanda_1_0_0_5243' : 0,
                'msgfplus_v9979' : 1e-100,
                'xtandem_cyclone_2010' : 0,
                'xtandem_jackhammer' : 0,
                'xtandem_piledriver' : 0,
                'xtandem_sledgehammer' : 0,
                'xtandem_vengeance' : 0,
            },
        },
        'uvalue_type' : "",
    },
    'validation_score_field' : {
        'available_in_unode' : [
            'percolator_2_08',
            'qvality_2_02',
            'ucontroller',
            'unify_csv_1_0_0',
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : None,
        'description' :  ''' Name of the column that is used for validation, e.g. by qvality and percolator ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'percolator_style_1' : 'validation_score_field',
            'qvality_style_1' : 'validation_score_field',
            'ucontroller_style_1' : 'validation_score_field',
            'unify_csv_style_1' : 'validation_score_field',
            'xtandem_style_1' : 'validation_score_field',
        },
        'utag' : [
            'validation',
        ],
        'uvalue_translation' : {
            'percolator_style_1' : {
                'msamanda_1_0_0_5242' : 'Amanda:Score',
                'msamanda_1_0_0_5243' : 'Amanda:Score',
                'msgfplus_v9979' : 'MS-GF:SpecEValue',
                'omssa_2_1_9' : 'OMSSA:pvalue',
                'xtandem_cyclone_2010' : 'X\!Tandem:hyperscore',
                'xtandem_jackhammer' : 'X\!Tandem:hyperscore',
                'xtandem_piledriver' : 'X\!Tandem:hyperscore',
                'xtandem_sledgehammer' : 'X\!Tandem:hyperscore',
                'xtandem_vengeance' : 'X\!Tandem:hyperscore',
            },
            'qvality_style_1' : {
                'msamanda_1_0_0_5242' : 'Amanda:Score',
                'msamanda_1_0_0_5243' : 'Amanda:Score',
                'msgfplus_v9979' : 'MS-GF:SpecEValue',
                'omssa_2_1_9' : 'OMSSA:pvalue',
                'xtandem_cyclone_2010' : 'X\!Tandem:hyperscore',
                'xtandem_jackhammer' : 'X\!Tandem:hyperscore',
                'xtandem_piledriver' : 'X\!Tandem:hyperscore',
                'xtandem_sledgehammer' : 'X\!Tandem:hyperscore',
                'xtandem_vengeance' : 'X\!Tandem:hyperscore',
            },
            'ucontroller_style_1' : {
                'msamanda_1_0_0_5242' : 'Amanda:Score',
                'msamanda_1_0_0_5243' : 'Amanda:Score',
                'msgfplus_v9979' : 'MS-GF:SpecEValue',
                'omssa_2_1_9' : 'OMSSA:pvalue',
                'xtandem_cyclone_2010' : 'X\!Tandem:hyperscore',
                'xtandem_jackhammer' : 'X\!Tandem:hyperscore',
                'xtandem_piledriver' : 'X\!Tandem:hyperscore',
                'xtandem_sledgehammer' : 'X\!Tandem:hyperscore',
                'xtandem_vengeance' : 'X\!Tandem:hyperscore',
            },
            'unify_csv_style_1' : {
                'msamanda_1_0_0_5242' : 'Amanda:Score',
                'msamanda_1_0_0_5243' : 'Amanda:Score',
                'msgfplus_v9979' : 'MS-GF:SpecEValue',
                'omssa_2_1_9' : 'OMSSA:pvalue',
                'xtandem_cyclone_2010' : 'X\!Tandem:hyperscore',
                'xtandem_jackhammer' : 'X\!Tandem:hyperscore',
                'xtandem_piledriver' : 'X\!Tandem:hyperscore',
                'xtandem_sledgehammer' : 'X\!Tandem:hyperscore',
                'xtandem_vengeance' : 'X\!Tandem:hyperscore',
            },
        },
        'uvalue_type' : "",
    },
    'visualization_column_names' : {
        'available_in_unode' : [
            'venndiagram_1_0_0',
        ],
        'default_value' : [
            'Modifications',
            'Sequence',
        ],
        'description' :  ''' The specified csv column names are used for the visualization. E.g. for a Venn diagram the entries of these columns are used (merged) to determine overlapping results. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'venndiagram_style_1' : 'visualization_column_names',
        },
        'utag' : [
            'visualization',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "list",
    },
    'visualization_font' : {
        'available_in_unode' : [
            'venndiagram_1_0_0',
        ],
        'default_value' : ('Helvetica', 31, 25, 20, 20),
        'description' :  ''' Font used for visualiyation plots (e.g. Venn diagram), given as tuple (font-type, font-size header, font-size major, font-size minor, font-size venn) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'venndiagram_style_1' : 'visualization_font',
        },
        'utag' : [
            'visualization',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "tuple",
    },
    'visualization_header' : {
        'available_in_unode' : [
            'venndiagram_1_0_0',
        ],
        'default_value' : "ursgal Venn Diagram",
        'description' :  ''' Header of visualization output (e.g. Venn diagram) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'venndiagram_style_1' : 'header',
        },
        'utag' : [
            'visualization',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "str",
    },
    'visualization_label_list' : {
        'available_in_unode' : [
            'venndiagram_1_0_0',
        ],
        'default_value' : [
        ],
        'description' :  ''' Specifies labels for the datasets that should be visualized. Needs to be given in the same order as the datasets. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'venndiagram_style_1' : 'visualization_label_list',
        },
        'utag' : [
            'visualization',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "list",
    },
    'visualization_opacity' : {
        'available_in_unode' : [
            'venndiagram_1_0_0',
        ],
        'default_value' : 0.35,
        'description' :  ''' Opacity used in visualiyation plots (e.g. Venn diagram) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'venndiagram_style_1' : 'opacity',
        },
        'utag' : [
            'visualization',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "float",
    },
    'visualization_scaling_factors' : {
        'available_in_unode' : [
            'venndiagram_1_0_0',
        ],
        'default_value' : (600, 400),
        'description' :  ''' Scaling factor for visualiyation plots (e.g. Venn diagram), given as tuple (x-axis-scaling-factor, y-axis-scaling-factor) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'venndiagram_style_1' : 'visualization_scaling_factors',
        },
        'utag' : [
            'visualization',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "tuple",
    },
    'visualization_size' : {
        'available_in_unode' : [
            'venndiagram_1_0_0',
        ],
        'default_value' : (1200, 800),
        'description' :  ''' Size of visualiyation plots (e.g. Venn diagram), given as tuple (width, height) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'venndiagram_style_1' : 'visualization_size',
        },
        'utag' : [
            'visualization',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "tuple",
    },
    'visualization_stroke_width' : {
        'available_in_unode' : [
            'venndiagram_1_0_0',
        ],
        'default_value' : 2.0,
        'description' :  ''' Stroke width used in visualiyation plots (e.g. Venn diagram) ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'venndiagram_style_1' : 'stroke-width',
        },
        'utag' : [
            'visualization',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "float",
    },
    'write_unfiltered_results' : {
        'available_in_unode' : [
            'filter_csv_1_0_0',
        ],
        'default_value' : False,
        'description' :  ''' writes rejected results if True ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'filter_csv_style_1' : 'write_unfiltered_results',
        },
        'utag' : [
            'conversion',
        ],
        'uvalue_translation' : {
        },
        'uvalue_type' : "bool",
    },
    'xtandem_stp_bias' : {
        'available_in_unode' : [
            'xtandem_cyclone_2010',
            'xtandem_jackhammer',
            'xtandem_piledriver',
            'xtandem_sledgehammer',
            'xtandem_vengeance',
        ],
        'default_value' : False,
        'description' :  ''' Interpretation of peptide phosphorylation models. ''',
        'trigger_rerun' : True,
        'ukey_translation' : {
            'xtandem_style_1' : 'protein, stP bias',
        },
        'utag' : [
            'Modifications',
        ],
        'uvalue_translation' : {
            'xtandem_style_1' : {
                False : 'no',
                True : 'yes',
            },
        },
        'uvalue_type' : "",
    },
}
