console.log('Funcuinou');
var searchbtn = $('#search-btn');
var searchform = $('#search-form');
var btneditar = $('#btneditar')


$(document).ready(function () {
    $("#id_cpf").mask("000.000.000-00")

})



$(document).ready(function () {
    $("#formulariopessoa").validate({

        rules: {
            nome: {
                minlength: 5,
                required: true,
                digits: false,



            },
            sobrenome: {
                minlength: 5,

            },
            cpf: {
                required: true,


            }

        },
        messages: {
            nome: "Preencha o campo Nome:!!!!",
            sobrenome: "Preencha o campo Sobre Nome",
            cpf: "Preencha o Campo CPF. Somente com Números "
        }


    })
})

$(document).ready(function () {
    setTimeout(function () {
        $('#message').fadeOut(1500);
    }, 3000);
});


$("#id_cpf").change(function () {
    var cpf = $(this).val();

    $.ajax({
        url: 'validate_editar/',
        data: {
            'cpf': cpf
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                alert("O Cpf digitado já existe .");
            }
            
        }
    });

});


function verificaNumero(e) {
    if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
        return true;
    }
}
$(document).ready(function () {
    $("#id_nome").keypress(verificaNumero);

});



$(searchbtn).on('click', function () {
    searchform.submit();


})

$("#formularioeditar").on('change paste', 'input, select, textarea', function () {
    $mudou = true;
});


$(btneditar).on('click',function(){
    
    if ($mudou == true) {

        var msj = 'Dados editados!! Deseja Salvar Edição?';
        if (!confirm(msj)) {
            return false;
        } else {
            $("#formularioeditar").submit();
            
        }
        
    }
  
    
    
       

});

function CriaPDF() {
    var descricao = document.getElementById('descricao').innerHTML;
    var style = "<style>";
    style = style + "table {width: 100%;font: 20px Calibri;}";
    style = style + "table, th, td {border: solid 1px #DDD; border-collapse: collapse;";
    style = style + "padding: 2px 3px;text-align: center;}";
    style = style + "</style>";
    // CRIA UM OBJETO WINDOW
    var win = window.open('', '', 'height=700,width=700');
    win.document.write('<html><head>');
    win.document.write('<title>Descricão da Pessoa</title>');   // <title> CABEÇALHO DO PDF.
    win.document.write(style);                                     // INCLUI UM ESTILO NA TAB HEAD
    win.document.write('</head>');
    win.document.write('<body>');
    win.document.write(descricao);                          // O CONTEUDO DA TABELA DENTRO DA TAG BODY
    win.document.write('</body></html>');
    win.document.close(); 	                                         // FECHA A JANELA
    win.print();                                                            // IMPRIME O CONTEUDO
}
































