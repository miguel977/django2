from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm

def index(request):
    # context = {
    #     'produtos': Produto.objects.all()
    # }
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        print(f'POST:{request.POST}')
        if form.is_valid():
            nome = form.changed_data['nome']
            email = form.changed_data['email']
            assunto = form.changed_data['assunto']
            mensagem = form.changed_data['mensagem']
            
            print('mensagem enviada')
            print(f'nome:{nome}')
            print(f'Email:{email}')
            print(f'assunto:{assunto}')
            print(f'mensagem:{mensagem}')
        
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')