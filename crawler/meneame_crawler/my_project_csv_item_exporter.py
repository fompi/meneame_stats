from scrapy.utils.project import get_project_settings
from scrapy.exporters import CsvItemExporter

settings = get_project_settings() 

class MyProjectCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter

        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export :
        	kwargs['fields_to_export'] = fields_to_export

        super(MyProjectCsvItemExporter, self).__init__(*args, **kwargs)
