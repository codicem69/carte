# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('movimenti', pkey='id', name_long='!![it]Movimenti', name_plural='!![it]Movimenti',caption_field='')
        self.sysFields(tbl,counter=True)
        tbl.column('carta_id',size='22', group='_', name_long='!![it]Nome Carta'
                    ).relation('carta.id', relation_name='mov_carta', mode='foreignkey', onDelete='raise')
        tbl.column('data', dtype='D', name_short='!![it]Data movimento')
        tbl.column('descrizione', name_short='!![it]Descrizione')
        tbl.column('entrate', dtype='money', name_short='!![it]Entrate')
        tbl.column('uscite', dtype='money', name_short='!![it]Uscite')
        tbl.formulaColumn('saldo',select=dict(table='carte.movimenti',
                                                columns='coalesce($entrate,0)-coalesce($uscite,0)',
                                                where='$id=#THIS.id'),
                                    dtype='N',name_long='!![it]Saldo', format='€ #,###.00')