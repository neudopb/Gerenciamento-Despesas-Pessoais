from django.http import HttpResponse
from django.views.generic import View
from despesasPessoais.utils import render_to_pdf
from django.template.loader import get_template
from gerenciador.models import Receita, Gerenciador

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):

        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        receita = Receita.objects.order_by('data', 'id_categoria', ).filter(id_gerenciador=gerenc.id)
        data = {'receitas': receita}

        #html = template.render(data)
        pdf = render_to_pdf('relatorio/invoice.html', data)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Relatorio_Receita_%s.pdf" %(gerenc.id)
            #content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
            content = 'attachment; filename=%s' %(filename)
            response['Content-Disposition'] = content
            return response
        else:
            return HttpResponse("Not found")