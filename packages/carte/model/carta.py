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
        tbl.formulaColumn('descr_carta',"$num_carta || ' ' || @proprietario_id.full_descr")
        