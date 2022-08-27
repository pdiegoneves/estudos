// function incentivarQuester(menagem, nomeQuester) {
//     console.log(`${menagem}, ${nomeQuester}`)
// }
function incentivarQuester(menagem, ...nomesQuesters) {
    nomesQuesters.map(nomeQuester => console.log(`${menagem}, ${nomeQuester}`))
}

incentivarQuester('Parabens por ter chego ao módulo de JavaScript avançado', "Diego", "Pedro", "Roberto")