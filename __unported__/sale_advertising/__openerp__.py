# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2016 Magnus (<http://www.magnus.nl>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'sale_advertising',
    'version': '1.0',
    'category': 'Sale',
    'description': """
This module allows you to use both CRM and Sales Management to run your advertising sales
=========================================================================================


    """,
    'author': 'Magnus - Willem Hulshof',
    'website': 'http://www.magnus.nl',
    'depends': [
        'sale_stock', 'sale_crm',
                'nsm_analytic', 'nsm_supportal_extension', 'nsm_hon',
                # 'base_partner_merge', 'calendar',
                ],
    'data': [
        "security/ir.model.access.csv",
             "security/security.xml",
             "wizard/sale_line_create_multi_view.xml",
             "wizard/crm_lead_to_opportunity_view.xml",
             # "wizard/crm_make_sale_view.xml",
             "sale_advertising_view.xml",
             "res_partner_view.xml",
             "crm_lead_view.xml",
             "res_company_view.xml",
             # "sale_workflow.xml",
             "crm_menu_view.xml",
             ],
    'demo': ['sale_advertising_demo.xml'],
    'installable': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

