import pandas as pd

def converter_unidades(df):
    #display(list(df['unid'].unique()))
    df.loc[:, 'unid'] = df['unid'].astype(str)
    df.loc[:, 'unid'] = df['unid'].astype(str).str.lower()
    df.loc[:, 'unid'] = df['unid'].str.strip()
    
    #df.loc[:, 'unid'] = df['unid'].str.lower() #
    df.loc[:, 'unid'] = df['unid'].replace('0', '')
    df.loc[:, 'unid'] = df['unid'].replace('m³', 'm3')
    
    df.loc[:, 'unid'] = df['unid'].replace('mês', 'mes')
    df.loc[:, 'unid'] = df['unid'].replace('vb x mês', 'mes')
    
    df.loc[:, 'unid'] = df['unid'].replace('m²', 'm2')
    df.loc[:, 'unid'] = df['unid'].replace('r$/m²', 'm2')
    
    df.loc[:, 'unid'] = df['unid'].replace('m²/mês', 'm2/mes')
    
    df.loc[:, 'unid'] = df['unid'].replace('ml', 'm')# entendo que seja metro linear
    
    df.loc[:, 'unid'] = df['unid'].replace('pç', 'un')
    df.loc[:, 'unid'] = df['unid'].replace('pc', 'un')
    df.loc[:, 'unid'] = df['unid'].replace('cj', 'un')
    df.loc[:, 'unid'] = df['unid'].replace('ud', 'un')
    df.loc[:, 'unid'] = df['unid'].replace('und', 'un')
    
    df.loc[:, 'unid'] = df['unid'].replace('gb', 'vb')
    
    df.loc[:, 'unid'] = df['unid'].replace('hora', 'h')
    
    df.loc[:, 'unid'] = df['unid'].replace('unid.', 'un')
    df.loc[:, 'unid'] = df['unid'].replace('unid', 'un')
    df.loc[:, 'unid'] = df['unid'].replace('um', 'un')
    df.loc[:, 'unid'] = df['unid'].replace('un.', 'un')
    
    df.loc[:, 'unid'] = df['unid'].replace('ton', 't')
    
    df.loc[:, 'unid'] = df['unid'].replace('m3 x km', 'm3xkm')
    df.loc[:, 'unid'] = df['unid'].replace('km x m³', 'm3xkm')
    df.loc[:, 'unid'] = df['unid'].replace('m³ x km', 'm3xkm')
    df.loc[:, 'unid'] = df['unid'].replace('m³.km', 'm3xkm')
    df.loc[:, 'unid'] = df['unid'].replace('m³xkm', 'm3xkm')
    
    df.loc[:, 'unid'] = df['unid'].replace('dm³', 'dm3')
    
    unid_unicas =list(df['unid'].unique())
    #display(unid_unicas)
    return df

def nome_minusculo(df):
    #cols_str = ['nome','unid']
    #df1[cols_str] = df[cols_str].astype(str)
    df.loc[:, 'nome'] = df['nome'].astype(str).str.lower()
    #df['nome'].str.lower()
    #df['unid'].str.lower()
    #df.loc[:, 'nome'] = df['nome'].str.lower() #
    #df.loc[:, 'unid'] = df['unid'].str.lower()
    return df

def agrupar_df(df,df_grupo):
    df1 = df.copy()
        
    df1.loc[:,'disciplina']='vazio'
    df1.loc[:,'etapa']='vazio'
    df1.loc[:,'grupo']='vazio'
    df1.loc[:,'subgrupo']='vazio'
    df1.loc[:,'tipo']='vazio'
    #df1.loc[:,'parcial'] = 0

    colunas = df_grupo.columns
    colunas_contem = [coluna for coluna in colunas if 'contem' in coluna]

    for i, lin in df_grupo.iterrows():
        mask_unid = df1['unid']==lin['unid']

        mask_ignorar=mask_unid
        if lin['ignorar']!=0:
            #display(lin['ignorar'])
            mask_ignorar = ~df1['nome'].str.contains(str(lin['ignorar']), case=False)

        mask_contem = mask_unid    
        for i,contem in enumerate(colunas_contem):
            if lin[contem]!=0:
                #print(lin[contem])
                mask_contem_loop = df1['nome'].str.contains(str(lin[contem]), case=False)
                mask_contem = mask_contem & mask_contem_loop

        filtro = mask_unid&mask_ignorar&mask_contem

        df1.loc[filtro,'disciplina'] = lin['disciplina']
        df1.loc[filtro,'etapa'] = lin['etapa']
        df1.loc[filtro,'grupo'] = lin['grupo']
        df1.loc[filtro,'subgrupo'] = lin['subgrupo']
        df1.loc[filtro,'tipo'] = lin['tipo']
        df1.loc[filtro,'apelido'] = lin['apelido']
        #display(df2[filtro])

        #df5 = pd.concat([df3, df4], ignore_index=True)
    etapas_unicas = df1['etapa'].unique()
    #display(etapas_unicas)
    escolha= etapas_unicas[2]
    #display(escolha)
    df_filtro = df1[df1['etapa']==etapas_unicas[2]]
    return df1#display(df_filtro)
