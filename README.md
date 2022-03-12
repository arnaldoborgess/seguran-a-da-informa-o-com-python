# Segurança da Informação com Python

### Dado?
O dado é uma representação simbólica, numérica ou textual qualquer.
Ele não tem nenhuma característica de entendimento.

### O que é a informação?
É o conjunto ou junção de dados que fazem um contexto ou sentido.

### O que é Segurança da Informação?
É uma área que tem como objetivo assefurar que todos os dados de uma ou mains informações estejam semprem **confidenciais, íntegros e dismponíveis** em qualquer meio de comunicação.
Tem como objetivo proteger o todo e os dados.
Se preocupa por todo o ciclo da informação. Desque é gerada, transportada, armazenada e excluída.

### Porque Segurança?
O ser humano tem necessidade de segurança.
> Pirâmide de Maslow.
> https://pt.wikipedia.org/wiki/Hierarquia_de_necessidades_de_Maslow

# Princípios da Segurança da Informação.

**Integridade, Confiabilidade, Disponibilidade, Identificação, Autenticação, Autorização, Não Repúdio.**

OS PRINCÍPIOS DA SEGURANÇA DE DADOS
 
    1. CONFIDENCIALIDADE
Esse princípio leva em consideração que os dados somente podem ser acessados pelos seus usuários legítimos e demais pessoas autorizadas, desde que previamente informado nos termos de serviço.

Esse conceito engloba a proteção dos dados dos usuários contra acessos não autorizados e medidas a fim de preservar a privacidade dos mesmos.

A única forma de cumprir esse princípio é através de autenticações, restringindo o acesso somente a indivíduos que saibam a senha ou tenha o nível de liberação para acessar tais dados. A confidencialidade não envolve somente dados de clientes, mas também da própria empresa!

 
   2 . INTEGRIDADE
A integridade dispõe sobre as condições dos dados, estes devem manter-se inalterados. O emissor (ou proprietário) deve ser capaz de emitir um documento e o mesmo ser disponibilizado para o destinatário sem a possibilidade de ter sido alterado proposital ou acidentalmente.

Quando funcionários excluem ou alteram dados importantes é considerada uma quebra desse princípio, isso também acontece quando um vírus é responsável pelas alterações, por exemplo.

Sendo assim, é necessário criar sistemas a fim de proteger documentos e também informações inseridas por usuários em plataformas.

A diferença entre Front-End, Back-End e Mobile;

 
    3.DISPONIBILIDADE
Não adianta nada ter a informação se a mesma não é entregue aos usuários legítimos quando requisitadas. Sendo assim, é importante que os recursos estejam disponíveis para usuários e funcionários sempre.

É importante que os sistemas utilizados para armazenar e processar os dados estejam sempre funcionando corretamente.

Dessa forma, considerar sistemas de alta disponibilidade permite que as informações resistam a falhas de hardware, software e até mesmo de energia, estando sempre disponíveis para o usuário.

 
    4. AUTENTICIDADE
Esse conceito se refere a confirmação de que o usuário é realmente quem alega ser, desde quem está emitindo a informação até quem irá recebê-la.

Essa garantia pode ser realizada de diversas formas, um exemplo bastante prático são os códigos de confirmação que são enviados por e-mail ou SMS após inserir uma senha. Outro exemplo é a autenticação biométrica e por senha para terá acesso a uma sala, combinando algo que você conhece com algo que você é.

 

    5.IRRETRATABILIDADE OU NÃO REPÚDIO
A irretratabilidade tem foco na legitimidade do autor da informação, isso funciona como uma forma de rastrear todas as ações de um indivíduo dentro do sistema de forma que não seja possível negar a autoria de uma ação.

A criação e assinatura de um documento ou arquivo é um exemplo bastante prático.

> https://auditeste.com.br/quais-sao-os-principios-da-seguranca-da-informacao/

## ICMP
ICMP (Internet Control Message Protocol), é um protocolo integrante do Protocolo IP utilizado para fornecer relatórios de erros à fonte original.

## PING
É uma ferramenta que usa o protocolo ICMP para testar a concectividad entre nós. É um comando disponível praticamente em todos os sistemas operacionais que consiste no envio de pacotes para o equipamento de destino na "escuta" das respostas.
Echo Request > Echo Replay (pergunta e resposta.) princípio de disponibilidade.

### Biblioteca OS
Módulo que fornece uma maneira simples de usar funcionalidades que são dependentes de sistema operacional.
