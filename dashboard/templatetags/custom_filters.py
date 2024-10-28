import os
from django import template
import re
from django.urls import reverse
from dashboard.models import *

register = template.Library()

@register.filter
def filename(value):
    if not value:  # Cek apakah value kosong atau None
        return None
    return os.path.basename(value)

@register.filter(name='replace_headings')
def replace_headings(value):
    # Replace all <h1>, <h2>, <h3>... tags with <p>
    value = re.sub(r'<h[1-6](.*?)>', r'<p\1>', value)
    value = re.sub(r'</h[1-6]>', '</p>', value)
    return value

@register.simple_tag
def get_surat_table_url(surat):
    if isinstance(surat, SuketPermohonanKTP):
        return reverse('suketpermohonanktp')
    elif isinstance(surat, SuketBelumMenikah):
        return reverse('suketbelummenikah')
    elif isinstance(surat, SuketTidakMampu):
        return reverse('sukettidakmampu')
    elif isinstance(surat, SKCK):
        return reverse('skck')
    elif isinstance(surat, SuketKTPBedaNama):
        return reverse('suketktpbedanama')
    elif isinstance(surat, SuketAhliWaris):
        return reverse('suketahliwaris')
    elif isinstance(surat, SuketMTQ):
        return reverse('suketMTQ')
    elif isinstance(surat, SuketKehilangan):
        return reverse('suketkehilangan')
    elif isinstance(surat, SuketKelahiran):
        return reverse('suketkelahiran')
    elif isinstance(surat, SuketKematian):
        return reverse('suketkematian')
    elif isinstance(surat, SuketPenghasilanTidakTetap):
        return reverse('suketpenghasilantidaktetap')
    elif isinstance(surat, SuketUsaha):
        return reverse('suketusaha')
    elif isinstance(surat, SuketVaksinNikah):
        return reverse('suketvaksinnikah')
    elif isinstance(surat, SuketPindahNikah):
        return reverse('suketpindahnikah')
    elif isinstance(surat, SuketRekKelTani):
        return reverse('suketrekkeltani')
    else:
        return "#"
    
