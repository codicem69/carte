#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('banca_id')
        r.fieldcell('num_carta')
        r.fieldcell('proprietario_id')
        r.fieldcell('descrizione')
        r.fieldcell('saldo',width='15em', 
                range_alto='value>0',range_alto_style='color:black;font-weight:bold;',range_basso='value<0',range_basso_style='font-weight:bold;color:red;')

    def th_order(self):
        return 'banca_id'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='')

    def th_options(self):
        return dict(partitioned=True)

class Form(BaseComponent):

    def th_form(self, form):
        
        bc = form.center.borderContainer()
        self.carta(bc.roundedGroupFrame(title='!![it]carta',region='top',datapath='.record',height='100px', splitter=True))
        tc = bc.tabContainer(margin='2px',region='center')
        self.movimentiCarta(tc.contentPane(title='!![it]Movimenti Carta'))

    def carta(self, pane):
        fb = pane.div(margin_left='50px',margin_right='80px').formbuilder(cols=2, border_spacing='4px',colswidth='auto',fld_width='100%')
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('banca_id', hasDownArrow=True )
        fb.field('num_carta' )
        fb.field('proprietario_id', hasDownArrow=True )
        fb.field('descrizione' )

    def movimentiCarta(self,pane):
        pane.inlineTableHandler(relation='@mov_carta',
                                viewResource='ViewFromMovimenti',extendedQuery=True,pbl_classes=True, liveUpdated=True,autoSave=True)
        
        


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
