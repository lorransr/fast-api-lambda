---
marp: true
theme: uncover
_class: invert
_backgroundColor: #2c363f
---
![bg opacity:0.6 left](res/wesual-click-rsWZ-P9FbQ4-unsplash.jpg)

# Fast API + AWS Lambda 
---
![bg](#edd892)
## Explicando "serverless" 

# 🍞

---
* ## 🥚
* ## 🌾
* ## 🛒
* ## 🧑‍🍳 <- eu
* ## 🍞

---

* ## 🧑‍🍳 <- Joaquim
* ## 🧾
* #### ✨Magic✨
* ## 🍞 🍞 🍞
		
---
![bg](#edd892)
# Conceito

---
* Você Escreve o Código
* Entrega para um provedor (AWS, GCP , Azure ...)
* Eles cuidam de rodar o código em escala
* Paga por uso

---
![bg](#edd892)
# AWS Lambda


---
* 💻 Agnostico em Linguagem (Node, Java, Python, C#)
* 🏋️ Balanço de carga
* ⏫ Auto Scaling
* 🐞 Falhas
* 🔒 Segurança
* :anchor: Gestão do Sistema Operacional
* ⏬ Utilização

...

---
![bg](#edd892)
# Caso de Uso

---
![w:1100](res/lambda.png)

---
 > Você é cobrado pelo **número** de solicitações de suas funções e pela **duração**

---
Free Tier: 
* 1 milhão de solicitações gratuitas por mês 
* 400.000 GB/segundos de tempo de computação por mês.

---
![bg](#2c363f)
![](white)

# Fast API 

---

* Rápido

* Rápido para desenvolver

* Menos Bugs

* Intuitivo

* Easy Game
* Sucinto
* Robusto
  * production-ready
  * documentação interativa automatica
* Baseado em Padrões
---

* Serverless FastAPI roda na AWS Lambda usando Mangum e AWS API Gateway resolve roteamento dos requests para Lambda.
