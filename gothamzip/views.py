from django.shortcuts import render
from django.views.generic import FormView
from gothamzip.forms import ZipForm


class ZipCheckView(FormView):
    template_name = "gothamzip.html"
    form_class = ZipForm

    def form_valid(self, form):
        zipcode = form.cleaned_data.get("zip")
        return render(
            self.request,
            self.template_name,
            {
                "zip": zipcode,
                "form": form,
            },
        )
