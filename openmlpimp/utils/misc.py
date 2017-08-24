from time import gmtime, strftime


def get_time():
    return strftime("[%Y-%m-%d %H:%M:%S]", gmtime())


def fixed_parameters_to_suffix(fixed_parameters):
    if fixed_parameters is not None and len(fixed_parameters) > 0:
        save_folder_suffix = [param + '_' + value for param, value in fixed_parameters.items()]
        save_folder_suffix = '/' + '__'.join(save_folder_suffix)
    else:
        save_folder_suffix = '/vanilla'
    return save_folder_suffix