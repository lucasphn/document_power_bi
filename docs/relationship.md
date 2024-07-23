
## Modelagem e Arquitetura de Dados
<div class="table-responsive">
<table border="1" class="dataframe styled-table">
  <thead>
    <tr style="text-align: right;">
      <th>De Tabela</th>
      <th>De Coluna</th>
      <th>De Cardinalidade</th>
      <th>De</th>
      <th>Para Tabela</th>
      <th>Para Coluna</th>
      <th>Para Cardinalidade</th>
      <th>Para</th>
      <th>Esta Ativo?</th>
      <th>Sentido</th>
      <th>De Para</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>d_plano_de_contas</td>
      <td>CONTA_GRUPO</td>
      <td>*</td>
      <td>'d_plano_de_contas'[CONTA_GRUPO]</td>
      <td>d_contas_grupo</td>
      <td>COD_CONTA</td>
      <td>1</td>
      <td>'d_contas_grupo'[COD_CONTA]</td>
      <td>True</td>
      <td>Único</td>
      <td>'d_plano_de_contas'[CONTA_GRUPO] * &lt;- 1 'd_contas_grupo'[COD_CONTA]</td>
    </tr>
    <tr>
      <td>d_plano_de_contas</td>
      <td>CONTA_SUBGRUPO_1</td>
      <td>*</td>
      <td>'d_plano_de_contas'[CONTA_SUBGRUPO_1]</td>
      <td>d_contas_subgrupo_1</td>
      <td>COD_CONTA</td>
      <td>1</td>
      <td>'d_contas_subgrupo_1'[COD_CONTA]</td>
      <td>True</td>
      <td>Único</td>
      <td>'d_plano_de_contas'[CONTA_SUBGRUPO_1] * &lt;- 1 'd_contas_subgrupo_1'[COD_CONTA]</td>
    </tr>
    <tr>
      <td>d_plano_de_contas</td>
      <td>CONTA_SUBGRUPO_2</td>
      <td>*</td>
      <td>'d_plano_de_contas'[CONTA_SUBGRUPO_2]</td>
      <td>d_contas_subgrupo_2</td>
      <td>COD_CONTA</td>
      <td>1</td>
      <td>'d_contas_subgrupo_2'[COD_CONTA]</td>
      <td>True</td>
      <td>Único</td>
      <td>'d_plano_de_contas'[CONTA_SUBGRUPO_2] * &lt;- 1 'd_contas_subgrupo_2'[COD_CONTA]</td>
    </tr>
    <tr>
      <td>d_plano_de_contas</td>
      <td>CONTA_SUBGRUPO_3</td>
      <td>*</td>
      <td>'d_plano_de_contas'[CONTA_SUBGRUPO_3]</td>
      <td>d_contas_subgrupo_3</td>
      <td>COD_CONTA</td>
      <td>1</td>
      <td>'d_contas_subgrupo_3'[COD_CONTA]</td>
      <td>True</td>
      <td>Único</td>
      <td>'d_plano_de_contas'[CONTA_SUBGRUPO_3] * &lt;- 1 'd_contas_subgrupo_3'[COD_CONTA]</td>
    </tr>
    <tr>
      <td>f_contabil</td>
      <td>CentroCusto</td>
      <td>*</td>
      <td>'f_contabil'[CentroCusto]</td>
      <td>d_centro_de_custo</td>
      <td>Centro de Custo</td>
      <td>1</td>
      <td>'d_centro_de_custo'[Centro de Custo]</td>
      <td>True</td>
      <td>Único</td>
      <td>'f_contabil'[CentroCusto] * &lt;- 1 'd_centro_de_custo'[Centro de Custo]</td>
    </tr>
    <tr>
      <td>f_contabil</td>
      <td>ContaContabil</td>
      <td>*</td>
      <td>'f_contabil'[ContaContabil]</td>
      <td>d_plano_de_contas</td>
      <td>COD_CONTA</td>
      <td>1</td>
      <td>'d_plano_de_contas'[COD_CONTA]</td>
      <td>True</td>
      <td>Único</td>
      <td>'f_contabil'[ContaContabil] * &lt;- 1 'd_plano_de_contas'[COD_CONTA]</td>
    </tr>
    <tr>
      <td>f_contabil</td>
      <td>ContaSintetica</td>
      <td>*</td>
      <td>'f_contabil'[ContaSintetica]</td>
      <td>d_estrutura_dre</td>
      <td>Conta</td>
      <td>1</td>
      <td>'d_estrutura_dre'[Conta]</td>
      <td>True</td>
      <td>Único</td>
      <td>'f_contabil'[ContaSintetica] * &lt;- 1 'd_estrutura_dre'[Conta]</td>
    </tr>
    <tr>
      <td>f_contabil</td>
      <td>Data</td>
      <td>*</td>
      <td>'f_contabil'[Data]</td>
      <td>d_calendario</td>
      <td>Data</td>
      <td>1</td>
      <td>'d_calendario'[Data]</td>
      <td>True</td>
      <td>Único</td>
      <td>'f_contabil'[Data] * &lt;- 1 'd_calendario'[Data]</td>
    </tr>
    <tr>
      <td>f_contabil</td>
      <td>Filial</td>
      <td>*</td>
      <td>'f_contabil'[Filial]</td>
      <td>d_empresas</td>
      <td>cod_empresas</td>
      <td>1</td>
      <td>'d_empresas'[cod_empresas]</td>
      <td>True</td>
      <td>Único</td>
      <td>'f_contabil'[Filial] * &lt;- 1 'd_empresas'[cod_empresas]</td>
    </tr>
  </tbody>
</table>
</div>
        