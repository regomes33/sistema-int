console.log('Funcuinou');
var btnsalvar=$('#btnsalvar');
var formpessoa=$('#formulariopessoa');
var nomepessoa=$('#id_nome');

$(document).ready(function(){
	$("#id_cpf").mask("000.000.000-00")

    })



$(document).ready(function(){
            $("#formulariopessoa").validate({

				rules:{
					nome: {
						minlength:5,
						required:true,
						digits:false,



					} ,
					sobrenome: {
					    minlength:5,

					},
					cpf:{
						required:true,


					}

				},
				messages:{
				nome: "Preencha o campo Nome:!!!!",
				sobrenome:"Preencha o campo Sobre Nome",
				cpf:"Preencha o Campo CPF. Somente com Números "
				}


			})
		  })
		  
window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
      $(this).remove();
    });
  }, 3000);


$("#id_cpf").change(function () {
	var cpf = $(this).val();

	$.ajax({
		url: 'validate_cpf/',
		data: {
			'cpf': cpf
		},
		dataType: 'json',
		success: function (data) {
			if (data.is_taken) {
				alert("O CPF DIGITADO JÁ SE ENCONTRA CADASTRADO NO SISTEMA  .");
			}
		}
	});

});





function verificaNumero(e) {
                if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
                    return true;
                }
            }
$(document).ready(function() {
                $("id_nome").keypress(verificaNumero);

            });


(btnsalvar).on('click',function(){
    if(document.getElementById("id_nome").value.length==""){
        alert("Não é Possivel Salvar");
        document.getElementById("id_nome").focus();
        return false
    }

});

(btnsalvar).on('click',function(){
    if(document.getElementById("id_nome").value.length > 3){
        document.getElementById("mensagem").onLoad
        return true
    }else{
        return false
    }

})











				











