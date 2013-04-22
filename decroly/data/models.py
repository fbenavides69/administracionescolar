# -*- coding: utf-8 -*-
# Create your models here
from django.db    import models
from django.forms import ModelForm
from django.conf  import settings
from django.core.files.storage import FileSystemStorage
import os.path
import datetime

# Create your models here
class ScholarCycle(models.Model):
    """
    ScholarCycle
    Yearly School Cycle (e.g. 2012-2013)
    """
    cycle = models.CharField(blank=False, max_length=9, verbose_name=u'Ciclo Escolar')

    def __unicode__(self):
        return u'%s' % self.cycle

    class Meta:
        db_table = u'Ciclo Escolar'
        ordering = ['cycle']
        verbose_name = u'Ciclo Escolar'
        verbose_name_plural = u'Ciclos Escolares'

    class Admin:
        pass
"""
class MonthlyFee(models.Model):
    FEE_AUGUST    = 0
    FEE_SEPTEMBER = 1
    FEE_OCTOBER   = 2
    FEE_NOVEMBER  = 3
    FEE_DECEMBER  = 4
    FEE_JANUARY   = 5
    FEE_FEBRUARY  = 6
    FEE_MARCH     = 7
    FEE_APRIL     = 8
    FEE_MAY       = 9
    FEE_JUNE      = 10
    FEE_CHOICES   = (
        (FEE_AUGUST,    u'Agosto'),
        (FEE_SEPTEMBER, u'September'),
        (FEE_OCTOBER,   u'Octubre'),
        (FEE_NOVEMBER,  u'Noviembre'),
        (FEE_DECEMBER,  u'Diciembre'),
        (FEE_JANUARY,   u'Enero'),
        (FEE_FEBRUARY,  u'Febrero'),
        (FEE_MARCH,     u'Marzo'),
        (FEE_APRIL,     u'Abril'),
        (FEE_MAY,       u'Mayo'),
        (FEE_JUNE,      u'Junio'),
    )

    MONTH_NOT_PAYED = 0
    MONTH_PAYED     = 1
    MONTH_CHOICES = (
        (MONTH_NOT_PAYED, u'No pagado'),
        (MONTH_PAYED,     u'Pagado'),
    )

    month      = models.IntegerField(null=True, blank=True, choices=FEE_CHOICES,   default=FEE_AUGUST,      verbose_name=u'Mes')
    payed      = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Pagado')
    date       = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    anotations = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')

    def payed_string(self):
        return self.MONTH_CHOICES[self.payed][1]

    def __unicode__(self):
        return u'%s %s' % (self.payed_string(), self.anotations)

    class Meta:
        db_table = u'Colegiatura'
        ordering = ['month']
        verbose_name = u'Mes'
        verbose_name_plural = u'Meses'

    class Admin:
        pass
"""

fs_photos = FileSystemStorage(location='/media/user/photos')
fs_docs   = FileSystemStorage(location='/media/user/docs')

