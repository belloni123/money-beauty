# MONEY BEAUTY

**Uma habilidade de IA para organizar as vendas e o atendimento de clínicas de saúde, beleza e bem-estar.**

MONEY BEAUTY reúne a base de conhecimento do **WOLF — Especialista em Vendas High Ticket**, o **framework comercial de 7 etapas** e uma aplicação prática para clínicas. Ajuda donos, gestores, recepcionistas e consultores a criar mensagens, esclarecer objeções, apresentar condições, organizar avaliações e acompanhar o funil comercial.

É um conjunto de instruções e arquivos de referência para a sua IA. Não é um modelo treinado, sistema de agenda, prontuário ou integração automática com WhatsApp. A IA continua sujeita às capacidades e aos limites da plataforma utilizada.

## Comece em 5 minutos, sem programar

1. Baixe [as instruções](dist/MONEY-BEAUTY-INSTRUCOES.md) e [o conhecimento completo](dist/MONEY-BEAUTY-CONHECIMENTO.md). Ao abrir o arquivo no GitHub, use a opção de baixar o arquivo bruto, evitando salvar a página HTML.
2. Na sua IA, abra uma conversa ou espaço de trabalho que aceite arquivos.
3. Anexe o arquivo de conhecimento e cole o conteúdo das instruções no campo de instruções, quando disponível; em uma conversa comum, envie as instruções como primeira mensagem.
4. Informe qual clínica será atendida. Preencha uma cópia privada do [contexto da clínica](skills/money-beauty/templates/contexto-clinica.md) e da [tabela de preços](skills/money-beauty/templates/tabela-precos.csv), ou escolha explicitamente o exemplo Althea.
5. Envie: **“Atue como MONEY BEAUTY. Leia as instruções e o conhecimento anexados. Minha clínica é [nome], atende [serviços] em [cidade]. Quero melhorar [objetivo]. Comece pelo contexto que estiver faltando.”**

Depois, teste: “Uma pessoa perguntou o preço pelo WhatsApp. Use minha tabela e escreva uma resposta curta, sem inventar condições.” A IA deve informar o preço conhecido e oferecer um próximo passo opcional. Se não conseguir ler os anexos, envie os arquivos pertinentes separadamente. Não basta colar o link do GitHub: muitas IAs não leem todo o repositório automaticamente.

## O que está incluído

- Os **11 arquivos originais de conhecimento do WOLF**, preservados e inventariados por SHA-256: sete bases de livros e quatro materiais de aplicação.
- Identidade e instruções novas como **MONEY BEAUTY**, especializadas em clínicas.
- Framework de 7 etapas com critérios de execução e entregáveis para clínicas.
- Scripts para WhatsApp, Instagram, ligação, avaliação, proposta, follow-up e pós-atendimento.
- Objeções, estrutura de ofertas e métricas comerciais com definições.
- Perfil **Althea**, com os 19 registros da tabela comercial e 15 durações do documento fornecido.
- Modelos para cada clínica cadastrar suas próprias informações e preços.
- Pacote ZIP de skill e arquivos de instruções/conhecimento para outras plataformas.

### Base WOLF preservada

| Material | Aplicação |
| --- | --- |
| Expert Secrets — Russell Brunson | Posicionamento, narrativa e funis |
| Gatilhos Mentais — Gustavo Ferreira | Comunicação e persuasão com informação verificável |
| SPIN Selling — Neil Rackham | Compreensão consultiva do objetivo |
| Negocie Como Se Sua Vida Dependesse Disso — Chris Voss | Escuta, empatia e negociação |
| Way of the Wolf — Jordan Belfort | Condução e diagnóstico de confiança |
| The Challenger Sale — Matthew Dixon / Brent Adamson | Educação e adaptação da conversa |
| $100M Money Models — Alex Hormozi | Ofertas, alternativas e continuidade |
| Síntese integrada | Escolha e combinação de metodologias |
| Playbook de scripts | Modelos comerciais históricos |
| Playbook de objeções | Diagnóstico e repertório de respostas |
| Guia de implementação | Organização e indicadores |

São os materiais disponíveis no plugin WOLF versão 0.4.1, não os livros integrais nem conhecimento interno inacessível do modelo. A base original é preservada para consulta; a camada MONEY BEAUTY adapta seu uso. Regras dos textos históricos não substituem as instruções atuais.

## Como funciona o framework de 7 etapas

