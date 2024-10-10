## Sistema de controle da reserva de materiais do CA

<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="Sobre o projeto#sobre-o-projeto">Sobre o projeto</a>
      <ul>
        <li><a href="Linguagens de programação utilizadas#linguagens-de-programação-utilizadash">Linguagens de programação utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="Primeiros passos#primeiros-passos">Primeiros assos</a>
      <ul>
        <li><a href="Pré requisitos#pré-requisitos">Pré requisitos</a></li>
        <li><a href="Instalação#instalação">Instalação</a></li>
      </ul>
    </li>
    <li><a href="Modo de uso#modo-de-uso">Modo de uso</a></li>
    <li><a href="Agradecimentos#agradecimentos">Agradecimentos</a></li>
  </ol>
</details>

## Sobre o projeto

O projeto de sistema de controle para a reserva de materias do Corpo de Alunos visa, fundamentalmente, promover uma solução simples e completa para o controle e gerenciamento dos itens armazenados na reserva que precisam ser retirados e repostos em diversas ocasiões, para inúmeros fins ao longo do ano.

A iniciativa visa, por meio da criação de um aplicativo, possibilitar a automatização do processo de cautela de descautela de materias, bem como um melhor controle da quantidade de itens de cada tipo armazenado em tempo real.

O projeto se encontra em fase inicial, portanto novas funções podem ser implementadas ao longo do tempo.

## Linguagens de programação utilizadas

- Python
- C++

## Primeiros passos

## Tutorial da biblioteca gráfica

1. Instalação do Tkinter
O Tkinter vem pré-instalado na maioria das distribuições do Python. Para verificar se o Tkinter está instalado.

2. Criando a Primeira Janela
Para começar, vamos criar uma janela simples. Esse é o ponto de partida de qualquer aplicação gráfica com o Tkinter.

- tk.Tk(): Cria a janela principal da aplicação.
- title("Minha Primeira Janela"): Define o título da janela.
- geometry("400x300"): Define as dimensões da janela (largura x altura).
- mainloop(): Mantém a janela aberta até que o usuário a feche.

3. Widgets
Tkinter oferece vários widgets (componentes visuais) que você pode adicionar à sua interface gráfica, como rótulos, botões e caixas de texto.

a) Rótulos
Um rótulo é usado para exibir texto ou imagens na janela.

- Label: Cria um rótulo.
- pack(): Posiciona o rótulo na janela.

b) Botões
Um botão pode ser clicado para executar uma ação.

- Button: Cria um botão.
- command=ao_clicar: Associa a função ao_clicar ao clique do botão.

c) Entradas de Texto
O widget Entry permite que o usuário insira texto.

d) Caixa de Texto 
A caixa de texto (Text) permite que o usuário insira e edite blocos maiores de texto. É útil quando é necessário manipular múltiplas linhas, como em editores de texto.

e) Menu 
Um menu é uma forma de organizar funcionalidades em uma barra de opções. No Tkinter, os menus podem ser criados para disponibilizar comandos, como opções de "Abrir", "Salvar" ou "Sair" em um menu de "Arquivo". 

f) Frame 
O Frame é um contêiner usado para agrupar e organizar outros widgets em seções. É útil para criar áreas específicas dentro da janela, facilitando a disposição de elementos e melhorando a organização visual da interface.

4. Organização da interface
A disposição dos widgets na janela é feita usando métodos como pack, grid e place. Cada método tem suas próprias características:

- pack(): Adiciona os widgets à janela um após o outro, como uma pilha.
- grid(): Organiza os widgets em uma grade de linhas e colunas, oferecendo mais controle sobre a disposição dos elementos.
- place(): Permite posicionar os widgets em coordenadas específicas, oferecendo liberdade total sobre onde cada elemento será colocado na janela.

5. Eventos e Funções
Um dos elementos centrais em interfaces gráficas é a interação com o usuário, que é tratada através de eventos. Eventos são ações realizadas pelo usuário, como clicar em um botão, pressionar uma tecla ou fechar a janela. Os widgets do Tkinter podem ser configurados para responder a esses eventos por meio de funções chamadas "callbacks", chamadas em resposta a um evento específico. 

6. Adicionando Imagens
O Tkinter também permite a inclusão de imagens na interface, como ícones e gráficos. Esse recurso é útil para tornar a aplicação mais atraente visualmente. As imagens podem ser usadas em rótulos, botões e outros widgets que aceitem elementos gráficos, ajudando a criar interfaces mais intuitivas e personalizadas.

7. Janela de Diálogo
As janelas de diálogo são pop-ups que surgem para interagir com o usuário de forma direta, solicitando confirmação, exibindo mensagens ou permitindo a seleção de arquivos. Elas são úteis para casos em que é necessário informar algo ao usuário ou solicitar que ele faça uma escolha.

8. Personalização Visual
No Tkinter, há a possibilidade de personalizar os widgets para ajustar a aparência da interface conforme o design desejado. A cor de fundo (background), a cor do texto (foreground), as fontes e os tamanhos dos widgets podem ser ajustados para garantir que a interface se adapte às necessidades específicas do usuário e ofereça uma experiência mais agradável.

9. Finalizando a Aplicação
É importante lembrar que o loop principal (mainloop) do Tkinter deve permanecer ativo para que a interface continue respondendo aos eventos e interações do usuário. Esse loop é responsável por manter a janela aberta e garantir que as ações dos usuários sejam capturadas e tratadas.

### Pré requisitos

### Instalação

## Modo de uso

## Agradecimentos





