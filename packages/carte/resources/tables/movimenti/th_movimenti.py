#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('carta_id')
        r.fieldcell('data')
        r.fieldcell('descrizione')
        r.fieldcell('entrate')
        r.fieldcell('uscite')

    def th_order(self):
        return 'data:d'

    def th_query(self):
        return dict(column='carta_id', op='contains', val='')
    
class ViewFromMovimenti(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        #r.fieldcell('carta_id')
        r.fieldcell('_row_count', counter=True, name='N.',width='3em')
        r.fieldcell('data',edit=True)
        r.fieldcell('descrizione',edit=True, width='100%')
        r.fieldcell('entrate',edit=True)
        r.fieldcell('uscite',edit=True)
        #r.cell('saldo',formula='entrate-uscite',format='€ #,###.00',font_weight='bold',hidden=True)
        r.fieldcell('saldo',hidden=True)
        r.cell('saldo_progressivo',name='!![it]Saldo',formula='+=saldo',dtype='N',format='€ #,###.00',width='15em', 
                range_alto='value>0',range_alto_style='color:black;font-weight:bold;',range_basso='value<0',range_basso_style='font-weight:bold;color:red;')

    def th_order(self):
        return 'data:d'

    def th_query(self):
        return dict(column='carta_id', op='contains', val='')

    def th_options(self):
        return dict(grid_selfDragRows=True)

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('carta_id' )
        fb.field('data')
        fb.field('descrizione')
        fb.field('entrate' )
        fb.field('uscite' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
