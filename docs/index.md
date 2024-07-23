# Documentação BI Contábil

Para acessar esta aplicação, visite <a href="https://app.powerbi.com/view?r=eyJrIjoiMTgwNWIxOWQtMTkyYS00ODlhLWIwOTktYWFjNzQ0YTE5MzY1IiwidCI6IjVhY2IyMzk2LWE2ZWEtNDY2Yy1iYmZlLWQ5YTM5MzZmZjUzOCJ9" target="_blank"> analytics.contabil</a>.


## Estrutura do Balanço Patrimonial

```mermaid
graph LR;

subgraph Demonstração de Resultado
    3_1["Receita Operacional"]
    3_2["Custo das Mercadorias Vendidas"]
    3_3["Despesas Operacionais"]
    3_4["Resultado Operacional"]
    3_5["Resultado Financeiro"]
end

subgraph Passivos
    2_1["Passivo Circulante"]
    2_2["Passivo Não Circulante"]
    2_3["Patrimônio Líquido"]
end

subgraph Ativos
    1_1["Ativo Circulante"]
    1_2["Ativo Não Circulante"]
    1_3["Investimentos"]
    1_4["Imobilizado"]
    1_5["Intangível"]
end


```

## Indicadores Financeiros

Nesta seção, vamos explorar alguns indicadores financeiros essenciais para avaliar a performance e a saúde financeira de uma empresa.

### EBITDA (Lucro Antes de Juros, Impostos, Depreciação e Amortização)

O **EBITDA** é um indicador financeiro amplamente utilizado para avaliar a lucratividade operacional de uma empresa, desconsiderando fatores não operacionais. Ele é calculado pela fórmula:

<div style="text-align: center;">
```mermaid
graph TD;
subgraph  
    EBITDA[EBITDA] --> |Receita Operacional| Receita[Receita Total]
    EBITDA --> |Custos Operacionais| Custos[Custos Operacionais]
    EBITDA --> |Despesas Operacionais| Despesas[Despesas Operacionais]
end
```
</div>

O EBITDA é útil para comparar a performance operacional entre empresas de diferentes setores e para analisar tendências ao longo do tempo.

### Margem Bruta

A **Margem Bruta** é calculada como a porcentagem de lucro bruto em relação à receita total. Ela é obtida pela fórmula:

<div style="text-align: center;">
```mermaid
graph TD;
subgraph  
    Margem[Margem Bruta] --> |Receita| Receita2[Receita Total]
    Margem --> |CPV| CPV[Custo dos Produtos Vendidos]
end
```
</div>

Onde:
- **CPV** = Custo dos Produtos Vendidos

A Margem Bruta indica a eficiência da empresa na geração de lucro a partir da venda de seus produtos ou serviços.

### Margem Líquida

A **Margem Líquida** representa a porcentagem de lucro líquido em relação à receita total. É calculada pela fórmula:

<div style="text-align: center;">
```mermaid
graph TD;
subgraph   
    MargemL[Margem Líquida] --> |Lucro Líquido| Lucro[Lucro Líquido]
    MargemL --> |Receita| Receita3[Receita Total]
end
```
</div>

A Margem Líquida é um indicador-chave da rentabilidade da empresa, levando em conta todos os custos e despesas, incluindo impostos e juros.

### Liquidez Geral

A **Liquidez Geral** é uma medida da capacidade de uma empresa de cumprir suas obrigações de curto e longo prazo. É calculada pela fórmula:

<div style="text-align: center;">
```mermaid
graph TD;
subgraph  
    Liquidez[Liquidez Geral] --> |Ativos Circulantes| Ativos[Ativos Circulantes]
    Liquidez --> |Passivos Circulantes| Passivos[Passivos Circulantes]
end
```
</div>

Um índice superior a 1 indica que a empresa possui mais ativos líquidos do que passivos a curto prazo, o que é positivo em termos de solvência financeira.

### Liquidez Imediata (ou Liquidez Seca)

A **Liquidez Imediata**, também conhecida como **Liquidez Seca**, é uma medida mais restrita da capacidade de pagamento imediato de uma empresa. É calculada pela fórmula:

<div style="text-align: center;">
```mermaid
graph TD;
subgraph  
    LiquidezI[Liquidez Imediata] --> |Ativos Circulantes - Estoques| Ativos2[Ativos Circulantes - Estoques]
    LiquidezI --> |Passivos Circulantes| Passivos2[Passivos Circulantes]
end
```
</div>

Esse indicador exclui os estoques da equação para fornecer uma visão mais conservadora da capacidade da empresa de pagar suas dívidas de curto prazo apenas com ativos líquidos imediatos.

