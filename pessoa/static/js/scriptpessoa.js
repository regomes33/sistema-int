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
						minlength:3,
						required:true,
						digits:false,



					} ,
					sobrenome: {
					    minlength:3,

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





$("#id_nome").on('input', function () {
	if (/[0-9]/g.test(this.value)) {
		alert("Apenas letras");
	}
});

$("#id_sobrenome").on('input', function () {
	if (/[0-9]/g.test(this.value)) {
		alert("Apenas letras");
	}
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











				











