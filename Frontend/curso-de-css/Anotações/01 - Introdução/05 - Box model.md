# Box model
Todos os box tem 4 camadas
1. Conteúdo
2. preenchimento interno - padding
3. Borda do conteúdo
4. preenchimento externo - margin

## box padrão
box-sizing: content-box;

o width se refere ao conteúdo

## border box
box-sizing: border-box;

O width se refere as camadas até a borda, excluindo apenas a margem do cálculo

## ordem
a ordem da medida dos elementos que se referem aos box:
* Top
* Right
* Botton
* Left

```
margin: 0 -> todos os lados
margin: 0 0 -> primeiro zero medidas verticais, segundo zero medidas horizontais
margin: 0 0 0 0 -> definindo todos os lados
```