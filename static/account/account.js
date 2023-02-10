$(document).ready( function() {
    $('#accountForm').submit( function (e) {
        e.preventDefault();
        
        form = $(this)

        $.ajax({
        url: '/api/login',
        method: 'POST',
        dataType: 'json',
        data: form.serialize(),
        success: function(resp){
            if ( resp.message == 'userLoginError' ) {
                userAccError();
            }
            else if (resp.message == 'logIn') {
                location.assign(resp.address) //send user to new address TODO: send them via server side
            }
        }
        });
    });
});
function userAccError() {
    self = $(':password')

    self.addClass('userAccErrorAnimTrigger');
    self.on('animationend', function() {
        self.removeClass('userAccErrorAnimTrigger')
    })
}