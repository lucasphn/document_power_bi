
## Medidas e Cálculos
<div class="table-responsive">
<table border="1" class="dataframe styled-table">
  <thead>
    <tr style="text-align: right;">
      <th>Tabela</th>
      <th>Medida</th>
      <th>Expressao</th>
      <th>Formato</th>
      <th>Está Oculto?</th>
      <th>Descrição</th>
      <th>Tipo</th>
      <th>Pasta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>💡 medidas</td>
      <td>(%) EBTIDA</td>
      <td>[Lucro Operacional Líquido (EBTIDA)]/[Receita Líquida]</td>
      <td>0.00%;-0.00%;0.00%</td>
      <td>False</td>
      <td>Lucros antes de Juros, Impostos, Depreciação e Amortização.</td>
      <td>Double</td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>(-) Custos Diretos de Produção</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_SUBGRUPO_1] = "41" )</td>
      <td></td>
      <td>False</td>
      <td>Calcula o custo direto de produção.</td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>(-) Deduções e Abatimentos</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_SUBGRUPO_1] = "32" )</td>
      <td></td>
      <td>False</td>
      <td>Calcula as deduções e abatimentos da receita bruta.</td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>(-) Despesas Financeiras</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_SUBGRUPO_2] = "471" )</td>
      <td></td>
      <td>False</td>
      <td>Despesas Financeiras</td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>(-) Despesas Operacionais</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_SUBGRUPO_1] = "42" )</td>
      <td></td>
      <td>False</td>
      <td>Despesas Operacionais</td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>(+) Receitas Financeiras</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_SUBGRUPO_2] = "472" )</td>
      <td></td>
      <td>False</td>
      <td>Receitas Financeiras</td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>AH</td>
      <td>VAR regra_dateadd = SELECTEDVALUE(d_calendario[MesAbrevDesc], "Ano") VAR periodo_anterior_year =   CALCULATE(     [Saldo_Conta],     DATEADD(         d_calendario[Data], -1, YEAR     ) )  VAR periodo_anterior_month =   CALCULATE(     [Saldo_Conta],     DATEADD(         d_calendario[Data], -1, MONTH     ) )  VAR definir_calculo =  IF(regra_dateadd = "Ano", periodo_anterior_year, periodo_anterior_month)  VAR varicao_periodo = ([Saldo_Conta]/definir_calculo) - 1   RETURN IF(definir_calculo = 0, BLANK() , varicao_periodo )</td>
      <td>0.00%;-0.00%;0.00%</td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>AV</td>
      <td>VAR conta_sintetica = SELECTEDVALUE(d_estrutura_dre[Índice_Descrição])  VAR receita_liquida =   CALCULATE(     [Receita Líquida], ALL(d_estrutura_dre) )  VAR receita_bruta =   CALCULATE(     [Receita Bruta], ALLSELECTED(d_estrutura_dre) )  VAR saldo_conta =   IF(     [Saldo_Conta] &lt; 0 , -([Saldo_Conta]), [Saldo_Conta])  return      SWITCH(         conta_sintetica,         1, "-",         2, saldo_conta/receita_bruta,         saldo_conta/receita_liquida     )</td>
      <td>0.00%;-0.00%;0.00%</td>
      <td>False</td>
      <td></td>
      <td></td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Endividamento Geral</td>
      <td>-- Mostra a proporção do financiamento da empresa por meio de dívidas em relação ao seu total de ativos.  VAR _AtivoTotal = CALCULATE([Saldo Atual (Acumulado)], d_contas_grupo[COD_CONTA] = "1") VAR _PassivoTotal = -CALCULATE([Saldo Atual (Acumulado)], d_contas_grupo[COD_CONTA] = "2")  RETURN  DIVIDE(_PassivoTotal, _AtivoTotal, 0)</td>
      <td>0.00</td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Filtro Balanço</td>
      <td>VAR _saldo_anterior = [Saldo Anterior (Acumulado)] VAR _mov_periodo = [Saldo] VAR _saldo_atual = [Saldo Atual (Acumulado)] VAR _debito = [Lançamento a Débito] VAR _credito = [Lançamento a Crédito]   RETURN       IF(         OR(_saldo_anterior = 0, _saldo_anterior = BLANK ()) &amp;&amp;          OR(_mov_periodo = 0, _mov_periodo = BLANK()) &amp;&amp;          OR(_saldo_atual = 0, _saldo_atual = BLANK()) &amp;&amp;          OR(_debito = 0, _debito = BLANK()) &amp;&amp;          OR(_credito = 0, _credito = BLANK()),          "Sem Movimento",          "Com Movimento"         )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>String</td>
      <td>Regras de Filtros de Dados</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Lançamento a Crédito</td>
      <td>CALCULATE(     SUM('f_contabil'[Valor]),     f_contabil[TipoOperacao] = "Crédito" )</td>
      <td>#,0</td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Partidas Dobradas</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Lançamento a Débito</td>
      <td>CALCULATE(     SUM('f_contabil'[Valor]),     f_contabil[TipoOperacao] = "Débito" )</td>
      <td>#,0</td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Partidas Dobradas</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Liquidez Corrente</td>
      <td>-- Indica a capacidade da empresa de pagar suas obrigações de curto prazo com seus ativos circulantes.  VAR _AtivoCirculante = CALCULATE([Saldo Atual (Acumulado)], d_contas_subgrupo_1[COD_CONTA] = "11") VAR _PassivoCirculante = -(CALCULATE([Saldo Atual (Acumulado)], d_contas_subgrupo_1[COD_CONTA] = "21"))  RETURN DIVIDE(_AtivoCirculante, _PassivoCirculante, 0)</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Liquidez Imediata</td>
      <td>-- Avalia a capacidade da empresa de pagar suas obrigações de curto prazo sem considerar os estoques.  VAR _AtivoCirculante_OmitindoEstoque = CALCULATE([Saldo Atual (Acumulado)], FILTER(d_contas_subgrupo_2, d_contas_subgrupo_2[REGISTRO_PAI_2] = "11" &amp;&amp;  d_contas_subgrupo_2[COD_CONTA] &lt;&gt;  "118")) VAR _PassivoCirculante = -(CALCULATE([Saldo Atual (Acumulado)], d_contas_subgrupo_1[COD_CONTA]  = "21"))  RETURN    DIVIDE(_AtivoCirculante_OmitindoEstoque, _PassivoCirculante, 0)</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Lucro Operacional Bruto</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_GRUPO] = "3" || d_plano_de_contas[CONTA_SUBGRUPO_1] = "41" )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Lucro Operacional Líquido (EBTIDA)</td>
      <td>[Lucro Operacional Bruto] - (-[(-) Despesas Operacionais])</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Margem Bruta</td>
      <td>[Lucro Operacional Bruto] / [Receita Líquida]</td>
      <td>0.00%;-0.00%;0.00%</td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Margem Resultado Líquido</td>
      <td>[Saldo] / [Receita Líquida]</td>
      <td>0.00%;-0.00%;0.00%</td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Provisões IRPJ e CSLL</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_SUBGRUPO_1] = "49" )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Receita Bruta</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_SUBGRUPO_1] = "31" )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Receita Bruta (Menos Devoluções)</td>
      <td>VAR devolucao =   CALCULATE(     [Saldo], d_plano_de_contas[CONTA_SUBGRUPO_3] = "32101"     )      RETURN [Receita Bruta] - (-devolucao)</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Receita Líquida</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_GRUPO] = "3" )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Resultado antes do IRPJ e CSLL</td>
      <td>CALCULATE(     [Saldo],     d_plano_de_contas[CONTA_SUBGRUPO_1] &lt;&gt; "49" )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Resultado Líquido</td>
      <td>[Resultado antes do IRPJ e CSLL] - (-[Provisões IRPJ e CSLL])</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>DRE</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>ROA</td>
      <td>-- Mede a eficiência da empresa em gerar lucro a partir de seus ativos.  VAR _AtivoTotal = CALCULATE([Saldo Atual (Acumulado)], d_contas_grupo[COD_CONTA] = "1")  RETURN DIVIDE([Lucro Operacional Bruto], _AtivoTotal, 0)</td>
      <td>0.00%;-0.00%;0.00%</td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>ROE</td>
      <td>-- O ROE é um indicador utilizado para mensurar a capacidade que uma empresa tem de agregar valor a si mesma utilizando seus próprios recursos. Ou seja, o ROE é utilizado para medir a rentabilidade de uma companhia ao mostrar o quanto ela pode gerar de lucro com o dinheiro investido por acionistas.  VAR _patrimonio_liquido = - CALCULATE([Saldo Atual (Acumulado)], d_contas_subgrupo_1[COD_CONTA] = "23")  RETURN DIVIDE([Lucro Operacional Líquido (EBTIDA)], _patrimonio_liquido, 0)</td>
      <td>#,0.00%;-#,0.00%;#,0.00%</td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Analytics</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Rótulo Saldo</td>
      <td>VAR vValor = [Saldo_Conta]  RETURN      SWITCH(         TRUE(),         vValor &gt;= 1000000000, FORMAT(vValor, "0,,,.0 Bi"),         vValor &gt;= 1000000, FORMAT(vValor, "0,,.0 Mi"),         vValor &gt;= 1000, FORMAT(vValor, "0,.0 Mil"),         FORMAT(vValor, "0")     )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>String</td>
      <td>Máscaras de Números</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Rótulo Saldo Despesas</td>
      <td>VAR vValor = [Saldo_Despesas]  RETURN      SWITCH(         TRUE(),         vValor &gt;= 1000000000, FORMAT(vValor, "0,,,.0 Bi"),         vValor &gt;= 1000000, FORMAT(vValor, "0,,.0 Mi"),         vValor &gt;= 1000, FORMAT(vValor, "0,.0 Mil"),         FORMAT(vValor, "0")     )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>String</td>
      <td>Máscaras de Números</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Saldo</td>
      <td>VAR _contexto = SELECTEDVALUE(d_plano_de_contas[CLASSIFICAO DE CONTA]) VAR _calculo_para_dre = [Lançamento a Crédito] - [Lançamento a Débito] VAR _calculo_para_balanco_patrimonial = [Lançamento a Débito] - [Lançamento a Crédito]  RETURN     -- Se o contexto de cálculo for entre contas da DRE, usar cálculo da DRE, caso contrário, utilizar o cálculo para balanço patrimonial.     SWITCH(_contexto, "DRE", _calculo_para_dre, _calculo_para_balanco_patrimonial)</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Saldos</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Saldo Anterior (Acumulado)</td>
      <td>VAR _data_contexto = MIN(d_calendario[Data])  RETURN CALCULATE([Saldo], FILTER(ALL(d_calendario), d_calendario[Data] &lt; _data_contexto))</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Saldos</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Saldo Atual (Acumulado)</td>
      <td>[Saldo Anterior (Acumulado)] + [Saldo]</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Saldos</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Saldo_Conta</td>
      <td>VAR conta_sintetica = SELECTEDVALUE(d_estrutura_dre[Índice_Descrição])   VAR receita_liquida =   CALCULATE(     [Receita Líquida],      ALLSELECTED(d_estrutura_dre) )   VAR lucro_bruto =   CALCULATE(     [Lucro Operacional Bruto],      ALLSELECTED(d_estrutura_dre) )  VAR lucro_liquido =   CALCULATE(     [Lucro Operacional Líquido (EBTIDA)],     ALLSELECTED(d_estrutura_dre) )  VAR resultado_antes_ir_csll =   CALCULATE(     [Resultado antes do IRPJ e CSLL],     ALLSELECTED(d_estrutura_dre) )  VAR resultado_liquido =   CALCULATE(     [Resultado Líquido],      ALLSELECTED(d_estrutura_dre) )   RETURN       SWITCH(         conta_sintetica,         3, receita_liquida,         5, lucro_bruto,         7, lucro_liquido,         10, resultado_antes_ir_csll,         12, resultado_liquido,         [Saldo]     )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Saldos</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>Saldo_Despesas</td>
      <td>- CALCULATE(     [Saldo_Conta], d_estrutura_dre[Categoria] = "DESPESAS" )</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Saldos</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>String Saldo Anterior</td>
      <td>VAR _ativo = CALCULATE([Saldo Anterior (Acumulado)], d_contas_grupo[COD_CONTA] = "1") VAR _passivo = -CALCULATE([Saldo Anterior (Acumulado)], d_contas_grupo[COD_CONTA] = "2") VAR _saldo_atual_ajustado = _ativo + _passivo  RETURN _saldo_atual_ajustado</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Máscaras de Números</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>String Saldo Atual</td>
      <td>VAR _ativo = CALCULATE([Saldo Atual (Acumulado)], d_contas_grupo[COD_CONTA] = "1") VAR _passivo = -CALCULATE([Saldo Atual (Acumulado)], d_contas_grupo[COD_CONTA] = "2") VAR _saldo_atual_ajustado = _ativo + _passivo  RETURN _saldo_atual_ajustado</td>
      <td></td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Máscaras de Números</td>
    </tr>
    <tr>
      <td>💡 medidas</td>
      <td>teste</td>
      <td>VAR _saldo_anterior = [Saldo Anterior (Acumulado)]  RETURN     _saldo_anterior     --IF(OR(_saldo_anterior = 0 , _saldo_anterior = BLANK()), "Sem movimento", _saldo_anterior)</td>
      <td>0.0000000000</td>
      <td>False</td>
      <td></td>
      <td>Double</td>
      <td>Testes práticos</td>
    </tr>
  </tbody>
</table>
</div>
        