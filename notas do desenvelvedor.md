# <center>NOTAS DO DESAFIO</center>

## Bate Papo:

**Pergunta**: *Por que o *BeautifulSoup* e não outros como o *scrapy* ou *parsel* ,
etc...?*<br /> **Resposta**:O _BeautifulSoup_ é a biblioteca que mais conheço e por isso
a escolha dela. Eu até pensei em fazer com o scrapy pois vi que ela facilita muito na
hora de fazer a navegação entre as paginas, mas por ter pouco tempo pra aprender e ver
que há uma abstração muito grande do código algo que poderia impactar na escolha da vaga
decidi por manter que eu já tinha uma certa afinidade.

**Pergunta**: *Por que o *httpx* e não o *request* ou outras *libs*?* <br />
**Resposta**: Diferente da outra resposta eu até conheço mais o _request_ pois já vi
muita coisa com ele, mas o _request_ é uma _lib_ abandonada e o _httpx_ está ganhando
popularidade. Por ser uma _lib_ com uma curva de aprendizagem muito curta e eu só usaria
o básico do básico escolhi por ela.

**Pergunta**:_Quais foram as suas maiores dificuldades na hora de desenvolver esse
scraping?_ <br /> **Resposta**:Com toda a certeza foi fazer com que o programa navegasse
por todos os arquivos e pastas. Gastei algumas horas quebrando a cabeça pois ele sempre
ficava na pagina inicial. A princípio cheguei a fazer ele a função `request_all_links`um
gerador, mas o desempenho caiu drasticamente. Fazendo o `request_all_links` recursivo
aumentou bastante o desempenho e também a legibilidade ~~(Isso é o que eu espero)~~,
pois ali se concentra tudo que precisa das urls, arquivos e pastas.

**Pergunta**: _Por que decidiu fazer uma classe no arquivo `web_scraping.py` e deixar o
resto como função?_ <br /> **Resposta**:A principio era tudo função, mas eu vi que era
necessário fazer com que outras funções pegassem valores que não tinha como fazer com o
`return` e etc... Até estava funcionando bem, mas estava usando muito o `Global` para
informar que eu estava usando uma variável global, ficou bem feio o código. Com a classe
já tive mais facilidade por conta da abstração do programa e por usar variáveis de
instância com o `self` que é uma mão na roda nessa situação.

**Pergunta**: _Por que seu código mistura Inglês e Português?_ <br /> **Resposta**: Vou
corrigir isso antes de ser analisado. As vezes falta criatividade para colocar o nome
das variáveis, métodos, funções , etc... Então sou completamente direto.

> "Se ela armazena um dicionário vai ter o nome de vardict"

Mas depois quando vou refatorando vou trocando o nome e colocando algo que fique mais
intuitivo para quem vai usar ou dar manutenção. PS: isso é sem dúvida a parte mais
difícil da programação. Nós nunca achamos um nome adequando para as nomear as variáveis,
funções, arquivos e por aí vai.
