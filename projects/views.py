from django.shortcuts import get_object_or_404, redirect, render

from projects.forms import ProjectsForm, SubItemForm
from projects.models import Projects, SubItem
from django.shortcuts import get_object_or_404, redirect, render

from users import forms
from .models import SubItem

def home(request):
    return render(request, 'projects/home.html')

def cadastrar_projeto(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjectsForm()
    return render(request, 'projects/cadastro.html', {'form': form})

def lista_projetos(request):
    projetos = Projects.objects.all()
    return render(request, 'projects/lista.html', {'projetos': projetos})
def subitem(request, project_id):
    project = get_object_or_404(Projects, id=project_id)

    if request.method =='POST':
        form = SubItemForm(request.POST)

        if form.is_valid():
            subitem = form.save(commit=False)
            subitem.project = project
            subitem.save()
            return redirect('detalhe', project_id=project.id)

        else:
                form = SubItemForm()
            
        context = {
                'form': form,
                'project': project
            }
        
        return render(request, 'projects/subitem.html', context)
    
def detalhe_projeto(request, project_id):
    project = get_object_or_404(Projects, id=project_id)

    subitens = project.subitens.all()  # ← aqui!

    context = {
        'project': project,
        'subitens': subitens
    }

    return render(request, 'projects/detalhe.html', context)

def criar_subitem(request, project_id):
    project = get_object_or_404(Projects, id=project_id)

    if request.method == 'POST':
        form = SubItemForm(request.POST)
        if form.is_valid():
            subitem = form.save(commit=False)
            subitem.project = project
            subitem.save()
            return redirect('detalhe_projeto', project_id=project.id)
    else:
        form = SubItemForm()

    return render(
        request,
        'projects/subitem.html',
        {'form': form, 'project': project}
    )

    
def deletar_projeto(request, project_id):
    projeto = get_object_or_404(Projects, id=project_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('lista_projetos')
    return render(request, 'projects/excluir_projeto.html', {'projeto': projeto})

def deletar_subitem(request, subitem_id):
    # O Django procura o subitem. Se não achar o ID, dá o erro 404 que você viu.
    subitem = get_object_or_404(SubItem, id=subitem_id)
    
    # Pega ID do projeto pai para saber para onde voltar depois
    projeto_id = subitem.project.id  

    if request.method == 'POST':
        subitem.delete()
        # Deleta e voltamos para a página de detalhes do projeto
        return redirect('detalhe_projeto', project_id=projeto_id)
    
    # Se for apenas um clique (GET), ele pede confirmação
    return render(request, 'projects/excluir.html', {'subitem': subitem})

def editar_projeto(request, project_id):
    project = get_object_or_404(Projects, id=project_id)

    if request.method == 'POST':
        form = ProjectsForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('detalhe_projeto', project_id=project.id)
    else:
        form = ProjectsForm(instance=project)

    return render(
        request,
        'projects/editar.html',
        {'form': form, 'project': project}
    )
