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
        tbl.formulaColumn('anno',"""to_char($data, :df)""", var_df='YYYY')
        
    def trigger_onInserted(self,record=None):
        self.aggiornaCarta(record)

    def trigger_onUpdated(self,record=None,old_record=None):
        self.aggiornaCarta(record)

    def trigger_onDeleted(self,record=None):
        if self.currentTrigger.parent:
            return
        self.aggiornaCarta(record)
    
    def aggiornaCarta(self,record):
        carta_id = record['carta_id']
        self.db.deferToCommit(self.db.table('carte.carta').ricalcolaSaldo,
                                    carta_id=carta_id,
                                    _deferredId=carta_id)