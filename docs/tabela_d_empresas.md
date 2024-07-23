
## Tabela: d_empresas
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
      <td>d_empresas</td>
      <td>cidade</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td></td>
    </tr>
    <tr>
      <td>d_empresas</td>
      <td>cnpj</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td></td>
    </tr>
    <tr>
      <td>d_empresas</td>
      <td>cod_empresas</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td></td>
    </tr>
    <tr>
      <td>d_empresas</td>
      <td>nome</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td></td>
    </tr>
    <tr>
      <td>d_empresas</td>
      <td>nome_2</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td>SWITCH(     TRUE(),     d_empresas[cod_empresas] = "01", "JOINVILLE",     d_empresas[cod_empresas] = "02", "RESENDE",     d_empresas[cod_empresas] = "03", "RESENDE METAIS",     d_empresas[cod_empresas] = "04", "CURITIBA" )</td>
    </tr>
    <tr>
      <td>d_empresas</td>
      <td>uf</td>
      <td></td>
      <td>String</td>
      <td>False</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>
            