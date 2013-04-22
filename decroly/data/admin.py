# -*- coding: utf-8 -*-
# Create your admin view here
from django.contrib import admin
from data.models import ScholarCycle, Alumni

class AlumniAdmin(admin.ModelAdmin):
    readonly_fields = ('cycle', 'folio', 'register_date', 'modified_date', )
    fieldsets = (
            ( 'Alumno', {
                'fields': ( 
                    'agreement',
                    ('child_name', 'child_familynames'),
                    'child_dob',
                    'child_curp_id',
                    'child_gender',
                    'child_schedule', 
                    'child_group', 
                    'child_blood_type',
                    'child_photo', 
                    'child_observations',
                    'emergency_telephone_number',
                    'emergency_contact',
                    'doctor',
                    'hospital',
                    )
               }  
            ),
            ( 'Padres', {
                'classes': ('collapse',),
                'fields':  (
                    'house_telephone',
                    ('street_name', 'street_exterior_number', 'street_interior_number'),
                    'area_colonia',
                    'zip_code',
                    'description',
                    'mapa',
                    ('father_name', 'father_familynames'),
                    ('father_telephone_work', 'father_telephone_extension'),
                    'father_cell_phone',
                    'father_email',
                    'father_occupation',
                    'father_photo',
                    ('father_ife_id', 'father_ife_file'),
                    'father_curp_id',
                    ('mother_name', 'mother_familynames'),
                    ('mother_telephone_work', 'mother_telephone_extension'),
                    'mother_cell_phone',
                    'mother_email',
                    'mother_occupation',
                    'mother_photo',
                    ('mother_ife_id', 'mother_ife_file'),
                    'mother_curp_id', 
                    )
               }
            ),
            ( 'Persona Autorizada', {
                'classes': ('collapse',),
                'fields':  (
                    ('authorized1_name', 'authorized1_familynames'),
                    'authorized1_parentezco',
                    'authorized1_cell_phone',
                    'authorized1_telephone',
                    ('authorized2_name', 'authorized2_familynames'),
                    'authorized2_parentezco',
                    'authorized2_cell_phone',
                    'authorized2_telephone',
                    ) 
               }
           ),
           ( 'Pagos y Convenios', {
               'classes': ('collapse',),
               'fields':  (
                   'august_payed',
                   'august_annotations',
                   'september_payed',
                   'september_annotations',
                   'october_payed',
                   'october_annotations',
                   'november_payed',
                   'november_annotations',
                   'december_payed',
                   'december_annotations',
                   'january_payed',
                   'january_annotations',
                   'february_payed',
                   'february_annotations',
                   'march_payed',
                   'march_annotations',
                   'april_payed',
                   'april_annotations',
                   'may_payed',
                   'may_annotations',
                   'june_payed',
                   'june_annotations',
                   ('register_payed',  'register_notes'),
                   ('insurance_payed', 'insurance_notes'),
                   ('uniform_payed',   'uniform_notes'),
                   ('supplies_payed',  'supplies_notes'),
                   ('events_payed',    'events_notes'),
                   ('otros_payed',     'otros_notes'),
               )
             }
           ),
           ( 'Documentos', {
               'classes': ('collapse',),
               'fields':  (
                   'birth_certificate',
                   'immunization_card',
                   'curp_card',
                )
             }
           )
    )

admin.site.register(ScholarCycle)
admin.site.register(Alumni, AlumniAdmin)

