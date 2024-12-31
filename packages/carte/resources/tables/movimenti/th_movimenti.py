#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrdecorator import metadata

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('carta_id')
        r.fieldcell('data')
        r.fieldcell('descrizione')
        r.fieldcell('entrate')
        r.fieldcell('uscite')

    def th_order(self):
        return 'data'

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
        return 'data'

    def th_query(self):
        return dict(column='carta_id', op='contains', val='')

    def th_options(self):
        return dict(grid_selfDragRows=True)

    #def th_sections_anno(self):
    #    return [dict(code='tutti',caption='!![it]Tutti'),
    #        dict(code="2023", caption="2023", condition="$anno='2023'"),
    #        dict(code="2024", caption="2024", condition="$anno='2024'"),
    #        dict(code="2025", caption="2025", condition="$anno='2025'"),
    #    ]
                
    def th_top_toolbarsuperiore(self,top):
        bar=top.slotToolbar('5,sections@anno,10,actions,resourceActions,5',
                        childname='superiore',_position='<bar',sections_anno_multivalue=True,
                        sections_anno_multiButton=10)
                        #,gradient_from='#999',gradient_to='#888')
        bar.actions.div('Actions')
    
    @metadata(multivalue=True)
    def th_sections_anno(self):
        result = [dict(code='tutti',caption='!![it]Tutti')]
        tbl_mov=self.db.table('carte.movimenti')
        anno=tbl_mov.query(columns="""to_char($data, 'YYYY')""",group_by="""to_char($data, 'YYYY')""",where='@carta_id.agency_id=:ag_id',
                           ag_id=self.db.currentEnv.get('current_agency_id')).fetch()
        #print(x)
        for c in anno:
            if c[0] is not None:
                result.append(dict(code=c[0],caption=c[0],
                            condition="$anno = :anno",
                            condition_anno=c[0]))
        return result
    
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
