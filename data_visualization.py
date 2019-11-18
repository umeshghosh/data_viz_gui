#!/usr/bin/env python
# version 0.1
# copyright Umesh Ghoshdastider

#import glob
from gooey import Gooey, GooeyParser
import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
import seaborn as sns

#def plot_table(a):
    #if a.ofile:
        #out=a.ofile
    #else:
        #out=a.ifile.split('.')[0]+'_plot_table.png'
    #f=np.loadtxt(a.ifile)
    #if a.xcol1:
        #for i in range(1,f.shape[1]):
            #plt.plot(f[:,0], f[:,i])
    #else:
        #plt.plot(f)
    #plt.savefig(out,dpi=150)
    #plt.show()

def csv_list_columns_index(a):
    d=pd.read_csv(a.ifile,index_col=0)
    out=a.ifile.split('.')[0]
    with open(out+'_columns.txt','w') as f:
        f.write('\n'.join(d.columns))
    with open(out+'_index.txt','w') as f:
        f.write('\n'.join( map(str, d.index.tolist() )))

def csv_box_plot(a):
    d=pd.read_csv(a.ifile,index_col=0)
#   d[a.columns.split()].boxplot()
    sns.boxplot(data=d[a.columns.split()])
    plt.show()
        
def csv_violin_plot(a):
    d=pd.read_csv(a.ifile,index_col=0)
    sns.violinplot(data=d[a.columns.split()], cut=1, linewidth=0)
    plt.show()
                
def csv_scatter_plot(a):
    d=pd.read_csv(a.ifile,index_col=0)
    sns.jointplot(x=d[a.X],y=d[a.Y], kind="reg")
    plt.show()   
    
def csv_many_scatter_plots(a):
    d=pd.read_csv(a.ifile,index_col=0)
    g=sns.PairGrid(d[a.columns.split()])
    g.map_lower(sns.kdeplot, cmap="Blues_d")
    g.map_upper(plt.scatter)
    g.map_diag(sns.kdeplot)
    plt.show()                  
    
@Gooey(default_size=(800, 600),advanced=True,  program_name='pyDataViz',) # (width,height)  
def main():
    p=GooeyParser(description='Data Visulaization ')
    sp=p.add_subparsers(help='commands', dest='command')

    #f1='plot_table'
    #sp1=sp.add_parser(f1)
    #a1=sp1.add_argument
    #a1('ifile', help='table input file (columns separated by spaces or tab), no header/ column name/ index', widget='FileChooser')
    #a1('-xcol1', action='store_true', help='column 1 is x-axis')
    #a1('-ofile', help='output file, default: ifile_plot_table.png', widget='FileChooser')
    #sp1.set_defaults(func=eval(f1))
    
    f2='csv_list_columns_index'
    sp2=sp.add_parser(f2)
    a2=sp2.add_argument
    a2('ifile', help='csv input file', widget='FileChooser')
    sp2.set_defaults(func=eval(f2))
    
    f3='csv_box_plot'
    sp3=sp.add_parser(f3)
    a3=sp3.add_argument
    a3('ifile', help='csv input file', widget='FileChooser')
    a3('columns', help='list column names separated by space')
    sp3.set_defaults(func=eval(f3))
    
    f4='csv_violin_plot'
    sp4=sp.add_parser(f4)
    a4=sp4.add_argument
    a4('ifile', help='csv input file', widget='FileChooser')
    a4('columns', help='list column names separated by space')
    sp4.set_defaults(func=eval(f4))
    
    f5='csv_scatter_plot'
    sp5=sp.add_parser(f5)
    a5=sp5.add_argument
    a5('ifile', help='csv input file', widget='FileChooser')
    a5('X', help='column name')
    a5('Y', help='column name')
    sp5.set_defaults(func=eval(f5))
    
    
    f6='csv_many_scatter_plots'
    sp6=sp.add_parser(f6)
    a6=sp6.add_argument
    a6('ifile', help='csv input file', widget='FileChooser')
    a6('columns', help='list column names separated by space')
    sp6.set_defaults(func=eval(f6))
    
    
    a=p.parse_args()

    a.func(a)



if __name__ == '__main__':
    main()
