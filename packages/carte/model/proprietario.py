# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('proprietario', pkey='id', name_long='!![it]Proprietario Carta', name_plural='!![it]Proprietari Carte',caption_field='full_descr')
        self.sysFields(tbl)
        tbl.column('nome', name_short='!![it]Nome')
        tbl.column('cognome', name_short='!![it]Cognome')
        tbl.column('ditta', name_short='!![it]Ditta')
        tbl.formulaColumn('full_descr',"$nome || ' ' || $cognome || ' - ' || $ditta")
        