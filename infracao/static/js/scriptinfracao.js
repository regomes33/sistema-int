console.log("Cadastro Infração");
var btnsalvar=$('#submit');
(btnsalvar).on('click',function(){
    if(document.getElementById("id_ocorrencia-0-dataDoFato").value.length==""){
        alert("Não é Possivel Salvar");
        document.getElementById("id_ocorrencia-0-dataDoFato").focus();
        return false
    }

});

$(document).ready(function(){
$("#id_ocorrencia-0-dataDoFato").mask("00/00/0000")
})

$(btnsalvar).on('click',function(){
    if(document.getElementById("id_ocorrencia-0-dataDoFato").value.length > 3){
        document.getElementById("mensagem").onLoad
        return true
    }else{
        return false
    }

});
window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
      $(this).remove();
    });
  }, 3000);





