# Seattle Lodging Data Analysis 🏡📊

![Python](https://img.shields.io/badge/-Python-blue?logo=python)
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-f7931e?logo=scikit-learn)

Repositório de referência para **transformação, manipulação e modelagem** de dados de hospedagens na cidade de Seattle.
Preparado como projeto‑vitrine para recrutadores e colegas de Data Science.

## Estrutura Recomendada
```
.
├── data/                  # datasets brutos
│   └── dados_hospedagem.json
├── notebooks/
│   └── projeto_final_pandas_hospedagem_rev.ipynb
├── src/                   # módulos auxiliares (opcional)
├── environment.yml        # dependências Conda
└── README.md
```

## Ambiente
```bash
conda env create -f environment.yml
conda activate seattle-lodging
jupyter lab
```

## Principais Insights
* **Preço médio** por noite apresenta forte assimetria; maioria dos listings abaixo de 200 USD.
* **Avaliação geral** mostra correlação positiva moderada com preço (ρ ≈ 0.36).
* **RandomForest** previu preços com R² médio ≈ 0.62 em 5‑fold CV.
* **Clusterização** revelou 3 perfis de imóveis (econômico, intermediário e premium).

## Próximos Passos
1. Criar dashboard Streamlit para exploração interativa.
2. Integrar dados climáticos e sazonais.
3. Realizar análise de sentimento nas reviews e adicionar como feature.

---

> Projeto desenvolvido por **Mauro Roberto Barbosa Cahu** – [LinkedIn](https://www.linkedin.com/in/mauro-cahu-159a05273)  
> 2025