Adaptado do [painel de Gabriel Magioli / Consultoria UP](https://frameworkcomercial.netlify.app/painel-7-etapas-fluxo.html), com atribuição e aplicação próprias para clínicas.

| Etapa | Pergunta da clínica | Entrega |
| --- | --- | --- |
| 1. ICP | Quem atendemos e o que essa pessoa busca? | Perfil e critérios de atendimento comercial |
| 2. Benefícios | Como explicar o serviço em relação ao objetivo declarado? | Matriz de características, benefícios possíveis e limites |
| 3. Etapas e Estatística | Onde a conversa avança ou trava? | Jornada, funil e indicadores |
| 4. Processo Comercial | O que fazer em cada momento? | Scripts, critérios de avanço e encaminhamentos |
| 5. Máquina de Vendas | Quem cuida de cada parte? | Papéis, treinamento e rotina |
| 6. Canais de Aquisição | De onde vêm os contatos adequados? | Plano e medição por canal |
| 7. Arquitetura de Receita | Como integrar aquisição, retenção e continuidade? | Ofertas aprovadas, capacidade, receita e margem |

As sete etapas organizam a gestão. Dentro da conversa, a jornada é abordagem → conexão → engajamento → desejo → conversão, com informação clara e liberdade de escolha. Os percentuais de previsibilidade do painel de origem não são garantias de resultado. Veja a [aplicação detalhada](skills/money-beauty/references/framework-7-etapas.md).

## Instalação no Codex

Para quem utiliza skills locais, com Git instalado:

```bash
git clone https://github.com/belloni123/money-beauty.git
cd money-beauty
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/money-beauty "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Se já existir uma pasta `money-beauty` no destino, faça uma cópia antes de substituí-la. Abra uma nova conversa e use:

```text
Use $money-beauty para melhorar o atendimento da minha clínica.
Minha tabela aprovada está em [arquivo]. Quero começar pelo WhatsApp.
```

A pasta instalada precisa conter `SKILL.md`, `references/`, `templates/` e `agents/`. O download ZIP de todo o repositório não é a pasta de skill; copie a pasta indicada acima.

## Instalação no Claude

### Claude com Skills

1. Baixe [money-beauty.skill.zip](dist/money-beauty.skill.zip).
2. Na área **Customize / Personalizar → Skills**, procure a opção de adicionar ou enviar uma skill. A disponibilidade depende da conta e da habilitação de execução de código.
3. Envie o ZIP específico da skill, sem descompactar. Ele contém uma pasta `money-beauty` com `SKILL.md` e as referências.
4. Ative a skill e peça: “Use MONEY BEAUTY para criar um roteiro de atendimento para minha clínica.”
5. Informe contexto e preços aprovados. Se a opção de Skills não estiver disponível, use o método de instruções e anexos do início do README.

Fonte: [guia oficial de skills do Claude](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

### Claude Code

Depois de baixar o repositório, na raiz do projeto em que deseja usar a habilidade:

```bash
mkdir -p .claude/skills
cp -R /caminho/para/money-beauty/skills/money-beauty .claude/skills/
```

Substitua `/caminho/para/money-beauty` pelo caminho do download. Inicie uma nova sessão e peça o uso da habilidade. [Documentação oficial](https://platform.claude.com/docs/en/managed-agents/skills).

## Uso no ChatGPT

Use primeiro o método universal de instruções e anexos acima. Para uma configuração persistente, utilize o recurso de instruções e arquivos disponível na sua conta ou espaço de trabalho.

Se você já tem um GPT editável, pode colocar o conteúdo de `MONEY-BEAUTY-INSTRUCOES.md` nas instruções e anexar `MONEY-BEAUTY-CONHECIMENTO.md` como conhecimento. Nomeie como **MONEY BEAUTY**, teste e salve conforme as permissões da conta. Em 17/11/2026, a documentação da OpenAI informa restrições de criação de novos GPTs e transição para plugins; por isso este README não depende de criar um GPT novo. [Disponibilidade oficial](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts).

## Uso no Gemini e outras IAs

No Gemini, use o método universal. Se sua conta ainda oferecer criação de Gems, defina o nome MONEY BEAUTY, cole as instruções e adicione o arquivo de conhecimento. Em novembro de 2026, o Google informa transição de Gems para skills em contas pessoais; siga a interface e as permissões da sua conta. [Guia oficial do Gemini](https://support.google.com/gemini/answer/15146780?hl=en).

Em outras IAs que aceitam instruções e arquivos, use os mesmos dois arquivos. Isso não garante importação nativa de skills, persistência ou leitura de todo o material. Em caso de limite de tamanho, envie a skill principal e somente as referências relevantes da pasta `skills/money-beauty/references/`, mantendo as instruções como prioridade.

## Como configurar sua clínica

1. Abra o [modelo de contexto](skills/money-beauty/templates/contexto-clinica.md) e crie uma cópia privada.
2. Preencha serviços, localização, responsáveis, canais, avaliação, duração e regras comerciais.
3. Preencha a [tabela de preços](skills/money-beauty/templates/tabela-precos.csv): avulso/pacote, quantidade, total, preço mínimo ou sob consulta, condições e validade.
4. Envie esses arquivos à sua IA e diga: “Use estes dados para [nome da clínica]. Não use os preços do exemplo Althea.”
5. Revise os primeiros scripts com a equipe antes de utilizá-los no atendimento.

O [perfil Althea](skills/money-beauty/references/perfil-althea.md) foi extraído do documento fornecido por Felipe em 17/11/2026 e serve como exemplo concreto. Não é tabela universal nem consulta em tempo real. Há serviços sob consulta e informações ausentes, como endereço, contato, juros e política de cancelamento. Confirme a vigência dos dados antes de usar com clientes.

## Exemplos de pedidos

```text
Diagnostique o comercial da minha clínica pelas 7 etapas.
Temos [contatos], [agendamentos] e [comparecimentos] no período [datas].
Mostre a primeira lacuna, uma ação e como medir.
```

```text
Use o perfil Althea como exemplo. Uma pessoa quer uma sessão avulsa
de Eletroface. Responda usando as condições da fonte e sinalize
que a vigência precisa ser confirmada antes do envio.
```

```text
Crie respostas acolhedoras para “está caro”, “vou pensar” e
“tenho medo do procedimento”, sem pressão nem promessa de resultado.
```

```text
Monte um plano de 30 dias para organizar recepção, agendamentos,
comparecimento e acompanhamento. Não invente metas ou dados.
```

## Limites de uso em saúde

MONEY BEAUTY cuida do processo comercial. Indicação, diagnóstico, contraindicação, prescrição e cuidado clínico pertencem aos profissionais habilitados. Documentos comerciais não comprovam eficácia. Alegações não validadas do documento original, como promessas sobre detox, imunidade, biorressonância e percentuais de recrutamento muscular, não foram adotadas como argumentos aprovados.

Preços devem ser claros; recusas devem ser respeitadas; não se deve criar urgência artificial, prometer cura ou vender procedimentos sem adequação. A habilidade não envia mensagens, agenda ou cobra sozinha. Não coloque prontuários, fotos de pacientes, documentos pessoais, senhas ou dados de cartão em repositórios públicos.

## Estrutura do repositório

```text
skills/money-beauty/
  SKILL.md                     Instruções da habilidade
  agents/openai.yaml           Nome e descrição para Codex
  references/base-wolf/        Os 11 arquivos originais
  references/                 Framework e adaptação para clínicas
  templates/                  Contexto e tabela da sua clínica
prompts/                      Instruções portáveis
dist/                         ZIP e arquivos prontos para baixar
origem/                       Instruções WOLF, inventário e documento-fonte
scripts/empacotar.py           Regenera os pacotes sem acessar a rede
docs/cenarios-validacao.md     Cenários para conferir o comportamento
```

`origem/` serve à rastreabilidade e fica fora do ZIP da skill e do conhecimento operacional. O documento original mantém alegações da fonte que não devem orientar o atendimento; a referência operacional é o perfil adaptado.

## Atualização e verificação

Edite a skill e as referências, depois regenere os arquivos de distribuição:

```bash
python3 scripts/empacotar.py
```

O script também cria `dist/manifesto.json`, com os hashes dos arquivos distribuídos. Compare os hashes da base WOLF com `origem/inventario-wolf.json` para verificar a preservação. Reinstale o ZIP/pasta ou substitua os anexos da sua IA após atualizar; a publicação no GitHub não atualiza cópias instaladas automaticamente.

Use os [cenários de validação](docs/cenarios-validacao.md) para testar preços, pacotes, recusa, limites clínicos e confirmação de agenda na plataforma escolhida. Verificações estruturais do pacote não garantem o comportamento de todos os modelos.

## Origem e créditos

- **WOLF — Especialista em Vendas High Ticket**, plugin fornecido por Felipe: base disponível na versão 0.4.1, com 11 arquivos copiados integralmente e instruções históricas preservadas.
- **Gabriel Magioli / Consultoria UP**: [framework comercial de 7 etapas](https://frameworkcomercial.netlify.app/painel-7-etapas-fluxo.html), integrado por adaptação textual; não se trata de cópia do site nem de afiliação oficial.
- **Documento “Quem é a empresa”**, fornecido por Felipe: [fonte de contexto e preços da Althea](https://docs.google.com/document/d/1ciwxgZspt-VhhmKrGC41N-9hipr2qZOKwXEyWH4DYAk/edit).

Veja [os créditos e direitos dos materiais](NOTICE.md). Versão inicial: **1.0.0 — 17/11/2026**.
