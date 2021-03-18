from django.http import HttpResponse
from django.views.generic import View
from despesasPessoais.utils import render_to_pdf
from gerenciador.models import Receita, Gerenciador, Despesa

class GeneratePDFGeral(View):
    def get(self, request, *args, **kwargs):

        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        receita = Receita.objects.order_by('data', 'id_categoria',).filter(id_gerenciador=gerenc.id)
        despesa = Despesa.objects.order_by('data', 'id_categoria',).filter(id_gerenciador=gerenc.id)
        data = {'receitas': receita, 'despesas': despesa, 'gerenciador': gerenc}

        #html = template.render(data)
        pdf = render_to_pdf('relatorio/invoice.html', data)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Relatorio_Geral.pdf"
            #content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
            content = 'attachment; filename=%s' %(filename)
            response['Content-Disposition'] = content
            return response
        else:
            return HttpResponse("Not found")

class GeneratePDFReceitas(View):
    def get(self, request, *args, **kwargs):

        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        receita = Receita.objects.order_by('data', 'id_categoria',).filter(id_gerenciador=gerenc.id)
        data = {'receitas': receita, 'gerenciador': gerenc}

        #html = template.render(data)
        pdf = render_to_pdf('relatorio/invoiceReceita.html', data)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Relatorio_Receitas.pdf"
            #content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
            content = 'attachment; filename=%s' %(filename)
            response['Content-Disposition'] = content
            return response
        else:
            return HttpResponse("Not found")

class GeneratePDFDespesas(View):
    def get(self, request, *args, **kwargs):

        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        despesa = Despesa.objects.order_by('data', 'id_categoria',).filter(id_gerenciador=gerenc.id)
        data = {'despesas': despesa, 'gerenciador': gerenc}

        #html = template.render(data)
        pdf = render_to_pdf('relatorio/invoiceDespesa.html', data)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Relatorio_Despesas.pdf"
            #content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
            content = 'attachment; filename=%s' %(filename)
            response['Content-Disposition'] = content
            return response
        else:
            return HttpResponse("Not found")