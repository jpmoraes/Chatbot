<<<<<<< HEAD

$(document).ready(function () {
    $("#perguntar").click(function () {
  
        var pergunta = $("#pergunta").val(); 
        console.log(pergunta);
        $.ajax({
            url: 'conectChat.php',
            method: 'post',
            dataType: 'json',
            data: {
                pergunta:pergunta                
            },
            success: function(data) {
                console.log(data);
                 if(data.status != "error"){        
                    var response = document.getElementById('resposta');
                    response.textContent = data;
                 }else{
                    $("#resposta").val("Erro");
                 }       
            
            },
            error: function(xhr, status, error) {
                console.log(xhr.responseText);
                
            }
        });





    });
});
=======

$(document).ready(function () {
    $("#perguntar").click(function () {
  
        var pergunta = $("#pergunta").val(); 
        console.log(pergunta);
        $.ajax({
            url: 'conectChat.php',
            method: 'post',
            dataType: 'json',
            data: {
                pergunta:pergunta                
            },
            success: function(data) {
                console.log(data);
                 if(data.status != "error"){        
                    var response = document.getElementById('resposta');
                    response.textContent = data;
                 }else{
                    $("#resposta").val("Erro");
                 }       
            
            },
            error: function(xhr, status, error) {
                console.log(xhr.responseText);
                
            }
        });





    });
});
>>>>>>> 1aa57ca8d2fcccb3ceafc9e2faf9488439827ee2
