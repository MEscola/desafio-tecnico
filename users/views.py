from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from .models import User
def cadastrar_usuario(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UserForm()

    return render(
        request,
        'users/cadastro.html',
        {'form': form}
    )

def listar_usuarios(request):
    usuarios_lista = User.objects.all()
    return render(
        request,
        'users/lista.html',
        {'usuarios': usuarios_lista}
    )

def perfil_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    projetos_dono = usuario.projetos.all()
    subitens_responsavel = usuario.subitem_set.all()

    context = {
        'usuario': usuario,
        'projetos_dono': projetos_dono,
        'subitens_responsavel': subitens_responsavel,
    }

    return render(request, 'users/perfil.html', context)

def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')

    return render(request, 'users/excluir.html', {'usuario': usuario})


