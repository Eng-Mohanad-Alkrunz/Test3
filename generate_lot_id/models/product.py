from odoo import api, fields, models, _

from datetime import datetime
from dateutil import tz

from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_round, float_compare
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

import string
import re
import logging



class ProductTemplate(models.Model):
    _inherit = "product.template"
    lot_abbv = fields.Char('Lot Code Format', help='To assist with manufacturing, '
                                'lot codes will automatically generate with this prefix.\n'
                                'You can add other pieces to be generated, such as \n'
                                '- [DATE]\n yyyymmdd'
                                '- [JULIAN] - Julian date code\n'
                                '- [JULIAN_DAY] - Julian day\n'
                                '- [YEARYY] - Last two digits of year\n'
                                '- [MONTH] - 01-12 Month\n'
                                '- [DAY] - 01-31 Day\n'
                                '- [YEAR] - Full year\n' 
                                '- [OPERATION_CODE] - Manufacturing Operation Code\n'                                
                                '- [WAREHOUSE_CODE] - Warehouse Code\n'
                                '- [USER_DEFINED] - Variable will be entered by user when creating lot\n'         
                                'For example, CCSS-[JULIAN_DAY]-[YEARYY] will output the Julian datecode: CCSS-19118\n'
                                'Add an extra underscore to offer employees tips on the user defined variable, \n'
                                'such as [USER_DEFINED_MACHINE_NUMBER], will print "Machine Number" below the field.\n')
