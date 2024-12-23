# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('carta', pkey='id', name_long='!![it]Carta', name_plural='!![it]Carte',caption_field='descr_carta')
        self.sysFields(tbl)

        tbl.column('banca_id',size='22', group='_', name_long='!![it]Banca'
                    ).relation('banca.id', relation_name='banca_carta', mode='foreignkey', onDelete='raise')
        tbl.column('num_carta', name_short='!![it]Numero carta')
        tbl.column('proprietario_id',size='22', group='_', name_long='!![it]Proprietario'
                    ).relation('proprietario.id', relation_name='proprietario_carta', mode='foreignkey', onDelete='raise')
        tbl.column('descrizione', name_short='!![it]Descrizione')
        tbl.column('saldo', dtype='N', name_short='!![it]Saldo',format='€ #,###.00')
        tbl.formulaColumn('descr_carta',"$num_carta || ' ' || @proprietario_id.full_descr")
        tbl.formulaColumn('saldo_carta',select=dict(table='carte.movimenti',
                                                columns='SUM(coalesce($entrate,0)-coalesce($uscite,0))',
                                                where='$carta_id=#THIS.id'),
                                    dtype='N',name_long='!![it]Saldo', format='€ #,###.00')
        
    def ricalcolaSaldo(self,carta_id=None):
        with self.recordToUpdate(carta_id) as record:
            saldo = self.db.table('carte.movimenti').readColumns(columns="""SUM(coalesce($entrate,0)-coalesce($uscite,0)) AS saldo""",
                                                                     where='$carta_id=:c_id',c_id=carta_id)
            record['saldo'] = saldo 