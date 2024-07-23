
## Tabela: d_estrutura_dre
<div class="table-responsive">
<table border="1" class="dataframe styled-table">
  <thead>
    <tr style="text-align: right;">
      <th>Tabela</th>
      <th>Coluna</th>
      <th>Ordenada Por</th>
      <th>Formato</th>
      <th>Está Oculto?</th>
      <th>Expressão</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>d_estrutura_dre</td>
      <td>Categoria</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td>IF(         d_estrutura_dre[Índice_Conta]         IN {1,4,10,21,22,24,25,27}, "RECEITAS", "DESPESAS"     )</td>
    </tr>
    <tr>
      <td>d_estrutura_dre</td>
      <td>Conta</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td></td>
    </tr>
    <tr>
      <td>d_estrutura_dre</td>
      <td>Descrição</td>
      <td>Índice_Descrição</td>
      <td>String</td>
      <td>False</td>
      <td></td>
    </tr>
    <tr>
      <td>d_estrutura_dre</td>
      <td>Descrição_2</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td>VAR resultado = LOOKUPVALUE(d_contas_subgrupo_3[DESCRICAO_CONTA], d_contas_subgrupo_3[COD_CONTA], d_estrutura_dre[Conta], BLANK())  RETURN IF(d_estrutura_dre[Conta] = "42901", "IMPOSTOS E TAXAS",              IF( resultado = BLANK(), d_estrutura_dre[Descrição], resultado) )</td>
    </tr>
    <tr>
      <td>d_estrutura_dre</td>
      <td>Descrição_3</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td>VAR resultado = LOOKUPVALUE(d_contas_subgrupo_3[DESCRICAO_CONTA], d_contas_subgrupo_3[COD_CONTA], d_estrutura_dre[Conta], BLANK())  RETURN IF(d_estrutura_dre[Conta] = "42901", [Conta] &amp; " - " &amp; "IMPOSTOS E TAXAS",              IF( resultado = BLANK(), d_estrutura_dre[Descrição], [Conta] &amp; " - " &amp; resultado) )</td>
    </tr>
    <tr>
      <td>d_estrutura_dre</td>
      <td>Índice_Conta</td>
      <td></td>
      <td>Int</td>
      <td>False</td>
      <td></td>
    </tr>
    <tr>
      <td>d_estrutura_dre</td>
      <td>Índice_Descrição</td>
      <td></td>
      <td>Int</td>
      <td>False</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>
            