# Fluxo de Persistência de Dados

![Fluxo de Persistência de Dados](ELT/Docs/Fluxo-ELT-1.0.png)

Trata-se de um processo de ***ELT*** (Extração, Carga e Transformação) que integra um sistema legado com um banco de dados ***relacional*** (no exemplo, um MySQL) para um banco ***NoSQL*** (ElasticSearch) sem alterações significativas nos dados transferidos.

Para implementar esse fluxo de ELT, optou-se por uma arquitetura baseada em containers para todas as aplicações. A simulação do sistema legado também foi feita por meio de containers, com um para o ***MySQL*** e outro para o sistema de ***ERP*** (uma aplicação em ***Python*** que cadastra novos clientes e vendas de maneira contínua). O servidor ***Apache Nifi*** é o responsável por se conectar ao database do sistema legado e enviar, de forma contínua, para o ***Elasticsearch*** todos os novos clientes e vendas registrados no ERP. Além disso, o container com ***Kibana*** é utilizado para visualização do resultado da integração.

Nesse exemplo específico, foram criados dois flows separados, um para capturar novos clientes e outro para novas vendas. Ambos os flows são versionados pelo ***Apache Nifi Registry*** e são executados continuamente, capturando novos dados à medida que são inseridos no sistema legado. Esses dados são capturados e enviados para o banco de dados NoSQL, sem grandes alterações em sua estrutura original. Dessa forma, garantimos uma integração eficiente entre as bases que são heterogêneas.


#### Apache Nifi

Apache Nifi é uma plataforma open source que permite o gerenciamento e processamento de dados em tempo real de forma simples e escalável. Ele foi desenvolvido para lidar com fluxos de dados em ambientes distribuídos, oferecendo uma interface gráfica amigável para o desenvolvimento de pipelines de dados. O Apache Nifi suporta diversos tipos de fontes de dados, incluindo sistemas de arquivos, bancos de dados, serviços web, fluxos de dados, e muitos outros. Além disso, ele oferece integração com outras ferramentas de Big Data, como Apache Hadoop, Spark, e Hive.

#### Apache Nifi Registry

O Apache Nifi Registry é um subprojeto do Apache Nifi que fornece um repositório central para gerenciamento de versionamento, controle de acesso e colaboração para flows do Apache Nifi. Isso permite que as organizações gerenciem seus flows de forma mais eficiente e compartilhem seu trabalho com outras pessoas de maneira controlada e segura.

#### Elasticsearch

Elasticsearch é uma ferramenta de busca e análise de dados distribuída que é amplamente utilizada para buscar, analisar e visualizar grandes conjuntos de dados em tempo real. É um banco de dados NoSQL que é otimizado para armazenar, pesquisar e analisar grandes volumes de dados não estruturados. O Elasticsearch é escalável e flexível, permitindo que os usuários realizem pesquisas e análises avançadas em seus dados em tempo real.

#### Kibana

Kibana é uma ferramenta de visualização de dados que funciona em conjunto com o Elasticsearch, permitindo a criação de gráficos, dashboards e relatórios interativos para ajudar a entender e extrair insights a partir dos dados armazenados. Ele oferece uma interface amigável que permite a criação de painéis personalizados com diferentes tipos de visualizações, incluindo gráficos de barras, tabelas, mapas, e muitos outros. O Kibana é amplamente utilizado em ambientes de análise de dados e big data para monitoramento de sistemas, detecção de fraudes, análise de logs, e muitas outras aplicações.

#### Docker

Docker é uma plataforma de virtualização de aplicativos que permite que os aplicativos sejam executados em ambientes isolados e portáteis chamados contêineres. Cada contêiner inclui todos os componentes necessários para executar um aplicativo, como código, bibliotecas, dependências e configurações. Isso permite que os desenvolvedores criem, gerenciem e implantem aplicativos de forma mais rápida e consistente em diferentes ambientes.

#### Docker Compose

O Docker Compose é uma ferramenta que permite que os usuários definam e executem aplicativos Docker compostos por vários contêineres. Ele usa um arquivo YAML para definir as configurações de cada contêiner e suas dependências. Isso facilita o gerenciamento de aplicativos complexos que requerem vários contêineres, permitindo que eles sejam gerenciados como uma unidade.

O Docker e o Docker Compose são amplamente usados no desenvolvimento de aplicativos modernos, especialmente em ambientes de desenvolvimento e produção baseados em nuvem. Eles permitem que os desenvolvedores criem aplicativos de forma rápida e consistente, reduzindo a complexidade do gerenciamento de dependências e configurações em diferentes ambientes. Além disso, o uso de contêineres permite que os aplicativos sejam escalonados facilmente, garantindo que as alterações feitas em um contêiner não afetem outros contêineres em execução no mesmo host.

# Implementação

Em Desenvolvimento...

# Referências

Apache/Nifi, ***Docker Hub***. Disponível em: <https://hub.docker.com/r/apache/nifi>. Acesso em: 19 abr. 2023.

NiFi System Administrator’s Guide, ***Apache NiFi***. Disponível em: <https://nifi.apache.org/docs/nifi-docs/html/administration-guide.html>. Acesso em: 22 abr. 2023.

apache/nifi-registry, ***Docker Hub***. Disponível em: <https://hub.docker.com/r/apache/nifi-registry>. Acesso em: 22 abr. 2023.

Getting Started with Apache NiFi Registry, ***Apache NiFi Registry***. Disponível em: <https://nifi.apache.org/docs/nifi-registry-docs/index.html>. Acesso em: 22 abr. 2023.

How to build a data lake from scratch - Part 1: The setup, ***Victor Seifert***. Disponível em: <https://towardsdatascience.com/how-to-build-a-data-lake-from-scratch-part-1-the-setup-34ea1665a06e>. acesso em: 19 abr. 2023.

How to build a data lake from scratch — Part 2: Connecting the components, ***Victor Seifert***. Disponível em: <https://medium.com/towards-data-science/how-to-build-a-data-lake-from-scratch-part-2-connecting-the-components-1bc659cb3f4f>. acesso em: 23 abr. 2023.

Texto, ***Origem***. Disponível em: <URL>. Acesso em: 23 abr. 2023.