class Alumni(models.Model):
    """
    Alumni
    The School Children
    """
    ALUMNI_GENDER_MALE    = 0
    ALUMNI_GENDER_FEMALE  = 1
    ALUMNI_GENDER_CHOICES = (
        (ALUMNI_GENDER_MALE,   u'Masculino'),
        (ALUMNI_GENDER_FEMALE, u'Femenino'),
    )

    ALUMNI_SCHEDULE_NORMAL     = 0
    ALUMNI_SCHEDULE_ASSISTANCE = 1
    ALUMNI_SCHEDULE_CHOICES    = (
        (ALUMNI_SCHEDULE_NORMAL, u'Normal'),
        (ALUMNI_SCHEDULE_ASSISTANCE, u'Asistencial'),
    )

    ALUMNI_GROUP_UNWEANED    = 0
    ALUMNI_GROUP_MATERNAL    = 1
    ALUMNI_GROUP_PRESCHOOL_1 = 2
    ALUMNI_GROUP_PRESCHOOL_2 = 3
    ALUMNI_GROUP_PRESCHOOL_3 = 4
    ALUMNI_GROUP_CHOICES     = (
        (ALUMNI_GROUP_UNWEANED,    u'Lactantes'),
        (ALUMNI_GROUP_MATERNAL,    u'Maternal'),
        (ALUMNI_GROUP_PRESCHOOL_1, u'Preescolar I'),
        (ALUMNI_GROUP_PRESCHOOL_2, u'Preescolar II'),
        (ALUMNI_GROUP_PRESCHOOL_3, u'Preescolar III'),
    )

    ALUMNI_BLOOD_TYPE_O_POSITIVE         = 0
    ALUMNI_BLOOD_TYPE_O_NEGATIVE         = 1
    ALUMNI_BLOOD_TYPE_A_POSITIVE         = 2
    ALUMNI_BLOOD_TYPE_A_NEGATIVE         = 3
    ALUMNI_BLOOD_TYPE_AB_POSITIVE        = 4
    ALUMNI_BLOOD_TYPE_AB_NEGATIVE        = 5
    ALUMNI_BLOOD_TYPE_B_POSITIVE         = 6
    ALUMNI_BLOOD_TYPE_B_NEGATIVE         = 7
    ALUMNI_BLOOD_TYPE_LANGEREIS_POSITIVE = 8
    ALUMNI_BLOOD_TYPE_LANGEREIS_NEGATIVE = 9
    ALUMNI_BLOOD_TYPE_JUNIOR_POSITIVE    = 10
    ALUMNI_BLOOD_TYPE_JUNIOR_NEGATIVE    = 11
    ALUMNI_BLOOD_TYPE_CHOICES            = (
        (ALUMNI_BLOOD_TYPE_O_POSITIVE,         u'O+'),
        (ALUMNI_BLOOD_TYPE_O_NEGATIVE,         u'O-'),
        (ALUMNI_BLOOD_TYPE_A_POSITIVE,         u'A+'),
        (ALUMNI_BLOOD_TYPE_A_NEGATIVE,         u'A-'),
        (ALUMNI_BLOOD_TYPE_AB_POSITIVE,        u'AB+'),
        (ALUMNI_BLOOD_TYPE_AB_NEGATIVE,        u'AB-'),
        (ALUMNI_BLOOD_TYPE_B_POSITIVE,         u'B+'),
        (ALUMNI_BLOOD_TYPE_B_NEGATIVE,         u'B-'),
        (ALUMNI_BLOOD_TYPE_LANGEREIS_POSITIVE, u'Langereis+'),
        (ALUMNI_BLOOD_TYPE_LANGEREIS_NEGATIVE, u'Langereis-'),
        (ALUMNI_BLOOD_TYPE_JUNIOR_POSITIVE,    u'Junior+'),
        (ALUMNI_BLOOD_TYPE_JUNIOR_NEGATIVE,    u'Junior-'),
    )

    ALUMNI_NOT_PAYED = 0
    ALUMNI_PAYED     = 1
    ALUMNI_CHOICES   = (
        (ALUMNI_NOT_PAYED, u'No Pagado'),
        (ALUMNI_PAYED,     u'Pagado'),
    )

    VOICE_CONTACT_TELEPHONE = 0
    VOICE_CONTACT_FAX       = 1
    VOICE_CONTACT_CELLULAR  = 2
    VOICE_CONTACT_NEXTEL    = 3
    VOICE_CONTACT_TOLLFREE  = 4
    VOICE_CONTACT_OTHER     = 5
    VOICE_CONTACT_CHOICES   = (
        (VOICE_CONTACT_TELEPHONE, u'Teléfono'),
        (VOICE_CONTACT_FAX,       u'Fax'),
        (VOICE_CONTACT_CELLULAR,  u'Celular'),
        (VOICE_CONTACT_NEXTEL,    u'Nextel'),
        (VOICE_CONTACT_TOLLFREE,  u'01 800'),
        (VOICE_CONTACT_OTHER,     u'Otro'),
    )

    VOICE_PLACE_HOME     = 0
    VOICE_PLACE_WORK     = 1
    VOICE_PLACE_PERSONAL = 2
    VOICE_PLACE_OTHER    = 3
    VOICE_PLACE_CHOICES = (
        (VOICE_PLACE_HOME,     u'Casa'),
        (VOICE_PLACE_WORK,     u'Trabajo'),
        (VOICE_PLACE_PERSONAL, u'Personal'),
        (VOICE_PLACE_OTHER,    u'Otro'), 
    )
    
    ALUMNI_AGREEMENT_PARTICULAR = 0
    ALUMNI_AGREEMENT_SEDESOL    = 1
    ALUMNI_AGREEMENT_SEBIDESO   = 2
    ALUMNI_AGREEMENT_DIF        = 3
    ALUMNI_AGREEMENT_OTHER      = 4
    ALUMNI_AGREEMENT_CHOICES    = (
        (ALUMNI_AGREEMENT_PARTICULAR, u'Particular'),
        (ALUMNI_AGREEMENT_SEDESOL,    u'SEDESOL'),
        (ALUMNI_AGREEMENT_SEBIDESO,   u'SEBIDESO'),
        (ALUMNI_AGREEMENT_DIF,        u'DIF'),
        (ALUMNI_AGREEMENT_OTHER,      u'Otro'),
    )

    MONTH_NOT_PAYED = 0
    MONTH_PAYED     = 1
    MONTH_CHOICES = (
        (MONTH_NOT_PAYED, u'No pagado'),
        (MONTH_PAYED,     u'Pagado'),
    )

    PARENTEZCO_ABUELO = 0
    PARENTEZCO_ABUELA = 1
    PARENTEZCO_TIO    = 2
    PARENTEZCO_TIA    = 3
    PARENTEZCO_HERMANO = 4
    PARENTEZCO_HERMANA = 5
    PARENTEZCO_PRIMO   = 6
    PARENTEZCO_PRIMA   = 7
    PARENTEZCO_OTRO    = 8
    PARENTEZCO_CHOICES = (
        (PARENTEZCO_ABUELO,  u'Abuelo'),
        (PARENTEZCO_ABUELA,  u'Abuela'),
        (PARENTEZCO_TIO,     u'Tío'),
        (PARENTEZCO_TIA,     u'Tía'),
        (PARENTEZCO_HERMANO, u'Hermano'),
        (PARENTEZCO_HERMANA, u'Hermana'),
        (PARENTEZCO_PRIMO,   u'Primo'),
        (PARENTEZCO_PRIMA,   u'Prima'),
        (PARENTEZCO_OTRO,    u'Otro'),
    )

    COLEGIATURA_NORMAL      = 0
    COLEGIATURA_ASISTENCIAL = 1
    COLEGIATURA_OTRO        = 2
    COLEGIATURA_CHOICES = (
        (COLEGIATURA_NORMAL,      u'Normal'),
        (COLEGIATURA_ASISTENCIAL, u'Asistencial'),
        (COLEGIATURA_OTRO,        u'Otro'),
    )

    cycle                   = models.ForeignKey(ScholarCycle, unique=False, null=False, blank=True, verbose_name=u'Ciclo Escolar')
    folio                   = models.CharField(null=False, blank=False, max_length=8, verbose_name=u'Número de Folio')
    agreement               = models.IntegerField(choices=ALUMNI_AGREEMENT_CHOICES, default=ALUMNI_AGREEMENT_PARTICULAR, verbose_name=u'Convenio')
    register_date           = models.DateTimeField(null=False, blank=False, verbose_name=u'Fecha de Inscripción')
    modified_date           = models.DateTimeField(null=False, blank=False, verbose_name=u'Fecha de Última Modificación')
    child_name              = models.CharField(blank=False, max_length=30, verbose_name=u'Nombre(s)')
    child_familynames       = models.CharField(blank=False, max_length=30, verbose_name=u'Apellidos')
    child_dob               = models.DateField(blank=False, verbose_name=u'Fecha de Nacimiento')
    child_curp_id           = models.CharField(blank=False, max_length=30, verbose_name=u'CURP')
    child_gender            = models.IntegerField(choices=ALUMNI_GENDER_CHOICES,     default=ALUMNI_GENDER_FEMALE,         verbose_name=u'Sexo')
    child_schedule          = models.IntegerField(choices=ALUMNI_SCHEDULE_CHOICES,   default=ALUMNI_SCHEDULE_NORMAL,       verbose_name=u'Horario')
    child_group             = models.IntegerField(choices=ALUMNI_GROUP_CHOICES,      default=ALUMNI_GROUP_PRESCHOOL_1,     verbose_name=u'Grupo')
    child_blood_type        = models.IntegerField(choices=ALUMNI_BLOOD_TYPE_CHOICES, default=ALUMNI_BLOOD_TYPE_O_POSITIVE, verbose_name=u'Tipo de Sangre')
    child_photo             = models.ImageField(blank=True, upload_to='photos', verbose_name=u'Foto')
    child_observations      = models.TextField(blank=True,  verbose_name=u'Observaciones')
    emergency_telephone_number = models.CharField(blank=True, max_length=15, verbose_name=u'Número de Emergencia')
    emergency_contact          = models.CharField(blank=True, max_length=30, verbose_name=u'Nombre del Contacto de Emergencia')
    doctor                  = models.CharField(blank=True, max_length=30, verbose_name=u'Médico')
    hospital                = models.CharField(blank=True, max_length=30, verbose_name=u'Hospital')
    house_telephone         = models.CharField(blank=True, max_length=15, verbose_name=u'Teléfono de casa')
    street_name             = models.CharField(blank=True, max_length=30, verbose_name=u'Calle')
    street_exterior_number  = models.CharField(blank=True, max_length=10, verbose_name=u'Número Exterior')
    street_interior_number  = models.CharField(blank=True,  max_length=5,  verbose_name=u'Número Interior')
    area_colonia            = models.CharField(blank=True,  max_length=60, verbose_name=u'Colonia')
    zip_code                = models.CharField(blank=True,  max_length=10, verbose_name=u'Código Postal')
    description             = models.TextField(blank=True, verbose_name=u'Notas')
    mapa                    = models.URLField(blank=True, verbose_name=u'Mapa')
    father_name             = models.CharField(blank=True, max_length=30, verbose_name=u'Nombre(s) Papá')
    father_familynames      = models.CharField(blank=True, max_length=30, verbose_name=u'Apellidos')
    father_cell_phone          = models.CharField(blank=True, max_length=15, verbose_name=u'Télefono Celular')
    father_telephone_work      = models.CharField(blank=True, max_length=15, verbose_name=u'Télefono Trabajo')
    father_telephone_extension = models.CharField(blank=True, max_length=6,  verbose_name=u'Extensión')
    father_email            = models.EmailField(blank=True, max_length=60, verbose_name=u'Dirección Electrónica')
    father_occupation       = models.CharField(blank=True, max_length=30, verbose_name=u'Ocupación')
    father_photo            = models.ImageField(blank=True, upload_to='photos', verbose_name=u'Archivo Foto')
    father_ife_id           = models.CharField(blank=True, max_length=30, verbose_name=u'IFE')
    father_ife_file         = models.FileField(blank=True, upload_to='docs', verbose_name=u'Archivo IFE')
    father_curp_id          = models.CharField(blank=True, max_length=30, verbose_name=u'CURP')
    mother_name             = models.CharField(blank=True, max_length=30, verbose_name=u'Nombre(s) Mamá')
    mother_familynames      = models.CharField(blank=True, max_length=30, verbose_name=u'Apellidos')
    mother_cell_phone          = models.CharField(blank=True, max_length=15, verbose_name=u'Télefono Celular')
    mother_telephone_work      = models.CharField(blank=True, max_length=15, verbose_name=u'Télefono Trabajo')
    mother_telephone_extension = models.CharField(blank=True, max_length=6,  verbose_name=u'Extensión')
    mother_email            = models.EmailField(blank=True, max_length=60, verbose_name=u'Dirección Electrónica')
    mother_occupation       = models.CharField(blank=True, max_length=30, verbose_name=u'Ocupación')
    mother_photo            = models.ImageField(blank=True, upload_to='photos', verbose_name=u'Archivo Foto')
    mother_ife_id           = models.CharField(blank=True, max_length=30, verbose_name=u'IFE')
    mother_ife_file         = models.FileField(blank=True, upload_to='docs', verbose_name=u'Archivo IFE')
    mother_curp_id          = models.CharField(blank=True, max_length=30, verbose_name=u'CURP')
    authorized1_name        = models.CharField(blank=True, max_length=30, verbose_name=u'Nombre(s) Persona Autorizada')
    authorized1_familynames = models.CharField(blank=True, max_length=30, verbose_name=u'Apellidos')
    authorized1_cell_phone  = models.CharField(blank=True, max_length=15, verbose_name=u'Teléfono Celular')
    authorized1_telephone   = models.CharField(blank=True, max_length=15, verbose_name=u'Teléfono')
    authorized1_parentezco  = models.IntegerField(null=True, blank=True, choices=PARENTEZCO_CHOICES,  max_length=15, verbose_name=u'Parentezco')
    authorized2_name        = models.CharField(blank=True, max_length=30, verbose_name=u'Nombre(s) Persona Autorizada')
    authorized2_familynames = models.CharField(blank=True, max_length=30, verbose_name=u'Apellidos')
    authorized2_cell_phone  = models.CharField(blank=True, max_length=15, verbose_name=u'Teléfono Celular')
    authorized2_telephone   = models.CharField(blank=True, max_length=15, verbose_name=u'Teléfono')
    authorized2_parentezco  = models.IntegerField(null=True, blank=True, choices=PARENTEZCO_CHOICES,  max_length=15, verbose_name=u'Parentezco')
    colegiatura             = models.IntegerField(null=True, blank=True, max_length=6, verbose_name=u'Colegiatura')
    august_payed            = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Agosto')
    august_payed_date       = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    august_annotations      = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    september_payed         = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Septiembre')
    september_payed_date    = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    september_annotations   = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    october_payed           = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Octubre')
    october_payed_date      = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    october_annotations     = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    november_payed          = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Noviembre')
    november_payed_date     = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    november_annotations    = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    december_payed          = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Diciembre')
    december_payed_date     = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    december_annotations    = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    january_payed           = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Enero')
    january_payed_date      = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    january_annotations     = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    february_payed          = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Febrero')
    february_payed_date     = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    february_annotations    = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    march_payed             = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Marzo')
    march_payed_date        = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    march_annotations       = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    april_payed             = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Abril')
    april_payed_date        = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    april_annotations       = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    may_payed               = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Mayo')
    may_payed_date          = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    may_annotations         = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    june_payed              = models.IntegerField(null=True, blank=True, choices=MONTH_CHOICES, default=MONTH_NOT_PAYED, verbose_name=u'Junio')
    june_payed_date         = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    june_annotations        = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    register_payed          = models.IntegerField(null=True, blank=True, choices=ALUMNI_CHOICES,  default=ALUMNI_NOT_PAYED, verbose_name=u'Inscripción Pagada')
    register_payed_date     = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    register_notes          = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    insurance_payed         = models.IntegerField(null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name=u'Seguro Pagado')
    insurance_payed_date    = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    insurance_notes         = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    uniform_payed           = models.IntegerField(null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name=u'Uniforme Pagado')
    uniform_payed_date      = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    uniform_notes           = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    supplies_payed          = models.IntegerField(null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name=u'Material Pagado')
    supplies_payed_date     = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    supplies_notes          = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    events_payed            = models.IntegerField(null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name=u'Evento Pagado')
    events_payed_date       = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    events_notes            = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    otros_payed             = models.IntegerField(null=True, blank=True, choices=ALUMNI_CHOICES, default=ALUMNI_NOT_PAYED, verbose_name=u'Otros Pagado')
    otros_payed_date        = models.DateField(null=True, blank=True, verbose_name=u'Fecha de Pago')
    otros_notes             = models.TextField(blank=True, max_length=400, verbose_name=u'Notas')
    birth_certificate       = models.FileField(blank=True, upload_to='docs', verbose_name=u'Acta de Nacimiento')
    immunization_card       = models.FileField(blank=True, upload_to='docs', verbose_name=u'Cartilla de Vacunación')
    curp_card               = models.FileField(blank=True, upload_to='docs', verbose_name=u'CURP')

    def set_payed_date(self):
        if self.august_payed == self.MONTH_PAYED:
            if self.august_payed_date == None:
                self.august_payed_date = datetime.datetime.now()
        if self.september_payed == self.MONTH_PAYED:
            if self.september_payed_date == None:
                self.september_payed_date = datetime.datetime.now()
        if self.october_payed == self.MONTH_PAYED:
            if self.october_payed_date == None:
                self.october_payed_date = datetime.datetime.now()
        if self.november_payed == self.MONTH_PAYED:
            if self.november_payed_date == None:
                self.november_payed_date = datetime.datetime.now()
        if self.december_payed == self.MONTH_PAYED:
            if self.december_payed_date == None:
                self.december_payed_date = datetime.datetime.now()
        if self.january_payed == self.MONTH_PAYED:
            if self.january_payed_date == None:
                self.january_payed_date = datetime.datetime.now()
        if self.february_payed == self.MONTH_PAYED:
            if self.february_payed_date == None:
                self.february_payed_date = datetime.datetime.now()
        if self.march_payed == self.MONTH_PAYED:
            if self.march_payed_date == None:
                self.march_payed_date = datetime.datetime.now()
        if self.april_payed == self.MONTH_PAYED:
            if self.april_payed_date == None:
                self.april_payed_date = datetime.datetime.now()
        if self.may_payed == self.MONTH_PAYED:
            if self.may_payed_date == None:
                self.may_payed_date = datetime.datetime.now()
        if self.june_payed == self.MONTH_PAYED:
            if self.june_payed_date == None:
                self.june_payed_date = datetime.datetime.now()
        if self.register_payed == self.ALUMNI_PAYED:
            if self.register_payed_date == None:
                self.register_payed_date = datetime.datetime.now()
        if self.insurance_payed == self.ALUMNI_PAYED:
            if self.insurance_payed_date == None:
                self.insurance_payed_date = datetime.datetime.now()
        if self.uniform_payed == self.ALUMNI_PAYED:
            if self.uniform_payed_date == None:
                self.uniform_payed_date = datetime.datetime.now()
        if self.supplies_payed == self.ALUMNI_PAYED:
            if self.supplies_payed_date == None:
                self.supplies_payed_date = datetime.datetime.now()
        if self.events_payed == self.ALUMNI_PAYED:
            if self.events_payed_date == None:
                self.events_payed_date = datetime.datetime.now()

    def schedule_string(self):
        return self.ALUMNI_SCHEDULE_CHOICES[self.child_schedule][1]

    def group_string(self):
        return self.ALUMNI_GROUP_CHOICES[self.child_group][1]
    
    def agreement_string(self):
        return self.ALUMNI_AGREEMENT_CHOICES[self.agreement][1]

    def get_absolute_url(self):
        return reverse('alumni-details', kwargs={'id': self.id})

    def set_cycle(self):
        try:
            self.cycle = ScholarCycle.objects.latest('id')
        except:
            self.cycle = None 

    def set_folio(self):
        try:
            lastFolio = Alumni.objects.latest('id').folio.split(':')
        except:
            lastFolio = None
        year = datetime.datetime.now().year
        if lastFolio == None:
            self.folio = str(year) + ':000'
        elif int(lastFolio[0]) == year:
            number = int(lastFolio[1])+1
            self.folio = str(year) + ':' + str(number).zfill(3)
        else:
            self.folio = str(year) + ':000'

    def set_uppercase(self):
        self.child_name              = self.child_name.upper()
        self.child_familynames       = self.child_familynames.upper()
        self.father_name             = self.father_name.upper()
        self.father_familynames      = self.father_familynames.upper()
        self.mother_name             = self.mother_name.upper()
        self.mother_familynames      = self.mother_familynames.upper()
        self.authorized1_name        = self.authorized1_name.upper()
        self.authorized1_familynames = self.authorized1_familynames.upper()
        self.authorized2_name        = self.authorized2_name.upper()
        self.authorized2_familynames = self.authorized2_familynames.upper()
    
    def age(self):
        if self.child_dob > datetime.date.today().replace(year = self.child_dob.year):
            return datetime.date.today().year - self.child_dob.year - 1
        else:
            return datetime.date.today().year - self.child_dob.year
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.register_date = datetime.datetime.now()
            self.set_folio()
        self.modified_date = datetime.datetime.now()
        self.set_uppercase()
        self.set_cycle()
        self.set_payed_date()
        super(Alumni,self).save(*args, **kwargs)

    def __unicode__(self):
       return u'%8s %20s %30s, %20s, %20s, %20s, Teléfono de emergencia: %15s' % (self.folio, self.child_name, self.child_familynames, self.group_string(), self.schedule_string(), self.agreement_string(), self.emergency_telephone_number)

    class Meta:
        db_table = u'Alumno'
        ordering = ['child_name', 'child_familynames']
        verbose_name = u'Alumno'
        verbose_name_plural = u'Alumnos'

    class Admin:
        pass
