# # -*- coding: UTF-8 -*-

class AppPref(object):
    
    def permission_carte(self,**kwargs):
        return 'admin'

    def prefpane_unlocode(self,parent,**kwargs):
        pane = parent.contentPane(**kwargs)
        fb = pane.formbuilder(cols=1,border_spacing='3px', margin='10px')
        fb.div('Press button to load/save default data')
        fb.button('Load data',action="""genro.mainGenroWindow.genro.publish('open_batch');
                                        genro.serverCall('_package.unlocode.loadStartupData',null,function(){});
                                        """,_tags='_DEV_')
        fb.button('Save data',action="""genro.mainGenroWindow.genro.publish('open_batch');
                                        genro.serverCall('_package.unlocode.createStartupData',null,function(){});
                                    """,_tags='_DEV_')
