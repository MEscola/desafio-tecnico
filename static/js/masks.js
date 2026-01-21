document.addEventListener("DOMContentLoaded", function () {

    const telefoneInput = document.querySelector("#id_telefone");

    if (telefoneInput) {
        telefoneInput.addEventListener("input", function () {
            let value = telefoneInput.value.replace(/\D/g, "");

            if (value.length > 11) {
                value = value.slice(0, 11);
            }

            if (value.length > 10) {
                value = value.replace(/^(\d{2})(\d{5})(\d{4})$/, "($1) $2-$3");
            } else if (value.length > 6) {
                value = value.replace(/^(\d{2})(\d+)(\d{4})$/, "($1) $2-$3");
            } else if (value.length > 2) {
                value = value.replace(/^(\d{2})(\d+)/, "($1) $2");
            }

            telefoneInput.value = value;
        });
    }

    const cpfInput = document.querySelector("#id_cpf");

if (cpfInput) {
    cpfInput.addEventListener("input", function () {
        let value = cpfInput.value.replace(/\D/g, "");

        if (value.length > 11) {
            value = value.slice(0, 11);
        }

        value = value.replace(/(\d{3})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

        cpfInput.value = value;
    });
}

const emailInput = document.querySelector("#id_email");

if (emailInput) {

    emailInput.addEventListener("blur", function () { 
        
        const emailValue = emailInput.value;
        const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (emailValue && !pattern.test(emailValue)) {
            emailInput.setCustomValidity("Por favor, insira um endereço de email válido.");
            emailInput.style.borderColor = "red";
        } else {
            emailInput.style.borderColor = "";
            emailInput.setCustomValidity("");  
        }
    });

    // 2. Limpa o erro qdo o usuário volta a digitar 
        emailInput.addEventListener("input", function () {
        emailInput.setCustomValidity(""); 
        emailInput.style.borderColor = "";
    });
}
}); 

