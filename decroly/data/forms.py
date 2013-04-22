# -*- coding: utf-8 -*-
# Create your forms here
from django.forms import ModelForm, Textarea
from django.forms import extras
import models
import datetime

class AlumniFormRegister(ModelForm):
    class Meta:
        model = models.Alumni
        readonly_fields = ('cycle', 'folio', 'register_date', 'modified_date', )
        fields = (
            'agreement', 
            'child_name', 
            'child_familynames', 
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
        widgets = {'child_dob': extras.widgets.SelectDateWidget(years=range(2006,datetime.date.today().year+1)),
                'child_observations': Textarea(attrs={'cols': 60, 'rows': 3})}

class AlumniFormRegisterAlumni(ModelForm):
    class Meta:
        model = models.Alumni
        readonly_fields = ('cycle', 'folio', 'register_date', 'modified_date', )
        fields = ('agreement', 
            'child_name', 
            'child_familynames', 
            'child_dob', 
            'child_curp_id', 
            'child_gender', 
            'child_schedule', 
            'child_group', 
            'child_blood_type', 
            'child_photo', 
            'child_observations',
            'emergency_telephone_number',
            'emergency_contact',)
        widgets = {'child_dob': extras.widgets.SelectDateWidget(years=range(2006,datetime.date.today().year+1)),
                'child_observations': Textarea(attrs={'cols': 60, 'rows': 3})}

class AlumniFormRegisterParents(ModelForm):
    class Meta:
        model = models.Alumni
        fields = ('father_name',
            'father_familynames',
            'father_cell_phone',
            'father_telephone_work',
            'father_telephone_extension',
            'father_email',
            'father_occupation',
            'father_photo',
            'father_ife_id',
            'father_ife_file',
            'father_curp_id',
            'mother_name',
            'mother_familynames',
            'mother_cell_phone',
            'mother_telephone_work',
            'mother_telephone_extension',
            'mother_email',
            'mother_occupation',
            'mother_photo',
            'mother_ife_id',
            'mother_ife_file',
            'mother_curp_id',
            'house_telephone',
            'street_name',
            'street_exterior_number',
            'street_interior_number',
            'area_colonia',
            'zip_code',
            'description',
            'mapa',)
        widgets = {'description': Textarea(attrs={'cols': 60, 'rows': 3})}

class AlumniFormRegisterAuthorized(ModelForm):
    class Meta:
        model = models.Alumni
        fields = ('authorized1_name',
            'authorized1_familynames',
            'authorized1_cell_phone',
            'authorized1_telephone',
            'authorized1_parentezco',
            'authorized2_name',
            'authorized2_familynames',
            'authorized2_cell_phone',
            'authorized2_telephone',
            'authorized2_parentezco',)

class AlumniFormRegisterFinance(ModelForm):
    class Meta:
        model = models.Alumni
        fields = ('august_payed',
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
            'register_payed',
            'register_notes',
            'insurance_payed',
            'insurance_notes',
            'uniform_payed',
            'uniform_notes',
            'supplies_payed',
            'supplies_notes',
            'events_payed',
            'events_notes',
            'otros_payed',
            'otros_notes',)
        widgets = {'august_annotations': Textarea(attrs={'cols': 40, 'rows': 3}),
            'september_annotations':     Textarea(attrs={'cols': 40, 'rows': 3}),
            'october_annotations':       Textarea(attrs={'cols': 40, 'rows': 3}),
            'november_annotations':      Textarea(attrs={'cols': 40, 'rows': 3}),
            'december_annotations':      Textarea(attrs={'cols': 40, 'rows': 3}),
            'january_annotations':       Textarea(attrs={'cols': 40, 'rows': 3}),
            'february_annotations':      Textarea(attrs={'cols': 40, 'rows': 3}),
            'march_annotations':         Textarea(attrs={'cols': 40, 'rows': 3}),
            'april_annotations':         Textarea(attrs={'cols': 40, 'rows': 3}),
            'may_annotations':           Textarea(attrs={'cols': 40, 'rows': 3}),
            'june_annotations':          Textarea(attrs={'cols': 40, 'rows': 3}),
            'register_notes':            Textarea(attrs={'cols': 40, 'rows': 3}),
            'insurance_notes':           Textarea(attrs={'cols': 40, 'rows': 3}),
            'uniform_notes':             Textarea(attrs={'cols': 40, 'rows': 3}),
            'supplies_notes':            Textarea(attrs={'cols': 40, 'rows': 3}),
            'events_notes':              Textarea(attrs={'cols': 40, 'rows': 3}),
            'otros_notes':               Textarea(attrs={'cols':40, 'rows':3})}

class AlumniFormRegisterDocs(ModelForm):
    class Meta:
        model = models.Alumni
        fields = ('birth_certificate',
            'immunization_card',
            'curp_card',)

