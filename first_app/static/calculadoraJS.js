let n1 = '';
let n2 = '';
let Operador = '';
let conta

function telaValor(valor){
    document.getElementById('tela').value = valor;
}

function numero(num){
    if (Operador == ''){
        n1 += num;
        telaValor(n1);
    } else {
        n2 += num;
        telaValor(n2);
    }
}

function operador(oper){
    Operador = oper;
}

function resultado(){

    n1 = parseFloat(n1);
    n2 = parseFloat(n2); 
    switch(Operador){
        case '+':
            conta = n1 + n2;
            telaValor(conta)
            break;
        case '-':
            conta = n1 - n2;
            telaValor(conta)
            break;
        case '/':
            if (n1 !== 0){
                if (n2 !== 0){
                    conta = n1 / n2;
                    telaValor(conta) 
                }else {
                    alert("Não é possível dividir por zero");
                    n1 = " ";
                    n2 = " ";
                    Operador = " ";
                }
            }else {
                alert("Não é possível dividir por zero");
                n1 = " ";
                n2 = " ";
                Operador = " ";
                telaValor(n1)
            }
            break;
        case '*':
            conta = n1 * n2;
            telaValor(conta)
            break;
    }
    Operador = '';
    n2 = '';

    conta = conta.toString()

    if (conta.includes('.')){
        conta = parseFloat(conta);
        telaValor(conta.toFixed(4))
    }else{
        conta = parseInt(conta);
        telaValor(conta)
    }

    n1 = conta;
}

function mudaSinal(){
    if (Operador == ''){
        n1 = -n1;
        telaValor(n1);
    } else {
        n2 = -n2;
        telaValor(n2);
    }
}

function decimal(){
    if (Operador == ''){ 
        if (!n1.includes('.')){
            n1 += ".";
            telaValor(n1);
        }
    } else {
        if (!n2.includes('.')){
            n2 += ".";
            telaValor(n2);
        }
    }
}

function limpaTela(){
    telaValor(0)
    Operador = '';
    n1 = '';
    n2 = '';
    conta = '';
}