# P2-INE5633
Código referente a segunda prova da disciplina INE5633

🌊 Propriedades da Água – Sistema Fuzzy

Este projeto implementa um sistema fuzzy para avaliar a qualidade da água, utilizando variáveis como aparência, pH e odor, com o objetivo de maximizar a qualidade. O projeto é composto por três etapas principais:

- Sistema Fuzzy baseado em regras.
- Modelo de Regressão (MLP) que simula o comportamento do sistema fuzzy.
- Otimizador inspirado na natureza, o PSO, para encontrar os melhores parâmetros que maximizam a qualidade da água.

-----------------------------------------------------------
🚀 Como executar

1. Clone este repositório:
git clone https://github.com/CunhaVanessa/P2-INE5633.git
cd P2-INE5633

2. Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Execute o código:
python src/main.py

-----------------------------------------------------------
📂 Estrutura do Projeto

-data               -> Dados gerados (opcional)
- notebooks          -> Análises exploratórias (opcional)
- outputs            -> Resultados, gráficos, relatórios
- src                -> Código-fonte
    - fuzzy_system.py -> Sistema fuzzy
    - regression.py   -> Modelo de regressão (MLP)
    - optimizer.py    -> Otimizador (PSO ou AG)
    -  main.py         -> Script principal que executa tudo
-  README.txt          -> Descrição do projeto
-  requirements.txt    -> Dependências do projeto
-  .gitignore          -> Arquivos ignorados no git
-  LICENSE             -> Licença MIT

-----------------------------------------------------------
🧠 Tecnologias utilizadas

- Python 3
- Scikit-Fuzzy
- Scikit-Learn
- Numpy
- Matplotlib

-----------------------------------------------------------
✍️ Autora

Vanessa Cunha (17100926)

-----------------------------------------------------------
📜 Licença

Projeto acadêmico sem fins comerciais.
