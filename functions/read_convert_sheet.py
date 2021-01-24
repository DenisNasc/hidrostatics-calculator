import pandas as pd


def read_convert_sheet(path: str) -> {}:
    sheet = pd.read_excel(path, skiprows=1)
    dict_sheet = sheet.to_dict('dict')

    length_dict_sheet = len(dict_sheet['Baliza'])
    converted_sheet = {}

    for i in range(length_dict_sheet):
        baliza = dict_sheet['Baliza'][i]
        ordem = dict_sheet['Ordem'][i]
        longitudinal = dict_sheet['Longitudinal'][i]
        vertical = dict_sheet['Vertical'][i]
        transversal = dict_sheet['Transversal'][i]

        if (baliza == 'Espelho de Popa'):
            baliza = 999

        try:
            converted_sheet[baliza].append({
                'id': ordem,
                'longitudinal': longitudinal,
                'vertical': vertical,
                'transversal': transversal
            })
        except:
            converted_sheet[baliza] = [{
                'id': ordem,
                'longitudinal': longitudinal,
                'vertical': vertical,
                'transversal': transversal
            }]

    return converted_sheet