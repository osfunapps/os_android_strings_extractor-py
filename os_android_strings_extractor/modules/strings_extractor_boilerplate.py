import os_tools.xml_file_handler as xh
import os_tools.file_handler as fh


##################################################################################
#
# just the StringsExtractor boiler plate script
#
##################################################################################


# will return a dictionary containing all of the strings in the xml file by "id": "value"
def build_strings_dict(project_path):
    string_nodes = get_relevant_string_nodes(project_path)
    return xh.nodes_to_dict(string_nodes, 'name')


def get_relevant_string_nodes(project_path):
    strings_path = project_path + '/app/src/main/res/values/strings.xml'
    xml = xh.read_xml_file(strings_path)
    return xh.get_nodes_from_xml_without_att(xml, 'string', 'translatable')


# will turn the strings dictionary to a good looking xls file
def dict_to_xlsx(project_path, strings_dict, output_path, src_language, languages_arr):
    import xlsxwriter

    # Create an new Excel file and add a worksheet.
    project_name = fh.get_dir_name(project_path)
    workbook = xlsxwriter.Workbook(output_path + '/' + project_name + '-Translations.xlsx')

    big_red_format = workbook.add_format()
    title_format = workbook.add_format()
    content_format = workbook.add_format()
    border_format = workbook.add_format()

    big_red_format.set_font_color('red')
    big_red_format.set_font_size(16)

    title_format.set_font_size(22)

    content_format.set_font_size(12)
    content_format.set_font('Arial')
    big_red_format.set_align('center')

    border_format.set_top()

    # set the border

    for language in languages_arr:
        worksheet = workbook.add_worksheet(language)

        # widen all of the columns used
        worksheet.set_column('A:A', 50, cell_format=content_format)
        worksheet.set_column('B:B', 50, cell_format=content_format)
        worksheet.set_column('C:C', 50, cell_format=content_format)
        worksheet.set_column('F:F', 50, cell_format=content_format)

        # set headers
        worksheet.write('A1', 'Translation Project', title_format)
        worksheet.write('A3', src_language, big_red_format)
        worksheet.write('B3', language, big_red_format)
        worksheet.write('F3', 'Code (DO NOT CHANGE)', big_red_format)

        # set strings
        keys_list = list(strings_dict.keys())
        for i in range(len(strings_dict)):
            key = keys_list[i]
            worksheet.write('A' + str(i + 4), strings_dict[key])
            worksheet.write('F' + str(i + 4), key)

    workbook.close()
