$(document).on('ready', iniciar);

function iniciar(){
    $varBtnAgregar = $('#btnAgregar');
    $varBtnAgregar.on('click', agregar);

    $varBtnListar = $('#btnListar');
    $varBtnListar.on('click', listar);

    $varBtnGuardar = $('#btnGuardar');
    $varBtnGuardar.on('click', guardar);
    
    $varTabla = $('#dataTable');
    $varFormulario = $('#inputsData');
    
    $varLinkPicture = $('#inputPicture');
    $varName = $('#inputName');
    $varAverage = $('#inputAverage');

}

function agregar(){
    $varTabla.hide();
    $varBtnAgregar.hide();
    $varBtnListar.show();
    $varFormulario.show();
    $varBtnGuardar.show();
}

function listar(){
    $varTabla.show();
    $varBtnAgregar.show();
    $varBtnListar.hide();
    $varFormulario.hide();
    $varBtnGuardar.hide();
}

function guardar (){
    if($varName.val() == '' || $varAverage.val() == ''){
        alert('Llene los campos vacios por favor');
    }else{
        $varTabla.append('<tr>    <td></td>    <td><img class="profile-image" src="'+$varLinkPicture.val()+'" alt="Profile Icon" width="35px" height="35px"></td>    <td>'+$varName.val()+'</td>    <td>'+$varAverage.val()+'</td></tr>');
        $varLinkPicture.val('');
        $varName.val('');
        $varAverage.val('');
        listar();
    }
}
