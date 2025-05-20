{
	"name" : "Modulo de Hotel",
	"version" : "17.0.0.0",
	"category" : "CRM",
	"depends" : [
        'base',
		'contacts',
		'crm'
    ],
	"author": "AppexBo",
	'summary': 'Modulo de Hotel',
	"description": "Este es el modulo de Hotel solicitado",
	"website" : "https://www.appexbo.com/",
	
	"data": [
		'security/ir.model.access.csv',
        'views/estado_civil/views.xml',
		'views/profession/views.xml',
		'views/partner/views.xml',

		'views/crm/views.xml'
	],

	"application": False,
	"auto_install": False,
	"installable": True,
    "license": "LGPL-3",
}